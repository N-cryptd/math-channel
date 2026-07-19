const { Innertube } = require('youtubei.js');

async function search(q) {
  const yt = await Innertube.create();
  const results = await yt.search(q);
  const videos = results.videos || [];
  const out = [];
  const seen = new Set();
  for (const v of videos) {
    const id = v.videoId || v.id || '';
    const title = v.title?.text || v.title || '';
    const dur = v.lengthText?.text || v.duration || '';
    const views = v.viewCountText?.text || v.views || '';
    const ch = v.ownerChannelName || v.channel?.name || '';
    if (id && id.length === 11 && !seen.has(id)) {
      seen.add(id);
      out.push({id, title, duration: dur, views, channel: ch});
    }
  }
  return out;
}

(async () => {
  const queries = [
    'complex analysis introduction',
    'complex analysis Cauchy integral formula',
    'complex analysis residue theorem explained',
    'Cauchy Riemann equations visualization',
    'complex analysis contour integrals',
    'analytic functions complex analysis',
    'Laurent series complex analysis explained',
    'complex differentiation visual',
  ];

  for (const q of queries) {
    console.log('=== ' + q + ' ===');
    try {
      const r = await search(q);
      r.slice(0, 6).forEach(v => console.log(v.id + ' | ' + v.channel + ' | ' + v.views + ' | ' + v.duration + ' | ' + v.title));
    } catch(e) { console.error(e.message); }
    console.log('');
  }
})();
