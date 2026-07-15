// Search YouTube for videos on a specific topic
// Usage: node search_topic.js "query string"
const { Innertube } = require('youtubei.js');

async function main() {
  const query = process.argv[2] || 'direct products finite abelian groups';
  const yt = await Innertube.create();
  
  const resp = await yt.actions.execute('/search', {
    query: query,
    context: { client: yt.session.context }
  });
  
  const items = resp?.data?.contents?.twoColumnSearchResultsRenderer?.primaryContents?.sectionListRenderer?.contents?.[0]?.itemSectionRenderer?.contents || [];
  const results = items.filter(i => i.videoRenderer).map(i => ({
    id: i.videoRenderer.videoId,
    title: i.videoRenderer.title.runs?.[0]?.text || '',
    views: i.videoRenderer.viewCountText?.simpleText || '',
    channel: i.videoRenderer.ownerText?.runs?.[0]?.text || '',
    date: i.videoRenderer.publishedTimeText?.simpleText || '',
    duration: i.videoRenderer.lengthText?.simpleText || ''
  }));
  
  console.log(JSON.stringify(results.slice(0, 15), null, 2));
}

main().catch(e => { process.stderr.write(`Error: ${e.message}\n`); process.exit(1); });
