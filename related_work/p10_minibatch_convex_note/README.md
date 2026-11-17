# P10 · Minibatch Random Reshuffling for Smooth Convex Optimization

完整标题：*Minibatch Random Reshuffling for Smooth Convex Optimization: Batch-Size Dependence, Finite-Population Variance, and Quadratic Growth*。

**位置：近期观察项，不与已经发表的基础工作同等看待；其固定分批约化非常适合入门。**

- 作者：Rajesh Kumar；[Optimization Online 页面](https://optimization-online.org/2026/11/minibatch-random-reshuffling-for-smooth-convex-optimization-batch-size-dependence-finite-population-variance-and-quadratic-growth/)，发布于 2026-11-11。
- 状态：8 页预印本；本轮未核实同行评审发表。PDF 已取得，无已核实的源码入口。
- 核对位置：§2 的 Algorithm / Assumptions；§3 的 batch 约化、Lemma 2 方差恒等式；尚未完整审计 restart 证明。

## 可直接理解的约化

固定划分 $\mathcal P=\{B_1,\ldots,B_m\}$，$m=n/b$，定义

$$g_j(x)=\frac1b\sum_{i\in B_j}f_i(x),\qquad F(x)=\frac1m\sum_{j=1}^m g_j(x).$$

每轮打乱这 $m$ 个固定目标，就是在 batch 分量上运行单样本 RR。P08 可作为所用黑箱，但必须重算光滑参数与最优点噪声。此约化本身可直接从算法验证。

## 有限总体修正

若划分最开始均匀随机产生，在固定最优点，有

$$\mathbb E_{\mathcal P}[\sigma_{\mathcal P}^2]=\sigma_\star^2\frac{n-b}{b(n-1)}.$$

其中 $\sigma_{\mathcal P}^2=m^{-1}\sum_j\|\nabla g_j(x_\star)\|^2$。注意这是对随机划分的期望；不能对任意固定划分声称同一个等式。$b=n$ 时方差为零，而主体定理使用 $m\ge2$，full-batch 需单独按 GD 处理。

## 范围与选题提醒

此文没有覆盖每轮重新划分 batch 的情况；作者将其作为未覆盖情形讨论。但这不是全领域没有相关理论的证据，宣称开放问题前必须检索其它工作。本文标题也不等于用户所说的“Few-Epoch Mini-batch RR”，目前不做身份认定。

主要学习价值是：batch 同时改变更新次数、有效光滑性和方差，不能只保留一个 $1/b$ 方差因子就宣布总梯度复杂度提高 $b$ 倍。
