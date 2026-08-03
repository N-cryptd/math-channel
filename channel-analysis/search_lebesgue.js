const { Innertube } = require('youtubei.js');
async function search() {
  const yt = await Innertube.create();
  const results = await yt.search('Lebesgue measure explained');
  for (const v of results.videos.slice(0, 6)) {
    console.log(v.id, '|', v.title.text, '|', v.view_count?.text || 'N/A', '|', v.channel?.name?.text || 'N/A');
  }
}
search().catch(e => console.error(e.message));
