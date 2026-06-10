#!/usr/bin/env node
const { Innertube } = require('youtubei.js');

async function main() {
  const yt = await Innertube.create();
  const ids = process.argv.slice(2);
  for (const id of ids) {
    try {
      const resp = await yt.actions.execute('/next', {
        videoId: id,
        context: { client: yt.session.context }
      });
      const mf = resp.data.microformat?.playerMicroformatRenderer;
      const results = resp.data.contents?.twoColumnWatchNextResults?.results?.results?.contents || [];
      let title = '', views = '', channel = '', subs = '', desc = '', date = '';
      for (const item of results) {
        if (item.videoPrimaryInfoRenderer) {
          const vpi = item.videoPrimaryInfoRenderer;
          title = vpi.title?.runs?.[0]?.text || '';
          views = vpi.viewCount?.videoViewCountRenderer?.viewCount?.simpleText || '';
          date = vpi.dateText?.simpleText || '';
        }
        if (item.videoSecondaryInfoRenderer) {
          const vsi = item.videoSecondaryInfoRenderer;
          channel = vsi.owner?.videoOwnerRenderer?.title?.runs?.[0]?.text || '';
          subs = vsi.owner?.videoOwnerRenderer?.subscriberCountText?.simpleText || '';
          desc = (vsi.attributedDescription?.content || '').substring(0, 300);
        }
      }
      console.log(JSON.stringify({
        id, title: title || mf?.title?.simpleText || '',
        views, channel, subs, date,
        duration: mf?.lengthSeconds || '',
        desc
      }, null, 2));
    } catch (e) {
      console.error(`Error for ${id}: ${e.message?.substring(0, 200)}`);
    }
  }
}
main();
