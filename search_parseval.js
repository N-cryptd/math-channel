const { Innertube } = require('youtubei.js');

async function main() {
  const yt = await Innertube.create();
  const queries = ['Parseval theorem Fourier', 'Parseval identity energy', 'Plancherel theorem Fourier transform', 'Wiener Khinchin theorem power spectral density'];
  for (const q of queries) {
    console.log('=== ' + q + ' ===');
    try {
      const results = await yt.search(q);
      const videos = results.videos || [];
      for (let i = 0; i < Math.min(5, videos.length); i++) {
        const v = videos[i];
        const id = v.videoId || v.id || '';
        const title = v.title?.text || v.title || '';
        const views = v.viewCountText?.text || v.views || '';
        const ch = v.ownerChannelName || v.channel?.name || '';
        const dur = v.lengthText?.text || v.duration || '';
        if (id && id.length === 11) console.log(id + ' | ' + views + ' | ' + dur + ' | ' + ch + ' | ' + title);
      }
    } catch(e) { console.log('Error: ' + e.message); }
  }
}
main();
