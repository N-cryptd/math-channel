const { Innertube } = require('youtubei.js');

async function main() {
  const yt = await Innertube.create();
  const search = await yt.search('But what is a Laplace Transform 3blue1brown');
  for (const v of search.videos.slice(0,5)) {
    console.log(v.id, '|', v.title?.text || v.title, '|', v.channel?.name || 'N/A');
  }
}
main().catch(e => console.error(e.message));
