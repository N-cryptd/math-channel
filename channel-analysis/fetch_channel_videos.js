// Fetch a YouTube channel's video list using youtubei.js (innerTube API).
// Works from ANY IP — no Tor, no browser, no login required.
// Usage: node fetch_channel_videos.js <channel_name> [--limit N]
//
// Accepts: channel handle (@3blue1brown), channel name (3Blue1Brown), or channel ID (UC...)

const { Innertube } = require('youtubei.js');

async function resolveChannelId(yt, query) {
    if (/^UC[\w-]{22}$/.test(query)) return query;
    
    const resp = await yt.actions.execute('/search', {
        query: query.replace('@', ''),
        context: { client: yt.session.context }
    });
    
    const items = resp?.data?.contents?.twoColumnSearchResultsRenderer?.primaryContents?.sectionListRenderer?.contents?.[0]?.itemSectionRenderer?.contents || [];
    for (const item of items) {
        if (item.channelRenderer?.channelId) return item.channelRenderer.channelId;
    }
    return null;
}

async function getChannelVideos(yt, channelId, limit) {
    // First browse request to get tab params
    const browseResp = await yt.actions.execute('/browse', {
        browseId: channelId,
        context: { client: yt.session.context }
    });
    
    // Find the Videos tab params
    let videosParams = null;
    const tabs = browseResp?.data?.contents?.twoColumnBrowseResultsRenderer?.tabs || [];
    for (const t of tabs) {
        const ep = t.tabRenderer?.endpoint?.browseEndpoint;
        if (t.tabRenderer?.title === 'Videos' && ep?.params) {
            videosParams = ep.params;
            break;
        }
    }
    
    if (!videosParams) {
        // Fallback: try known params for "Videos" tab sorted by newest
        videosParams = 'EgZ2aWRlb3PyBgQKAjoA';
    }
    
    // Browse the videos tab
    const videosResp = await yt.actions.execute('/browse', {
        browseId: channelId,
        params: videosParams,
        context: { client: yt.session.context }
    });
    
    const videos = [];
    
    const tabs2 = videosResp?.data?.contents?.twoColumnBrowseResultsRenderer?.tabs || [];
    for (const t of tabs2) {
        const grid = t.tabRenderer?.content?.richGridRenderer;
        if (!grid?.contents) continue;
        
        for (const item of grid.contents) {
            if (videos.length >= limit) break;
            
            const lvm = item.richItemRenderer?.content?.lockupViewModel;
            if (!lvm) continue;
            
            const meta = lvm.metadata?.lockupMetadataViewModel;
            const rows = meta?.metadata?.contentMetadataViewModel?.metadataRows || [];
            
            // Extract views, date, duration from metadata rows
            let views = '', date = '', duration = '';
            for (const row of rows) {
                const parts = row.metadataParts || [];
                for (const part of parts) {
                    const text = part.text?.content || '';
                    if (text.match(/[\d.]+[KMBT]? views/i)) views = text;
                    else if (text.match(/(ago|year|month|week|day|hour)/i)) date = text;
                    else if (text.match(/^\d+:\d+/)) duration = text;
                }
            }
            
            videos.push({
                video_id: lvm.contentId || '',
                title: meta?.title?.content || '',
                views: views,
                date: date,
                duration: duration,
                channel: meta?.subtitle?.content || '',
            });
        }
        break;  // Only process first tab with content
    }
    
    return videos.slice(0, limit);
}

async function main() {
    const args = process.argv.slice(2);
    if (!args.length) {
        process.stderr.write('Usage: node fetch_channel_videos.js <channel_name> [--limit N]\n');
        process.exit(1);
    }
    
    let channelQuery = args[0];
    let limit = 20;
    const li = args.indexOf('--limit');
    if (li > -1 && args[li + 1]) limit = parseInt(args[li + 1]) || 20;
    
    const yt = await Innertube.create();
    
    let channelId = channelQuery;
    if (!channelId.startsWith('UC')) {
        process.stderr.write(`Resolving: ${channelQuery}...`);
        channelId = await resolveChannelId(yt, channelQuery);
        if (!channelId) {
            process.stderr.write(` not found\n`);
            process.exit(1);
        }
        process.stderr.write(` ${channelId}\n`);
    }
    
    const videos = await getChannelVideos(yt, channelId, limit);
    process.stderr.write(`Fetched ${videos.length} videos\n`);
    console.log(JSON.stringify(videos, null, 2));
}

main().catch(e => { process.stderr.write(`Error: ${e.message}\n`); process.exit(1); });
