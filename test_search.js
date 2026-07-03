const { Innertube } = require('youtubei.js');
(async () => {
  try {
    const yt = await Innertube.create();
    const search = await yt.search('existence uniqueness proof explained math');
    console.log(JSON.stringify({
      query: 'existence uniqueness proof explained math',
      results: search.data.contents
        .filter(r => r.video && r.video.videoId)
        .map(r => ({
          title: r.video.title.text || 'N/A',
          id: r.video.videoId,
          channel: r.video.channel?.name?.text || 'unknown',
          views: r.video.viewCount?.text || 'N/A',
          duration: r.video.duration?.text || 'N/A'
        }))
        .slice(0, 8)
    }, null, 2));
  } catch(e) {
    console.error('Error:', e.message.substring(0, 500));
  }
})();
