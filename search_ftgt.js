#!/usr/bin/env node
const path = require('path');
const modDir = path.join('/root/math-channel', 'node_modules');
const { Innertube } = require(path.join(modDir, 'youtubei.js'));
async function main() {
  const yt = await Innertube.create();
  const results = await yt.search('Fundamental Theorem of Galois Theory', { type: 'video' });
  const vids = results.data.contents.filter(c => c.type === 'Video').slice(0, 8);
  for (const v of vids) {
    const d = v.video;
    console.log(d.videoId + ' | ' + d.title.text + ' | ' + (d.viewCount ? d.viewCount.text : '?') + ' | ' + d.channel.name.text);
  }
}
main().catch(e => console.error(e.message));
