const { Innertube } = require('youtubei.js');
(async () => {
  const yt = await Innertube.create();
  const results = await yt.search('first second third isomorphism theorem');
  for (let i = 0; i < Math.min(10, results.videos.length); i++) {
    const r = results.videos[i];
    console.log(r.id + ' | ' + r.duration?.seconds + 's | ' + r.channel?.name + ' | ' + (r.title?.text || r.title || '').toString().substring(0, 120));
  }
})().catch(e => console.error(e.message));
