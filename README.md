# ZilongYin-Drawio

Codex skill for generating academic paper figures in Zilong Yin's recent draw.io style.

## Install

Copy the skill folder into your Codex skills directory:

```powershell
git clone https://github.com/LieLieLieLieLie/YinZiLong.git
Copy-Item -Recurse .\YinZiLong\zilongyin-drawio $env:USERPROFILE\.codex\skills\
```

Restart Codex if the skill does not appear immediately.

## Use

Invoke it in Codex with:

```text
Use $zilongyin-drawio to design a paper figure from this method section and generate an editable draw.io file.
```

Good prompts include:

```text
Use $zilongyin-drawio. Create Fig. 2 as an A4 portrait method overview. Output editable .drawio. Use English labels and include Input, Encoder, Fusion, Prediction Head, and Loss.
```

```text
Use $zilongyin-drawio to write a GPT Image2 prompt for this paper figure, matching my recent draw.io style.
```

## Contents

- `zilongyin-drawio/SKILL.md`: skill instructions
- `references/style-guide.md`: concise visual rules
- `references/*stats*.json`: style statistics from recent figures
- `scripts/create_zilongyin_drawio.py`: JSON-to-draw.io helper
