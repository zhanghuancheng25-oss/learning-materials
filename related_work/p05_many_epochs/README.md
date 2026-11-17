# P05 · Random Shuffling Beats SGD Only After Many Epochs on Ill-Conditioned Problems

**位置：少轮次研究必须面对的条件数障碍；结论是最坏情形，不是逐任务预测。**

- 作者：Itay Safran、Ohad Shamir；NeurIPS 2021。
- [arXiv 2106.06880v2](https://arxiv.org/abs/2106.06880v2)。
- 核对位置：Assumptions 1–2；Theorem 2 的 RR 下界与 Theorem 4 的上界；§5 实验。
- 阅读深度：主定理、条件与公式核对；未逐行核验完整证明。

## 主结果

令 $\kappa_F=\lambda_{\max}/\lambda$，这里来自总二次目标的谱参数，**不要自动等同于最大分量光滑度 $L/\lambda$**。对论文的函数类，RR 最坏情形误差有以下结构：

$$\frac{G^2}{\lambda nK}\min\left\{1,\frac{\kappa_F}{nK}+\frac{\kappa_F^2}{K^2}\right\}.$$

Theorem 2 给出固定步长类的困难实例下界；Theorem 4 在分量 Hessian 为可交换半正定矩阵、固定维数等条件下，以 $\eta=\log(nK)/(\lambda nK)$ 得到匹配到对数项的上界。

当 $K\lesssim\kappa_F$ 时，该最坏情形不能获得相对 with-replacement SGD 的量级改进。它并没有证明“每个病态问题在前 $\kappa_F$ 轮都一样慢”。

## 与 P08 不矛盾

P08 讨论一般光滑凸类、特定平均输出的界，消除旧上界在短训练下**反而更差**的问题。P05 的条件数显式困难实例、常步长和轮末输出，与 P08 的比较对象、输出和参数化不一致。“不更差”也不是所有短训练都“严格更快”。

## 实验入口与验收

[官方代码](https://github.com/ItaySafran/SGD_condition_number) 已定位；主文件为 `with- vs without-replacement SGD.py`，另有作者输出压缩包。正式复现应记录具体提交、构造公式、$n,\lambda,\lambda_{\max},G,K$、步长搜索预算、种子及图轴。

验收要点：先重现论文选定构造和趋势，再谈改变 batch；必须分别给 SGD 与 RR 同等调参预算。当前没有运行该官方脚本，教学实验不替代此复现。
