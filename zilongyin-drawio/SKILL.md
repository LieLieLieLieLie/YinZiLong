---
name: zilongyin-drawio
description: Recreate Zilong Yin's academic draw.io figure style using only the 2025-12-01 through 2026-06-28 corpus, and generate either GPT Image2-ready prompts or editable diagrams.net/draw.io source files. Use when the user asks to make, imitate, redesign, beautify, export, or generate paper figures, model architecture diagrams, workflow diagrams, method overview figures, ablation/experiment schematics, or draw.io files in the user's established style. Do not use any pre-2025-12-01 examples or statistics.
---

# ZilongYin-Drawio

## Purpose

Use this skill to make academic figures that match the user's recent draw.io work: dense paper-ready diagrams, thin technical strokes, many small modules, mixed Chinese/English labels, embedded experiment images where useful, pastel grouping panels, and editable diagrams.net source files.

The training reference is only the corpus from 2025-12-01 through 2026-06-28: 150 first-level `.drawio` files and 143 exported PNG files.

## Priority Rule

Use only the 2025-12-01 through 2026-06-28 corpus. Do not reference, infer from, or blend in any examples, statistics, contact sheets, or impressions from before 2025-12-01.

Use these bundled references:

- `references/recent_drawio_style_stats_2025-12-01_to_2026-06-28.json`
- `references/recent_root_drawio_manifest.json`
- `references/recent_delivery_png_manifest.json`

Do not use any non-recent contact sheet or global/all-time statistics file.

## Workflow

1. Determine the requested output:
   - **GPT Image2 reference prompt**: read `references/style-guide.md`, then write a prompt that names layout, density, palette, line style, typography, embedded-image treatment, and negative constraints.
   - **Editable draw.io source**: read `references/style-guide.md`, then create an uncompressed `.drawio` XML file. Prefer `scripts/create_zilongyin_drawio.py` when the figure can be represented as panels, nodes, labels, and arrows.
   - **Both**: make the `.drawio` first, then use it as the structural reference for the GPT Image2 prompt.
2. If the user gives vague method text, convert it into a figure plan: panels, data flow, modules, screenshots/visual examples, legends, arrows, and concise labels.
3. Keep visible labels short and paper-like. Use Chinese labels when the user content is Chinese; use English labels for paper architecture conventions.
4. Preserve editability. In `.drawio`, create text as text cells, modules as simple shapes, arrows as connectors, and imported examples as separate images.

## Recent Visual Defaults

Apply these defaults unless the user specifies otherwise:

- Canvas: A4 portrait `826 x 1169`; white or transparent background.
- Density: very high, with multiple subfigures or a full pipeline plus side legends; keep whitespace functional.
- Structure: more grid/table-like and paper-finished than decorative; use panels, dashed group boxes, legends, and small repeated modules.
- Lines: thin strokes, usually `0.75`; use `0.5` for secondary connectors and tiny cells.
- Typography: Helvetica 12 px by default; Times New Roman 10-12 px for formulas; 6-10 px for dense annotations; Chinese labels may use Microsoft YaHei/SimSun when needed.
- Colors: mostly white/gray structure with pastel semantic panels. Core pairs: blue `#CCE5FF/#66B2FF`, peach `#FFF2E8/#FFB366`, mint `#E9F7F0/#85DFB2`, pink `#FFFAF9/#FF9999`, lavender `#F9F4FF/#CC99FF`, gray `#E6E6E6/#999999`.
- Images: use embedded images/screenshots/medical/remote-sensing/navigation samples as small, aligned evidence blocks when the figure topic needs them.
- Shapes: compact rounded rectangles, many 10-20 px tiny cells, feature-map cubes, table cells, braces, dashed boundaries, orthogonal arrows, and small legend swatches.
- Avoid: large poster typography, glossy gradients, heavy shadows, thick outlines, ornamental layouts, one-note color palettes, and low-density infographic composition.

## GPT Image2 Prompt Pattern

When preparing a prompt for image generation, include:

```text
Create a paper-ready academic figure in ZilongYin-Drawio recent style, based on the complete 2025-12-01 to 2026-06-28 reference corpus: A4 portrait, white background, very high information density, thin 0.5-0.75 px draw.io strokes, compact pastel grouped panels, many small aligned modules, Helvetica/Times labels, orthogonal arrows, dashed group boxes, tiny legends, and embedded evidence thumbnails where relevant. Use [specific content]. Avoid photorealism, glossy 3D rendering, thick outlines, heavy shadows, oversized text, and decorative gradients.
```

Mention exact panel content, label names, arrow directions, and color grouping. Ask for a flat vector-like diagram, not a freehand illustration, unless the user explicitly wants raster art.

## Draw.io Generation

For direct `.drawio` output:

1. Build a JSON spec with `panels`, `nodes`, `edges`, and optional `labels`.
2. Run:

```bash
python scripts/create_zilongyin_drawio.py spec.json output.drawio
```

3. Inspect the output against the recent contact sheets and refine spacing, label scale, and density.

The script creates uncompressed XML, so another agent can patch it later. Use it for first-pass source files; for highly complex geometry, write XML directly but reuse the same recent styles from `references/style-guide.md`.

## References

- Read `references/style-guide.md` for the detailed recent-corpus style guide.
- Read `references/recent_drawio_style_stats_2025-12-01_to_2026-06-28.json` when exact frequencies matter.
- If local recent contact sheets are available, compare visually before finalizing prompts or diagrams; otherwise use the recent style guide and statistics.
