#!/usr/bin/env python3
"""
Fetch a YouTube channel's video list via Tor + Playwright.
Scrapes the channel's Videos tab to get all public video metadata.

Usage:
    python3 fetch_channel_videos.py <channel_url_or_id> [--limit 50] [--sort popular]

Output: JSON array of video metadata objects.
"""

import argparse
import asyncio
import json
import os
import re
import sys


def extract_channel_id(url_or_id: str) -> str:
    """Extract channel ID or handle from URL."""
    url_or_id = url_or_id.strip()
    if url_or_id.startswith("@"):
        return url_or_id
    patterns = [
        r'(?:channel/|/c/)([a-zA-Z0-9_-]+)',
        r'@([a-zA-Z0-9_-]+)',
        r'^([a-zA-Z0-9_-]{24})$',
    ]
    for p in patterns:
        m = re.search(p, url_or_id)
        if m:
            return m.group(1)
    return url_or_id


async def fetch_channel_videos(channel: str, limit: int = 50, sort: str = "newest"):
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

        if channel.startswith("@"):
            url = f"https://www.youtube.com/{channel}/videos"
        elif channel.startswith("UC"):
            url = f"https://www.youtube.com/channel/{channel}/videos"
        else:
            url = f"https://www.youtube.com/{channel}/videos"

        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=60000)
            await page.wait_for_timeout(5000)

            # Handle YouTube consent dialog (Tor exit nodes often get it)
            try:
                accept = page.locator(
                    'button:has-text("Accept all"), '
                    'button:has-text("Reject all"), '
                    'form button[type="submit"]'
                )
                if await accept.count() > 0:
                    await accept.first.click()
                    await page.wait_for_timeout(3000)
            except Exception:
                pass
        except Exception as e:
            await browser.close()
            return {"error": f"Failed to load channel: {e}"}

        # Scroll to load more videos
        videos = []
        scroll_attempts = 0
        max_scrolls = min((limit // 30) + 3, 15)

        while len(videos) < limit and scroll_attempts < max_scrolls:
            batch = await page.evaluate("""
                () => {
                    const items = document.querySelectorAll('ytd-rich-item-renderer');
                    return Array.from(items).map(item => {
                        const vids = new Set();
                        item.innerHTML.replace(/\\/watch\\?v=([a-zA-Z0-9_-]{11})/g, (_, id) => vids.add(id));
                        const video_id = vids.values().next().value || '';

                        const titleEl = item.querySelector('#video-title, h3 a');
                        const metaEl = item.querySelector('#metadata-line, ytd-video-meta-block');
                        const thumbEl = item.querySelector('img');
                        const linkEl = item.querySelector('a[href*="/watch?v="]');

                        return {
                            title: titleEl ? titleEl.textContent.trim() : '',
                            video_id: video_id,
                            url: linkEl ? linkEl.href : (video_id ? 'https://www.youtube.com/watch?v=' + video_id : ''),
                            meta_text: metaEl ? metaEl.textContent.trim() : '',
                            thumbnail: thumbEl ? thumbEl.src : '',
                        };
                    }).filter(v => v.title && v.video_id);
                }
            """)

            existing_ids = {v["video_id"] for v in videos}
            new_videos = [v for v in batch if v["video_id"] not in existing_ids]
            videos.extend(new_videos)

            if len(new_videos) == 0:
                break

            await page.evaluate("window.scrollBy(0, 8000)")
            await page.wait_for_timeout(2000)
            scroll_attempts += 1

        await browser.close()
        return videos[:limit]


async def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube channel videos via Tor")
    parser.add_argument("channel", help="Channel URL, @handle, or channel ID")
    parser.add_argument("--limit", "-n", type=int, default=50, help="Max videos to fetch")
    parser.add_argument("--sort", "-s", choices=["newest", "oldest", "popular"], default="newest")
    args = parser.parse_args()

    channel = extract_channel_id(args.channel)
    result = await fetch_channel_videos(channel, args.limit, args.sort)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
