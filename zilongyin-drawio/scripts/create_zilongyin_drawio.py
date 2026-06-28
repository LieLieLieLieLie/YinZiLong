#!/usr/bin/env python3
"""Create an editable diagrams.net .drawio file in the ZilongYin-Drawio recent style.

Input JSON example:
{
  "title": "Method Overview",
  "panels": [{"id": "p1", "label": "Encoder", "x": 40, "y": 80, "w": 320, "h": 240, "theme": "blue"}],
  "nodes": [{"id": "n1", "label": "Input", "x": 70, "y": 150, "w": 80, "h": 36, "theme": "peach"}],
  "edges": [{"source": "n1", "target": "n2", "label": "features"}],
  "labels": [{"label": "(a)", "x": 40, "y": 40}]
}
"""

from __future__ import annotations

import html
import json
import sys
import uuid
import xml.etree.ElementTree as ET
from pathlib import Path


THEMES = {
    "mint": ("#E9F7F0", "#85DFB2"),
    "peach": ("#FFF2E8", "#FFB366"),
    "blue": ("#F4FAFF", "#66B2FF"),
    "lavender": ("#F9F4FF", "#CC99FF"),
    "pink": ("#FFFAF9", "#FF9999"),
    "yellow": ("#FFFFCC", "#E0E086"),
    "gray": ("#F0F0F0", "#999999"),
}


def theme(name: str | None) -> tuple[str, str]:
    return THEMES.get((name or "blue").lower(), THEMES["blue"])


def style_rect(fill: str, stroke: str, rounded: bool = True) -> str:
    return (
        f"rounded={1 if rounded else 0};whiteSpace=wrap;html=1;"
        f"fillColor={fill};strokeColor={stroke};arcSize=4;strokeWidth=0.75;"
        "fontFamily=Helvetica;fontSize=12;fontColor=#333333;"
    )


def style_panel(fill: str, stroke: str) -> str:
    return (
        "rounded=1;whiteSpace=wrap;html=1;"
        f"fillColor={fill};strokeColor={stroke};arcSize=3;strokeWidth=0.75;"
        "fontFamily=Helvetica;fontSize=12;fontColor=#333333;"
    )


def style_cube(fill: str, stroke: str) -> str:
    return (
        "shape=cube;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;"
        "darkOpacity=0.05;darkOpacity2=0.1;size=5;flipH=1;"
        f"fillColor={fill};strokeColor={stroke};gradientColor=none;"
        "gradientDirection=north;aspect=fixed;container=0;strokeWidth=0.5;"
        "fontFamily=Helvetica;fontSize=10;fontColor=#333333;"
    )


def style_text(size: int = 12) -> str:
    return (
        "text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];"
        f"autosize=1;strokeColor=none;fillColor=none;fontFamily=Helvetica;fontSize={size};fontColor=#333333;"
    )


def add_cell(root: ET.Element, cell_id: str, value: str, style: str, x: float, y: float, w: float, h: float) -> ET.Element:
    cell = ET.SubElement(
        root,
        "mxCell",
        {
            "id": cell_id,
            "value": html.escape(value or ""),
            "style": style,
            "parent": "1",
            "vertex": "1",
        },
    )
    ET.SubElement(
        cell,
        "mxGeometry",
        {"x": str(x), "y": str(y), "width": str(w), "height": str(h), "as": "geometry"},
    )
    return cell


def add_edge(root: ET.Element, edge_id: str, source: str, target: str, label: str = "") -> ET.Element:
    cell = ET.SubElement(
        root,
        "mxCell",
        {
            "id": edge_id,
            "value": html.escape(label or ""),
            "style": "endArrow=classic;html=1;rounded=0;endSize=3;strokeWidth=0.75;strokeColor=#4D4D4D;fontFamily=Helvetica;fontSize=10;",
            "parent": "1",
            "source": source,
            "target": target,
            "edge": "1",
        },
    )
    ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})
    return cell


def build(spec: dict) -> ET.ElementTree:
    mxfile = ET.Element("mxfile", {"host": "Codex", "version": "29.0.3"})
    diagram = ET.SubElement(mxfile, "diagram", {"id": str(uuid.uuid4()), "name": spec.get("name", "Page-1")})
    model = ET.SubElement(
        diagram,
        "mxGraphModel",
        {
            "dx": "1200",
            "dy": "900",
            "grid": "1",
            "gridSize": "10",
            "guides": "1",
            "tooltips": "1",
            "connect": "1",
            "arrows": "1",
            "fold": "0",
            "page": "1",
            "pageScale": "1",
            "pageWidth": str(spec.get("page_width", 826)),
            "pageHeight": str(spec.get("page_height", 1169)),
            "background": "none",
            "math": "1",
            "shadow": "0",
        },
    )
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})

    if spec.get("title"):
        add_cell(root, "title", spec["title"], style_text(14), 40, 24, 740, 28)

    for panel in spec.get("panels", []):
        fill, stroke = theme(panel.get("theme"))
        add_cell(
            root,
            panel["id"],
            panel.get("label", ""),
            style_panel(fill, stroke),
            panel.get("x", 40),
            panel.get("y", 80),
            panel.get("w", panel.get("width", 200)),
            panel.get("h", panel.get("height", 120)),
        )

    for node in spec.get("nodes", []):
        fill, stroke = theme(node.get("theme"))
        node_type = node.get("type", "block")
        if node_type == "cube":
            style = style_cube(fill, stroke)
        elif node_type == "label":
            style = style_text(int(node.get("font_size", 12)))
        else:
            style = style_rect(fill, stroke, rounded=node.get("rounded", True))
        add_cell(
            root,
            node["id"],
            node.get("label", ""),
            style,
            node.get("x", 80),
            node.get("y", 120),
            node.get("w", node.get("width", 80)),
            node.get("h", node.get("height", 36)),
        )

    for i, label in enumerate(spec.get("labels", []), 1):
        add_cell(
            root,
            label.get("id", f"label-{i}"),
            label.get("label", ""),
            style_text(int(label.get("font_size", 12))),
            label.get("x", 40),
            label.get("y", 40 + i * 20),
            label.get("w", label.get("width", 80)),
            label.get("h", label.get("height", 24)),
        )

    for i, edge in enumerate(spec.get("edges", []), 1):
        add_edge(root, edge.get("id", f"edge-{i}"), edge["source"], edge["target"], edge.get("label", ""))

    return ET.ElementTree(mxfile)


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: create_zilongyin_drawio.py spec.json output.drawio", file=sys.stderr)
        return 2
    spec = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8-sig"))
    tree = build(spec)
    ET.indent(tree, space="  ")
    tree.write(sys.argv[2], encoding="utf-8", xml_declaration=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
