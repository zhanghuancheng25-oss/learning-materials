# 实验版本记录

每完成一版追加一行，保留失败与作废版本。参数和评价口径先写入 [evaluation.md](evaluation.md)。

| 版本 | 性质与变化 | 范围 / 主指标 | 检查与结论 | 状态 |
|---|---|---|---|---|
| v1_sampling_quadratic | 首个采样机制教学实验 | 5 方法 × 3 batch × 2 条件数 × 3 学习率 × 10 种子，共 900 条轨迹；完整目标差见 metrics | 梯度、样本覆盖、full-batch=GD、有限总体方差与手算例子通过；不支持逐配置 RR 必胜 | 已运行；不属于论文图表复现 |

输出：[metrics](v1_sampling_quadratic/metrics.json)、[全部轨迹](v1_sampling_quadratic/trajectories.json)、[图](v1_sampling_quadratic/convergence.png)、[限制配置](v1_sampling_quadratic/failure_cases.md)、[报告](../复现/v1_sampling_quadratic/复现报告.md)。

数值结果未作废。只修改过绘图坐标范围，原图与运行脚本快照保留；未更换评测指标。

尚未运行：P03 作者代码图表；P05 原始病态构造；P07 平均动态恒等式。具体计划见 [复现入口](../复现/README.md)。
