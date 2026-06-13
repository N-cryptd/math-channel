const path = require('path');
process.chdir('/root/math-channel');
const { Innertube } = require(path.join(process.cwd(), 'node_modules', 'youtubei.js'));
async function main() {
  const yt = await Innertube.create();
  const search = await yt.search('But what is a Laplace Transform 3blue1brown');
  for (const v of search.videos.slice(0,3)) {
    console.log(v.id, '|', v.title.text, '|', v.channel?.name);
  }
}
main().catch(e => console.error(e.message));
