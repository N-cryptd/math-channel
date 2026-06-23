const { Innertube } = require('youtubei.js');
(async () => {
  const yt = await Innertube.create();
  const results = await yt.search('equivalence relations discrete math');
  for (let i = 0; i < Math.min(10, results.length); i++) {
    const r = results[i];
    let id = 'unknown', title = 'no title', channel = 'unknown';
    try { id = r.id || r.videoId || 'unknown'; } catch(e) {}
    try { title = (r.title?.text || r.title || 'no title').toString().substring(0, 80); } catch(e) {}
    try { channel = (r.channel?.name || r.author?.name || 'unknown').toString(); } catch(e) {}
    console.log(i + ': ' + JSON.stringify({id, title, channel}));
  }
})().catch(e => console.error('ERR:', e.message));
