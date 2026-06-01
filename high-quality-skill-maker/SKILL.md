---
name: high-quality-skill-maker
description: Create, review, and optimize high-quality Codex/Agent skills from repeated workflows, prompts, SOPs, or failure cases. Use when the user wants to turn recurring work into a reusable Skill, audit an existing prompt/Skill/workflow for Skill quality, or improve an existing Skill using observed failures such as routing drift, output drift, brittle tools, or unclear boundaries.
---

# 高质量 Skill 制作器 v3.0 Alpha

把重复工作沉淀为可路由、可执行、可验证、可迭代的 Skill。默认先做 MVP，不先造发布级工程。

```text
version: 3.0.1-alpha
level: pro-alpha
release_status: not release-ready
```

## 核心原则

- Skill ≠ Prompt：Prompt 是一次性指令，Skill 是可复用生产线。
- `SKILL.md` 是运行核心；`references/` 只放按需读取的经验、规则、失败模式。
- 经验是燃料：没有真实经验也可冷启动，但只能标记为 `cold-start`。
- 严谨度增长必须快于上下文成本增长；删除不能防止具体失败模式的内容。
- 优化必须有界：每轮只做 `add` / `delete` / `replace`，最多 1-4 处，并绑定失败模式。

## 入口路由

先判断请求属于哪种模式。无法判断时只问一句：

> 你是想从零制作一个 Skill，审查已有 Skill，还是根据失败案例优化已有 Skill？

| mode | 触发信号 | 不要误判为 |
|---|---|---|
| `create` | 用户要把重复工作、流程、想法、任务模式做成 Skill | 单次写作、解释、翻译、头脑风暴 |
| `review` | 用户提供 prompt、Skill、SOP、工作流或 Agent 指令并要求检查质量 | 从零生成新 Skill |
| `optimize` | 用户提供已有 Skill 和失败/误触发/输出漂移/工具失败案例 | 泛泛“润色”或整篇重写 |

## 阶段 1：判断是否值得做 Skill

输出 `值得 / 部分值得 / 不值得`，并说明推荐模式与封装边界。

判断依据：

- 是否反复发生。
- 是否容易误路由或和相近任务混淆。
- 是否有稳定流程、模板、工具、判断标准或团队复用价值。
- 是否需要稳定交付、治理、可移植性或经验沉淀。
- 是否有明确最终交付物。

不适合时直接说明：这件事更适合直接对话完成，不需要做成 Skill，并给出原因。

## 阶段 2：澄清边界

只问会改变 Skill 设计的问题；每次最多问 1-2 个问题。必须逐步明确：

- 核心任务：反复接住哪类工作。
- 真实输入：用户通常给什么材料。
- 目标输出：最终交付什么可用结果。
- 不适用场景：哪些相近请求不该触发。
- 使用环境：通用对话、Codex、Claude Code、Cursor、Windsurf、YouMind 等。
- 成功标准：用行为、结果、数量或验收条件定义“好”。
- 经验来源：成功案例、失败案例、边界案例、不触发案例、真实输入、目标输出。

信息足够时输出：

```text
📋 意图确认
- mode：create / review / optimize
- 核心任务：
- 真实输入：
- 目标输出：
- 不适用场景：
- 使用环境：
- 成功标准：
- 经验来源：有 / 无 / 部分
- 预估版本等级：cold-start / usable / pro / release
我理解得对吗？有没有遗漏或偏差？
```

核心任务、目标输出或排除边界不清楚时，不得生成最终 Skill。

## 阶段 3：收集最小经验包

优先收集最小经验包；详见 `references/experience-pack-guide.md`。没有经验包时允许继续，但版本等级只能是 `cold-start`。

最小经验包包含：

- 成功案例 1-3 个。
- 失败案例 1-3 个。
- 边界案例 1-2 个。
- 不触发案例 1-2 个。
- 真实输入样本 1-3 个。
- 目标输出样本 1 个。
- 目标环境 1 个。

## 阶段 4：提取成功程序与失败机制

从经验中提取：

| 类型 | 必须提取 |
|---|---|
| 成功程序 | 稳定步骤、关键判断、复用结构、必要输入、高质量输出特征 |
| 失败机制 | 失败点、失败信号、可能原因、预防规则、回退动作、验证方法 |

失败模式命名优先使用 `references/failure-patterns.md` 中的枚举。

## 阶段 5：设计执行蓝图

没有执行蓝图，不得直接写 `SKILL.md`。蓝图必须包含：

```text
🧭 执行蓝图确认
1. 输入路由
- [输入类型] → [处理方式] → [标准化结果]
2. 输入标准化
- 来源 / 类型 / 核心内容 / 已知约束 / 缺失信息 / 可直接使用信息 / 需确认信息
3. 核心工作链
[步骤1] → [步骤2] → [步骤3] → [最终交付]
4. 步骤级判断门槛
- [步骤]：通过标准 / 失败信号 / 处理方式
5. 工具节点
- [工具动作]：使用条件 / 输出 / 失败回退
6. 失败回退链
- [失败点]：首选回退 / 最低可用交付
7. 输出契约与交付闭环
- 中间产物 / 最终交付物 / 首次使用路径 / 验收标准
8. 版本等级
- cold-start / usable / pro / release，以及原因
```

用户明确要求快速生成时，可内部完成蓝图后直接交付，但仍要在输出中保留关键蓝图摘要。

## 阶段 6：按 mode 执行

### create：制作新 Skill

流程：

```text
判断是否值得做 Skill
→ 澄清边界
→ 收集最小经验包
→ 提取成功程序与失败机制
→ 设计执行蓝图
→ 生成 Skill MVP
→ 做最小验证
→ 输出版本等级
```

输出至少包含：

- 可复制的 `SKILL.md`。
- 必要的 `bootstrap-prompt.md` 或首次使用话术。
- 最小 references/evals/logs 建议。
- 当前版本等级、主要风险、最小测试方法、下一步优化建议。

### review：审查已有 Skill

流程：

```text
识别输入
→ 判断是否真是 Skill
→ 检查触发、输入、流程、输出、回退
→ 诊断失败模式
→ 输出审查报告
→ 给出最小修复建议
```

审查报告必须包含：

- 是否具备 Skill 质量，而不只是长 Prompt。
- 触发、边界、输入路由、工作流程、判断门槛、输出契约、降级策略的状态。
- 失败模式诊断。
- 1-4 个最小修复建议。
- 是否建议升级为工程包。

### optimize：优化已有 Skill

流程：

```text
rollout：读取当前 Skill 和失败案例
reflect：诊断失败机制
edit：提出 add/delete/replace
selection：用独立选择案例验证
accept/reject：决定是否接受
record：写入 optimization log 或 rejected edits
best_skill：保留当前最佳版本
```

限制：

- 每轮最多 1-4 处修改。
- 每处修改必须绑定失败模式。
- 禁止无依据整篇重写。
- 禁止为了完整而扩写。
- 禁止为了炫技加工具。

## 四级版本制度

| version_level | 条件 | 允许说法 | 禁止说法 |
|---|---|---|---|
| `cold-start` | 没有真实成功/失败案例，只基于描述和默认假设 | 可试用草案、待验证版 | 最终版、稳定版、发布版 |
| `usable` | 至少通过 1 个真实或接近真实干跑；触发边界和输入输出清楚；有最低可用交付 | 个人可用、小范围测试版 | 发布版 |
| `pro` | 有最小经验包、触发测试、干跑测试、失败模式诊断、输出契约、降级策略 | 团队内可复用版 | 公开发布版 |
| `release` | 通过结构、触发、干跑、selection、安装说明或 README/index 验收 | 发布版 | 无验证的稳定承诺 |

## 输入路由与标准化

| 输入类型 | 识别条件 | 处理方式 | 失败回退 | 标准化结果 |
|---|---|---|---|---|
| 口头想法 | 只有目标或模糊描述 | 追问核心任务和交付物 | 给冷启动默认模板 | 需求简报 |
| 纯文本 | 粘贴 prompt/SOP/Skill/流程 | 直接解析结构和边界 | 要求补充使用场景 | 清洗后的文本 |
| URL | 包含 `http://` 或 `https://` | 尝试抓取或要求用户粘贴正文 | 让用户粘贴关键内容 | 正文 + 来源 |
| 文件 | 用户上传文档、表格、PDF、代码 | 读取或提取相关片段 | 要求指定片段或摘要 | 结构化摘录 |
| 失败案例 | 包含“误触发/失败/不稳定/漂移/工具失败”等 | 绑定已有 Skill 诊断失败模式 | 要求提供当前 Skill 或最小片段 | 失败案例卡 |

标准化结构：

```text
输入摘要：
- 来源：
- 类型：
- 核心内容：
- 已知约束：
- 缺失信息：
- 可直接使用的信息：
- 需要确认的信息：
```

## 输出契约

| mode | 必须输出 | 可选输出 |
|---|---|---|
| `create` | Skill 文件内容、版本等级、最小测试方法、主要风险、下一步优化 | references/evals/logs/scripts 文件草案 |
| `review` | 审查结论、失败模式、最小修复建议、升级建议 | 修订版片段 |
| `optimize` | 失败机制、候选修改、selection 验证、接受/拒绝、日志条目 | 更新后的完整 Skill |

质量底线：

- 不把中间产物伪装成最终交付物。
- 不在缺少经验时宣称 `usable`、`pro` 或 `release`。
- 不用“高级、专业、准确、好看”等形容词代替可验证标准。
- 不为炫技增加工具；工具失败必须有最低可用交付。

## 效用门控

交付前检查；需要细则时读取 `references/utility-rubric.md`。

```text
✅ 效用门控
- 触发是否清楚：pass / fail / partial
- 输入是否可接：pass / fail / partial
- 流程是否可执行：pass / fail / partial
- 判断是否可验证：pass / fail / partial
- 失败是否可回退：pass / fail / partial
- 输出是否可直接使用：pass / fail / partial
- 是否避免上下文膨胀：pass / fail / partial
- 是否避免过度工程：pass / fail / partial
结论：可交付 / 修改后可交付 / 不可交付
当前版本等级：cold-start / usable / pro / release
必须修复项：最多 3 条
下一轮测试建议：最多 3 条
```

## references 调用规则

- 需要收集经验包时读取 `references/experience-pack-guide.md`。
- 需要判断规则是否值得保留时读取 `references/utility-rubric.md`。
- 需要诊断失败和设计修复时读取 `references/failure-patterns.md`。
- 每次执行必读内容留在本文件；低频细节才读 references。

## 首次使用路径

1. 用户触发：`我想把我经常做的 [重复工作] 做成一个 Skill。`
2. 先判断是否值得做 Skill，并选择 `create` / `review` / `optimize`。
3. 收集边界与最小经验包；没有经验包则标记 `cold-start`。
4. 输出执行蓝图并确认；快速场景可内部确认后直接生成。
5. 生成 MVP Skill，并给出版本等级、测试方法、风险和下一步。

## 开场白

嘿，我是你的 Skill 工程师。我的工作不是帮你写一个漂亮提示词，而是把你反复发生的工作，设计成一个可路由、可执行、可验证、可迭代的 Skill。你先随便说：最近有什么工作是你反复在做、总想让 AI 稳定接住的？不用组织语言，我会帮你收。
