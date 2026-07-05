#!/usr/bin/env node
const { Innertube } = require('youtubei.js');

async function search() {
  const yt = await Innertube.create();
  const results = await yt.search('continuity definition real analysis epsilon delta');
  for (const r of results.data) {
    if (r.type === 'Video') {
      console.log(JSON.stringify({
        id: r.id,
        title: r.title?.text || String(r.title),
        views: r.view_count?.text || '',
        channel: r.channel?.name?.text || ''
      }));
    }
  }
}
search().catch(e => console.error(e.message));
