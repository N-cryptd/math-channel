const { Innertube } = require('youtubei.js');
async function search() {
  const yt = await Innertube.create();
  
  // Try multiple search terms
  const terms = ['Lp spaces measure theory', 'LP spaces introduction functional analysis'];
  
  for (const term of terms) {
    console.log('\n=== Search: "' + term + '" ===');
    const results = await yt.search(term);
    const contents = results.data?.contents || results.data || [];
    for (const item of contents) {
      // Try different data structures
      const data = item?.content || item;
      const videoId = data?.videoId || data?.id;
      const title = data?.title?.text || data?.title || '';
      const views = data?.viewCount?.text || '';
      const dur = data?.lengthText?.text || data?.duration || '';
      if (videoId && title) {
        console.log(videoId + ' | ' + title.substring(0, 70) + ' | views:' + views + ' | dur:' + dur);
      }
    }
  }
}
search().catch(e => console.error(e.message));
