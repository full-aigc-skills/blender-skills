---
name: blender-sequence-editing
description: Assemble editable Blender VSE timelines from images, image sequences, scenes, movies, text, and sound, including timing, speed, transitions, audio fades, compositor modifiers, and verified local output.
---

# Blender sequence editing

Use approved local media and explicit frame, channel, resolution and FPS requirements. Choose IMAGE_SEQUENCE for numbered rendered frames, SCENE for an editable Blender scene, and TEXT for local titles or captions. Place strips on deliberate channels, trim with final frame bounds, and overlap clips only for an intended transition.

Use CROSS, GAMMA_CROSS or WIPE only on overlapping visual strips. SOUND_CROSSFADE is implemented as opposing volume keyframes because Blender 5.2 does not expose it as an Effect Strip. Set speed through a SPEED strip and use a compositor modifier only with an existing CompositorNodeTree group.

Before export, inspect strip names, types, channels and frame ranges. For long or restartable output, render a durable frame sequence and submit COMPOSE_VIDEO. Probe the resulting MP4 for dimensions, frame rate, duration and required audio stream, then reopen the `.blend` to verify editability.

This Skill edits a supplied timeline; it does not create story structure, authorize external publishing or replace a dedicated audio-mixing workflow.

## 什么时候使用（When to Use）

已有素材需要在 Blender VSE 中完成可编辑编排、裁切、速度、转场、标题、音频淡化或本地输出时使用。

## 输入与前置条件（Prerequisites）

- 批准的本地媒体、FPS、分辨率、帧范围、频道规划、时码和音频要求。
- 素材序列必须可枚举；重叠仅用于明确转场，输出目录需授权。

## 执行流程（Workflow）

Step 1. 探测媒体属性并建立时间线基准，不混用不明 FPS。
Step 2. 按类型创建 strip，设置开始/结束帧和频道，避免无意覆盖。
Step 3. 配置 speed、视觉转场、文本和音频关键帧；检查实际重叠区间。
Step 4. 检查 strip 清单与时间线，再生成持久帧序列或提交视频合成作业。
Step 5. 探测输出并重开 `.blend` 验证可编辑性。

## 验证与交付证据（Validation）

提供 strip 名称、类型、频道、帧范围、速度/转场参数、音频流以及输出尺寸、FPS、时长和重开结果。

## Rules 与能力边界（不适用场景）

只编辑已提供时间线，不创作故事结构、不授权外部发布，也不替代专业混音或版权审核。

## Gotchas（常见问题与恢复）

- 音画不同步：核对源 FPS、采样率和裁切边界。
- 转场无效：确认视觉 strip 真正重叠且类型受支持。
- 输出缺音轨：检查 SOUND strip、音量关键帧与媒体探测结果。
