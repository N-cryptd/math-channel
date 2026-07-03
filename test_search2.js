const { Innertube } = require('youtubei.js');
(async () => {
  try {
    const yt = await Innertube.create();
    const search = await yt.search('existence uniqueness proof explained math');
    const keys = Object.keys(search);
    console.log('Top-level keys:', keys);
    if (search.results) {
      console.log('results type:', typeof search.results);
      console.log('results keys:', Object.keys(search.results));
      if (search.results.contents) {
        const items = search.results.contents.filter(r => r.type === 'Video');
        items.slice(0, 8).forEach(r => {
          const v = r.toBasicVideo ? r.toBasicVideo() : r;
          console.log('VIDEO:', v.title || 'no title', '| ID:', v.id || 'no id', '| Channel:', v.channel?.name || 'N/A');
        });
      }
    }
    // Try accessing via .videos
    if (search.videos && search.videos.length > 0) {
      console.log('\n--- Via .videos ---');
      search.videos.slice(0, 8).forEach(v => {
        console.log('VIDEO:', v.title?.text || 'no title', '| ID:', v.id || v.videoId || 'no id');
      });
    }
    // Try raw data
    const raw = search.page;
    if (raw) {
      console.log('\n--- Raw page keys ---', Object.keys(raw));
    }
  } catch(e) {
    console.error('Error:', e.message.substring(0, 1000));
    console.error('Stack:', e.stack?.substring(0, 500));
  }
})();
