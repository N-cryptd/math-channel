const { Innertube } = require('youtubei.js');
(async () => {
  const yt = await Innertube.create();
  const searches = ['cyclotomic fields explained', 'cyclotomic polynomial', 'roots of unity Galois'];
  for (const q of searches) {
    console.log('\n=== ' + q + ' ===');
    const s = await yt.search(q);
    for (const v of s.videos.slice(0, 4)) {
      console.log(v.id + ' | ' + v.title.text + ' | ' + (v.view_count || 0) + ' views');
    }
  }
})().catch(e => console.error(e.message));
