# ZilongYin-Drawio

这是一个 Codex skill，用来按照我的论文图审美生成图，支持：

- 给 GPT Image2 写论文图提示词
- 生成可编辑的 `.drawio` 源文件
- 按 `2025.12.1` 之后的近期论文图风格统一输出

## 安装

把 skill 文件夹复制到 Codex skills 目录：

```powershell
git clone https://github.com/LieLieLieLieLie/YinZiLong.git
Copy-Item -Recurse .\YinZiLong\zilongyin-drawio $env:USERPROFILE\.codex\skills\
```

如果 Codex 没有立刻识别，重启 Codex。

## 使用

在 Codex 里直接说：

```text
使用 $zilongyin-drawio，根据下面论文方法部分设计一张论文图，并生成可编辑 drawio。
```

也可以更具体：

```text
使用 $zilongyin-drawio，生成 Fig. 2 方法总览图。要求 A4 竖版、英文标签、可编辑 drawio，包含 Input、Encoder、Fusion、Prediction Head、Loss。
```

如果只想给 GPT Image2 出图：

```text
使用 $zilongyin-drawio，根据下面论文内容写一个论文图生成提示词，严格贴近我的近期 drawio 风格。
```

## 文件

- `zilongyin-drawio/SKILL.md`：skill 主说明
- `references/style-guide.md`：风格规则
- `references/*stats*.json`：近期图的样式统计
- `scripts/create_zilongyin_drawio.py`：JSON 转 `.drawio` 辅助脚本
