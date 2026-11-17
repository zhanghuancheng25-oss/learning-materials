# 学习与共享资料

用于上传、整理和共享学习资料与笔记。

当前专题：**Random Reshuffling（RR）、少轮次与 mini-batch 优化**，首次调研日期 2026-11-17。

## 从这里开始

- [文献库总入口](related_work/README.md)：10 篇精选工作、逐篇中文笔记、原文链接与下载方式。
- [零基础入门](related_work/00_入门.md)：先理解算法、采样、batch 与计算预算。
- [调研综述](related_work/01_调研综述.md)与[论文对照矩阵](related_work/02_论文对照矩阵.md)。
- [分阶段学习路线](related_work/03_学习路线.md)。
- [教学实验与正式复现计划](复现/README.md)。

按 [research-workflow](https://github.com/skJack/research-workflow) 建立固定文档职责；来源与适配见 [tools/WORKFLOW_PROVENANCE.md](tools/WORKFLOW_PROVENANCE.md)。当前是学习与调研项目，尚无已验证的创新结论。

## 目录

- `materials/`：学习资料、文档及参考链接。
- `notes/`：个人学习笔记。
- `related_work/`：文献笔记、书目及元数据。本地 PDF / 源码按 workflow 约定不提交，可用下载器恢复。
- `复现/`：教学实验报告与正式论文复现任务。
- `experiment/`：固定测评、实验代码、版本结果和图。
- `AGENTS.md`、`handoff.md`：项目规则与交接；`brainstorm.md`：问题记录。
- `dataset.md`、`DataSet/`：数据说明和本地数据位置。

## 通过网页上传

1. 打开仓库，进入对应目录。
2. 点击 **Add file → Upload files**，拖入要上传的文件。
3. 填写简短说明，点击 **Commit changes** 完成上传。

共享资料时，复制仓库或具体文件的网页链接即可。

## 通过本地 Git 上传

在本仓库目录中打开 PowerShell，放入资料后执行：

```powershell
git pull --ff-only
git add materials notes related_work 复现 experiment scripts tools DataSet/README.md README.md AGENTS.md handoff.md brainstorm.md dataset.md .gitignore .gitattributes
git diff --cached --stat
git commit -m "更新学习资料"
git push
```

`pull` 同步远端更新，`add` 选择本次上传的文件，`diff` 检查文件清单，`commit` 保存本地版本，`push` 上传到 GitHub。
