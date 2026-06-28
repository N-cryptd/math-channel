const { Innertube } = require('/root/math-channel/node_modules/youtubei.js');
async function main() {
  const yt = await Innertube.create();
  const searches = [
    'planar graphs Euler formula',
    'Kuratowski theorem planar',
    'Euler formula V-E+F planar visual proof',
  ];
  for (const q of searches) {
    console.log('=== ' + q + ' ===');
    const r = await yt.search(q);
    for (const v of r.videos.slice(0,5)) {
      console.log(v.id, '|', v.title.text, '|', v.channel?.name);
    }
    console.log('');
  }
}
main().catch(e => console.error(e.message));
