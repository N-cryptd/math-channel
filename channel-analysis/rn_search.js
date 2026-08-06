
const { Innertube } = require('youtubei.js');

async function search(q) {
  const yt = await Innertube.create();
  const results = await yt.search(q);
  const videos = results.videos || [];
  const seen = new Set();
  const out = [];
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
  for (const q of process.argv.slice(2)) {
    console.log('=== ' + q + ' ===');
    try {
      const r = await search(q);
      r.slice(0, 8).forEach(v => console.log(v.id + ' | ' + v.channel + ' | ' + v.views + ' | ' + v.duration + ' | ' + v.title));
    } catch(e) { console.error(e.message); }
  }
})();
