const { Innertube } = require('youtubei.js');
(async () => {
  const yt = await Innertube.create();
  const results = await yt.search('equivalence relations discrete math');
  console.log('Total results:', results.length);
  for (let i = 0; i < Math.min(10, results.length); i++) {
    const r = results[i];
    console.log('---');
    console.log('Type:', r.type);
    console.log('ID:', r.id);
    console.log('Keys:', Object.keys(r).join(', '));
    if (r.title) console.log('Title:', JSON.stringify(r.title));
    if (r.channel) console.log('Channel:', JSON.stringify(r.channel));
    if (r.author) console.log('Author:', JSON.stringify(r.author));
    if (r.duration) console.log('Duration:', r.duration);
    if (r.view_count) console.log('Views:', r.view_count);
  }
})().catch(e => console.error('ERR:', e.message));
