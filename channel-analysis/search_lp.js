const { Innertube } = require('youtubei.js');
async function search() {
  const yt = await Innertube.create();
  const results = await yt.search('Lp spaces explained measure theory');
  for (const r of (results.data?.contents || [])) {
    const c = r?.content || r;
    const vid = c?.videoId || '';
    const title = (c?.title?.text || '').substring(0, 80);
    const views = c?.viewCount?.text || '';
    const ch = (c?.author?.name || '');
    if (vid && title) console.log(vid + ' | ' + title + ' | ' + views + ' | ' + ch);
  }
}
search().catch(e => console.error(e.message));
