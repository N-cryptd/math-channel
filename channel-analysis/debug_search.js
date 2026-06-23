const { Innertube } = require('youtubei.js');
(async () => {
  const yt = await Innertube.create();
  const resp = await yt.search('equivalence relations discrete math');
  const results = resp.results;
  console.log('Results type:', results?.constructor?.name, 'length:', results?.length);
  if (results) {
    results.slice(0, 15).forEach((r, i) => {
      let id = 'N/A', title = 'N/A', channel = 'N/A', dur = '';
      try { id = r.id || 'N/A'; } catch(e) {}
      try { title = (r.title?.text || String(r.title || 'N/A')).substring(0, 80); } catch(e) {}
      try { channel = r.channel?.name || r.author?.name || 'N/A'; } catch(e) {}
      try { dur = r.duration?.text || ''; } catch(e) {}
      console.log(`${i} | ${id} | ${channel} | ${title} | ${dur}`);
    });
  }
})().catch(e => console.error('ERR:', e.message));
