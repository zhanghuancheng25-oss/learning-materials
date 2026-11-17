# Random Reshuffling 学习与文献调研

在有限和优化背景下，从零学习 Random Reshuffling（RR）、少轮次训练和 mini-batch；建立可核查文献库，再开展 baseline 复现。

**当前目标是理解与复现，不预设“RR 总是更好”，也没有已经验证的创新主张。**

投稿会议、截止日期与具体研究问题：尚未设定。用户明确自己没有该方向背景，讲解需从基本概念开始。

## 每次先读

1. 本文件。
2. [handoff.md](handoff.md)。
3. 文献工作读 [related_work/README.md](related_work/README.md)；运行实验前读 [experiment/evaluation.md](experiment/evaluation.md) 和 [experiment/results.md](experiment/results.md)。

按需读，不通读全部 PDF / LaTeX。长 PDF 先摘要、设定、主定理、关键图与局限，再按问题查看证明。表格文件默认只看变量名、表头；确需数值分析时明确限定范围。

## 目录

| 路径 | 职责 |
|---|---|
| `related_work/` | 总览、学习入口、对照矩阵、逐篇笔记、元数据；本地另存 PDF 和源码 |
| `复现/` | 教学实验与正式论文复现报告，二者必须区分 |
| `experiment/` | 固定测评规范、版本记录、可重复的代码与结果 |
| `DataSet/`、`dataset.md` | 数据与生成方式；大数据不提交 |
| `brainstorm.md` | 已发生的讨论、待验证问题，不虚构用户观点 |
| `scripts/` | Windows 可运行的论文下载工具 |
| `tools/research-workflow/` | 固定版本的上游 workflow 与模板，保留 Apache-2.0 许可证 |
| `materials/`、`notes/` | 原共享仓库保留目录 |

## 硬规矩

- 中文解释结论在前，严谨直接；发现错误立即指出。数学用 LaTeX，实验默认 Python。
- 标准术语：finite-sum optimization、SGD、with/without replacement、RR、Shuffle Once、Incremental Gradient、epoch、mini-batch、smoothness、strong convexity、PL condition、gradient complexity。
- 区分：每轮重新分批 / 固定批次打乱；epoch / update / 单样本梯度次数；平均迭代点 / 最后迭代点；最坏情形界 / 实测性能；凸 / 强凸 / PL / 一般非凸。
- 每条论文结论标明来源、版本、假设与定位。摘要筛选、定理核对、完整证明检查、数值复现分别记录，不能相互替代。
- 新文献改变研究边界，不能直接照抄旧论文的“open problem”。未经系统排查，不宣称首创。
- 改实验前说明改什么及目的；完整保存失败配置。先固定测评，再运行，不按结果选择口径。
- 版本名用 `v<序号>_<核心变化>`；结果只追加，不覆盖。小型教学脚本通过不等于论文复现成功。
- 不假装有用户尚未确认的目标；“Few-Epoch Mini-batch RR”精确书目暂待确认，不能绑定到相似论文。
- GitHub 远端已是 `zhanghuancheng25-oss/learning-materials`。本次用户授权同步成果；后续新任务的发布范围按其指令判断。
- 窗口结束前更新 handoff。不要记录凭据、无关个人信息或机器本地敏感路径。
