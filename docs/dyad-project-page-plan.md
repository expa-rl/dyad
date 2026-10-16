# Dyad 项目页内容与证据方案

依据：[EARL 整体分析](earl-project-page-analysis.md)、[EARL 正文与图注分析](earl-writing-and-captions.md)、[Dyad 论文 v1](https://arxiv.org/html/2609.36116v1)。网页采用自己的图表编号。

## 1. 阅读顺序

1. 标题、作者、带编号的机构 logo、论文入口。
2. 一句话 TL;DR 概括架构贡献；随后的段落只解释共同文本接口的问题、固定动作空间的局限，以及通过动作描述构造决策接口的设计方向。训练方式和实验结论分别留给结果节。
3. **1. Modular Adaptation with a Frozen LLM**：解释为什么冻结 LLM 仍可改善决策，展示 Table 1。
4. **2. Stronger Agents with Preserved General Capabilities**：先 Figure 1 展示迁移表现，再 Figure 2 展示通用能力，默认 CodeGym，左右切换 DIVE。
5. **Approach**：typed decision-making、Jev 和概念 Figure 3 均并入方法部分；Figure 4 展示无音轨的架构动画；末尾介绍 JevBench 并展示 Table 2。
6. BibTeX 和精简的上游模板、机构标识来源说明；网页页脚不再列出 ExpA / EARL，仓库中保留来源记录。

每个主节只用一个 h2，之后直接进入段落，不使用重复的标签与子标题。正文解释问题、能力和意义；型号与必要设置放在 caption。正文用 single training environment、both training environments 等概括表述，CodeGym / DIVE 的具体名称留在图表、caption 与切换控件中。正文中的 Dyad 一律加粗；少量关键结论采用深蓝色加粗，字号为正文的 110%，包括冻结 LLM、免再次训练和三项能力提升。

## 2. 先让 typed decision-making 可理解

术语定义：直接对环境提供的候选操作赋予概率并作出选择。用 click、type、scroll 的例子与图连接，不用“类型安全”暗示决策一定正确。

[Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) 是专门作出直接决策的 System 1 模型；常规 LLM agent 生成推理文字与动作文字；Dyad 在同一架构中结合语言推理和原生动作决策。System 1/2 是解释计算模式的类比。

**Figure 3. Reasoning and acting in one architecture.** 使用论文概念图的原始矢量稿 `resources/figures/dyad_comparison_no_caption.pdf`，保留为 `static/pdfs/dyad-concept.pdf`，用 Poppler 渲染为网页 SVG。手机版顺序堆叠三个原图面板，所有内容直接显示。

## 3. JevBench：只展示与论点有关的准确率

JevBench 给定状态、指令、判断标准和候选答案，检验独立决策；任务包括分类、是非判断和有序评分。它与后续多步环境交互评估互补。

**Table 2. Direct decisions on JevBench.** 选用论文公开子集上的 Overall 与 Hard 准确率，保留 Jev、原始 LLM 和 Dyad 三行。LLM 和 Dyad 只展示启用推理的结果，caption 统一交代，不再设置 Reasoning 列或 Off/On 行。

桌面端采用双栏：左侧是表格与 caption，右侧用两段说明基准的作用和结果。右栏不另设标题，强调相对原始 LLM 的整体 +7.08、困难样本 +12.20 个百分点，以及略高于 Jev 的结果。增量由表格同一数据源计算，不再用“语言推理与直接动作相结合”的通用结论收尾。900px 及以下恢复表格在上、分析在下的单栏，保留正常字号。

| 方法 | Overall (%) | Hard (%) |
|---|---:|---:|
| Jev 1.13 | 85.01 | 70.88 |
| Original LLM | 79.10 | 59.88 |
| Dyad | 86.18 | 72.08 |

型号是 Qwen3.5-4B，Dyad 在 CodeGym 上使用 GRPO 训练。分数来自论文 `resources/tables/table_jevbench_results.tex`，不是当前 JevBench 维护者排行榜。公开子集为 231 项；来源文件 hash 和子集信息保存在 `static/data/results.json`。页面不宣称排行榜领先，也不把不同部署的 API 时间当作同硬件速度比较。

## 4. 冻结 LLM 的模块化适配

**Table 1. Improving decisions with a frozen LLM.** Qwen3.5-9B；在 DIVE 上用 GRPO 训练动作编码器，LLM 与语言头固定。

| 环境 | Original LLM | Frozen Dyad | 变化，百分点 |
|---|---:|---:|---:|
| ALFWorld | 45.66 | 48.82 | +3.16 |
| WebShop | 33.43 | 35.00 | +1.57 |
| τ²-bench | 62.17 | 64.23 | +2.06 |
| SWE-bench Verified | 44.56 | 45.50 | +0.94 |

来源：论文 `resources/tables/table_frozen_llm_adaptation.tex`。正文强调不更新 LLM 仍能改善环境决策。

## 5. 将代理表现与通用能力串成同一论点

**Figure 1. Agent performance beyond the training environment.** 跨环境表现仍只展示 CodeGym 训练的 Qwen3.5-9B/GRPO 设置，加入原始 pretrained LLM 作为独立系列。三组绝对分数直接可读，并在 Dyad-GRPO 分数旁标注相对 Original LLM 的增量：+9.47、+4.64、+0.85、+6.06 个百分点。手机版将增量另起一行，避免挤压数值。

| 环境 | Original LLM | GRPO | Dyad-GRPO |
|---|---:|---:|---:|
| ALFWorld | 45.66 | 51.55 | 55.13 |
| WebShop | 33.43 | 36.23 | 38.07 |
| τ²-bench | 62.17 | 61.31 | 63.02 |
| SWE-bench Verified | 44.56 | 49.40 | 50.62 |

三组均来自论文 `resources/tables/table_joint_generalization.tex`；原始模型的分数还与冻结实验基线相互核对。保留原始模型在 τ²-bench 上高于 GRPO 的事实，不把常规 RL 写成在所有环境都提高了原始模型。Dyad 在这里的四个环境中均高于另外两组。此处不扩展为所有型号和算法的结论。

**Figure 2. General capabilities after agentic training.** 保留 DIVE 和 CodeGym 两种训练来源，各自生成一张相同坐标范围的图。默认显示 CodeGym，使用图表左右两侧垂直居中的按钮或键盘方向键切换，无自动播放。移除顶部按钮组和重复的环境标题，当前训练环境仍在图内显示；无障碍 live status 保留切换播报。用 Knowledge、Mathematical Reasoning、Coding 三项能力表达；caption 说明对应 MMLU-Pro、HMMT February 2026、LiveCodeBench v6。

| 训练来源与能力 | GRPO 相对原始模型 | Dyad-GRPO 相对原始模型 |
|---|---:|---:|
| DIVE · Knowledge | −1.32 | +0.09 |
| DIVE · Mathematical Reasoning | −0.23 | +0.69 |
| DIVE · Coding | +0.59 | +2.48 |
| CodeGym · Knowledge | +0.15 | +0.75 |
| CodeGym · Mathematical Reasoning | +2.27 | +5.66 |
| CodeGym · Coding | +3.58 | +3.66 |

来源：`resources/figures/figure_general_capabilities.tex`。两种训练来源用于说明能力保留的不同情形，CodeGym-only 的选择只限制代理迁移图。图保留原始 LLM 零线与图例，所有变化直接标注；没有提供原始运行日志，不添加误差条。

## 6. Approach 与 caption 规则

**Figure 4. How Dyad reasons and acts.** 使用作者 2026-10-16 提供的录屏，封装为无音轨的 H.264 MP4，保持原始视频编码和 2518 × 1166 比例。首帧与末帧各额外停留 1 秒，中间动画节奏不变，总时长约 31.3 秒。原生控件、默认静音、不自动播放；封面取动画第 17 秒。原架构图保留为加载失败或未启用 JavaScript 时的回退。正文解释独立编码候选动作、语言头与交互 token、环境反馈和两阶段训练，不在图注重述整段机制。

所有 caption 保留加粗的编号、简短名称，以及理解图表必须知道的型号、训练来源、单位和 benchmark 映射。删除 seed 数、重复图例解释和可留在论文中的评估流程细节。caption 桌面 14px，手机 13.6px，左对齐。

## 7. 展示与验证

- 不使用折叠、隐藏表格或只在悬停时可见的数据。用户指定的通用能力轮播每次显示一个完整图；无 JavaScript 或打印时显示两个训练环境。
- JevBench 和原始基线用独立来源文件核对；验证生成图中的 12 个迁移分数、4 个新增百分点标注、12 个能力变化与 6 个 JevBench 分数。
- 检查单句 TL;DR、平级标题、Table 1–2 / Figure 1–4 编号与锚点、模型规格留在 caption、桌面与手机无横向溢出。
- 机构标识使用完整原版图文，不拼写 HTML 缩写，桌面与手机均为两行三列且整体缩小；各 section 交替使用白色和淡蓝背景。较小 caption 字号保留。视频接入时检查完整解码、音轨数量、浏览器播放和手机比例。
- 完整域内实验、多型号/算法结果、训练曲线、消融、超参数和 prompt 留在论文中。

## 8. 正文各部分的分工与去重

2026-10-16：通读全文后调整段落职责，避免每节都从头介绍架构、两种训练方式及其收益。

- **TL;DR**：一句话说明架构贡献和目标，保留已确认的版本。
- **开场段落**：说明现有文本接口的问题和动态动作空间的动机，不提前总结冻结适配、联合训练及通用能力结果。动作编码器仅介绍其接口作用，独立并行编码、状态打分等计算过程留给 Approach。
- **冻结适配**：说明只更新动作编码器的设置和四个未见环境的表现。“不更新任何 LLM 参数”的突出表达只在此处出现一次；不再解释内部状态如何与动作表示匹配。
- **联合训练**：先讲跨环境表现，再讲通用能力。前一段补充常规 RL 在工具使用上的退步与 Dyad 的改善；后一段区分能力损失恢复与已有收益增加，不再重述动作描述构造决策头的机制。
- **Approach**：用购物代理的目标推理与连续动作选择举例，将两种计算类比为 System 2 reasoning 与 System 1 decision-making，再引出 Jev 和 Dyad；不对 typed decision-making 下正式定义。随后依次说明状态与动作语义分离、动作表示复用、交互 token 触发决策、监督对齐和交互奖励。两种训练方式的更新对象已在结果节说明，此处不再重复列举。
- **JevBench**：解释与多步交互评估互补的独立决策比较，并保留有数据支持的差值；不再次概括整个架构贡献。按用户要求，正文用 `absolute gains of 7.08% overall and 12.20% on hard cases` 展示绝对增益；计算仍为两项准确率之差，不改成相对增长率。

措辞依据仍为论文 Abstract、Introduction、Architecture、Learning 和 Experiments。固定动作空间的局限限定为部分已有 LLM 扩展；结果段落由相邻图表限定比较设置，不写成对所有模型或训练环境的无条件保证。必要的术语释义和独立可读的 caption 保留。

页面单位展示补充：所有增益和变化统一使用 `%`，不显示 `pp` 或 `percentage points`。Table 1 列名为 `Gain (%)`，迁移图标注为 `(+9.47%)` 等，能力图横轴与图注注明 `absolute change`。这些变化仍按原始百分制成绩直接相减计算，图注通过 `absolute gains` / `absolute score changes` 保留绝对差值的含义；本文件中以百分点记录的原始差值仍是计算依据。
