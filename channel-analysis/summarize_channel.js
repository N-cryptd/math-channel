// Summarize channel videos
// Usage: node summarize_channel.js "@channel" [--limit N]
const { Innertube } = require('youtubei.js');

async function main() {
  const query = process.argv[2] || '3blue1brown';
  let limit = 10;
  const li = process.argv.indexOf('--limit');
  if (li > -1 && process.argv[li + 1]) limit = parseInt(process.argv[li + 1]) || 10;
  
  const yt = await Innertube.create();
  
  // Resolve channel
  const resp = await yt.actions.execute('/search', {
    query: query.replace('@', ''),
    context: { client: yt.session.context }
  });
  const items = resp?.data?.contents?.twoColumnSearchResultsRenderer?.primaryContents?.sectionListRenderer?.contents?.[0]?.itemSectionRenderer?.contents || [];
  let channelId = null;
  for (const item of items) {
    if (item.channelRenderer?.channelId) { channelId = item.channelRenderer.channelId; break; }
  }
  if (!channelId) { process.stderr.write('Channel not found\n'); process.exit(1); }
  
  // Get videos
  const browseResp = await yt.actions.execute('/browse', {
    browseId: channelId,
    context: { client: yt.session.context }
  });
  
  let videosParams = null;
  const tabs = browseResp?.data?.contents?.twoColumnBrowseResultsRenderer?.tabs || [];
  for (const t of tabs) {
    const ep = t.tabRenderer?.endpoint?.browseEndpoint;
    if (t.tabRenderer?.title === 'Videos' && ep?.params) { videosParams = ep.params; break; }
  }
  if (!videosParams) videosParams = 'EgZ2aWRlb3PyBgQKAjoA';
  
  const videosResp = await yt.actions.execute('/browse', {
    browseId: channelId,
    params: videosParams,
    context: { client: yt.session.context }
  });
  
  const videoItems = videosResp?.data?.contents?.twoColumnBrowseResultsRenderer?.tabs?.[0]?.tabRenderer?.content?.richGridRenderer?.contents || [];
  const results = [];
  for (const item of videoItems) {
    const r = item.richItemRenderer?.content?.videoRenderer;
    if (r?.videoId) {
      results.push({
        title: r.title.runs?.[0]?.text || '',
        views: r.viewCountText?.simpleText || '',
        date: r.publishedTimeText?.simpleText || ''
      });
    }
    if (results.length >= limit) break;
  }
  
  console.log(`=== ${query} (recent ${limit} videos) ===`);
  for (const v of results) {
    console.log(`  ${v.title}`);
    console.log(`    ${v.views} | ${v.date}`);
  }
}

main().catch(e => { process.stderr.write(`Error: ${e.message}\n`); process.exit(1); });
