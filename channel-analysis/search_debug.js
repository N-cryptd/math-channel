const { Innertube } = require('youtubei.js');
async function search() {
  const yt = await Innertube.create();
  const results = await yt.search('Lp spaces introduction pth power summable');
  for (const item of results.data?.contents || []) {
    const c = item?.content;
    if (c) {
      console.log('Keys:', Object.keys(c).join(', '));
      console.log('videoId:', c.videoId);
      console.log('id:', c.id);
      console.log('title:', c.title?.text || c.title);
      console.log('type:', c.type);
      console.log('---');
    }
  }
}
search().catch(e => console.error(e.message));
