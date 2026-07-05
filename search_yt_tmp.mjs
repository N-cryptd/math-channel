import { Innertube } from '/root/math-channel/node_modules/youtubei.js/dist/src/platform/node.js';

async function main() {
  const yt = await Innertube.create();
  const queries = [
    'limits of functions real analysis epsilon delta',
    'epsilon delta definition limit function rigorous proof',
    'limits of functions Bright Side of Mathematics real analysis',
  ];
  for (const q of queries) {
    console.log('=== QUERY:', q, '===');
    try {
      const search = await yt.search(q);
      for (const v of search.videos.slice(0,3)) {
        console.log(v.id, '|', v.title?.text, '|', v.channel?.name);
      }
    } catch(e) { console.error(e.message); }
    console.log('');
  }
}
main().catch(e => console.error(e.message));
