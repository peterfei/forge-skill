# 翻译贡献 Review 流程

> 本文档定义 forge-skill 社区翻译贡献的审核标准和流程。

## 翻译贡献类型

| 类型 | 内容 | 复杂度 | 审核要求 |
|------|------|--------|---------|
| 术语补充 | 新增 i18n/term-glossary/ 词条 | 低 | 1 人审核 |
| 术语修正 | 修正已有术语翻译 | 低 | 1 人审核 |
| Skill 翻译 | 翻译完整 methods/*/SKILL.md | 高 | 2 人审核 |
| 文档翻译 | 翻译 README/CONTRIBUTING 等 | 中 | 1 人审核 |

## Review 流程

### 术语补充/修正

```
提交者 → PR → Review Checklist → 1 位 Reviewer 审核 → 通过/修改
```

**Review Checklist**：
- [ ] 目标语言中是否有已有的对应术语？（避免重复）
- [ ] 翻译是否在专业文献中已有约定俗成的译法？（优先使用公认译法）
- [ ] 如果有多语言术语表，新增术语是否在每种已有语言中都有一致映射？
- [ ] 术语表 YAML 格式正确（`term: translated_term`）

### Skill 完整翻译

```
提交者 → PR → 格式 Review → 术语 Review → 语言 Review → 2 人批准 → 通过
```

**Phase 1: 格式 Review**
- [ ] 翻译后的 SKILL.md 保持了原始的 frontmatter 结构
- [ ] 所有章节标题层级（##/###/####）与原文一致
- [ ] 表格格式没有被破坏
- [ ] 链接和引用路径正确

**Phase 2: 术语 Review**
- [ ] 核心方法学术语与 i18n/term-glossary/ 一致
- [ ] 首次出现的术语标注了原文（如：涌现 Emergence）
- [ ] 方法论的专有名词保留了原文标注（如：Build-Measure-Learn 循环）

**Phase 3: 语言 Review**
- [ ] 翻译准确传达了原文含义（不仅字面准确，更要语义准确）
- [ ] 学术引用格式正确（作者名、书名、年份以目标语言习惯呈现）
- [ ] 没有遗漏原文的任何章节

### 审查时间承诺

| 贡献类型 | 期望审核时间 |
|---------|------------|
| 术语补充/修正 | 3 个工作日内 |
| Skill 翻译 | 7 个工作日内 |
| 文档翻译 | 5 个工作日内 |

## Reviewer 指南

### 成为 Reviewer

- 至少提交过 2 个术语翻译贡献
- 对目标语言有母语级掌握
- 了解 forge-skill 的 Skill 结构和术语体系

### Reviewer 职责

1. **准确性**：确认翻译忠实于原文含义
2. **一致性**：确保术语与已有机翻一致
3. **完整性**：无遗漏章节
4. **建设性**：提修改建议而非仅指出问题

### 翻译争议处理

当翻译选择存在争议时：
1. Reviewer 和提交者先讨论，各提供依据（文献引用、使用频度等）
2. 如果无法达成一致，引入第三位 Reviewer 仲裁
3. 最终决策基于：专业文献使用频度 > 直译准确性 > 个人偏好

## 术语表维护

### 新增术语规则

```
新增术语条目命名规范：
  key: english_term
  zh-CN: 中文翻译
  ja: 日本語訳（如有）
  ko: 한국어 번역（如有）

示例：
  first_principles:
    en: First Principles
    zh-CN: 第一性原理
    ja: 第一原理
    ko: 제1원리
```

### 术语冲突解决

当同一概念在不同方法论中有不同常用翻译时：
- 在术语表中标注适用范围
  ```yaml
  leverage:
    en: Leverage
    zh-CN:
      general: 杠杆
      systems_thinking: 杠杆点
      finance: 杠杆效应
  ```

## 自动化检查

CI 流水线将自动执行：
1. YAML 格式有效性
2. SKILL.md 结构完整性
3. 与术语表的一致性检查（`scripts/check_terms.py`）

> 本流程由 [Forge Skill — 锻造思维工具](https://github.com/peterfei/forge-skill) 生成
