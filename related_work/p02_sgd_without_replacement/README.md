# P02 · SGD without Replacement: Sharper Rates for General Smooth Convex Functions

**位置：从早期额外二阶正则假设，转向更一般的光滑凸非渐近分析。**

- ICML 2019 会议页面书目作者顺序：Dheeraj Nagaraj、Prateek Jain、Praneeth Netrapalli；[会议页面](https://proceedings.mlr.press/v97/nagaraj19a.html)。
- 阅读版：[arXiv 1903.01463v2](https://arxiv.org/abs/1903.01463v2)，其封面作者顺序不同，引用会议版本时按会议页面。
- 阅读深度：摘要、引言与研究设定筛选；尚未逐定理审查。PDF / 源码已取得。

## 贡献

用 exchangeable pairs 与 Wasserstein 距离控制采样索引和迭代点的耦合。对光滑强凸有限和目标给出非渐近分析，去掉此前一类结果的 Hessian Lipschitz 要求。大轮次下可出现 $K^{-2}$ 级别改进，小轮次下提供与 SGD 同阶的保证。

## 不能省略的内容

“去掉 Hessian Lipschitz”不意味着没有其它约束。原文分析还包含定义域 / 梯度界、步长与轮次要求；仅根据摘要无法把 $O(K^{-2})$ 当成所有 $n,L,\mu,K$ 下的完整定理。故本库暂不抄一个省略参数的速率作为可直接应用公式。

## 后续问题

与 P03 比较：P03 如何进一步改变梯度有界假设及 RR / SO 的分析方式？与 P08 比较：一般光滑凸情形的步长限制后来怎样放宽？

下一次精读应整理“定义域、光滑常数、强凸、梯度界、输出平均、轮次下限”六项，再逐式比较。当前无数值复现。
