#!/usr/bin/env python3
"""
Local pixel-level thumbnail analysis (no API needed).
Fallback for when NVIDIA NIM vision models are unavailable (HTTP 410 since ~Sep 2026).

Extracts actionable design features from a YouTube thumbnail:
- dominant color palette (quantized)
- brightness / contrast / saturation
- edge density (visual busyness)
- content-mass distribution across thirds (composition balance)
- high-frequency horizontal-band energy (text-likeness proxy)

Usage:
    python3 analyze_thumbnail_local.py IMAGE [IMAGE ...]
Output: JSON per image on stdout.
"""

import json
import sys

from PIL import Image, ImageFilter
import numpy as np


def analyze(path: str) -> dict:
    img = Image.open(path).convert("RGB")
    W, H = img.size
    arr = np.asarray(img, dtype=float)

    # --- Dominant palette via adaptive quantization ---
    q = img.quantize(colors=5, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette() or []
    counts = sorted(q.getcolors(W * H) or [], reverse=True)
    total = W * H
    palette = []
    for cnt, idx in counts[:5]:
        if isinstance(idx, tuple):
            continue
        base = int(idx) * 3
        if base + 2 >= len(pal):
            continue
        r, g, b = pal[base], pal[base + 1], pal[base + 2]
        palette.append({
            "rgb": [r, g, b],
            "hex": f"#{r:02x}{g:02x}{b:02x}",
            "share": round(cnt / total * 100, 1),
        })

    # --- Basic stats ---
    luma = 0.2126 * arr[..., 0] + 0.7152 * arr[..., 1] + 0.0722 * arr[..., 2]
    hsv = np.asarray(img.convert("HSV"), dtype=float)
    brightness = round(luma.mean(), 1)
    contrast = round(luma.std(), 1)
    saturation = round(hsv[..., 1].mean(), 1)

    # --- Edge density (busyness) ---
    edges = np.asarray(img.convert("L").filter(ImageFilter.FIND_EDGES), dtype=float)
    edge_density = round((edges > 40).sum() / total * 100, 1)

    # --- Content mass by thirds (where the "stuff" is) ---
    thirds_v = [arr[:, : W // 3], arr[:, W // 3: 2 * W // 3], arr[:, 2 * W // 3:]]
    bg = np.median(arr.reshape(-1, 3), axis=0)
    def content_mass(region):
        d = np.abs(region - bg).max(axis=2)
        return round((d > 60).sum() / region.shape[0] / region.shape[1] * 100, 1)
    thirds_h = [arr[: H // 3], arr[H // 3: 2 * H // 3], arr[2 * H // 3:]]
    composition = {
        "left_third": content_mass(thirds_v[0]),
        "center_third": content_mass(thirds_v[1]),
        "right_third": content_mass(thirds_v[2]),
        "top_third": content_mass(thirds_h[0]),
        "middle_third": content_mass(thirds_h[1]),
        "bottom_third": content_mass(thirds_h[2]),
    }

    # --- Text-likeness: high-frequency energy in horizontal strips ---
    # Text produces strong repeated horizontal transitions; measure row-wise
    # gradient energy in the middle band where titles usually sit.
    band = luma[H // 8: H * 3 // 8]  # upper-middle band (title zone)
    grad = np.abs(np.diff(band, axis=1))
    text_likeness = round((grad > 80).sum() / grad.size * 100, 1)

    return {
        "file": path,
        "size": [W, H],
        "palette": palette,
        "brightness": brightness,
        "contrast": contrast,
        "saturation": saturation,
        "edge_density_pct": edge_density,
        "composition_content_mass": composition,
        "text_band_gradient_pct": text_likeness,
        "notes": interpret(brightness, contrast, edge_density, composition),
    }


def interpret(brightness, contrast, edge_density, comp):
    notes = []
    if brightness < 60:
        notes.append("dark background (high-contrast thumbnail style)")
    elif brightness > 170:
        notes.append("light/white background (classroom style)")
    else:
        notes.append("mid-tone background")
    if contrast > 70:
        notes.append("very high contrast — bold read-at-small-size")
    elif contrast < 35:
        notes.append("low contrast — may read as flat at feed size")
    if edge_density > 25:
        notes.append("busy frame (many distinct elements)")
    elif edge_density < 8:
        notes.append("minimal frame (1-2 elements, lots of whitespace)")
    side = max(comp, key=comp.get)
    notes.append(f"content mass concentrated: {side} ({comp[side]}%)")
    return notes


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    print(json.dumps([analyze(p) for p in sys.argv[1:]], indent=1))


if __name__ == "__main__":
    main()
