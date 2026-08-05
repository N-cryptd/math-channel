const { Innertube } = require('youtubei.js');

(async () => {
    const yt = await Innertube.create();
    const queries = [
        "monotone convergence theorem measure theory",
        "dominated convergence theorem proof",
        "fatou lemma measure theory",
        "lebesgue convergence theorems"
    ];
    
    for (const q of queries) {
        console.log(`\n--- Search: "${q}" ---`);
        try {
            const resp = await yt.actions.execute('/search', {
                query: q,
                context: { client: yt.session.context }
            });
            const items = resp?.data?.contents?.twoColumnSearchResultsRenderer?.primaryContents?.sectionListRenderer?.contents?.[0]?.itemSectionRenderer?.contents || [];
            for (const item of items.slice(0, 3)) {
                if (item.videoRenderer) {
                    const v = item.videoRenderer;
                    console.log(`  [${v.videoId}] ${v.title?.runs?.[0]?.text} (${v.viewCountText?.simpleText || ''})`);
                    console.log(`    Channel: ${v.ownerText?.runs?.[0]?.text || ''} | Date: ${v.publishedTimeText?.simpleText || ''}`);
                }
            }
        } catch(e) {
            console.log(`  Error: ${e.message?.substring(0, 80)}`);
        }
    }
})();
