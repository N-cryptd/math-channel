const path = require('path');
process.chdir('/root/math-channel');
const { Innertube } = require(path.join(process.cwd(), 'node_modules', 'youtubei.js'));
async function main() {
  const yt = await Innertube.create();
  const queries = [
    'limits of functions real analysis epsilon delta',
    'epsilon delta definition limit function rigorous',
    'limits of functions Bright Side of Mathematics',
  ];
  for (const q of queries) {
    console.log('=== QUERY:', q, '===');
    try {
      const search = await yt.search(q);
      for (const v of search.videos.slice(0,3)) {
        console.log(v.id, '|', v.title.text, '|', v.channel?.name);
      }
    } catch(e) { console.error(e.message); }
    console.log('');
  }
}
main().catch(e => console.error(e.message));
