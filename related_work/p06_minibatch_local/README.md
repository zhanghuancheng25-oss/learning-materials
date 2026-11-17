# P06 · Minibatch vs Local SGD with Shuffling: Tight Convergence Bounds and Beyond

**位置：mini-batch 核心工作，但主上界明确属于大轮次区间。不是已确认的“Few-Epoch Mini-batch RR”。**

- 作者：Chulhee Yun、Shashank Rajput、Suvrit Sra；ICLR 2022。
- [arXiv 2110.10342v2](https://arxiv.org/abs/2110.10342v2)；[OpenReview](https://openreview.net/forum?id=u6kRArugFrx)。
- 核对位置：§2、Algorithms 1–2、Assumptions 1–4、§3.1 Theorem 1；源码 `2_setting.tex`、`3_upper.tex`。
- 阅读深度：算法、假设与 minibatch 主上界核对；76 页论文未完整读完；local / SyncShuf 仅作方向性阅读，未复核全部下界证明。

## 符号与算法

$M$ 台机器，每台 $N$ 个样本，本地 batch / 通信间隔参数为 $B$，运行 $K$ 个 epoch。

- Minibatch RR：每台提供 $B$ 个在共同参数处计算的梯度，总共 $MB$ 个梯度平均后更新。
- Local RR：每台先做 $B$ 次局部参数更新，然后服务器平均参数。

两者可在同样的梯度计算数与通信次数下比较。它们通常不等价，因为 local 的后续梯度在不同参数处计算。

## 主定理的完整关键项

总目标满足 $\mu$-PL；分量 $L$-smooth；局部分量梯度相对局部平均梯度偏差被 $\nu$ 一致控制，另有论文规定的异质性条件。设 $\kappa=L/\mu$、$B\mid N$，minibatch 的定理取 $1\le B\le N/2$。

Theorem 1 使用

$$\eta=\frac{B\log(MNK^2)}{\mu NK},\qquad K\ge6\kappa\log(MNK^2),$$

以至少 $1-\delta$ 的概率保证

$$F(x_{K,N/B})-F_\star\le\frac{F(x_0)-F_\star}{MNK^2}+\widetilde O\!\left(\frac{L^2\nu^2}{\mu^3MNK^2}\right).$$

本库核对了源码，避免 PDF 排版把 $B$、$M$ 和分母读错。这里是高概率函数差界；与期望界比较时要说明概率口径。

## 最容易漏掉的区别

1. 定理成立的轮次约为 $K\gtrsim\kappa$；与文中 SGD 基准比较获得更好量级可能需要 $K\gtrsim\kappa^2$。这不是同一门槛。
2. 以 epoch 表示时某些项不显含 $B$；改写到通信轮数 $R=NK/B$ 后会出现 $B$。因此“batch size 没影响”是错误解读。
3. 同步打乱 SyncShuf 改变了算法和跨机采样相关性，不能说它违反原算法的下界。

## 下一步

先令 $M=1$，核对 minibatch RR 的实现和 $b=N$ 时退化为 GD 的边界，再进入多机异质性。论文复现尚未运行；官方代码入口本轮未可靠定位。
