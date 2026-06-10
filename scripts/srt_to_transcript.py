#!/usr/bin/env python3
"""
srt_to_transcript.py — 字幕清洗工具

将 SRT 字幕文件清洗为纯文本转录，去除时间戳和格式标记，
合并短句，输出干净的研究素材文本。

用法: python3 srt_to_transcript.py <input.srt> [output.txt]
依赖: 无（纯 Python 标准库）
"""

import re
import sys
from pathlib import Path


def clean_srt(srt_text: str) -> str:
    """清洗 SRT 字幕为纯文本。"""
    # 移除 SRT 序号
    lines = srt_text.splitlines()
    cleaned = []

    for line in lines:
        line = line.strip()
        # 跳过空行
        if not line:
            continue
        # 跳过纯数字行（序号）
        if re.match(r'^\d+$', line):
            continue
        # 跳过时间戳行 (00:00:00,000 --> 00:00:00,000)
        if re.match(r'^\d{2}:\d{2}:\d{2}[,\.]\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}[,\.]\d{3}$', line):
            continue
        # 跳过 HTML 标签
        line = re.sub(r'<[^>]+>', '', line)
        # 跳过纯标记行
        if not line or line in ('[Music]', '[Applause]', '(laughter)', '(applause)'):
            continue
        cleaned.append(line)

    return '\n'.join(cleaned)


def merge_short_lines(text: str, min_length: int = 20) -> str:
    """合并过短的连续行为完整句子。"""
    paragraphs = text.split('\n\n')
    merged_paragraphs = []

    for para in paragraphs:
        sentences = para.split('\n')
        merged = []
        buffer = ''

        for sentence in sentences:
            buffer += (' ' if buffer else '') + sentence
            # 如果当前缓冲足够长，或者当前行以句末标点结束
            if len(buffer) >= min_length or sentence[-1:] in '.!?。！？':
                merged.append(buffer)
                buffer = ''

        if buffer:
            merged.append(buffer)

        merged_paragraphs.append('\n'.join(merged))

    return '\n\n'.join(merged_paragraphs)


def process_file(input_path: str, output_path: str = None) -> None:
    """处理单个 SRT 文件。"""
    input_file = Path(input_path)
    if not input_file.exists():
        print(f"错误: 文件不存在: {input_path}", file=sys.stderr)
        sys.exit(1)

    if output_path is None:
        output_path = str(input_file.with_suffix('.txt'))

    srt_text = input_file.read_text(encoding='utf-8')
    cleaned = clean_srt(srt_text)
    merged = merge_short_lines(cleaned)

    Path(output_path).write_text(merged, encoding='utf-8')
    print(f"清洗完成: {input_path} -> {output_path}")
    print(f"  原始行数: {len(srt_text.splitlines())}")
    print(f"  输出行数: {len(merged.splitlines())}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"用法: {sys.argv[0]} <input.srt> [output.txt]", file=sys.stderr)
        sys.exit(1)

    process_file(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
