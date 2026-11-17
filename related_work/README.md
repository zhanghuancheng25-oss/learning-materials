# Random Reshuffling：文献库与学习入口

调研日期：**2026-11-17**。本轮选择 10 篇工作：基础 2 篇、核心 6 篇、反例 1 篇、近期观察 1 篇。范围是有限和优化中的 RR、少轮次与 mini-batch，不是整个领域的穷尽检索。

**先读 [00_入门.md](00_入门.md)，再读 [01_调研综述.md](01_调研综述.md)。不要从长篇附录或最新预印本开始。**

## 导航

- [00_入门.md](00_入门.md)：SGD / RR / SO / IG、batch 与 epoch、基本假设、一个可手算例子。
- [01_调研综述.md](01_调研综述.md)：研究脉络、关键分歧、少轮次问题的现状。
- [02_论文对照矩阵.md](02_论文对照矩阵.md)：模型、采样、输出、前提和阅读优先级。
- [03_学习路线.md](03_学习路线.md)：分阶段阅读，附每阶段验收问题。
- [04_检索记录与待确认.md](04_检索记录与待确认.md)：检索范围、来源与待核实信息。
- [references.bib](references.bib)：书目；[papers.json](papers.json)：下载清单。
- [../复现/README.md](../复现/README.md)：教学实验与下一步正式复现。

## 论文目录

| ID | 工作 | 年份 / 状态 | 为什么读 |
|---|---|---|---|
| P01 | [Why RR Beats SGD](p01_why_rr_beats_sgd/README.md) | 2015 首稿；Mathematical Programming 2021 | epoch 内相关误差的处理起点 |
| P02 | [SGD without Replacement](p02_sgd_without_replacement/README.md) | ICML 2019 | 去掉 Hessian Lipschitz 的非渐近分析 |
| P03 | [Simple Analysis with Vast Improvements](p03_simple_analysis/README.md) | NeurIPS 2020；阅读 arXiv v3 | 第一篇重点读，统一比较 RR / SO / IG |
| P04 | [How Good is SGD with Random Shuffling?](p04_how_good/README.md) | COLT 2020 | 下界与采样方式的区分 |
| P05 | [Only After Many Epochs](p05_many_epochs/README.md) | NeurIPS 2021 | 少轮次、条件数与最坏情形障碍 |
| P06 | [Minibatch vs Local SGD with Shuffling](p06_minibatch_local/README.md) | ICLR 2022 | 分布式 minibatch / local RR，明确大轮次条件 |
| P07 | [Error dynamics of mini-batch GD with RR](p07_minibatch_least_squares/README.md) | ALT 2025 | 最小二乘、固定分批、有限步长与平均轨迹 |
| P08 | [RR Dominates SGD：扩展版](p08_rr_dominates/README.md) | COLT 2026 前身；2026-11 扩展预印本 | 一般光滑凸情形的新步长和少轮次结论 |
| P09 | [RR is Not Always Better](p09_not_always_better/README.md) | NeurIPS 2020 | 防止把理论速率误读为逐实例必胜 |
| P10 | [Minibatch RR for Smooth Convex Optimization](p10_minibatch_convex_note/README.md) | 2026-11-11 预印本 | 固定分批约化、batch size 与有限总体修正 |

“Few-Epoch Mini-batch RR”目前不是本库中已经确认的独立论文标题。其精确身份待用户补充；围绕它的主题已经安排 P05、P06、P08、P10 的阅读链。

## 文件与同步约定

每篇目录包含已提交的 `README.md`、`metadata.json`，以及本地缓存的 `paper.pdf`、`paper.txt`、`source/`。本轮 10 篇 PDF 都已下载；8 篇有 arXiv 源码。P09、P10 尚无经过核实的源码入口，不能把网络未找到等同于作者没有源码。

按上游 workflow 的 `.gitignore` 约定，PDF、解压源码、数据不进入 Git；GitHub 共享笔记、固定版本链接、SHA-256、代码与结果。其他电脑可重新下载：

```powershell
python scripts/fetch_papers.py
# 仅下载一篇
python scripts/fetch_papers.py --only p03_simple_analysis
```

Python 标准库即可下载，`pdftotext` 是文本抽取的可选外部命令。源码只解压，不执行；清洗版用于阅读，`.orig` 保留原文，编译应使用原始版本。源码清洗采用上游的简易百分号规则，复杂 verbatim / 宏场景仍需对照 PDF。

下载版本、哈希与阅读位置以逐篇元数据及笔记为准。论文权益属于各作者；上游工作流的 Apache-2.0 许可证不适用于这些论文。
