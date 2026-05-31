# Rejected Edits

记录被拒绝的修改，避免下一轮重复提出同样的坏修改。

| 日期 | 候选修改 | 拒绝原因 | 导致的问题 | 后续避免规则 |
|---|---|---|---|---|
| 2026-05-31 | 把 Skill Maker 改成完整 Web App / CLI 工程 | 当前阶段目标是 Skill MVP，不是发布级工程化产品 | over_engineering / context_bloat | 除非进入 release 阶段，否则不新增复杂外部依赖和 UI 工程 |

## 条目模板

```text
## [YYYY-MM-DD]
- 候选修改：
- 拒绝原因：
- 可能导致的问题：routing_drift / context_bloat / over_engineering / delivery_gap / other
- 后续避免规则：
```

## 2026-05-31
- 候选修改：把 Skill Maker 改成完整 Web App / CLI 工程
- 拒绝原因：当前阶段目标是 Skill MVP，不是发布级工程化产品
- 可能导致的问题：over_engineering / context_bloat
- 后续避免规则：除非进入 release 阶段，否则不新增复杂外部依赖和 UI 工程
