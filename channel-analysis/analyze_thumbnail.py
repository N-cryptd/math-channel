#!/usr/bin/env python3
"""
Analyze YouTube thumbnails using AI vision models (NVIDIA NIM).
Primary: microsoft/phi-4-multimodal-instruct
Fallback: nvidia/llama-3.1-nemotron-nano-vl-8b-v1

Usage:
    python3 analyze_thumbnail.py <image_path_or_url> [--json]
    python3 analyze_thumbnail.py <image_path_or_url> --batch --urls-file <file>

Requirements:
    - NVIDIA_NIM_API_KEY in ~/.hermes/.env
    - Internet access to NVIDIA NIM API
"""

import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.request

PRIMARY_MODEL = "microsoft/phi-4-multimodal-instruct"
FALLBACK_MODELS = [
    "nvidia/llama-3.1-nemotron-nano-vl-8b-v1",
    "nvidia/nemotron-nano-12b-v2-vl",
]

ANALYSIS_PROMPT = """You are a visual design analyst for YouTube math education channels. Analyze this thumbnail:

1. COLOR PALETTE: List all colors used and their roles (background, text, accent, math objects)
2. TEXT STYLE: Font weight, size hierarchy, color, placement, any text effects
3. COMPOSITION: Layout type (centered, left-right, etc.), visual flow, use of whitespace
4. MATH VISUALS: What mathematical objects/shapes are shown? How are they styled?
5. BRAND CONSISTENCY: Does this look like it belongs to a consistent channel brand?
6. CLICK-WORTHINESS: Rate 1-10. What makes it compelling or weak?
7. QUALITY: Rate visual quality 1-10

Output as JSON with keys: colors, text_style, composition, math_visuals, brand_consistency, clickworthiness (int), quality (int), summary (1 sentence)"""

QUICK_PROMPT = "Describe this YouTube math thumbnail in 3 sentences: background, text style, math visuals, overall quality (1-10)."


def get_nvidia_key():
    env_path = os.path.expanduser("~/.hermes/.env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if line.startswith("NVIDIA_NIM_API_KEY="):
                    return line.split("=", 1)[1].strip()
    return os.environ.get("NVIDIA_NIM_API_KEY", "")


def load_image(path_or_url: str) -> str:
    """Load image and return as base64 data URL."""
    if path_or_url.startswith("http"):
        req = urllib.request.Request(path_or_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
        ext = "jpg" if "jpg" in path_or_url or "jpeg" in path_or_url else "png"
    else:
        with open(path_or_url, "rb") as f:
            data = f.read()
        ext = os.path.splitext(path_or_url)[1].lstrip(".") or "png"
    mime = f"image/{ext}"
    b64 = base64.b64encode(data).decode()
    return f"data:{mime};base64,{b64}"


def call_vision_model(image_data_url: str, model: str, prompt: str, max_tokens: int = 800, timeout: int = 30) -> dict:
    """Call a vision model and return the result."""
    api_key = get_nvidia_key()
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": [
            {"type": "image_url", "image_url": {"url": image_data_url}},
            {"type": "text", "text": prompt}
        ]}],
        "max_tokens": max_tokens,
        "temperature": 0.3,
    }).encode()
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    req = urllib.request.Request(url, data=payload, headers=headers)

    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.loads(resp.read())
        raw = data["choices"][0]["message"]["content"]
        tokens = data.get("usage", {}).get("total_tokens", 0)
        return {"text": raw, "tokens": tokens, "model": model}


def parse_analysis(text: str) -> dict:
    """Try to extract JSON from model output, fallback to raw text."""
    json_match = re.search(r"\{.*\}", text, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group())
        except json.JSONDecodeError:
            pass
    return {"raw_analysis": text}


def analyze_thumbnail(image_path_or_url: str, quick: bool = False) -> dict:
    """Analyze a single thumbnail with fallback chain."""
    try:
        data_url = load_image(image_path_or_url)
    except Exception as e:
        return {"error": f"Failed to load image: {e}"}

    prompt = QUICK_PROMPT if quick else ANALYSIS_PROMPT
    max_tok = 200 if quick else 800

    # Try primary model first
    for model in [PRIMARY_MODEL] + FALLBACK_MODELS:
        try:
            result = call_vision_model(data_url, model, prompt, max_tokens=max_tok)
            analysis = parse_analysis(result["text"])
            analysis["model_used"] = result["model"]
            analysis["tokens"] = result["tokens"]
            return analysis
        except Exception as e:
            print(f"  {model} failed: {type(e).__name__}: {str(e)[:80]}", file=sys.stderr)
            continue

    return {"error": "All vision models failed"}


def download_thumbnail(video_id: str, output_dir: str = "/tmp") -> str:
    """Download max-res thumbnail for a video ID."""
    url = f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg"
    out_path = os.path.join(output_dir, f"{video_id}_thumb.jpg")
    try:
        urllib.request.urlretrieve(url, out_path)
        return out_path
    except Exception:
        # Fallback to hqdefault (always available)
        url2 = f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"
        urllib.request.urlretrieve(url2, out_path)
        return out_path


def main():
    parser = argparse.ArgumentParser(description="Analyze YouTube thumbnail with AI vision")
    parser.add_argument("image", help="Image file path, YouTube thumbnail URL, or video ID")
    parser.add_argument("--quick", "-q", action="store_true", help="Quick 3-sentence analysis")
    parser.add_argument("--download", "-d", help="Download thumbnail to directory before analyzing")
    args = parser.parse_args()

    # If input looks like a video ID (11 chars), download thumbnail first
    image = args.image
    if len(args.image) == 11 and not args.image.startswith("http") and not os.path.exists(args.image):
        out_dir = args.download or "/tmp"
        image = download_thumbnail(args.image, out_dir)
        print(f"Downloaded thumbnail to {image}", file=sys.stderr)

    result = analyze_thumbnail(image, quick=args.quick)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
