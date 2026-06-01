# Dry Run Cases

真实干跑记录用于把 `high-quality-skill-maker` 从结构完整的 Alpha，推进到经过真实任务验证的稳定版本。

这些记录不是正式 eval，也不是自动化测试。它们用于沉淀真实使用中的成功信号、失败信号、边界案例和下一轮优化依据。

## 使用规则

- 每条记录必须来自一次真实或接近真实的 Skill 制作 / 审查 / 优化任务。
- 不记录敏感信息；必要时对用户输入做脱敏摘要。
- 不为了证明 Skill 正确而美化结果。
- 如果失败，要明确写出 failure_mode。
- 每条记录都应能回答：这次干跑是否证明当前 Skill 更可靠，还是暴露了下一轮必须修的问题。
- 不因单次成功就把版本提升为 release。

## 记录模板

```text
## [YYYY-MM-DD] - [案例名称]

- mode：create / review / optimize
- 输入类型：口头想法 / 纯文本 / URL / 文件 / 失败案例 / 混合输入
- 用户原始需求摘要：
- 用户提供的关键材料：
- 目标输出：
- 不适用或边界信号：
- 执行结果：
  - 是否完成意图判断：pass / partial / fail
  - 是否完成输入标准化：pass / partial / fail
  - 是否完成执行蓝图：pass / partial / fail
  - 是否生成可直接使用的交付物：pass / partial / fail
  - 是否完成效用门控：pass / partial / fail
- 主要成功信号：
- 暴露的问题：
- 对应 failure_mode：
  - routing_drift / trigger_gap / boundary_blur / input_mismatch / execution_break / output_drift / quality_vagueness / tool_fragility / context_bloat / delivery_gap / over_engineering / none
- 是否需要修改 Skill：
  - no_change / add / delete / replace / investigate
- 建议进入下一轮优化吗：
  - yes / no
- 备注：
```

## 2026-06-01 - 行业研究流程 Skill 冷启动

- mode：create
- 输入类型：口头想法
- 用户原始需求摘要：
  用户希望把每周行业研究流程沉淀成一个 Skill，用于稳定生成研究框架、信息收集路径、分析维度和最终报告。
- 用户提供的关键材料：
  只提供了任务目标，没有提供真实输入样本和目标输出样本。
- 目标输出：
  一个可复制的 `SKILL.md` MVP，以及最小测试方法。
- 不适用或边界信号：
  不能把它误判为一次性行业研究报告生成。
- 执行结果：
  - 是否完成意图判断：pass
  - 是否完成输入标准化：partial
  - 是否完成执行蓝图：partial
  - 是否生成可直接使用的交付物：partial
  - 是否完成效用门控：pass
- 主要成功信号：
  能正确判断这是 create 场景，并且没有直接伪装成 release 版。
- 暴露的问题：
  缺少真实输入和目标输出时，生成结果只能是 cold-start，后续需要更明确地提醒用户补经验包。
- 对应 failure_mode：
  - input_mismatch
  - delivery_gap
- 是否需要修改 Skill：
  - investigate
- 建议进入下一轮优化吗：
  - yes
- 备注：
  这个案例适合用于检查 cold-start 版本声明是否足够醒目。

## 2026-06-01 - 内容生产 SOP 审查

- mode：review
- 输入类型：纯文本
- 用户原始需求摘要：
  用户提供一段团队内容生产 SOP，希望判断它是否能改造成 Skill，以及当前结构有什么问题。
- 用户提供的关键材料：
  SOP 正文、目标使用场景、部分输出要求。
- 目标输出：
  审查报告，包括是否具备 Skill 质量、主要失败模式、最小修复建议和升级建议。
- 不适用或边界信号：
  不应直接从零重写完整 Skill，除非用户明确要求。
- 执行结果：
  - 是否完成意图判断：pass
  - 是否完成输入标准化：pass
  - 是否完成执行蓝图：partial
  - 是否生成可直接使用的交付物：pass
  - 是否完成效用门控：pass
- 主要成功信号：
  能区分 review 和 create，没有直接整篇重写。
- 暴露的问题：
  审查报告如果没有固定字段，容易出现输出结构漂移。
- 对应 failure_mode：
  - output_drift
- 是否需要修改 Skill：
  - investigate
- 建议进入下一轮优化吗：
  - yes
- 备注：
  后续可用这个案例检查 review 输出契约是否足够稳定。

## 2026-06-01 - 网页抓取失败后的工具脆弱性优化

- mode：optimize
- 输入类型：失败案例
- 用户原始需求摘要：
  用户反馈某个 Skill 在网页抓取失败后，仍然假装读到了网页内容，并继续生成结论。
- 用户提供的关键材料：
  当前 Skill 片段、失败时的用户请求、错误输出、期望行为。
- 目标输出：
  诊断失败模式，并提出不超过 1-4 处有界修改。
- 不适用或边界信号：
  不应整篇重写 Skill；不应新增复杂抓取系统。
- 执行结果：
  - 是否完成意图判断：pass
  - 是否完成输入标准化：pass
  - 是否完成执行蓝图：pass
  - 是否生成可直接使用的交付物：pass
  - 是否完成效用门控：pass
- 主要成功信号：
  能诊断为 `tool_fragility`，并提出工具失败回退和最低可用交付。
- 暴露的问题：
  selection case 是否足够独立仍需要后续验证。
- 对应 failure_mode：
  - tool_fragility
- 是否需要修改 Skill：
  - no_change
- 建议进入下一轮优化吗：
  - no
- 备注：
  这个案例可作为工具失败处理策略的正向样本。

## 2026-06-01 - book-to-skill v2 技能冷启动

- mode：create
- 输入类型：URL
- 用户原始需求摘要：
  用户要求使用 high-quality-skill-maker 执行一次真实 dry-run，以 `https://github.com/virgiliojr94/book-to-skill` 为参考，制作一个更加好用、更加实用的 book to skill v2 技能；完成后额外输出 dry-run record draft；不要直接修改 Skill，只记录本次运行证据。
- 用户提供的关键材料：
  GitHub 仓库 URL。通过网页读取到原项目目标、生成文件结构、支持格式、提取链路、质量规则和安装方式。尝试用 shell `git clone --depth 1 https://github.com/virgiliojr94/book-to-skill` 获取仓库失败，错误为 `CONNECT tunnel failed, response 403`，后改用网页和 raw 文件读取。
- 目标输出：
  一份 book-to-skill v2 Skill MVP 草案，包括意图判断、输入标准化、执行蓝图、可复制 `SKILL.md`、首次使用话术、最小 references/evals/logs 建议、版本等级、风险、测试方法和下一步优化建议；同时输出严格按本文件模板填写的 dry-run record draft。
- 不适用或边界信号：
  不应把任务误判为直接转换某一本书；不应改动 high-quality-skill-maker 的 Skill 文件；不应实际安装或覆盖用户本地技能；不应声称生成的是 release 版；不应复制原仓库实现作为最终版本。
- 执行结果：
  - 是否完成意图判断：pass
  - 是否完成输入标准化：pass
  - 是否完成执行蓝图：pass
  - 是否生成可直接使用的交付物：partial
  - 是否完成效用门控：partial
- 主要成功信号：
  能从 URL 输入进入 create 模式；能识别参考项目的核心机制是把文档提取为按需加载的技能包，而不是一次性摘要；能把 v2 的改进方向收敛到输入路由、版权安全、成本预估、质量门控、降级链和验收测试；遵守了“不直接修改 Skill”的约束，只记录 dry-run 证据。
- 暴露的问题：
  shell 侧无法克隆 GitHub 仓库，依赖网页读取作为回退，证据完整性低于本地仓库审查；用户没有提供真实书籍样本、失败案例和目标运行环境，导致生成的 v2 只能是 cold-start/usable 边缘草案；为满足“先正常完成工作”和“只记录证据”的组合要求，最终交付物主要在对话中给出，没有落地为可运行 Skill 包；效用门控只能做结构性检查，不能验证真实 PDF/EPUB 转换质量；任务类型字段给出 create / review / optimize 三选项但自然语言目标偏 create，存在轻微边界歧义。
- 对应 failure_mode：
  - tool_fragility
  - input_mismatch
  - delivery_gap
  - boundary_blur
- 是否需要修改 Skill：
  - investigate
- 建议进入下一轮优化吗：
  - yes
- 备注：
  该案例可用于后续检查 URL 输入回退、dry-run 记录模板遵循、以及 create 模式在缺少最小经验包时是否能稳定标记版本风险。
