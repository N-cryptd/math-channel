const { Innertube } = require('youtubei.js');
(async () => {
  const yt = await Innertube.create();
  const results = await yt.search('isomorphism theorems abstract algebra');
  console.log('Type of results:', typeof results);
  console.log('Keys:', Object.keys(results));
  if (results.videos) {
    console.log('Videos count:', results.videos.length);
    for (let i = 0; i < Math.min(15, results.videos.length); i++) {
      const r = results.videos[i];
      console.log('--- Video', i, '---');
      console.log('ID:', r.id);
      console.log('Title:', (r.title?.text || r.title || 'none').toString().substring(0, 120));
      console.log('Channel:', (r.channel?.name || r.author?.name || 'none').toString());
      console.log('Duration:', r.duration?.seconds);
    }
  }
  // Try iterating directly
  let count = 0;
  for (const item of results) {
    if (count >= 15) break;
    console.log('--- Item', count, '---');
    console.log('Type:', item.type);
    console.log('ID:', item.id);
    console.log('Title:', (item.title?.text || item.title || 'none').toString().substring(0, 120));
    console.log('Channel:', (item.channel?.name || item.author?.name || 'none').toString());
    count++;
  }
})().catch(e => console.error(e.message));
