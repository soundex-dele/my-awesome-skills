
import json
import os
import sys
import io

# 设置标准输出编码为 UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from jy_wrapper import JyProject
import pyJianYingDraft as draft

def apply_smart_zoom(project: JyProject, video_segment, events_json_path: str, zoom_scale=150, zoom_duration_us=500000):
    """
    根据记录的 events.json 自动为视频片段添加缩放关键帧 (类似产品演示效果)
    
    Args:
        project: JyProject 实例
        video_segment: 要应用缩放的视频片段对象
        events_json_path: 录制时生成的 _events.json 路径
        zoom_scale: 缩放比例 (%)
        zoom_duration_us: 缩放动画持续时间 (微秒), 默认 0.5s
    """
    if not os.path.exists(events_json_path):
        print(f"❌ Events file not found: {events_json_path}")
        return

    with open(events_json_path, 'r', encoding='utf-8') as f:
        events = json.load(f)

    # 提取点击事件
    click_events = [e for e in events if e['type'] == 'click']
    # 提取ESC事件用于恢复缩放
    esc_events = [e for e in events if e['type'] == 'esc_press']

    if not click_events:
        print("ℹ️ No click events found in JSON.")
        return

    print(f"🎯 Found {len(click_events)} click events and {len(esc_events)} ESC events. Applying smart zoom keyframes...")

    # 禁用移动事件处理 - 移动事件不再触发缩放跟随
    move_events = []
    
    # 将点击事件分组 (Session-based)
    grouped_events = []
    if click_events:
        current_group = [click_events[0]]
        for i in range(1, len(click_events)):
            prev_time = click_events[i-1]['time']
            curr_time = click_events[i]['time']
            if (curr_time - prev_time) <= 5.0:
                current_group.append(click_events[i])
            else:
                grouped_events.append(current_group)
                current_group = [click_events[i]]
        grouped_events.append(current_group)

    print(f"🔄 Grouped into {len(grouped_events)} zoom sessions.")

    from pyJianYingDraft.keyframe import KeyframeProperty as KP

    # 准备红点素材路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    skill_root = os.path.dirname(current_dir)
    marker_path = os.path.join(skill_root, "assets", "click_marker.png")
    
    # 缩放参数
    scale_val = float(zoom_scale) / 100.0
    ZOOM_IN_US = 300000    # 0.3s
    HOLD_US = 5000000      # 5.0s
    ZOOM_OUT_US = 600000   # 0.6s
    ESC_RESTORE_US = 200000  # ESC恢复时间 (0.2s)

    def calculate_center_offset(click_x, click_y, scale):
        """
        计算让点击位置成为中心所需的位置偏移
        click_x, click_y: 点击的归一化坐标 (0-1)
        scale: 缩放倍率
        返回: (pos_x, pos_y) 剪映位置参数
        """
        # 目标：让点击位置 (click_x, click_y) 成为画面中心
        # 当前中心是 (0.5, 0.5)，需要移动到让点击点居中

        # 点击位置相对于中心的偏移 (归一化坐标)
        offset_x = (click_x - 0.5) * 2  # -1 到 1
        offset_y = (0.5 - click_y) * 2  # -1 到 1 (Y轴翻转)

        # 剪映的位置参数：偏移量 * 缩放倍率
        pos_x = -offset_x * scale
        pos_y = -offset_y * scale

        # 边界限制，防止黑边
        limit = max(0.0, scale - 1.0)
        pos_x = max(-limit, min(pos_x, limit))
        pos_y = max(-limit, min(pos_y, limit))

        return pos_x, pos_y

    for group in grouped_events:
        # --- 1. Start Phase (整体进场) ---
        first_event = group[0]
        t0_us = int(first_event['time'] * 1000000)
        t_start = max(0, t0_us - ZOOM_IN_US)

        # 设置初始状态
        video_segment.add_keyframe(KP.uniform_scale, t_start, 1.0)
        video_segment.add_keyframe(KP.position_x, t_start, 0.0)
        video_segment.add_keyframe(KP.position_y, t_start, 0.0)

        # 检查此缩放会话期间是否有ESC事件
        group_start_time = group[0]['time']
        group_end_time = group[-1]['time'] + 5.0  # 包括预期的停留时间
        group_esc_events = [e for e in esc_events if group_start_time <= e['time'] <= group_end_time]

        # 如果有ESC事件，找到最早的ESC时间
        first_esc_time = None
        if group_esc_events:
            first_esc_time = min(e['time'] for e in group_esc_events)
            print(f"Detected ESC at {first_esc_time}s, will restore zoom to 100%")

        # 记录第一次点击的位置（用于整个缩放会话）
        first_click_pos_x = 0.0
        first_click_pos_y = 0.0

        # 遍历组内每个点击事件
        for i, event in enumerate(group):
            # 如果有ESC事件且当前点击时间超过ESC时间，停止处理
            if first_esc_time and event['time'] >= first_esc_time:
                break

            t_curr_us = int(event['time'] * 1000000)

            # --- A. 添加红点标记 (Sticker) ---
            if os.path.exists(marker_path):
                try:
                    project.add_sticker_at(marker_path, t_curr_us, 500000)
                except:
                    pass

            # --- B. 只在第一次点击时计算和设置位置 ---
            if i == 0:
                # 计算让第一次点击位置居中的位置偏移
                first_click_pos_x, first_click_pos_y = calculate_center_offset(event['x'], event['y'], scale_val)

                # 设置缩放和位置关键帧，让第一次点击位置居中
                video_segment.add_keyframe(KP.uniform_scale, t_curr_us, scale_val)
                video_segment.add_keyframe(KP.position_x, t_curr_us, first_click_pos_x)
                video_segment.add_keyframe(KP.position_y, t_curr_us, first_click_pos_y)
            else:
                # 后续点击只设置缩放关键帧，保持第一次的位置不变
                video_segment.add_keyframe(KP.uniform_scale, t_curr_us, scale_val)

        # --- 3. 处理ESC恢复或正常结束 ---
        if first_esc_time:
            # 有ESC事件：立即恢复到100%
            t_esc_us = int(first_esc_time * 1000000)
            t_restore = t_esc_us + ESC_RESTORE_US

            # 保持ESC时刻的缩放状态和位置（使用第一次点击的位置）
            video_segment.add_keyframe(KP.uniform_scale, t_esc_us, scale_val)
            video_segment.add_keyframe(KP.position_x, t_esc_us, first_click_pos_x)
            video_segment.add_keyframe(KP.position_y, t_esc_us, first_click_pos_y)

            # 恢复全景
            video_segment.add_keyframe(KP.uniform_scale, t_restore, 1.0)
            video_segment.add_keyframe(KP.position_x, t_restore, 0.0)
            video_segment.add_keyframe(KP.position_y, t_restore, 0.0)
        else:
            # 无ESC事件：正常结束流程
            last_event = group[-1]
            last_activity_time = last_event['time']

            # 最终结束时间
            t_hold_end = int((last_activity_time + 5.0) * 1000000)

            # 添加 Hold 结束帧（使用第一次点击的位置）
            video_segment.add_keyframe(KP.uniform_scale, t_hold_end, scale_val)
            video_segment.add_keyframe(KP.position_x, t_hold_end, first_click_pos_x)
            video_segment.add_keyframe(KP.position_y, t_hold_end, first_click_pos_y)

            # 恢复全景
            t_restore = t_hold_end + ZOOM_OUT_US
            video_segment.add_keyframe(KP.uniform_scale, t_restore, 1.0)
            video_segment.add_keyframe(KP.position_x, t_restore, 0.0)
            video_segment.add_keyframe(KP.position_y, t_restore, 0.0)

    print("✅ Smart zoom keyframes applied successfully.")

if __name__ == "__main__":
    # 示例用法
    if len(sys.argv) < 3:
        print("Usage: python smart_zoomer.py <project_name> <video_path> <events_json>")
        sys.exit(1)
        
    proj_name = sys.argv[1]
    video_path = sys.argv[2]
    json_path = sys.argv[3]
    
    p = JyProject(proj_name)
    seg = p.add_media_safe(video_path, "0s")
    apply_smart_zoom(p, seg, json_path)
    p.save()
