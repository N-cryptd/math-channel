const { Innertube } = require('youtubei.js');
const fs = require('fs');
(async () => {
  const yt = await Innertube.create();
  const results = await yt.search('mathematical induction proof explained');
  let out = 'Total results: ' + results.length + '\n';
  if (results.length > 0) {
    out += 'First result keys: ' + Object.keys(results[0]).join(', ') + '\n';
  }
  for (let i = 0; i < Math.min(15, results.length); i++) {
    const r = results[i];
    const id = r.video_id || r.id || r.videoId || 'no-id';
    const title = typeof r.title === 'object' ? (r.title?.text || '').toString().substring(0, 100) : (r.title || '').toString().substring(0, 100);
    const ch = r.channel ? (typeof r.channel.name === 'object' ? (r.channel.name?.text || '').toString() : (r.channel.name || '').toString()) : (r.author?.name || '').toString();
    out += i + ' | ' + id + ' | ' + ch + ' | ' + title + '\n';
    out += '  keys: ' + Object.keys(r).join(', ') + '\n';
  }
  fs.writeFileSync('/tmp/induction_search.txt', out);
})().catch(e => fs.writeFileSync('/tmp/induction_search.txt', 'ERROR: ' + e.message + '\n' + e.stack));
