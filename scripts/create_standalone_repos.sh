#!/bin/bash
# create_standalone_repos.sh — 为每个方法论 Skill 创建独立 GitHub 仓库并推送
set +e
cd "$(dirname "$0")/.."

get_chinese_name() {
  case "$1" in
    first-principles-skill) echo "第一性原理" ;;
    systems-thinking-skill) echo "系统思维" ;;
    growth-hacking-skill)   echo "增长黑客" ;;
    lean-startup-skill)     echo "精益创业" ;;
    design-thinking-skill)  echo "设计思维" ;;
    triz-skill)             echo "TRIZ" ;;
    feynman-learning-skill) echo "费曼学习法" ;;
    kaizen-skill)           echo "改善（Kaizen）" ;;
    premortem-skill)        echo "事前验尸" ;;
    five-forces-skill)      echo "五力分析" ;;
    double-diamond-skill)   echo "双钻模型" ;;
    occams-razor-skill)        echo "奥卡姆剃刀" ;;
    cynefin-skill)              echo "Cynefin 框架" ;;
    second-order-thinking-skill) echo "二阶思维" ;;
    jtbd-skill)                 echo "JTBD（Jobs to Be Done）" ;;
    inversion-skill)            echo "逆向思维（Inversion）" ;;
    swot-skill)                 echo "SWOT 分析" ;;
    lateral-thinking-skill)     echo "横向思维（Lateral Thinking）" ;;
    five-whys-skill)             echo "5 Whys（五个为什么）" ;;
    pareto-principle-skill)      echo "帕累托法则（80/20）" ;;
    blue-ocean-strategy-skill)   echo "蓝海战略（Blue Ocean Strategy）" ;;
    business-model-canvas-skill) echo "商业模式画布（BMC）" ;;
    value-chain-skill)           echo "价值链分析（Value Chain）" ;;
    *) echo "$1" ;;
  esac
}

create_and_push() {
  local skill_name="$1"
  local repo_name="forge-skill-${skill_name}"
  local chinese_name=$(get_chinese_name "$skill_name")
  local skill_file="methods/${skill_name}/SKILL.md"
  local tmp="/tmp/${repo_name}"

  echo ""
  echo "📦 ${repo_name}"

  # 1. 创建 GitHub 仓库
  if gh repo create "peterfei/${repo_name}" --public \
    --description "${chinese_name} — forge-skill 锻造的结构化思维工具 Skill" 2>&1 | tail -1; then
    echo "  ✅ GitHub 仓库创建成功"
  else
    echo "  ⚠ 仓库已存在或创建失败，继续推送"
  fi

  # 2. 准备文件并推送
  rm -rf "$tmp"
  mkdir -p "$tmp"
  cp "$skill_file" "$tmp/SKILL.md"

  cat > "$tmp/README.md" <<README
# Forge Skill: ${chinese_name}

> 本 Skill 由 [forge-skill](https://github.com/peterfei/forge-skill) 锻造引擎自动生成。
> 基于 [Agent Skills](https://skills.sh) 开放协议。

## 安装

\`\`\`bash
npx skills add peterfei/${repo_name}
\`\`\`

## License

MIT
README

  cat > "$tmp/package.json" <<PACKAGE
{
  "name": "@forge-skill/${skill_name}",
  "version": "1.0.0",
  "description": "${chinese_name} — forge-skill 锻造的结构化思维工具",
  "main": "SKILL.md",
  "skills": {
    "name": "${skill_name}",
    "files": ["SKILL.md"]
  },
  "keywords": ["forge-skill", "skill", "methodology", "agent-skills", "thinking-tool"],
  "license": "MIT",
  "repository": "https://github.com/peterfei/${repo_name}"
}
PACKAGE

  cd "$tmp"
  git init -q
  git checkout -b main -q
  git add -A
  git commit -q -m "feat: ${chinese_name} Skill — forge-skill 锻造" 2>/dev/null
  git remote add origin "git@github.com:peterfei/${repo_name}.git" 2>/dev/null || git remote set-url origin "git@github.com:peterfei/${repo_name}.git"
  if git push -u origin main -q 2>&1; then
    echo "  ✅ 推送成功"
  else
    echo "  ❌ 推送失败"
    cd - > /dev/null
    return 1
  fi
  cd - > /dev/null
  rm -rf "$tmp"
}

echo "🔨 创建独立 Skill 仓库并推送..."
echo ""

for skill_dir in methods/*-skill/; do
  skill_name=$(basename "$skill_dir")
  if [ -f "$skill_dir/SKILL.md" ]; then
    create_and_push "$skill_name"
  fi
done

echo ""
echo "✅ 全部完成"
