# Forge Skill — Forge Thinking Tools for Any Domain

![forge-skill logo](assets/logo-horizontal.svg)

![forge-skill hero](assets/hero-en.svg)

> Don't role-play an expert. Forge an executable thinking tool.
> Input a methodology name or a vague need → auto deep research → structured extraction → generate a runnable AI Skill.

[中文](README.md)

---

## What is this?

Forge Skill is a thinking tool forge engine built on the [Agent Skills](https://skills.sh) open protocol. It transforms classic methodologies (First Principles, Systems Thinking, TRIZ, etc.) into executable AI Skills — making AI follow precise methodological processes instead of "role-playing experts."

**In one sentence**: Turn methodologies into cognitive Swiss Army knives you can invoke anytime.

## Core Features

- **Forge Engine**: Input a methodology name → 6-way parallel research → triple-verified extraction → generate executable Skill
- **Diagnostic Recommendation**: Not sure which method to use? Describe your problem, the engine recommends the best match
- **Misuse Detection**: Each Skill has a built-in misuse detector that proactively warns when a methodology is misapplied
- **Honest Boundaries**: Clearly labels method limitations — never pretends to be universal
- **Cross-Runtime**: Compatible with Claude Code, Codex CLI, Cursor, Gemini CLI, and 50+ runtimes
- **Multilingual**: Chinese, English, Japanese, Korean, and more

## Quick Start

```bash
# Install (requires an Agent Skills runtime, e.g., Claude Code)
npx skills add peterfei/forge-skill

# Direct forge (specific methodology)
> Forge a First Principles skill

# Diagnostic recommendation (vague need)
> My product retention keeps dropping, I don't know what to do
```

## Forge Pipeline

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

## Methodology Library

### Thinking Tools

| # | Methodology | Domain | One-line Description |
|---|-------------|--------|---------------------|
| F1 | First Principles | Problem-solving/Innovation | Reduce to fundamental truths, reason up from physical limits |
| F2 | Systems Thinking | Complex Systems | See overall structure and feedback loops through causal loop diagrams |
| F7 | Feynman Learning Technique | Learning/Teaching | Test your understanding by teaching it to others |
| F12 | Occam's Razor | Decision/Simplification | Choose the solution with fewest assumptions given equal explanatory power |
| F14 | Second-Order Thinking | Decision/Systems | Trace cascading higher-order consequences beyond immediate effects |
| F16 | Inversion | Decision/Risk | Avoid failure by asking "what causes certain failure" then preventing it |
| F18 | Lateral Thinking | Creativity/Problem-solving | Break fixed thinking patterns, find creative solutions from unconventional angles |

### Business & Strategy

| # | Methodology | Domain | One-line Description |
|---|-------------|--------|---------------------|
| F3 | Growth Hacking | Product Growth/Retention | Data-driven experimentation cycles to find growth levers |
| F4 | Lean Startup | Startup Validation | Validate hypotheses rapidly with minimum viable products |
| F8 | Kaizen | Continuous Improvement | Small-step incremental optimization philosophy |
| F9 | Premortem | Risk Anticipation/Decision | Assume the project failed, reverse-engineer all possible causes |
| F10 | Five Forces | Competitive Strategy | Assess industry competitive landscape from five dimensions |
| F17 | SWOT Analysis | Strategy/Planning | Cross-analyze strengths, weaknesses, opportunities, threats to formulate strategy |

### Design & Innovation

| # | Methodology | Domain | One-line Description |
|---|-------------|--------|---------------------|
| F5 | Design Thinking | Product Design/Innovation | Five-step innovation framework starting from user empathy |
| F11 | Double Diamond | Design Process/Problem Definition | Diverge→converge→diverge→converge structured process |
| F15 | JTBD | Product Design/Needs | People "hire" products to get jobs done, not buy features |

### Problem Solving

| # | Methodology | Domain | One-line Description |
|---|-------------|--------|---------------------|
| F6 | TRIZ | Engineering/Contradiction Resolution | 40 invention principles for systematic resolution of technical contradictions |
| F13 | Cynefin | Decision/Complexity | Classify problems into 5 domains, match decision strategy to domain |

## Ecosystem

Forge Skill is part of a three-project ecosystem:

```
nuwa-skill   → Distill human cognitive frameworks (WHO)
forge-skill  → Forge methodology tools (HOW)
darwin-skill → Optimize existing Skills (BETTER)
```

- [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) — Distill notable thinkers' mindsets
- [darwin-skill](https://github.com/alchaincyf/darwin-skill) — Continuously evolve and optimize Skills

## License

[MIT](LICENSE)
