const { Innertube } = require('youtubei.js');

async function search() {
  const yt = await Innertube.create();
  const results = await yt.search('rings and fields abstract algebra');
  for (const r of (results.videos || []).slice(0, 10)) {
    console.log(r.id + ' | ' + (r.title?.text || '') + ' | ' + (r.channel?.name || ''));
  }
}
search().catch(e => console.error(e.message));
