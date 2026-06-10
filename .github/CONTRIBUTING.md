# Contributing to Forge Skill

> [中文版](#中文版) | [English](#english)

感谢你对 forge-skill 的兴趣! 这份指南将帮助你了解如何贡献。

---

## English

Thank you for your interest in forge-skill! This guide will help you understand how to contribute.

### Ways to Contribute

| Contribution | Effort | Impact |
|---|---|---|
| Request a new methodology Skill | Low | High |
| Report a bug or quality issue | Low | High |
| Suggest improvements to existing Skill | Medium | High |
| Translate terminologies | Medium | Medium |
| Submit a complete methodology Skill | High | Very High |
| Improve the forging engine | High | Very High |

### Quick Start: Request a New Methodology

1. **Check if it exists**: Search `methods/` directory first
2. **Open an Issue**: Use the "新方法论请求" template
3. **Provide context**: Why do you need this methodology? What problem does it solve?
4. **Identify sources**: List 2-3 primary sources (books, papers, talks) we can research from

### Submitting a Skill (Forge or Write)

**Option A: Let forge-skill forge it (recommended for new contributors)**
1. Open an Issue with the methodology request
2. We'll run forge-skill's full pipeline (6-agent research → extract principles → build Skill → quality check → dual-agent refinement)
3. You review the final SKILL.md

**Option B: Write it yourself**
1. Read [`references/skill-template.md`](references/skill-template.md) for the required structure
2. Write your SKILL.md following the template exactly — every section is mandatory
3. Run `python scripts/quality_check.py methods/<your-skill>/SKILL.md` — all 6 checks must pass
4. Submit a PR using the "方法论 Skill 贡献" template

### Quality Standards

Every SKILL.md must pass these 6 checks (run `quality_check.py`):

| # | Check | Requirement |
|---|-------|-------------|
| 1 | Core Principles | 3-7 principles, each with ≥2 cross-domain evidence |
| 2 | Agentic Protocol | 3 executable steps with research dimensions |
| 3 | Applicability Boundaries | Clearly state when the method does NOT apply |
| 4 | Misuse Detector | ≥3 misuse patterns with detection logic |
| 5 | Honest Boundaries | ≥3 specific limitations (no generic disclaimers) |
| 6 | Research Sources | >50% primary sources; all sources cited |

### Skill Writing Principles

**Must-Do (from [Skill Template](references/skill-template.md)):**

- ✅ Every principle has ≥2 cross-domain evidence
- ✅ Every research step in Step 2 traces back to a specific principle
- ✅ "Not applicable" signals are specific, not generic
- ✅ Honest boundaries contain real, actionable limitations
- ✅ Primary sources account for ≥50%

**Must-Not-Do:**

- ❌ No principle with only 1 evidence
- ❌ No "search for related information" in research steps — every step must derive from a principle
- ❌ No generic disclaimers like "does not constitute professional advice"
- ❌ No fabricated sources; all sources must be verifiable

### Translation Contributions

See [`references/i18n-guide.md`](references/i18n-guide.md) for detailed instructions.

### Code of Conduct

Be respectful. Be constructive. Focus on making methodology skills better.

---

## 中文版

### 贡献方式

| 贡献类型 | 工作量 | 影响力 |
|---------|--------|--------|
| 请求锻造新方法论 Skill | 低 | 高 |
| 报告 Bug 或质量问题 | 低 | 高 |
| 建议改进已有 Skill | 中 | 高 |
| 翻译术语 | 中 | 中 |
| 提交完整的方法论 Skill | 高 | 极高 |
| 改进锻造引擎 | 高 | 极高 |

### 快速入门：请求新方法论

1. 先搜索 `methods/` 目录确认尚未存在
2. 用「新方法论请求」模板开 Issue
3. 提供上下文：你为什么需要这个方法？它解决什么问题？
4. 列出 2-3 个可调研的一手来源（书籍、论文、演讲）

### 提交 Skill（锻造或手写）

**方式 A：由 forge-skill 自动锻造（推荐新贡献者使用）**
1. 开 Issue 描述方法需求
2. 我们会运行完整的 6 路调研→提炼→构建→质量验证→双 Agent 精炼流程
3. 你来审核最终的 SKILL.md

**方式 B：手写 Skill**
1. 阅读 `references/skill-template.md` 了解规定结构
2. 严格按模板撰写——每节都是必填
3. 运行 `python scripts/quality_check.py methods/<your-skill>/SKILL.md`，6 项必须全部通过
4. 用「方法论 Skill 贡献」模板提交 PR

### 质量检查清单

每个 SKILL.md 必须通过 6 项检查：

1. **核心原理**：3-7 个，每个附 ≥2 个跨域证据
2. **操作协议**：3 步可执行，含研究维度
3. **适用边界**：明确写出不适用场景
4. **误用检测器**：≥3 种误用模式+检测逻辑
5. **诚实边界**：≥3 条具体局限（禁止空话）
6. **调研来源**：一手来源 >50%

### 翻译贡献

详见 `references/i18n-guide.md`。

> 本指南由 [Forge Skill — 锻造思维工具](https://github.com/peterfei/forge-skill) 生成
