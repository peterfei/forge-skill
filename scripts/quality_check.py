#!/usr/bin/env python3
"""
quality_check.py — Skill 质量检查工具

对锻造完成的 SKILL.md 执行 6 项质量检查，输出通过/不通过结果。
用于 Phase 4 质量验证的自动化辅助。

用法: python3 quality_check.py <skill.md>
依赖: 无（纯 Python 标准库）
"""

import re
import sys
from pathlib import Path


def load_skill(path: str) -> str:
    """加载 SKILL.md 文件。"""
    p = Path(path)
    if not p.exists():
        print(f"错误: 文件不存在: {path}", file=sys.stderr)
        sys.exit(1)
    return p.read_text(encoding='utf-8')


def check_principles(text: str) -> dict:
    """检查 1: 核心原理数量（3-7 个，每个有跨域证据）。"""
    # 查找核心原理章节（## 标题开头，后可能有约束文本）
    principle_match = re.search(
        r'^##\s*(?:核心原理|Core Principles)[^\n]*\n((?:.|\n)*?)(?=^##\s(?!核心原理|Core)|\Z)',
        text, re.IGNORECASE | re.MULTILINE
    )

    if not principle_match:
        return {'pass': False, 'detail': '未找到核心原理章节'}

    section = principle_match.group(1)
    # 计算原理数量（以 ### 开头的子标题，支持中英文编号）
    principles = re.findall(r'###\s*(?:原理|Principle)\s*\d+', section, re.IGNORECASE)
    count = len(principles)

    # 检查跨域证据
    cross_domain = re.findall(r'跨域|cross.domain|领域', section, re.IGNORECASE)
    has_evidence = len(cross_domain) >= count

    passed = 3 <= count <= 7 and has_evidence
    return {
        'pass': passed,
        'detail': f'核心原理 {count} 个（要求 3-7）' + (' ✓' if 3 <= count <= 7 else ' ✗')
                  + f'，跨域证据 {"有" if has_evidence else "无"}'
    }


def check_protocol(text: str) -> dict:
    """检查 2: 操作协议可执行性（有 Step 1/2/3 结构）。"""
    protocol_match = re.search(
        r'^##\s*(?:操作协议|Agentic Protocol)[^\n]*\n((?:.|\n)*?)(?=^##\s(?!操作|Agentic|\Z))',
        text, re.IGNORECASE | re.MULTILINE
    )

    if not protocol_match:
        return {'pass': False, 'detail': '未找到操作协议章节'}

    section = protocol_match.group(1)
    steps = re.findall(r'###\s*Step\s+\d+', section, re.IGNORECASE)
    count = len(steps)

    # 检查是否有研究维度
    has_research_dims = bool(re.search(r'研究维度|维度|dimension', section, re.IGNORECASE))

    # 检查 Step 2 中是否有通用指令（只检查研究维度/Step 2 部分，排除禁止说明中的引用）
    step2_match = re.search(r'Step\s*2[^\n]*\n((?:.|\n)*?)(?=Step\s*3|Phase\s|\n###\s|\Z)', section, re.IGNORECASE)
    has_generic = False
    if step2_match:
        step2_text = step2_match.group(1)
        # 排除引号内的文字（如"禁止使用通用'搜索相关信息'"）
        clean_step2 = re.sub(r'[""[].*?[""\]]', '', step2_text)
        has_generic = bool(re.search(r'搜索相关信息|全面了解背景|查找资料', clean_step2))

    passed = count >= 3 and has_research_dims and not has_generic
    return {
        'pass': passed,
        'detail': f'操作步骤 {count} 个（要求 ≥3）' + (' ✓' if count >= 3 else ' ✗')
                  + f'，研究维度 {"有" if has_research_dims else "无"}'
                  + (' ✗ 含通用指令' if has_generic else '')
    }


def check_boundaries(text: str) -> dict:
    """检查 3: 适用边界明确性（写出不适用场景和误用模式）。"""
    # 检查不适用场景
    has_inapplicable = bool(re.search(
        r'不适用|不擅长|not.applicable|不适合', text, re.IGNORECASE
    ))

    # 检查误用模式
    has_misuse = bool(re.search(
        r'误用|misuse|误用模式|误用检测', text, re.IGNORECASE
    ))

    passed = has_inapplicable and has_misuse
    return {
        'pass': passed,
        'detail': f'不适用场景 {"有" if has_inapplicable else "无"}'
                  + f'，误用模式 {"有" if has_misuse else "无"}'
    }


def check_misuse_detector(text: str) -> dict:
    """检查 4: 误用检测器覆盖度（≥3 种误用模式）。"""
    detector_match = re.search(
        r'^##\s*(?:误用检测器|Misuse Detector)[^\n]*\n((?:.|\n)*?)(?=^##\s(?!误用|Misuse)|\Z)',
        text, re.IGNORECASE | re.MULTILINE
    )

    if not detector_match:
        return {'pass': False, 'detail': '未找到误用检测器章节'}

    section = detector_match.group(1)
    # 计算误用模式数量（表格行）
    rows = re.findall(r'\|\s*[^|]+\|', section)
    # 减去表头和分隔线
    mode_count = max(0, len(rows) - 2)

    passed = mode_count >= 3
    return {
        'pass': passed,
        'detail': f'误用模式 {mode_count} 个（要求 ≥3）' + (' ✓' if passed else ' ✗')
    }


def check_honesty(text: str) -> dict:
    """检查 5: 诚实边界（≥3 条具体局限，禁止空话）。"""
    honesty_match = re.search(
        r'^##\s*(?:诚实边界|Honest Boundaries)[^\n]*\n((?:.|\n)*?)(?=^##\s(?!诚实|Honest)|\Z)',
        text, re.IGNORECASE | re.MULTILINE
    )

    if not honesty_match:
        return {'pass': False, 'detail': '未找到诚实边界章节'}

    section = honesty_match.group(1)

    # 检查是否有空话
    has_generic = bool(re.search(
        r'不能替代专业建议|not.replace.professional|不构成投资建议',
        section, re.IGNORECASE
    ))

    # 计算具体局限数量（列表项）
    limitations = re.findall(r'(?:^|\n)\s*\d+\.\s+\*\*', section)

    passed = len(limitations) >= 3 and not has_generic
    return {
        'pass': passed,
        'detail': f'具体局限 {len(limitations)} 条（要求 ≥3）' + (' ✓' if len(limitations) >= 3 else ' ✗')
                  + (' ✗ 含空话' if has_generic else '')
    }


def check_sources(text: str) -> dict:
    """检查 6: 调研来源（一手来源占比须 >50%）。"""
    source_match = re.search(
        r'^##\s*(?:调研来源|Sources|References)[^\n]*\n((?:.|\n)*?)(?=^##\s(?!调研|Sources|Ref)|\Z)',
        text, re.IGNORECASE | re.MULTILINE
    )

    if not source_match:
        return {'pass': False, 'detail': '未找到调研来源章节'}

    section = source_match.group(1)
    # 支持表格和编号列表两种格式
    table_rows = len(re.findall(r'\|\s*\d+', section))
    numbered_items = len(re.findall(r'^\s*\d+\.', section, re.MULTILINE))
    total = max(table_rows, numbered_items)
    first_hand = len(re.findall(r'一手|first.hand|primary', section, re.IGNORECASE))

    if total == 0:
        return {'pass': False, 'detail': '未找到来源条目'}

    ratio = first_hand / total
    passed = ratio > 0.5
    return {
        'pass': passed,
        'detail': f'来源 {total} 个，一手 {first_hand} 个（占比 {ratio:.0%}，要求 >50%）'
                  + (' ✓' if passed else ' ✗')
    }


def run_quality_check(skill_path: str) -> None:
    """运行全部质量检查。"""
    text = load_skill(skill_path)

    checks = [
        ('核心原理数量', check_principles),
        ('操作协议可执行性', check_protocol),
        ('适用边界明确性', check_boundaries),
        ('误用检测器', check_misuse_detector),
        ('诚实边界', check_honesty),
        ('调研来源', check_sources),
    ]

    print(f"质量检查报告: {skill_path}")
    print("=" * 60)

    passed = 0
    failed = 0

    for name, check_fn in checks:
        result = check_fn(text)
        status = "PASS" if result['pass'] else "FAIL"
        icon = "✓" if result['pass'] else "✗"
        print(f"  [{status}] {name}: {result['detail']}")

        if result['pass']:
            passed += 1
        else:
            failed += 1

    print("=" * 60)
    print(f"结果: {passed}/{len(checks)} 通过, {failed}/{len(checks)} 不通过")

    if failed > 0:
        print(f"\n建议: 修复 {failed} 项不通过的检查后再交付。")
        sys.exit(1)
    else:
        print("\n所有检查通过。Skill 质量达标。")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"用法: {sys.argv[0]} <skill.md>", file=sys.stderr)
        sys.exit(1)

    run_quality_check(sys.argv[1])
