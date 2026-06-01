# high-quality-skill-maker

把重复工作沉淀为可路由、可执行、可验证、可迭代的 Skill。

## 适用场景

- 用户想把反复发生的工作做成 Skill
- 用户想审查已有 prompt / SOP / Skill
- 用户提供失败案例，希望优化已有 Skill
- 用户希望沉淀可复用工作流，而不是只要一次性答案

## 不适用场景

- 单次翻译
- 单次写作
- 单次总结
- 普通头脑风暴
- 没有稳定复用需求的临时任务

## 文件结构

```text
SKILL.md
bootstrap-prompt.md
references/
evals/
logs/
scripts/
requirements-dev.txt
VALIDATION.md
```

## 使用方式

普通对话中可复制 `bootstrap-prompt.md`。

作为 Skill 使用时，以 `SKILL.md` 为核心入口。

## 验证方式

```bash
python3 scripts/validate_structure.py .
python3 -m json.tool evals/trigger-cases.json >/tmp/trigger.json
python3 -m json.tool evals/selection-cases.json >/tmp/selection.json
python3 -m py_compile scripts/*.py
```

## 当前状态

当前版本：3.0.2-alpha
当前等级：pro-alpha
发布状态：not release-ready

说明：结构已经具备 Skill 工程包特征，但真实案例验证仍需继续补充。

## 后续优化规则

每轮优化最多修改 1-4 处。每处修改必须绑定失败模式，并记录到 `logs/optimization-log.md` 或 `logs/rejected-edits.md`。
