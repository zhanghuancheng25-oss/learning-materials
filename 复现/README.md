# 教学实验与正式论文复现

**已完成：采样机制教学实验。未完成：任何论文原始图表的正式复现。**

- [教学实验报告](v1_sampling_quadratic/复现报告.md)：5 种采样、3 种 batch、2 种条件数、3 种步长、10 个种子，共 900 条轨迹。
- [固定测评规范](../experiment/evaluation.md)。
- [完整结果记录](../experiment/results.md)。

## 本机直接运行

```powershell
& 'C:/Users/26520/Miniconda3/envs/pytorch/python.exe' -X utf8 experiment/rr_quadratic_demo.py --output experiment/v2_sampling_quadratic_repeat
```

此 Python 环境已实际验证含 NumPy 与 Matplotlib。原始 `v1` 目录不能覆盖，所以重复时使用新的输出目录。跨电脑可自行选择 Python 环境：

```powershell
python -m pip install -r experiment/requirements.txt
python experiment/rr_quadratic_demo.py --output experiment/v2_sampling_quadratic_repeat
```

`pip install` 安装绘图库与数值库，脚本生成合成目标、按固定参数运行，并保存全部结果。它不下载真实数据集、不训练神经网络。

## 正式复现顺序

| 任务 | 状态 | 下一步及验收 |
|---|---|---|
| P03 官方代码中的一个明确图表 | 作者仓库已确认；未运行 | 固定代码提交与数据，核对算法、正则系数、步长和图轴，保存环境与差异报告 |
| P05 病态二次构造 | 作者仓库已确认；未运行 | 对照原文公式与脚本，先原参数复现趋势，再改变条件数 / batch |
| P07 平均轨迹公式 | 未实现 | 小批次数枚举所有排列，比较理论平均映射、Monte Carlo 平均点与期望损失 |
| Few-Epoch Mini-batch RR | 书目待确认 | 用户补充题名 / 链接后定位其算法、定理与作者代码 |

没有正式复现数值之前，不把教学曲线写进论文“重现已有方法”的表格。
