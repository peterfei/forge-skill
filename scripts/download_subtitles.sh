#!/bin/bash
# download_subtitles.sh — 视频字幕下载工具
# 用于从 YouTube 等平台下载字幕作为调研素材
#
# 依赖: yt-dlp (pip install yt-dlp)
# 用法: ./download_subtitles.sh <video_url> [output_dir]

set -euo pipefail

VIDEO_URL="${1:?用法: $0 <video_url> [output_dir]}"
OUTPUT_DIR="${2:-./subtitles}"

# 创建输出目录
mkdir -p "$OUTPUT_DIR"

# 获取视频标题作为文件名前缀
VIDEO_TITLE=$(yt-dlp --print title "$VIDEO_URL" 2>/dev/null | tr '/' '-' | tr ' ' '_')

echo "正在下载字幕: $VIDEO_TITLE"
echo "视频 URL: $VIDEO_URL"
echo "输出目录: $OUTPUT_DIR"

# 下载所有可用语言的字幕（优先手动字幕，回退自动生成）
yt-dlp \
  --write-sub \
  --write-auto-sub \
  --sub-langs "en,zh-CN,zh-Hans,zh-Hant,ja,ko" \
  --sub-format "srt" \
  --convert-subs "srt" \
  --skip-download \
  -o "$OUTPUT_DIR/${VIDEO_TITLE}" \
  "$VIDEO_URL"

echo "字幕下载完成: $OUTPUT_DIR/${VIDEO_TITLE}*.srt"
