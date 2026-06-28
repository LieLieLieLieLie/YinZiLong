# ZilongYin-Drawio Recent Style Guide

## Primary Corpus

Use the complete recent corpus, not a sample:

- Date range: 2025-12-01 through 2026-06-28.
- Source files: 150 first-level `.drawio` files.
- Exported references: 143 PNG files.
- Parsed content: 150 pages, about 71k cells, 54k vertices, and 16.5k edges.
- Canvas: 149 of 150 pages use A4 portrait `826 x 1169` with `background="none"`.

Do not use files, statistics, contact sheets, or impressions from before 2025-12-01. This guide intentionally excludes that material.

## Recent Overall Look

- Academic paper figure, not a poster or product infographic.
- Very high information density with compact but aligned subfigures.
- White background with gray/black technical structure as the dominant base.
- Pastel color is used for semantic grouping, not decoration.
- Frequent multi-panel summaries: method overview, module detail, experimental comparison, screenshots, tables, legends, and flow steps in one figure.
- Embedded raster images are common when the domain needs evidence: medical slices, remote-sensing images, navigation screenshots, soil/scene photos, charts, masks, heatmaps, or UI-like examples.
- Chinese and English labels can coexist. Chinese workflow boxes appear more often in the recent corpus.

## Layout Patterns

Use one of these patterns:

- **Dense method overview**: left-to-right pipeline with top/bottom detail insets and side legends.
- **Multi-panel paper figure**: `(a)`, `(b)`, `(c)` blocks arranged in a grid with thin panel boundaries.
- **Architecture table**: repeated small modules in rows/columns, often with arrows between rows.
- **Comparison sheet**: many small examples, masks, charts, or thumbnails aligned in a matrix.
- **Chinese flowchart**: boxed hierarchy or process tree with pastel branches and short Chinese labels.
- **Evidence plus mechanism**: real image thumbnails on one side, draw.io modules and arrows on the other.

Keep the page full but controlled. Align to a 10 px grid. Use 30-50 px margins where possible.

## Palette

Recent files use more neutral/white structure than the full corpus. Use muted fills and thin borders:

| Role | Fill | Stroke |
| --- | --- | --- |
| Blue technical module | `#CCE5FF`, `#E2EFFF`, `#F4FAFF` | `#66B2FF`, `#99CCFF`, `#0066CC` |
| Peach/data/input | `#FFF2E8`, `#FFFBF4` | `#FFB366`, `#FF9933`, `#CC6600` |
| Mint/process/valid | `#E9F7F0` | `#85DFB2`, `#00CC00`, `#009900` |
| Pink/output/warning | `#FFFAF9`, `#FFF1F7`, `#FFCCCC` | `#FF9999`, `#FF6666` |
| Lavender/attention/group | `#F9F4FF`, `#F2EFFF`, `#e1d5e7` | `#CC99FF`, `#B8B7FF` |
| Gray/neutral/tensor | `#E6E6E6`, `#CCCCCC`, `#B3B3B3`, `#999999`, `#808080` | `#999999`, `#4D4D4D`, `#000000` |
| Note/table | `#FFFFCC`, `#FFF9D6` | `#E0E086` |

Avoid glossy gradients. In recent stats, `gradientColor=none` dominates; gradients are rare accents only.

## Lines And Arrows

- Main stroke width: `0.75`.
- Secondary connector width: `0.5`.
- Tiny detail lines: `0.1-0.3` only for dense internal structure.
- Arrows: `endArrow=classic;endSize=3`.
- Use `endArrow=none` for separators, brackets, and table-like connectors.
- Prefer orthogonal connectors for pipelines and architecture.
- Use dashed boundaries for optional paths, search areas, grouping boxes, or comparison regions.
- Use red/blue/green arrows sparingly to highlight semantic direction.

## Typography

- Main labels: Helvetica 12 px.
- Dense annotations: Helvetica 6-10 px.
- Section/panel labels: Helvetica 12-14 px.
- Formulas/math: Times New Roman 10-12 px.
- Chinese labels: Microsoft YaHei, SimSun, or the draw.io default Chinese-compatible font.
- Keep labels short. Use paper terms like `Input`, `Encoder`, `Decoder`, `Conv`, `BN`, `ReLU`, `Concat`, `Output`, `Loss`, `Query`, `Key`, `Value`, `Mask`, `Feature Map`.

## Shape Recipes

### Recent Panel Box

```text
rounded=1;whiteSpace=wrap;html=1;fillColor=#F4FAFF;strokeColor=#66B2FF;arcSize=3;strokeWidth=0.75;fontFamily=Helvetica;fontSize=12;
```

### Compact Module Block

```text
rounded=1;whiteSpace=wrap;html=1;fillColor=#E9F7F0;strokeColor=#85DFB2;arcSize=4;strokeWidth=0.75;fontFamily=Helvetica;fontSize=12;fontColor=#333333;
```

### Table Cell / Micro Block

```text
rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#999999;strokeWidth=0.5;fontFamily=Helvetica;fontSize=7;
```

### Tensor Or Feature Map Cube

```text
shape=cube;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;darkOpacity=0.05;darkOpacity2=0.1;size=5;flipH=1;fillColor=#CCE5FF;strokeColor=#66B2FF;gradientColor=none;gradientDirection=north;aspect=fixed;container=0;strokeWidth=0.5;
```

### Text Label

```text
text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontFamily=Helvetica;fontSize=12;
```

### Arrow

```text
endArrow=classic;html=1;rounded=0;endSize=3;strokeWidth=0.75;strokeColor=#4D4D4D;
```

## GPT Image2 Checklist

Include these phrases when style fidelity matters:

- "ZilongYin-Drawio recent corpus style"
- "complete 2025-12-01 to 2026-06-28 reference set"
- "paper-ready A4 portrait draw.io figure"
- "very high information density, compact aligned modules"
- "white background with thin gray technical structure"
- "pastel semantic panels, not decorative color blocks"
- "0.5-0.75 px orthogonal draw.io connector arrows"
- "Helvetica/Times labels, tiny annotations, mixed Chinese/English when needed"
- "embedded evidence thumbnails/screenshots where relevant"
- "no glossy gradients, no poster typography, no heavy shadows, no thick outlines"

## Direct Draw.io Notes

- Prefer uncompressed XML for editability.
- Use `mxfile > diagram > mxGraphModel > root > mxCell`.
- Keep visible shapes as `mxCell vertex="1"`.
- Keep connectors as `mxCell edge="1"` with `mxGeometry relative="1"`.
- Use explicit `x`, `y`, `width`, and `height`.
- Use stable IDs so future edits are easy.
- If importing images, keep them separate and aligned; do not flatten the entire figure into one image.
- Before final delivery, compare against `assets/recent_contact_sheet_all_01.png`, `assets/recent_contact_sheet_all_02.png`, and `assets/recent_contact_sheet_all_03.png`.
