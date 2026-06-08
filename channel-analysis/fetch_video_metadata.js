#!/usr/bin/env python3
// Fetch YouTube video metadata using youtubei.js (innerTube API).
// Works from any IP — no login required.
// Usage: node fetch_video_metadata.js <video_id> [video_id2 ...]

const { Innertube } = require('youtubei.js');

async function getMetadata(videoId) {
    const yt = await Innertube.create();
    
    const response = await yt.actions.execute('/next', {
        videoId: videoId,
        context: { client: yt.session.context }
    });
    
    const results = response?.data?.contents?.twoColumnWatchNextResults?.results?.results?.contents;
    const mf = response?.data?.microformat?.playerMicroformatRenderer;
    const panels = response?.data?.engagementPanels || [];
    
    let metadata = { video_id: videoId };
    
    for (const item of (results || [])) {
        if (item.videoPrimaryInfoRenderer) {
            const vpi = item.videoPrimaryInfoRenderer;
            metadata.title = vpi.title?.runs?.[0]?.text || '';
            const vc = vpi.viewCount?.videoViewCountRenderer;
            metadata.views = vc?.viewCount?.simpleText || '';
            metadata.date = vpi.dateText?.simpleText || '';
            
            // Likes
            const buttons = vpi.videoActions?.menuRenderer?.topLevelButtons || [];
            for (const btn of buttons) {
                const seg = btn.segmentedLikeDislikeButtonRenderer;
                if (seg?.likeButton?.toggleButtonRenderer) {
                    metadata.likes = seg.likeButton.toggleButtonRenderer.defaultText?.accessibility?.accessibilityData?.label || '';
                }
            }
        }
        if (item.videoSecondaryInfoRenderer) {
            const vsi = item.videoSecondaryInfoRenderer;
            metadata.channel = vsi.owner?.videoOwnerRenderer?.title?.runs?.[0]?.text || '';
            metadata.subscribers = vsi.owner?.videoOwnerRenderer?.subscriberCountText?.simpleText || '';
            metadata.description = (vsi.attributedDescription?.content || '').substring(0, 5000);
        }
    }
    
    if (mf) {
        metadata.publish_date = mf.publishDate || metadata.date;
        metadata.duration_seconds = mf.lengthSeconds;
        metadata.category = mf.category || '';
        metadata.thumbnail = mf.thumbnail?.thumbnails?.pop()?.url || '';
        if (!metadata.title) metadata.title = mf.title?.simpleText || '';
    }
    
    metadata.has_captions = panels.some(p => 
        p.engagementPanelSectionListRenderer?.panelIdentifier === 'engagement-panel-searchable-transcript'
    );
    
    metadata.url = `https://www.youtube.com/watch?v=${videoId}`;
    
    return metadata;
}

async function main() {
    const ids = process.argv.slice(2);
    if (!ids.length) {
        console.error('Usage: node fetch_video_metadata.js <video_id> [video_id2 ...]');
        process.exit(1);
    }
    
    const results = [];
    for (const id of ids) {
        try {
            const meta = await getMetadata(id);
            results.push(meta);
        } catch (e) {
            results.push({ video_id: id, error: e.message?.substring(0, 200) });
        }
    }
    
    if (ids.length === 1) {
        console.log(JSON.stringify(results[0], null, 2));
    } else {
        console.log(JSON.stringify(results, null, 2));
    }
}

main();
