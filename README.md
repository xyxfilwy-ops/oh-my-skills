# oh-my-skills

一个用于沉淀、审查、优化 AI Agent / Codex / ChatGPT Skill 的技能集合。

## Skills

| Skill | 用途 | 状态 |
|---|---|---|
| high-quality-skill-maker | 把重复工作制作成可路由、可执行、可验证、可迭代的 Skill | v3.0.1-alpha / pro-alpha |

## 当前重点 Skill

### high-quality-skill-maker

用于以下场景：

- 从零制作新 Skill
- 审查已有 prompt / Skill / SOP / Agent 指令
- 根据失败案例优化已有 Skill

不适合以下场景：

- 单次翻译
- 单次写作
- 单次总结
- 普通头脑风暴
- 没有复用意图的一次性任务

## 快速使用

普通对话冷启动：

1. 打开 `high-quality-skill-maker/`
2. 阅读 `SKILL.md`
3. 可复制 `bootstrap-prompt.md` 到普通对话中使用

本地验证：

```bash
python3 high-quality-skill-maker/scripts/validate_structure.py high-quality-skill-maker
python3 -m json.tool high-quality-skill-maker/evals/trigger-cases.json >/tmp/trigger-cases.formatted.json
python3 -m json.tool high-quality-skill-maker/evals/selection-cases.json >/tmp/selection-cases.formatted.json
python3 -m py_compile high-quality-skill-maker/scripts/*.py
```

## 状态说明

当前是 Alpha 版，适合个人使用和小范围测试。

当前目标状态：

```text
version: 3.0.1-alpha
level: pro-alpha
release_status: not release-ready
```

暂不建议标记为 release，除非后续补充真实干跑记录、失败案例记录、selection 验证记录和安装验收记录。
