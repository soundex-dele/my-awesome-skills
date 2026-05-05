#!/usr/bin/env python3
"""
测试用图片生成脚本 - 本地生成模拟图片
不调用大模型 API，使用 PIL 本地生成简单测试图片

参考 gen_image.py 的接口结构，但用本地绘图替代 API 调用
"""

import argparse
import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import random

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# 模拟的尺寸配置（与 gen_image.py 类似）
MOCK_SIZES = {
    "cover": {"width": 900, "height": 500},
    "illustration": {"width": 1024, "height": 768},
    "thumbnail": {"width": 400, "height": 400},
}


def generate_solid_image(topic, width, height, bg_color, text_color):
    """生成纯色背景+文字的简单图片"""
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # 尝试加载字体
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 40)
        small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
    except:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # 绘制主题文字
    text = topic if len(topic) <= 20 else topic[:20] + "..."
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (width - text_width) // 2
    y = (height - text_height) // 2

    draw.text((x, y), text, fill=text_color, font=font)

    # 添加尺寸标签
    size_text = f"{width}x{height}"
    draw.text((10, height - 30), size_text, fill=text_color, font=small_font)

    return img


def generate_gradient_image(topic, width, height):
    """生成渐变色背景的图片"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    # 创建从上到下的渐变
    start_color = (78, 205, 196)   # 青色
    end_color = (255, 107, 107)    # 红色

    for y in range(height):
        ratio = y / height
        r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # 添加白色半透明矩形作为文字背景
    overlay = Image.new('RGBA', (width, height), (255, 255, 255, 180))
    img.paste(overlay, (0, 0), overlay)

    # 绘制文字
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
    except:
        font = ImageFont.load_default()

    text = topic if len(topic) <= 15 else topic[:15] + "..."
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]

    x = (width - text_width) // 2
    y = (height - 60) // 2

    draw.text((x, y), text, fill=(50, 50, 50), font=font)

    return img.convert('RGB')


def generate_pattern_image(topic, width, height):
    """生成几何图形图案"""
    img = Image.new('RGB', (width, height), (247, 247, 247))
    draw = ImageDraw.Draw(img)

    # 生成随机颜色
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#FFE66D']

    # 绘制随机矩形
    num_shapes = 8
    for i in range(num_shapes):
        x1 = random.randint(0, width - 100)
        y1 = random.randint(0, height - 100)
        x2 = x1 + random.randint(50, 150)
        y2 = y1 + random.randint(50, 150)
        color = random.choice(colors)
        draw.rectangle([x1, y1, x2, y2], fill=color, outline='white', width=2)

    # 绘制圆形
    for i in range(5):
        center_x = random.randint(50, width - 50)
        center_y = random.randint(50, height - 50)
        radius = random.randint(20, 60)
        color = random.choice(colors)
        draw.ellipse([center_x - radius, center_y - radius,
                      center_x + radius, center_y + radius],
                     fill=color, outline='white', width=2)

    # 添加主题文字（半透明白色背景）
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
    except:
        font = ImageFont.load_default()

    text = topic if len(topic) <= 25 else topic[:25] + "..."
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # 文字背景框
    padding = 20
    box_x1 = (width - text_width) // 2 - padding
    box_y1 = (height - text_height) // 2 - padding
    box_x2 = box_x1 + text_width + padding * 2
    box_y2 = box_y1 + text_height + padding * 2

    # 半透明背景
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.rectangle([box_x1, box_y1, box_x2, box_y2],
                           fill=(255, 255, 255, 220))

    img.paste(overlay, (0, 0), overlay)

    # 绘制文字
    draw = ImageDraw.Draw(img)
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    draw.text((x, y), text, fill=(50, 50, 50), font=font)

    return img


def gen_image(topic, image_type="illustration", output="output.png", style=None):
    """
    生成本地模拟图片

    参数：
        topic: 图片主题
        image_type: 图片类型 (cover/illustration/thumbnail)
        output: 输出文件路径
        style: 图片风格 (solid/gradient/pattern/minimalist/colorful/vintage)
               如果为 None，则根据 image_type 自动选择

    返回：
        output: 输出文件路径
    """
    # 获取目标尺寸
    size_config = MOCK_SIZES.get(image_type, MOCK_SIZES["illustration"])
    width = size_config["width"]
    height = size_config["height"]

    print(f"🎨 生成模拟 {image_type}: {topic}")
    print(f"📐 尺寸: {width}x{height}")

    # 如果没有指定风格，根据 image_type 自动选择
    if style is None:
        if image_type == "cover":
            style = "gradient"
        elif image_type == "thumbnail":
            style = "solid"
        else:
            style = "pattern"

    print(f"🎭 风格: {style}")

    # 根据风格选择不同的生成函数
    if style == "solid":
        # 纯色背景
        bg_colors = {
            "blue": ('#4ECDC4', '#FFFFFF'),
            "green": ('#98D8C8', '#2D3436'),
            "orange": ('#FFA07A', '#FFFFFF'),
            "purple": ('#A29BFE', '#FFFFFF'),
        }
        bg_color, text_color = random.choice(list(bg_colors.values()))
        img = generate_solid_image(topic, width, height, bg_color, text_color)

    elif style == "gradient":
        # 渐变背景
        img = generate_gradient_image(topic, width, height)

    elif style == "pattern":
        # 几何图案
        img = generate_pattern_image(topic, width, height)

    elif style == "minimalist":
        # 极简风格 - 浅色背景 + 小文字
        light_bg = (250, 250, 250)
        img = generate_solid_image(topic, width, height, light_bg, '#2D3436')

    elif style == "colorful":
        # 彩色风格 - 鲜艳的渐变
        img = generate_gradient_image(topic, width, height)

    elif style == "vintage":
        # 复古风格 - 暖色调
        img = generate_solid_image(topic, width, height, '#D4A574', '#5D4037')

    else:
        # 默认使用图案风格
        img = generate_pattern_image(topic, width, height)

    # 确保输出目录存在
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 保存图片
    img.save(str(output_path), "PNG", optimize=True)
    print(f"💾 已保存: {output_path} ({width}x{height})")

    return str(output_path)


def main():
    """命令行入口"""
    parser = argparse.ArgumentParser(description="测试用本地图片生成器")
    parser.add_argument("topic", help="图片主题描述")
    parser.add_argument("--type", choices=["cover", "illustration", "thumbnail"],
                        default="illustration", help="图片类型")
    parser.add_argument("--style", choices=["solid", "gradient", "pattern", "minimalist", "colorful", "vintage"],
                        default=None, help="图片风格（如未指定则根据 type 自动选择）")
    parser.add_argument("--output", "-o", default="output.png", help="输出文件名")

    args = parser.parse_args()

    # 支持相对路径和绝对路径
    if not os.path.isabs(args.output):
        # 默认保存到 test_images 目录
        output_dir = os.path.join(ROOT_DIR, "test_images")
        os.makedirs(output_dir, exist_ok=True)
        output = os.path.join(output_dir, args.output)
    else:
        output = args.output

    gen_image(args.topic, args.type, output, args.style)


if __name__ == "__main__":
    main()
