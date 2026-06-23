const { Innertube } = require('youtubei.js');
(async () => {
  const yt = await Innertube.create();
  const results = await yt.search('equivalence relations discrete math');
  for (let i = 0; i < Math.min(10, results.length); i++) {
    const r = results[i];
    const id = r.id || r.videoId || 'unknown';
    const title = (r.title?.text || r.title || 'no title').toString().substring(0, 80);
    const channel = (r.channel?.name || r.author?.name || 'unknown').toString();
    console.log(id + ' | ' + channel + ' | ' + title);
  }
})().catch(e => console.error(e.message));
