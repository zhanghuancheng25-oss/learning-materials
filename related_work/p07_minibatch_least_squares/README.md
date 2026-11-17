# P07 · Error dynamics of mini-batch gradient descent with random reshuffling for least squares regression

**位置：适合连接线性代数、离散系统与 mini-batch；必须注意它研究的是固定分批及平均迭代轨迹。**

- 作者：Jackie Lok、Rishi Sonthalia、Elizaveta Rebrova；ALT 2025。
- [会议页面](https://proceedings.mlr.press/v272/lok25a.html)；[arXiv 2406.03696v2](https://arxiv.org/abs/2406.03696v2)。
- 核对位置：§2 Model，Theorems 3.3、3.9；源码 `batch.tex`。
- 阅读深度：算法设定、平均量定义、主动态公式及限制核对；随机矩阵渐近部分未完整审查。

## 模型与贡献

线性观测 $y=X\beta_\star+\varepsilon$。原文 $B$ 表示**批次数**，每批样本数为 $n/B$。最初划分固定的 $X_1,\ldots,X_B$，每轮仅随机改变这些批次的访问顺序。

利用批次矩阵乘积构造修正特征 $\widetilde X$ 与 $Z=n^{-1}\widetilde X^TX$，刻画排列平均后的参数轨迹、训练及泛化误差。有限步长的高阶项带来梯度流极限看不到的效应，小步长下与按比例缩放步长的 full-batch 动态在首阶对应。

## 关键限定

论文定义 $\bar\beta_k=\mathbb E_{\text{排列}}[\beta_k]$。Theorem 3.3 对其误差给出矩阵递推，并有 $\operatorname{Range}(\widetilde X^T)\subseteq\operatorname{Range}(\widetilde X^TX)$ 等技术条件。Theorem 3.9 分析的是该平均轨迹的风险。

$$\mathbb E[F(\beta_k)]\quad\text{与}\quad F(\mathbb E[\beta_k])$$

一般不同。前者还有随机参数的方差贡献，不能用后者代替。有限步长导致的极限变化也须在原模型、秩及稳定性条件下解释。

## 适合的第一项正式复现

用小型线性模型及少量固定批次，枚举所有批次排列，核对一轮平均映射，再比较多轮 Monte Carlo 的平均参数。分别报告平均参数误差、平均目标差和参数方差。然后才考虑重新分批算法，作为新设置明确标记。

本轮没有验证 Theorem 3.3 的数值恒等式，也没有复现论文图表。官方代码未可靠定位。
