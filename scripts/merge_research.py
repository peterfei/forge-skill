#!/usr/bin/env python3
"""
merge_research.py — 调研合并统计工具

合并 6 路调研结果，统计来源数量、识别矛盾点、标注信息不足维度，
输出调研 Review 摘要供 Phase 1.5 检查点使用。

用法: python3 merge_research.py <research_dir>
依赖: 无（纯 Python 标准库）
"""

import re
import sys
from pathlib import Path
from collections import defaultdict


RESEARCH_FILES = {
    '01': '经典文献',
    '02': '实践案例',
    '03': '批判视角',
    '04': '跨域迁移',
    '05': '工具化程度',
    '06': '演化时间线',
}

MIN_SOURCES_THRESHOLD = 2  # 低于此数量标注为信息不足


def count_sources(text: str) -> int:
    """粗略统计文本中引用的来源数量。"""
    # 匹配 [N], (Author, Year), Author (Year) 等引用模式
    patterns = [
        r'\[\d+\]',           # [1], [2]
        r'\([A-Z][^)]*,\s*\d{4}\)',  # (Smith, 2020)
        r'[A-Z][a-z]+\s*\(\d{4}\)',  # Smith (2020)
    ]
    count = 0
    for pattern in patterns:
        count += len(re.findall(pattern, text))
    return count


def extract_key_findings(text: str, max_chars: int = 100) -> str:
    """提取调研文件的关键发现（第一段非空内容）。"""
    for line in text.split('\n'):
        line = line.strip()
        if line and len(line) > 10 and not line.startswith('#') and not line.startswith('```'):
            return line[:max_chars] + ('...' if len(line) > max_chars else '')
    return '无关键发现'


def find_contradictions(all_findings: dict) -> list:
    """跨 Agent 识别矛盾点（基于关键词冲突检测）。"""
    contradictions = []
    contradiction_keywords = [
        ('然而', '但是', '相反', 'however', 'but', 'contrary'),
        ('不支持', '反对', '质疑', 'challenge', 'criticize', 'reject'),
        ('误用', '滥用', '局限', 'misuse', 'limitation', 'flaw'),
    ]

    for kw_group in contradiction_keywords:
        agents_with_kw = []
        for agent_id, finding in all_findings.items():
            text_lower = finding.lower()
            if any(kw.lower() in text_lower for kw in kw_group):
                agents_with_kw.append(agent_id)

        if len(agents_with_kw) >= 2:
            contradictions.append({
                'signal': kw_group[0],
                'agents': agents_with_kw,
            })

    return contradictions


def analyze_research_dir(research_dir: str) -> None:
    """分析调研目录，输出 Review 摘要。"""
    research_path = Path(research_dir)
    if not research_path.exists():
        print(f"错误: 调研目录不存在: {research_dir}", file=sys.stderr)
        sys.exit(1)

    findings = {}
    source_counts = {}
    insufficient = []

    print("┌──────────────────┬──────────┬──────────────────────────┐")
    print("│ Agent            │ 来源数量 │ 关键发现                   │")
    print("├──────────────────┼──────────┼──────────────────────────┤")

    for file_prefix, agent_name in RESEARCH_FILES.items():
        # 查找匹配的前缀文件
        matching = list(research_path.glob(f"{file_prefix}-*.md"))
        if not matching:
            print(f"│ {agent_name:<14} │ 缺失     │ 无调研文件               │")
            insufficient.append(agent_name)
            continue

        file_path = matching[0]
        text = file_path.read_text(encoding='utf-8')
        sources = count_sources(text)
        key = extract_key_findings(text)

        findings[file_prefix] = text
        source_counts[file_prefix] = sources

        status = f"{sources} 个" if sources > 0 else "0 个"
        print(f"│ {agent_name:<14} │ {status:<8} │ {key:<24} │")

        if sources < MIN_SOURCES_THRESHOLD:
            insufficient.append(agent_name)

    print("├──────────────────┼──────────┼──────────────────────────┤")

    # 矛盾点检测
    contradictions = find_contradictions(findings)
    print(f"│ 矛盾点            │ {len(contradictions)} 处     │ {'; '.join(f'Agent{c[\"agents\"][0]} vs Agent{c[\"agents\"][1]}' for c in contradictions[:3]) or '无':<24} │")

    # 信息不足维度
    if insufficient:
        print(f"│ 信息不足维度      │ {len(insufficient)} 处     │ {', '.join(insufficient[:3]):<24} │")
    else:
        print(f"│ 信息不足维度      │ 无       │ {'':<24} │")

    print("└──────────────────┴──────────┴──────────────────────────┘")

    # 总计
    total = sum(source_counts.values())
    print(f"\n总计来源数量: {total}")
    print(f"调研文件数: {len(findings)}/{len(RESEARCH_FILES)}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"用法: {sys.argv[0]} <research_dir>", file=sys.stderr)
        sys.exit(1)

    analyze_research_dir(sys.argv[1])
