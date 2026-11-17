# P03 · Random Reshuffling: Simple Analysis with Vast Improvements

**位置：第一篇核心精读。用同一框架认识 RR、SO 和 IG，但不同定理的假设不能混用。**

- 作者：Konstantin Mishchenko、Ahmed Khaled、Peter Richtárik。
- NeurIPS 2020；阅读 [arXiv 2006.05988v3](https://arxiv.org/abs/2006.05988v3)，该版增加了结果，不能把全部内容都称为会议初版。
- 核对位置：§1.1 算法；§3 Definition 2、Theorems 1–3；源码 `rr_arxiv.tex`。
- 阅读深度：算法与上述定理假设、公式已核对；未逐行验证全部证明和非凸附录。

## 关键想法

轮内迭代不始终围绕同一个 $x_\star$ 摆动。构造与排列对应的参考点

$$x_\star^j=x_\star-\eta\sum_{s<j}\nabla f_{\pi(s)}(x_\star),$$

再比较实际轨迹与这条参考轨迹。由 Bregman divergence 定义 shuffling variance，避免直接要求全局有界梯度。

## 可以准确引用的结论

Theorem 1：**每个分量**均 $\mu$-强凸且 $L$-smooth，常步长 $\eta\le1/L$ 时，RR / SO 的轮末输出满足

$$\mathbb E\|x_K-x_\star\|^2\le(1-\eta\mu)^{nK}\|x_0-x_\star\|^2+\frac{2\eta\sigma_{\mathrm{Shuffle}}^2}{\mu}.$$

$\sigma_{\mathrm{Shuffle}}^2$ 本身依赖 $\eta$。有一个几何衰减项，不代表常步长一定精确收敛到最优点。

Theorem 2 放宽为每个分量凸、仅总目标强凸，但需要更小步长。Theorem 3 的一般凸结果，在 $\eta\le1/(\sqrt2Ln)$ 下，对轮末点的平均 $\hat x_K=K^{-1}\sum_{k=1}^Kx_k$ 给出

$$\mathbb E[F(\hat x_K)-F_\star]\le\frac{\|x_0-x_\star\|^2}{2\eta nK}+\frac{\eta^2Ln\sigma_\star^2}{4}.$$

这两个输出及误差量不同。摘要中“去掉小步长 / 大轮次限制”不能覆盖式中仍有 $1/n$ 限制的一般凸定理。

## 与本项目的关系

先学这里的轮内参考轨迹与误差递推，再读 P05 的下界和 P08 的一般凸改进。不要把 P03 单样本 RR 的结论直接替换 $n\to n/b$：必须先说明分批是否固定、分量光滑性和噪声如何变化。

## 复现入口

[作者代码](https://github.com/konstmish/random_reshuffling) 已确认存在，含 `run_and_plot.ipynb`、SGD / shuffling 实现及 logistic regression 数据。下一步先复现一个明确图表，锁定提交、数据与步长；本轮仅核实入口，未运行作者代码。
