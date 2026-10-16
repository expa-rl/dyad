# Dyad project page：基于 EARL 调研的重构方案

日期：2026-10-16。状态：已用于本轮网页重构；发布状态以仓库与 GitHub Pages 为准。

依据：[EARL 页面与论文拆解](earl-project-page-analysis.md)、[Dyad 论文 v1](https://arxiv.org/html/2609.36116v1)、[本地 PDF](../static/pdfs/dyad.pdf)。当前页面审阅基于仓库提交 `0871880`。以下论文图表编号仅用于内部核查，不进入公开页面正文。

## 1. 页面应该让读者记住什么

**Dyad 是一种扩展预训练 LLM 的架构：语言头负责推理，动作编码器让模型直接在动态提供的 typed actions 上决策。这个接口既支持冻结 LLM 的模块化适配，也支持联合训练，并带来跨环境收益与较好的通用能力保留。**

推荐保留三个价值主节，但把第二节从训练操作“Joint optimization”改为读者关心的结果“Cross-environment Generalization”。第一节回答能否不更新 LLM 就改善代理；第二节回答联合训练的收益能否迁移；第三节回答是否以损失原有能力为代价。完整机制放在 Approach 的 MP4 中。

这三节与论文摘要中的两种训练设置及能力结果相符；不需要把所有实验都变成章节。[Dyad 摘要与 §1](https://arxiv.org/pdf/2609.36116v1#page=1)

## 2. 推荐阅读顺序与版式

```text
题目 / 作者 / 机构 / 资源按钮

浅灰开场区
  TL;DR
  一段动机与最低限度的架构说明

1. Modular Adaptation with a Frozen LLM
  两段说明 → 一张代表性对比图 → 自足图注

2. Cross-environment Generalization
  两段说明 → 一张迁移结果图 → 自足图注

3. Preserving General Capabilities
  两段说明 → 一张能力变化图 → 自足图注

浅灰 Approach 区
  Approach
  一段机制引导 → 一个 MP4 → 两段解释

BibTeX / 模板署名
```

直接复用 EARL 的主容器、字号层级和“编号标题 → 段落 → 证据”的结构。主节使用单列，不再将一段文字压在表格旁边，也不把两个不同结论的密集结果并排。图内可以有 DIVE/CodeGym 分组标签；它们是数据标签，不再生成页面子标题。

公开页面的主标题只保留：

```html
<h2>1. Modular Adaptation with a Frozen LLM</h2>
<h2>2. Cross-environment Generalization</h2>
<h2>3. Preserving General Capabilities</h2>
<h2>Approach</h2>
<h2>BibTeX</h2>
```

每个主节标题之后直接是段落，不再出现 section-label，不再配第二个解释同一含义的大标题。Approach 内也以连续段落解释，不再将三个机制都升级为 h3。

## 3. 三节各展示什么，为什么这样选

### 第一节：Modular Adaptation with a Frozen LLM

**论点：** 冻结预训练 LLM 及其语言头，只训练新增动作编码器，也能改善代理表现。

段落先解释模块化适配的意义，再说明在 DIVE 上训练、在四个未进一步训练的环境上评估的设置；最后讨论这个结果说明新增接口能够学到什么。不要把“冻结 LLM”误写成整个系统没有训练，或只训练一个很小的 projector：RL 阶段更新的是完整动作编码器。[§3.2、§5.3](https://arxiv.org/pdf/2609.36116v1#page=4)

**主证据：** 从 Table 4 选择 Qwen3.5-9B，展示 Base 与 Frozen Dyad 在四个环境上的成绩。用四组配对点或短条形图；不放 joint 行，因为它回答的是另一种训练设置的问题。

| 评估环境 | Base | Frozen Dyad | 变化，百分点 |
|---|---:|---:|---:|
| ALFWorld | 45.66 | 48.82 | +3.16 |
| WebShop | 33.43 | 35.00 | +1.57 |
| τ²-bench | 62.17 | 64.23 | +2.06 |
| SWE-bench Verified | 44.56 | 45.50 | +0.94 |

来源：[Table 4，p.8](https://arxiv.org/pdf/2609.36116v1#page=8)。四项成绩保留各自任务定义，不求一个没有明确意义的跨任务平均分。

正文补充范围：两种 Qwen 均在四个环境上改善，Llama/Gemma 的收益并不覆盖所有设置。按全表逐项统计，16 项中 14 项改善；Llama 的 τ²-bench 和 Gemma 的 SWE 分别下降 0.28、0.51 个百分点。这是整体边界，不需要再复制整张十二行表。

**取舍依据：** 冻结模式是 Dyad 最直观的架构价值。选择 9B 是为了和后面两节使用相同主例；不按每一节的最大提升重新挑模型。正文保留其他模型的覆盖范围与例外。

### 第二节：Cross-environment Generalization

**论点：** 联合训练的收益可以延伸到没有继续训练的评估环境。这比在首页再放一张域内榜单更直接支持“可复用的决策架构”。

先交代从冻结模式转到联合训练，再说明训练环境与评估环境分开。避免混淆“直接评估”与“原始模型完全未经过后训练”。

**主证据：** 从 Table 3 固定选择 Qwen3.5-9B + GRPO，保留 DIVE 和 CodeGym 两种训练来源，以及四个评估环境，共八个配对比较。图使用相对配对 GRPO baseline 的百分点变化，包含负值；图注写明这是代表性子集。

| 训练环境 | ALFWorld | WebShop | τ²-bench | SWE-bench Verified |
|---|---:|---:|---:|---:|
| DIVE | +1.15 | +1.79 | +2.82 | −1.02 |
| CodeGym | +3.58 | +1.84 | +1.71 | +1.22 |

来源：[Table 3，p.6](https://arxiv.org/pdf/2609.36116v1#page=6)。每个变化比较相同 LLM、相同训练环境与相同 RL 算法。网页图注同时提供原始成绩或可读的数据说明，不能只靠悬停理解。

正文用一句话说明完整实验范围：覆盖 4B/9B/27B 和 GRPO/GiGPO，48 项比较中 41 项优于配对 RL baseline，即也有 7 项未改善。图里的 −1.02 保留在主视图，不能只选择全为正的 CodeGym 行。47/48 相对原始模型的第二种统计不再同时强调，减少基准切换。

**取舍依据：** 图与正文分别承担“看懂一个固定设置”和“了解完整覆盖范围”。八个比较足以说明迁移设置和结果差异；不再让读者同时消化完整 48 格热图与另一个域内表。

### 第三节：Preserving General Capabilities

**论点：** 代理训练的结果还应从原有知识、数学推理与编码能力评估，不能只看环境得分。

先解释为什么需要检查能力保留，再分别说明原始模型参考线和配对 RL baseline。结论使用“generally better retention”，不承诺每个模型、每个 benchmark 都不下降，也不把架构归因写成已经证明的因果机制。[§5.2、Figure 3](https://arxiv.org/pdf/2609.36116v1#page=6)

**主证据：** 从 Figure 3 选择同一主例 Qwen3.5-9B + GRPO，保留 DIVE 与 CodeGym 两组、MMLU-Pro / HMMT February 2026 / LiveCodeBench v6 三项。展示配对 RL 与 Dyad 的位置，以及相对原始模型的零参考线，共六个对照。原图整张三模型、两算法的大面板不再直接缩小铺到网页上。

原图中该子集的 Dyad 相对原始模型变化为：

| 训练环境 | MMLU-Pro | HMMT | LiveCodeBench |
|---|---:|---:|---:|
| DIVE | +0.09 | +0.69 | +2.48 |
| CodeGym | +0.75 | +5.66 | +3.66 |

来源：[Figure 3，p.7](https://arxiv.org/pdf/2609.36116v1#page=7)。

这些是相对原始模型的变化，不能误标为相对 RL baseline 的收益。实施时已从 [arXiv v1 源码](https://arxiv.org/src/2609.36116v1)中的 `resources/figures/figure_general_capabilities.tex` 找到作者保留的精确绝对成绩及配对变化，已写入 `static/data/results.json`。据此使用 Matplotlib 重绘选定子集，保留原始模型零参考线与 GRPO/Dyad 成对点。数据是论文源码中的 manuscript score backup，并非原始 seed 日志，因此不添加未经提供的误差区间。

正文补充：完整评估中 CodeGym 的 Dyad 结果均高于各自原始模型，但部分 DIVE 设置仍有下降。保留这个范围说明，比增加另一套完整表更有帮助。

**取舍依据：** 此节回答“更强的代理是否伴随一般能力受损”，与迁移成绩是互补证据；保留同一个 9B/GRPO 主例，方便沿着前一节继续阅读。

## 4. Approach 的内容与 MP4

沿用 EARL 用动画解释机制的思路，但只使用用户准备的一个 MP4，不强行拆成三段视频，也不借用 EARL 的 CPO/Zero-RL 叙事。

建议 MP4 内解释三个连续环节：

1. 传统接口在语言词表上逐 token 生成动作文本；Dyad 另行给当前可执行的 typed actions 分配概率。
2. LLM 编码交互历史，动作编码器独立、并行编码环境条件下的动作描述；两者共同形成决策分布。动作集合可以随环境变化。
3. 执行动作后将观察送回历史，继续推理。说明可冻结 LLM 或联合训练；两种模式不需要重新画成两个独立系统。

视频前一段交代状态/动作语义的分解；视频后两段说明推理与决策如何切换，以及“先监督对齐、再 RL”的训练流程。缓存只在动作描述与环境上下文不变时适用，不能写成所有动作永远只编码一次。现有架构图作为 MP4 未就绪或加载失败时的替代画面；最终页面不同时重复展示完整概念图、架构图和同内容动画。[§2–3](https://arxiv.org/pdf/2609.36116v1#page=3)

开场不再单独占一大块展示 System 1/System 2/Dyad 对照图。最低限度的概念用开场段落说清，完整对照交给视频，避免在结果之前先完整讲一次、Approach 再讲一次。

## 5. 明确留在论文里的内容

| 内容 | 决定 | 理由 |
|---|---|---|
| Table 2：ALFWorld/WebShop 域内成绩 | 不进入主页面 | 已选择跨环境收益作为第二主节；不再用第二套环境成绩分散论点 |
| Table 3 完整 48 项比较 | 保留源数据，首页仅展示上述子集 | 正文交代完整范围与 41/48；避免密集矩阵成为阅读任务 |
| Table 4 全模型、冻结/联合完整表 | 首页只展示 9B 的 Base/Frozen | 这一节只证明冻结模式的价值，其他家族用文字交代范围与例外 |
| Figure 3 完整大面板 | 首页只展示统一主例 | 同时保留三种能力与两种训练环境，而缩减重复的规模/算法维度 |
| Figure 4：训练动态 | 留在论文 | 奖励、长度、交互次数是进一步分析，当前不另立效率主张 |
| Table 5、Figure 5：JevBench 与 Jev 对比 | 留在论文 | 会引入专用决策模型、延迟测量和另一套设置；当前主线已有三项充分理由 |
| Figure 6、Table 6：训练组件、对齐与 pooling 消融 | 留在论文 | 用来回答方法归因与实现选择，非首次访问必须理解的内容 |
| Table 1、公式、超参数、prompt、数据构造 | 留在论文 | Approach 只保留理解机制和两种训练模式所需的信息 |
| 现有两处折叠补充区 | 从页面移除 | 不把删减的全部实验重新藏在折叠区里 |

因此，页面主体是三项主张、三幅对应结果图和一个方法 MP4。并非所有论文实验都需要一个可视化模块。这里的“三幅”来自当前论点选择，不是以后必须维持的模板规则。

## 6. 可用于下一版的英文正文草稿

以下是连续段落的内容草稿；小节在公开页面中只使用第 2 节列出的五个 h2。图表位置与图注另按第 3 节实施，不添加论文编号引用。

### 开场

**TL;DR:** Dyad is an architecture that extends pretrained LLMs with native typed decision-making over dynamic action spaces. It supports adaptation with a frozen LLM and joint training, improving agent performance across environments while generally better preserving knowledge, reasoning, and coding capabilities.

An agent must reason about its goals and decide how to act. Yet most LLM agents use the same token-generation interface for both: even a decision among available operations is expressed as text. Dyad adds an environment-conditioned action encoder that represents candidate actions independently, letting the LLM assign probabilities directly to the current choices while retaining its language reasoning. The actions are supplied through descriptions rather than a fixed set of learned identifiers. We study what this architecture enables in three complementary ways.

### 第一节正文

Dyad offers a separate component that can learn from environment interaction while leaving an existing LLM fixed. We freeze the pretrained LLM and its language head, and train the action encoder using task rewards. This tests whether learning a decision interface can improve agent behavior without updating the pretrained model's parameters.

After training on DIVE, frozen adaptation improves Qwen3.5-9B on all four evaluation environments, without further training on those environments. The same holds for Qwen3.5-4B. Results also extend to Llama and Gemma, although not in every setting: across the full evaluation, 14 of 16 model–environment comparisons improve. The takeaway is a modular route to adaptation, with benefits that do not require changes to the pretrained LLM.

### 第二节正文

Dyad also supports joint optimization of the LLM and action encoder. To test whether the resulting gains extend beyond the training environment, we train on DIVE or CodeGym and evaluate on four other environments without further adaptation. Each comparison uses the same pretrained LLM, training environment, and RL algorithm as its conventional baseline.

The representative Qwen3.5-9B results below retain both training environments and all four evaluation tasks, including a regression on SWE-bench Verified after DIVE training. Across the complete study, spanning three model scales and both GRPO and GiGPO, Dyad outperforms its paired RL baseline in 41 of 48 comparisons. The benefits therefore extend to unseen evaluation environments, while varying across training and evaluation settings.

### 第三节正文

Better environment scores are only part of the picture. Agentic post-training may also change the knowledge and reasoning abilities of the pretrained LLM. We therefore evaluate general knowledge with MMLU-Pro, mathematical reasoning with HMMT February 2026, and coding with LiveCodeBench v6. The zero reference marks each original model before additional training; the paired markers compare conventional RL with Dyad.

Dyad generally retains more capability than the corresponding RL baselines, recovering losses in some settings and increasing gains in others. Across the full CodeGym evaluation, both Dyad variants remain above their original pretrained models on all three capability benchmarks; some DIVE settings still show declines. Together with the agent results, these observations suggest that an additional route for action adaptation can help limit interference with pretrained language capabilities.

### Approach 正文

Dyad factorizes a decision into the evolving interaction state and the meaning of each available action in its environment. The LLM represents the interaction history, while a separate encoder maps action descriptions into compatible representations. The walkthrough shows how these components support language reasoning and typed decisions within one policy.

The language head continues to generate tokens. When the model emits an interaction token, its state is scored against the available action representations to produce a typed action distribution. The chosen operation executes in the environment, and its observation returns to the history. Action representations can be reused while their descriptions and environment context stay unchanged; newly introduced actions can be encoded when encountered.

Training begins with supervised alignment of the action projector, keeping both transformer backbones fixed. Reinforcement learning then learns from environment rewards. In frozen adaptation, only the action encoder is updated; in joint optimization, both the LLM and action encoder are updated. These two settings use the same decision architecture.

## 7. 实施时的核查条件

- 三幅结果展示使用同一个预先指定的主例 Qwen3.5-9B + GRPO；冻结实验本身采用 GRPO。每幅图注明训练来源、评估环境、对比对象与三次评估 seed。
- 区分成绩、相对原始模型的变化、相对配对 RL baseline 的变化；百分点不能写成相对百分比提升。
- 主图保留所选范围内的负值；全文不把局部改善写成普遍保证。
- 通用能力图保留可读坐标、benchmark 名、两组训练环境、baseline 与 Dyad 图例；精确成绩已从作者提供的源码备份确认。
- 主节无重复标题、无论文编号引用、无完整实验折叠区；正文能脱离图注独立说明论点，图注能脱离正文说明设置。
- MP4 未提供时继续使用架构图替代；视频就绪后检查播放、移动端与失败回退。

实施记录：网页已采用三节单列结构与本记录的英文正文；三幅结果图分别输出桌面与手机 SVG，并附供屏幕阅读器访问的精确成绩表。完整原始图与完整结果数据保留在仓库中，不进入主阅读路径。MP4 尚未提供，页面保留架构图回退与后续接入位置。
