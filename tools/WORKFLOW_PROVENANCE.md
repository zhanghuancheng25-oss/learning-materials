# research-workflow 的来源与本地适配

- 用户指定来源：[skJack/research-workflow](https://github.com/skJack/research-workflow)。
- 固定提交：[14c882df49a7991b9833f2ff416e4dfd38668827](https://github.com/skJack/research-workflow/tree/14c882df49a7991b9833f2ff416e4dfd38668827)。
- 调研 / 下载日期：2026-11-17。
- 原始 SKILL、README、模板、脚本和 LICENSE 保存在 [research-workflow/](research-workflow/)，未改写。

本项目采用其文件职责和“文献→复现→假设→实验”顺序。项目名、学习目标与术语依据当前请求填写；未提供投稿目标和 deadline，明确记为未设定，不把这些信息当成阻塞项。

Windows 适配使用 [../scripts/fetch_papers.py](../scripts/fetch_papers.py)：Python 标准库下载、验证 PDF 文件头、固定 arXiv 版本、记录 SHA-256、只解压普通文件、隔离旧稿、保留 `.orig`。源码下载失败记录真实原因，不用“PDF-only 投稿”猜测代替。`pdftotext -layout` 仅辅助阅读，公式仍核对 LaTeX / PDF。

原 workflow 忽略 PDF、源码及大数据。本仓库沿用此约定；GitHub 提交原创笔记、元数据、下载器与小型结果。未安装到全局技能目录，避免改变其他项目配置。

模板中的监督学习 split、失败样例数不是本项目的通用数学要求。教学有限和优化只衡量训练目标，不声称泛化；后续实数据实验再制定相应的划分方法。
