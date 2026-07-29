// Search YouTube for topic-specific videos using youtubei.js (innerTube API)
// Usage: node search_topic.js "Cauchy integral formula complex analysis" [--limit 10]

const { Innertube } = require('youtubei.js');

async function main() {
    const args = process.argv.slice(2);
    if (!args.length) {
        process.stderr.write('Usage: node search_topic.js <query> [--limit N]\n');
        process.exit(1);
    }

    const query = args[0];
    let limit = 10;
    const li = args.indexOf('--limit');
    if (li > -1 && args[li + 1]) limit = parseInt(args[li + 1]) || 10;

    const yt = await Innertube.create();
    const resp = await yt.actions.execute('/search', {
        query: query,
        context: { client: yt.session.context }
    });

    const items = resp?.data?.contents?.twoColumnSearchResultsRenderer?.primaryContents?.sectionListRenderer?.contents?.[0]?.itemSectionRenderer?.contents || [];
    const results = [];

    for (const item of items) {
        if (results.length >= limit) break;
        const vid = item.videoRenderer;
        if (!vid?.videoId) continue;
        results.push({
            video_id: vid.videoId,
            title: vid.title?.runs?.[0]?.text || '',
            views: vid.viewCountText?.simpleText || vid.shortViewCountText?.simpleText || '',
            channel: vid.ownerText?.runs?.[0]?.text || '',
            date: vid.publishedTimeText?.simpleText || '',
            duration: vid.lengthText?.simpleText || '',
        });
    }

    console.log(JSON.stringify(results, null, 2));
}

main().catch(e => { process.stderr.write('Error: ' + e.message + '\n'); process.exit(1); });
