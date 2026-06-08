#!/usr/bin/env python3
"""
Fetch YouTube video metadata via Tor + Playwright.
Gets title, description, views, date, channel info, and takes a screenshot.

Usage:
    python3 fetch_video_metadata.py <video_id_or_url> [--screenshot] [--output-dir DIR]
"""

import argparse
import asyncio
import json
import os
import re
import sys


def extract_video_id(input_str: str) -> str:
    """Extract video ID from URL or return as-is."""
    if re.match(r"^[a-zA-Z0-9_-]{11}$", input_str):
        return input_str
    m = re.search(r"(?:v=|/embed/|youtu\.be/)([a-zA-Z0-9_-]{11})", input_str)
    if m:
        return m.group(1)
    return input_str


async def fetch_metadata(video_id: str, screenshot: bool = False, output_dir: str = "/tmp"):
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            proxy={"server": "socks5://127.0.0.1:9050"},
            args=["--no-sandbox", "--disable-gpu"]
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            locale="en-US",
            viewport={"width": 1920, "height": 1080}
        )
        page = await context.new_page()
        await context.add_cookies([{
            "name": "CONSENT", "value": "YES+1",
            "domain": ".youtube.com", "path": "/"
        }])

        url = f"https://www.youtube.com/watch?v={video_id}"
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=60000)
            await page.wait_for_timeout(5000)
        except Exception as e:
            await browser.close()
            return {"error": f"Failed to load: {e}"}

        metadata = await page.evaluate("""
            () => ({
                title: (document.querySelector('#info-contents h1') || 
                        document.querySelector('h1.ytd-video-primary-info-renderer') ||
                        document.querySelector('title')).textContent.trim(),
                view_count: (document.querySelector('#info-text span') || {}).textContent || '',
                date_text: (document.querySelectorAll('#info-text span')[1] || {}).textContent || '',
                description: (document.querySelector('#description-inner') || 
                             document.querySelector('meta[name=description]') || {}).textContent || '',
                channel_name: (document.querySelector('#channel-name a') || {}).textContent || '',
                subscriber_count: (document.querySelector('#owner-sub-count') || {}).textContent || '',
                likes: (document.querySelectorAll('#top-level-buttons-computed ytd-toggle-button-renderer button span')[0] || {}).textContent || '',
            })
        """)

        result = {
            "video_id": video_id,
            "title": metadata["title"].split(" - YouTube")[0] if " - YouTube" in metadata["title"] else metadata["title"],
            "view_count_text": metadata["view_count"],
            "date_text": metadata["date_text"],
            "description": metadata["description"][:2000],
            "channel_name": metadata["channel_name"],
            "subscriber_count": metadata["subscriber_count"],
            "likes_text": metadata["likes"],
            "url": f"https://www.youtube.com/watch?v={video_id}",
        }

        if screenshot:
            os.makedirs(output_dir, exist_ok=True)
            path = os.path.join(output_dir, f"{video_id}.png")
            await page.screenshot(path=path, full_page=False)
            result["screenshot"] = path

        await browser.close()
        return result


def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube video metadata via Tor")
    parser.add_argument("video", help="Video ID or YouTube URL")
    parser.add_argument("--screenshot", action="store_true", help="Take screenshot")
    parser.add_argument("--output-dir", "-o", default="/tmp", help="Screenshot output directory")
    args = parser.parse_args()

    video_id = extract_video_id(args.video)
    result = asyncio.run(fetch_metadata(video_id, args.screenshot, args.output_dir))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
