const { Innertube } = require('youtubei.js');

(async () => {
  try {
    const yt = await Innertube.create();
    const search = await yt.search('banach spaces functional analysis explained');
    const videos = search.videos || [];
    for (let i = 0; i < Math.min(8, videos.length); i++) {
      const v = videos[i];
      const title = typeof v.title === 'string' ? v.title : (v.title?.text || 'N/A');
      console.log(v.id + ' | ' + title.substring(0, 100) + ' | ' + (v.viewCount?.text || 'N/A'));
    }
  } catch(e) { console.error('ERROR:', e.message || e); }
})();
