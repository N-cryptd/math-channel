const { Innertube } = require('youtubei.js');
(async () => {
  const yt = await Innertube.create();
  const queries = [
    'Faculty of Khan separation of variables PDE',
    'commutant separation of variables PDE',
    'separation of variables PDE math animation',
    'Dr Peyam separation of variables PDE'
  ];
  const seen = new Set();
  for (const q of queries) {
    console.log('=== ' + q + ' ===');
    try {
      const results = await yt.search(q);
      const videos = results.videos || [];
      for (const v of videos.slice(0, 8)) {
        const id = v.videoId || v.id || '';
        const title = v.title?.text || v.title || '';
        const dur = v.lengthText?.text || v.duration || '';
        const views = v.viewCountText?.text || v.views || '';
        const ch = v.ownerChannelName || v.channel?.name || '';
        if (id && id.length === 11 && !seen.has(id)) {
          seen.add(id);
          console.log(id + ' | ' + ch + ' | ' + views + ' | ' + dur + ' | ' + title);
        }
      }
    } catch(e) { console.error(e.message); }
  }
})();
