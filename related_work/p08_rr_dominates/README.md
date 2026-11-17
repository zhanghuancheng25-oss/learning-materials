# P08 · Random Reshuffling for Smooth Convex Optimization: Dominates Stochastic Gradient Descent

**位置：少轮次阅读链中必须更新的 2026 年结果。“Dominates”是相应理论界的比较，不是每个实例的严格优势。**

- 作者：Zijian Liu。
- 前身：[Random Reshuffling Dominates SGD，COLT 2026](https://proceedings.mlr.press/v336/liu26d.html)，[arXiv 2606.32005v1](https://arxiv.org/abs/2606.32005v1)。
- 本轮阅读：[扩展版 arXiv 2611.07406v1](https://arxiv.org/abs/2611.07406v1)，2026-11-05 发布。扩展版新增的下界、quadratic growth 等不能全部归到前身会议论文。
- 核对位置：Assumptions 1–3；§3 Theorem 1、Corollary 1；源码 `preliminaries.tex`、`algorithm.tex`。主定理 PDF 第 5 页。
- 阅读深度：前提、输出、主界、调优界与比较说明已核对；未独立完成全部证明审计。

## 假设与输出

每个 $f_i$ 凸且 $L_i$-smooth，有限和存在最小点。定义 $\widehat L=\max_iL_i$、$\bar L=n^{-1}\sum_iL_i$、$D=\|x_0-x_\star\|$、$\sigma_\star^2=n^{-1}\sum_i\|\nabla f_i(x_\star)\|^2$。

允许每轮步长 $0<\eta_k<2/\widehat L$。输出是跨轮、跨轮内位置的加权平均，权重正比 $(2-\eta_k\widehat L)\eta_k$，不是最后迭代点。

## 一个便于阅读的常步长形式

由 Theorem 1 令 $\eta_k=\eta$，可得

$$\mathbb E[F(\bar x_K)-F_\star]\lesssim\frac{D^2}{(2-\eta\widehat L)\eta nK}+\frac{\min\{1,\eta n\bar L\}\eta\sigma_\star^2}{(2-\eta\widehat L)^2}.$$

这里 $\lesssim$ 隐藏绝对常数。常步长时输出是所有更新前迭代点的均匀平均。不能仅凭 $\eta<2/\widehat L$ 说非零噪声下常步长误差必然趋零。

Corollary 1 对已调优的常步长给出

$$\mathbb E[F(\bar x_K)-F_\star]\lesssim\frac{\widehat L D^2}{nK}+\min\left\{\frac{\sigma_\star D}{\sqrt{nK}},\left(\frac{\bar L\sigma_\star^2D^4}{nK^2}\right)^{1/3}\right\}.$$

右侧含有 SGD 型噪声项与 RR 型噪声项的较小者，所以旧 RR 上界在小 $K$ 时比 SGD 更差的缺陷得到修正。某些区间仍然同阶；不保证每个 $K$ 都有严格量级优势。

## 对研究选题的直接影响

- 不能继续把“一般光滑凸 RR 是否能在合理步长、任意有限轮数获得不劣于 SGD 的界”原封不动当作未解问题。
- 不能直接延伸为非凸神经网络、最后迭代点、每轮重新分批或 Adam / momentum 的保证。
- 与 P05 比较必须统一函数类、条件数、输出与预算；与 P09 的逐实例反例也不冲突。

复现方向：先在凸问题上同时记录最后点与全部迭代点平均，核对步长及梯度预算。当前只有公式核对，没有该定理的完整数值验证。
