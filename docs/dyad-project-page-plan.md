# Dyad project page：内容与表达方案

日期：2026-10-16。本文已按本轮用户反馈更新，取代上一版的代表性子集叙述与隐藏数据表方案。实现位于 `index.html`；发布状态以 GitHub Pages 为准。

依据：[EARL 整体分析](earl-project-page-analysis.md)、[EARL 正文与图注分析](earl-writing-and-captions.md)、[Dyad 论文 v1](https://arxiv.org/html/2609.36116v1)。以下论文来源编号用于内部核查；网页拥有自己独立的 Table/Figure 编号。

## 1. 开场与阅读顺序

TL;DR 使用一句话，介绍架构及代理价值。紧接一个简短段落，只保留现有文字动作接口、动作编码器与动态决策、保留语言推理及两种训练设置；并行编码等机制细节交给 Approach。

页面顺序：

1. 标题、作者、机构、论文入口。
2. 一句话 TL;DR 与解释段落。
3. **1. Modular Adaptation with a Frozen LLM**：问题与价值、观察到的能力变化、可见 Table 1。
4. **2. Cross-environment Generalization**：新环境中的决策问题、CodeGym 训练后的迁移能力、Figure 1。
5. **3. Preserving General Capabilities**：代理训练为何还要检查通用能力、Figure 2。
6. **Approach**：架构机制、Figure 3 / MP4 位置、推理与训练流程。
7. BibTeX 与模板署名。

每个主节只用一个 h2，标题之后直接是段落。模型型号、算法配置、seed 数、图例与度量定义放在 caption，正文围绕研究问题、能力变化及其含义展开。

## 2. Table 1：冻结 LLM 的模块化适配

网页名称：**Modular adaptation without updating the LLM.**

数据来源：[论文 Table 4，p.8](https://arxiv.org/pdf/2609.36116v1#page=8)。仅展示 Qwen3.5-9B 的原始模型与 Frozen Dyad，不重复展示联合训练行。

| 环境 | 原始 LLM | Frozen Dyad | 变化，百分点 |
|---|---:|---:|---:|
| ALFWorld | 45.66 | 48.82 | +3.16 |
| WebShop | 33.43 | 35.00 | +1.57 |
| τ²-bench | 62.17 | 64.23 | +2.06 |
| SWE-bench Verified | 44.56 | 45.50 | +0.94 |

正文强调只更新动作编码器、LLM 与语言头固定所带来的模块化价值。caption 写明模型、GRPO、DIVE、冻结对象、评估范围与 seeds。表格直接显示全部选定数值，改善后的成绩加粗。

## 3. Figure 1：CodeGym 训练后的跨环境泛化

网页名称：**Generalization to unseen environments.**

按用户指定，这一节只展示 CodeGym 训练后的结果。选择 Qwen3.5-9B + GRPO，四个环境全部保留；不展示 DIVE 数据，也不在正文中混用全实验的 41/48 汇总。正文使用“CodeGym-trained agent”限定所述结果，caption 精确限定模型与算法，不写成所有模型、所有训练来源都获得同样改善。

数据来源：[论文 Table 3，p.6](https://arxiv.org/pdf/2609.36116v1#page=6)。

| 环境 | GRPO | Dyad-GRPO | 变化，百分点 |
|---|---:|---:|---:|
| ALFWorld | 51.55 | 55.13 | +3.58 |
| WebShop | 36.23 | 38.07 | +1.84 |
| τ²-bench | 61.31 | 63.02 | +1.71 |
| SWE-bench Verified | 49.40 | 50.62 | +1.22 |

图直接标注两种方法的成绩，Dyad 成绩后的括号标注变化；所有选择展示的信息都能直接读到。桌面与手机分别生成 SVG，不依赖悬停或点击。

图注说明：这是 CodeGym 训练后的 Qwen3.5-9B，配对比较使用相同 RL 算法、训练环境与初始 LLM；在四个其他环境上评估，不继续训练，使用三个评估 seed。

## 4. Figure 2：通用能力保留

网页名称：**Retaining knowledge, reasoning, and coding after agentic training.**

来源：[论文 Figure 3，p.7](https://arxiv.org/pdf/2609.36116v1#page=7)，精确绝对成绩来自 [arXiv v1 源码](https://arxiv.org/src/2609.36116v1)的 `resources/figures/figure_general_capabilities.tex`。来源文件 hash 保存在 `static/data/results.json`。

这一节仍保留 DIVE 与 CodeGym，展示同一 Qwen3.5-9B/GRPO 配置在三项通用能力上的变化。用户对 CodeGym-only 的选择针对跨环境节；此处的两个训练来源用于解释能力保留的不同情形。

| 训练来源与 benchmark | GRPO 相对原始模型 | Dyad-GRPO 相对原始模型 |
|---|---:|---:|
| DIVE · MMLU-Pro | −1.32 | +0.09 |
| DIVE · HMMT | −0.23 | +0.69 |
| DIVE · LiveCodeBench | +0.59 | +2.48 |
| CodeGym · MMLU-Pro | +0.15 | +0.75 |
| CodeGym · HMMT | +2.27 | +5.66 |
| CodeGym · LiveCodeBench | +3.58 | +3.66 |

图中以 Knowledge、Mathematical Reasoning、Coding 三项能力命名，并直接标出两种方法的变化值。caption 再对应说明 MMLU-Pro、HMMT February 2026、LiveCodeBench v6，并解释原始模型零参考线、空心/实心点和单位。连接线表示方法之间的配对比较，不表示误差区间。没有原始 seed 日志，因此不添加未经提供的误差条。

## 5. Figure 3：Approach

网页名称：**Language reasoning and typed decisions within one policy.**

使用论文原架构图作为 MP4 未提供或加载失败时的回退画面；caption 与编号一直可见。用户准备的 MP4 后续接入同一个位置。

解释顺序为：LLM 编码交互历史；动作编码器独立并行编码候选描述；语言头生成推理 token；交互 token 触发 typed action 分布；动作执行后的观察回到历史。缓存适用于动作描述和环境上下文不变的情况。

训练说明保留监督对齐、冻结适配与联合训练，明确 RL 阶段更新完整动作编码器。这里不增加 CPO、Zero-RL 或未经验证的统一速度提升声明。

## 6. 写作与排版规则

- 正文先讲问题与能力，再给结论及意义；型号与具体设置交给 caption。
- 删除“代表性子集”“我们保留了哪些数据”等图表编辑过程的叙述。
- 页面独立编号 Table 1、Figure 1–3；正文中的编号链接只定位到已经可见的证据。
- 每个 caption 以加粗的编号和简短名称起句，再说明模型、训练/评估设置与必要图例。
- 正文每节只强调少量关键能力或结果；caption 中强调模型名；表格中强调配对更好的成绩。
- 正文保持 EARL 的 960px 桌面容器、19.2px 字号；caption 为左对齐 16px，手机为 15.2px。
- 不使用隐藏结果表、折叠实验区、仅悬停可读的分数或点击展开的数据。图像替代文本包含选定数值，供屏幕阅读器使用。

## 7. 继续留在论文中的内容

域内成绩、完整跨模型/跨算法结果、Jev 对比、训练曲线、组件消融、pooling 对照、超参数和 prompt 不进入页面主体。完整来源数据继续保存在仓库，页面只介绍所选论点并明确证据范围。

## 8. 验证

检查单句 TL;DR、单层主标题、caption 编号与锚点、正文无型号、可见表格、CodeGym-only 迁移图、图中全部数值、桌面与手机渲染、无横向溢出、BibTeX 复制和视频回退。真实 MP4 播放需要在用户提供文件后检查。
