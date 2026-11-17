# 学习与共享资料

用于上传、整理和共享学习资料与笔记。

## 目录

- `materials/`：学习资料、文档及参考链接。
- `notes/`：个人学习笔记。

## 通过网页上传

1. 打开仓库，进入对应目录。
2. 点击 **Add file → Upload files**，拖入要上传的文件。
3. 填写简短说明，点击 **Commit changes** 完成上传。

共享资料时，复制仓库或具体文件的网页链接即可。

## 通过本地 Git 上传

在本仓库目录中打开 PowerShell，放入资料后执行：

```powershell
git pull --ff-only
git add materials notes README.md
git diff --cached --stat
git commit -m "更新学习资料"
git push
```

`pull` 同步远端更新，`add` 选择本次上传的文件，`diff` 检查文件清单，`commit` 保存本地版本，`push` 上传到 GitHub。
