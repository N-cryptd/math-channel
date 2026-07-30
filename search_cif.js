#!/usr/bin/env node
// Search for Cauchy Integral Formula competitor videos
const path = require('path');
process.chdir('/root/math-channel');
const { Innertube } = require(path.join(process.cwd(), 'node_modules', 'youtubei.js'));

async function search() {
  const yt = await Innertube.create();
  const results = await yt.search('Cauchy Integral Formula complex analysis');
  const items = results.data?.contents?.twoColumnSearchResultsRenderer?.primaryContents?.sectionListRenderer?.contents?.[0]?.itemSectionRenderer?.contents || [];
  for (const item of items.slice(0, 15)) {
    const v = item.videoRenderer;
    if (v) {
      console.log(v.videoId + ' | ' + (v.title?.runs?.[0]?.text || '').substring(0, 100) + ' | ' + (v.viewCountText?.simpleText || ''));
    }
  }
}
search().catch(e => console.error(e.message));
