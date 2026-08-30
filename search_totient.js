const { Innertube } = require('youtubei.js');
(async () => {
  const yt = await Innertube.create();
  const queries = ['Euler totient function phi explained', 'Euler totient number theory animation', 'phi function modular arithmetic'];
  for (const q of queries) {
    console.log('--- Query:', q, '---');
    try {
      const results = await yt.search(q);
      const vids = results.videos || [];
      for (let i = 0; i < Math.min(vids.length, 6); i++) {
        const v = vids[i];
        const title = v.title?.text || v.title || 'N/A';
        const ch = v.channel?.name || v.channel?.text || 'N/A';
        const id = v.id || 'N/A';
        console.log(id + ' | ' + title + ' | ' + ch);
      }
    } catch(e) {
      console.error('Error:', e.message);
    }
  }
  process.exit(0);
})().catch(e => { console.error(e.message); process.exit(1); });
