const { Innertube } = require('./node_modules/youtubei.js');
async function main() {
  const yt = await Innertube.create();
  const queries = ['Fermat little theorem proof', 'Fermat little theorem Mathologer', 'Wilson theorem number theory animation', 'Fermat little theorem explained'];
  for (const q of queries) {
    console.log('\n=== QUERY: ' + q + ' ===');
    const search = await yt.search(q);
    for (const v of search.videos.slice(0, 3)) {
      console.log(v.id, '|', v.title.text, '|', v.channel?.name, '|', v.view_count, '|', v.duration?.seconds);
    }
  }
}
main().catch(e => console.error(e.message));
