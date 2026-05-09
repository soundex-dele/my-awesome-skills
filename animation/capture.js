const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function captureTransparentAnimation() {
    console.log('🎬 Starting capture...');

    const browser = await puppeteer.launch({
        headless: 'new',
    });

    const page = await browser.newPage();
    const htmlPath = path.join(__dirname, 'index.html');
    const fileUrl = `file://${htmlPath}`;

    // 设置视口
    await page.setViewport({
        width: 800,
        height: 600,
        deviceScaleFactor: 1,
    });

    // 加载页面
    console.log('📄 Loading HTML:', fileUrl);
    await page.goto(fileUrl, {
        waitUntil: 'networkidle0',
    });

    // 创建输出目录
    const outputDir = path.join(__dirname, 'frames');
    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
    }

    // 获取总时长
    const totalDuration = await page.evaluate(() => window.getTotalDuration());
    console.log(`⏱️  Total duration: ${totalDuration}s`);

    // 捕获参数
    const fps = 30;
    const totalFrames = Math.floor(totalDuration * fps);

    console.log(`📸 Capturing ${totalFrames} frames at ${fps}fps...`);

    // 逐帧捕获
    for (let frame = 0; frame < totalFrames; frame++) {
        const currentTime = frame / fps;

        // 设置动画时间
        await page.evaluate((time) => {
            window.seekTo(time);
        }, currentTime);

        // 等待一帧的时间让动画更新
        await new Promise(resolve => setTimeout(resolve, 1000 / fps));

        // 截图 - 关键：omitBackground: true 保留透明通道
        const framePath = path.join(outputDir, `frame_${frame.toString().padStart(4, '0')}.png`);
        await page.screenshot({
            path: framePath,
            omitBackground: true,  // 🔥 关键：保留透明背景
        });

        // 进度显示
        if (frame % 10 === 0 || frame === totalFrames - 1) {
            const progress = Math.round((frame / totalFrames) * 100);
            console.log(`   Progress: ${progress}% (${frame}/${totalFrames} frames)`);
        }
    }

    await browser.close();
    console.log('✅ Capture complete!');
    console.log(`📁 Frames saved to: ${outputDir}`);
    console.log('');
    console.log('🎥 To create a video with transparency, run:');
    console.log(`   ffmpeg -framerate ${fps} -i ${outputDir}/frame_%04d.png -c:v libvpx-vp9 -pix_fmt yuva420p output.webm`);
    console.log('');
    console.log('🎨 To verify transparency, open any PNG in an image viewer with checkerboard background');
}

// 运行捕获
captureTransparentAnimation().catch(console.error);
