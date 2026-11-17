# P01 · Why Random Reshuffling Beats Stochastic Gradient Descent

**位置：历史起点。先理解“按 epoch 分析误差”，不把渐近速率用于少轮次判断。**

- 作者：Mert Gürbüzbalaban、Asuman Ozdaglar、Pablo A. Parrilo。
- 版本：[arXiv 1510.08560v4](https://arxiv.org/abs/1510.08560v4)；2015 首稿，Mathematical Programming 186:49–84 (2021)，[DOI](https://doi.org/10.1007/s10107-019-01440-w)。本地 v4 为 2022 年修订，不与期刊排版等同。
- 阅读深度：摘要、引言与主结果概述；未逐项审查完整证明。PDF / 源码已下载，见 metadata。

## 问题与贡献

处理一轮中梯度误差相互依赖的困难，将轮内累计误差分解为可跨轮处理的项及高阶余项。对总目标强凸、分量二次或满足额外 Hessian 正则性的情形，分析递减步长与迭代平均。

主线中取 $\alpha_k=\Theta(k^{-s})$、$s\in(1/2,1)$，平均输出目标误差具有 $k^{-2s}$ 阶的渐近结论。摘要中的 $\Theta$ 需结合非退化条件理解；不能说包括零噪声等每个特例都具有同一个严格下界。

## 前提与限制

- 原文主问题采用分量**求和**，本库常用平均；光滑常数与步长要随归一化换算。
- 泛光滑非二次情形还涉及 Hessian Lipschitz；不能压缩成“只要光滑就成立”。
- 渐近、平均输出、递减步长的结论，不是固定有限 $K$、常步长、最后迭代点的结论。

## 阅读 / 复现入口

先读摘要及 Introduction，再定位主定理中的 averaging 与步长条件。学习目标：用两句话说明为什么按整轮分析比逐步套 SGD 无偏性更自然。当前无论文数值复现。
