# Forge Skill — 锻造任何领域的思维工具

> 不是角色扮演一个智者，而是锻造一把可执行的思维工具。
> 输入方法论名称或模糊需求，自动深度调研 → 方法论结构化提炼 → 生成可运行的思维工具 Skill。

[English](#english) | [简体中文](#简体中文)

---

## 简体中文

### 这是什么？

Forge Skill 是一个基于 [Agent Skills](https://skills.sh) 开放协议的思维工具锻造引擎。它将经典方法论（第一性原理、系统思维、TRIZ 等）转化为可执行的 AI Skill，让 AI 不再"扮演专家"，而是按照方法论的精确流程帮你分析问题。

**一句话**：把方法论变成你随时调用的认知瑞士军刀。

### 核心特性

- **锻造引擎**：输入方法论名 → 6 路并行调研 → 三重验证提炼 → 生成可执行 Skill
- **诊断推荐**：不确定用什么方法？描述你的困惑，引擎推荐最匹配的方法论
- **误用检测**：每个 Skill 内置误用检测器，主动警告方法论被错误应用
- **诚实边界**：明确标注方法的局限，不伪装万能
- **跨 Runtime**：兼容 Claude Code、Codex CLI、Cursor、Gemini CLI 等 50+ 运行时
- **多语言**：中文、英语、日语、韩语等

### 快速开始

```bash
# 安装（需要 Agent Skills 运行时，如 Claude Code）
npx skills add peterfei/forge-skill

# 直接锻造（明确方法论）
> 锻造一个第一性原理

# 诊断推荐（模糊需求）
> 我的产品留存率持续下降，不知道怎么办
```

### 锻造流程

```
Phase 0  入口分流 → 直接锻造 or 诊断推荐
Phase 1  多源采集 → 6 路并行调研（文献/案例/批评/跨域/工具/时间线）
Phase 1.5 调研 Review → 展示摘要，确认质量
Phase 2  方法论提炼 → 三重验证核心原理 + 操作流程 + 适用边界
Phase 2.5 提炼确认 → 展示摘要，确认方向
Phase 3  Skill 构建 → Agentic Protocol + 误用检测器 + 诚实边界
Phase 4  质量验证 → 已知案例 + 边缘案例 + 误用检测验证
Phase 5  双 Agent 精炼 → 方法论评审 + 可用性评审
```

### 预锻造方法论库

| # | 方法论 | 领域 | 一句话定位 |
|---|--------|------|-----------|
| F1 | 第一性原理 | 解决问题/创新 | 回归基本事实，从物理极限重新推导 |
| F2 | 系统思维 | 复杂系统分析 | 用因果回路图看清整体结构和反馈循环 |
| F3 | 增长黑客 | 产品增长/留存 | 以数据驱动的实验循环寻找增长杠杆 |
| F4 | 精益创业 | 创业验证 | 用最小可行产品快速验证假设 |
| F5 | 设计思维 | 产品设计/创新 | 以用户共情为起点的五步创新框架 |
| F6 | TRIZ | 工程创新/矛盾解决 | 40 个发明原理系统化解决技术矛盾 |
| F7 | 费曼学习法 | 学习/教学 | 用教别人的方式检验自己是否真正理解 |
| F8 | 改善（Kaizen） | 持续改进/管理 | 小步快跑的渐进式优化哲学 |
| F9 | 事前验尸（Premortem） | 风险预判/决策 | 假设项目已失败，反推所有可能死因 |
| F10 | 五力分析 | 竞争战略 | 从五个维度评估行业竞争格局 |
| F11 | 双钻模型 | 设计流程/问题定义 | 发散→收敛→发散→收敛的结构化流程 |
| F12 | 奥卡姆剃刀 | 决策/简化 | 在同等解释力下选择最少假设的方案 |

### 生态

Forge Skill 是三项目生态的一部分：

```
nuwa-skill（女娲）  → 蒸馏人的认知框架（WHO）
forge-skill（熔炉） → 锻造方法论工具（HOW）
darwin-skill（达尔文）→ 优化已有 Skill（BETTER）
```

- [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) — 蒸馏名人思维方式
- [darwin-skill](https://github.com/alchaincyf/darwin-skill) — 持续进化优化 Skill

### License

[MIT](LICENSE)

---

## English

### What is this?

Forge Skill is a thinking tool forge engine based on the [Agent Skills](https://skills.sh) open protocol. It transforms classic methodologies (First Principles, Systems Thinking, TRIZ, etc.) into executable AI Skills — making AI follow precise methodological processes instead of "role-playing experts."

**In one sentence**: Turn methodologies into cognitive Swiss Army knives you can invoke anytime.

### Core Features

- **Forge Engine**: Input a methodology name → 6-way parallel research → triple-verified extraction → generate executable Skill
- **Diagnostic Recommendation**: Not sure which method to use? Describe your problem, the engine recommends the best match
- **Misuse Detection**: Each Skill has a built-in misuse detector that proactively warns when a methodology is misapplied
- **Honest Boundaries**: Clearly labels method limitations — never pretends to be universal
- **Cross-Runtime**: Compatible with Claude Code, Codex CLI, Cursor, Gemini CLI, and 50+ runtimes
- **Multilingual**: Chinese, English, Japanese, Korean, and more

### Quick Start

```bash
# Install (requires an Agent Skills runtime, e.g., Claude Code)
npx skills add peterfei/forge-skill

# Direct forge (specific methodology)
> Forge a First Principles skill

# Diagnostic recommendation (vague need)
> My product retention keeps dropping, I don't know what to do
```

### Forge Pipeline

```
Phase 0   Entry Routing → Direct forge or diagnostic recommendation
Phase 1   Multi-source Collection → 6-way parallel research (literature/cases/criticism/cross-domain/tools/timeline)
Phase 1.5 Research Review → Show summary, confirm quality
Phase 2   Methodology Extraction → Triple-verified core principles + operational flow + applicability boundaries
Phase 2.5 Extraction Confirmation → Show summary, confirm direction
Phase 3   Skill Construction → Agentic Protocol + misuse detector + honest boundaries
Phase 4   Quality Validation → Known cases + edge cases + misuse detection verification
Phase 5   Dual Agent Refinement → Methodology review + usability review
```

### Pre-forged Methodology Library

| # | Methodology | Domain | One-line Description |
|---|-------------|--------|---------------------|
| F1 | First Principles | Problem-solving/Innovation | Reduce to fundamental truths, reason up from physical limits |
| F2 | Systems Thinking | Complex Systems | See overall structure and feedback loops through causal loop diagrams |
| F3 | Growth Hacking | Product Growth/Retention | Data-driven experimentation cycles to find growth levers |
| F4 | Lean Startup | Startup Validation | Validate hypotheses rapidly with minimum viable products |
| F5 | Design Thinking | Product Design/Innovation | Five-step innovation framework starting from user empathy |
| F6 | TRIZ | Engineering/Contradiction Resolution | 40 invention principles for systematic resolution of technical contradictions |
| F7 | Feynman Learning Technique | Learning/Teaching | Test your understanding by teaching it to others |
| F8 | Kaizen | Continuous Improvement | Small-step incremental optimization philosophy |
| F9 | Premortem | Risk Anticipation/Decision | Assume the project failed, reverse-engineer all possible causes of death |
| F10 | Five Forces | Competitive Strategy | Assess industry competitive landscape from five dimensions |
| F11 | Double Diamond | Design Process/Problem Definition | Diverge→converge→diverge→converge structured process |
| F12 | Occam's Razor | Decision/Simplification | Choose the solution with fewest assumptions given equal explanatory power |

### Ecosystem

Forge Skill is part of a three-project ecosystem:

```
nuwa-skill   → Distill human cognitive frameworks (WHO)
forge-skill  → Forge methodology tools (HOW)
darwin-skill → Optimize existing Skills (BETTER)
```

- [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) — Distill notable thinkers' mindsets
- [darwin-skill](https://github.com/alchaincyf/darwin-skill) — Continuously evolve and optimize Skills

### License

[MIT](LICENSE)
