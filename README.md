# Forge Skill — 锻造任何领域的思维工具

![forge-skill logo](assets/logo-horizontal.svg)

<p align="center">
  <img src="assets/readme-banner.gif" alt="forge-skill · 从方法论到 Skill 的锻造过程" width="800" />
</p>

> 不是角色扮演一个智者，而是锻造一把可执行的思维工具。
> 输入方法论名称或模糊需求，自动深度调研 → 方法论结构化提炼 → 生成可运行的思维工具 Skill。

[English](README_EN.md)

---

## 这是什么？

Forge Skill 是一个基于 [Agent Skills](https://skills.sh) 开放协议的思维工具锻造引擎。它将经典方法论（第一性原理、系统思维、TRIZ 等）转化为可执行的 AI Skill，让 AI 不再"扮演专家"，而是按照方法论的精确流程帮你分析问题。

**一句话**：把方法论变成你随时调用的认知瑞士军刀。

## 核心特性

- **锻造引擎**：输入方法论名 → 6 路并行调研 → 三重验证提炼 → 生成可执行 Skill
- **诊断推荐**：不确定用什么方法？描述你的困惑，引擎推荐最匹配的方法论
- **误用检测**：每个 Skill 内置误用检测器，主动警告方法论被错误应用
- **诚实边界**：明确标注方法的局限，不伪装万能
- **跨 Runtime**：兼容 Claude Code、Codex CLI、Cursor、Gemini CLI 等 50+ 运行时
- **多语言**：中文、英语、日语、韩语等

## 快速开始

```bash
# 安装（需要 Agent Skills 运行时，如 Claude Code）
npx skills add peterfei/forge-skill

# 直接锻造（明确方法论）
> 锻造一个第一性原理

# 诊断推荐（模糊需求）
> 我的产品留存率持续下降，不知道怎么办
```

## 锻造流程

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

## 方法论库

> 点击安装命令可快速添加到你的 Agent Skills 工具箱。

### 思维工具

| # | 方法论 | 领域 | 一句话定位 | 安装 |
|---|--------|------|-----------|------|
| F1 | [第一性原理](https://github.com/peterfei/forge-skill-first-principles-skill) | 解决问题/创新 | 回归基本事实，从物理极限重新推导 | `npx skills add peterfei/forge-skill-first-principles-skill` |
| F2 | [系统思维](https://github.com/peterfei/forge-skill-systems-thinking-skill) | 复杂系统分析 | 用因果回路图看清整体结构和反馈循环 | `npx skills add peterfei/forge-skill-systems-thinking-skill` |
| F7 | [费曼学习法](https://github.com/peterfei/forge-skill-feynman-learning-skill) | 学习/教学 | 用教别人的方式检验自己是否真正理解 | `npx skills add peterfei/forge-skill-feynman-learning-skill` |
| F12 | [奥卡姆剃刀](https://github.com/peterfei/forge-skill-occams-razor-skill) | 决策/简化 | 在同等解释力下选择最少假设的方案 | `npx skills add peterfei/forge-skill-occams-razor-skill` |
| F14 | [二阶思维](https://github.com/peterfei/forge-skill-second-order-thinking-skill) | 决策/系统分析 | 推演决策的连锁高阶后果，而非只看直接效果 | `npx skills add peterfei/forge-skill-second-order-thinking-skill` |
| F16 | [逆向思维](https://github.com/peterfei/forge-skill-inversion-skill) | 决策/风险预判 | 不问"怎么赢"，问"怎么死"然后避开 | `npx skills add peterfei/forge-skill-inversion-skill` |
| F18 | [横向思维](https://github.com/peterfei/forge-skill-lateral-thinking-skill) | 创意/问题解决 | 打破固有思维定式，从非传统角度寻找创造性解法 | `npx skills add peterfei/forge-skill-lateral-thinking-skill` |
| F19 | [帕累托法则](https://github.com/peterfei/forge-skill-pareto-principle-skill) | 资源聚焦/优化 | 识别关键少数，集中资源获取非线性回报 | `npx skills add peterfei/forge-skill-pareto-principle-skill` |

### 商业与战略

| # | 方法论 | 领域 | 一句话定位 | 安装 |
|---|--------|------|-----------|------|
| F3 | [增长黑客](https://github.com/peterfei/forge-skill-growth-hacking-skill) | 产品增长/留存 | 以数据驱动的实验循环寻找增长杠杆 | `npx skills add peterfei/forge-skill-growth-hacking-skill` |
| F4 | [精益创业](https://github.com/peterfei/forge-skill-lean-startup-skill) | 创业验证 | 用最小可行产品快速验证假设 | `npx skills add peterfei/forge-skill-lean-startup-skill` |
| F8 | [改善（Kaizen）](https://github.com/peterfei/forge-skill-kaizen-skill) | 持续改进/管理 | 小步快跑的渐进式优化哲学 | `npx skills add peterfei/forge-skill-kaizen-skill` |
| F9 | [事前验尸（Premortem）](https://github.com/peterfei/forge-skill-premortem-skill) | 风险预判/决策 | 假设项目已失败，反推所有可能死因 | `npx skills add peterfei/forge-skill-premortem-skill` |
| F10 | [五力分析](https://github.com/peterfei/forge-skill-five-forces-skill) | 竞争战略 | 从五个维度评估行业竞争格局 | `npx skills add peterfei/forge-skill-five-forces-skill` |
| F17 | [SWOT 分析](https://github.com/peterfei/forge-skill-swot-skill) | 战略/规划 | 从优势、劣势、机会、威胁四维度交叉制定策略 | `npx skills add peterfei/forge-skill-swot-skill` |
| F20 | [蓝海战略](https://github.com/peterfei/forge-skill-blue-ocean-strategy-skill) | 战略创新/竞争突围 | 价值创新开创无人争抢的市场空间 | `npx skills add peterfei/forge-skill-blue-ocean-strategy-skill` |
| F21 | [商业模式画布](https://github.com/peterfei/forge-skill-business-model-canvas-skill) | 商业设计/创业 | 9 个构造块系统化描述商业逻辑 | `npx skills add peterfei/forge-skill-business-model-canvas-skill` |
| F22 | [价值链分析](https://github.com/peterfei/forge-skill-value-chain-skill) | 竞争优势/成本优化 | 分解企业活动，识别成本与差异化来源 | `npx skills add peterfei/forge-skill-value-chain-skill` |
| F24 | [OKR](https://github.com/peterfei/forge-skill-okr-skill) | 目标管理/组织协同 | 聚焦少数要事，量化可测量的目标与关键结果 | `npx skills add peterfei/forge-skill-okr-skill` |

### 设计与创新

| # | 方法论 | 领域 | 一句话定位 | 安装 |
|---|--------|------|-----------|------|
| F5 | [设计思维](https://github.com/peterfei/forge-skill-design-thinking-skill) | 产品设计/创新 | 以用户共情为起点的五步创新框架 | `npx skills add peterfei/forge-skill-design-thinking-skill` |
| F11 | [双钻模型](https://github.com/peterfei/forge-skill-double-diamond-skill) | 设计流程/问题定义 | 发散→收敛→发散→收敛的结构化流程 | `npx skills add peterfei/forge-skill-double-diamond-skill` |
| F15 | [JTBD](https://github.com/peterfei/forge-skill-jtbd-skill) | 产品设计/需求分析 | 用户不是买产品，而是"雇佣"产品完成特定任务 | `npx skills add peterfei/forge-skill-jtbd-skill` |

### 问题解决

| # | 方法论 | 领域 | 一句话定位 | 安装 |
|---|--------|------|-----------|------|
| F6 | [TRIZ](https://github.com/peterfei/forge-skill-triz-skill) | 工程创新/矛盾解决 | 40 个发明原理系统化解决技术矛盾 | `npx skills add peterfei/forge-skill-triz-skill` |
| F13 | [Cynefin 框架](https://github.com/peterfei/forge-skill-cynefin-skill) | 决策/复杂度分类 | 按 5 域分类匹配决策策略，避免跨域误判 | `npx skills add peterfei/forge-skill-cynefin-skill` |
| F14 | [场景规划](https://github.com/peterfei/forge-skill-scenario-planning-skill) | 战略前瞻/不确定性决策 | 构建多个合理未来场景，改变心智模型应对深度不确定性 | `npx skills add peterfei/forge-skill-scenario-planning-skill` |
| F23 | [5 Whys](https://github.com/peterfei/forge-skill-five-whys-skill) | 根因分析/质量改进 | 连续追问穿透表面症状，定位系统性根因 | `npx skills add peterfei/forge-skill-five-whys-skill` |

## 生态

Forge Skill 是三项目生态的一部分：

```
nuwa-skill（女娲）  → 蒸馏人的认知框架（WHO）
forge-skill（熔炉） → 锻造方法论工具（HOW）
darwin-skill（达尔文）→ 优化已有 Skill（BETTER）
```

- [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) — 蒸馏名人思维方式
- [darwin-skill](https://github.com/alchaincyf/darwin-skill) — 持续进化优化 Skill

## License

[MIT](LICENSE)
