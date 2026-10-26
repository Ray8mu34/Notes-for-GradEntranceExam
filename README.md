# 考研笔记

这是一个使用Hugo构建的考研笔记网站，包含如下内容，希望能对备考有所帮助。

- 微积分笔记
- 线性代数笔记
- 概率论与数理统计笔记
- 控制理论笔记
- 控制理论习题
- 英语一大作文讲解
- 英语一小作文讲解

## 公式与结论汇总

以下四份笔记已同步校正公式后的 Markdown。可以直接在 GitHub 中阅读，也可以访问[笔记网站](https://ray8mu34.github.io/Notes-for-GradEntranceExam/)。

- [微积分公式与结论汇总](content/微积分笔记/index.md)
- [线性代数公式与结论汇总](content/线代笔记/index.md)
- [概率论与数理统计公式与结论汇总](content/概统笔记/index.md)
- [控制理论公式与结论汇总](content/控制理论笔记/index.md)

行内公式使用 `$...$`，独立公式使用 `math` 代码块，使公式同时适用于 GitHub 阅读页和 Hugo 网站。图片与笔记放在同一目录，通过相对路径引用。

## 项目结构

- `content/`：存放Markdown格式的笔记内容
- `static/`：存放静态资源，如图片等
- `themes/`：存放Hugo主题
- `hugo.toml`：Hugo配置文件

## 本地开发

1. 安装Hugo 0.159.1（与自动部署使用同一版本）
2. 克隆仓库
3. 运行 `hugo server -D` 启动本地服务器
4. 访问 `http://localhost:1313/` 查看网站

## 部署

项目使用GitHub Actions自动部署到GitHub Pages。
