const { Innertube } = require('youtubei.js');
(async () => {
  try {
    const yt = await Innertube.create();
    const search = await yt.search('proof by cases math animation');
    const videos = search.videos.slice(0, 8);
    console.log('=== Search: "proof by cases math animation" ===');
    videos.forEach((v, i) => {
      console.log(`${i+1}. "${v.title?.text}" | ID: ${v.id} | Channel: ${v.channel?.name?.text || 'N/A'} | Views: ${v.view_count?.text || 'N/A'} | Duration: ${v.duration?.text || 'N/A'}`);
    });
    console.log('\n=== Search: "proof by cases explained" ===');
    const search2 = await yt.search('proof by cases explained');
    const videos2 = search2.videos.slice(0, 8);
    videos2.forEach((v, i) => {
      console.log(`${i+1}. "${v.title?.text}" | ID: ${v.id} | Channel: ${v.channel?.name?.text || 'N/A'} | Views: ${v.view_count?.text || 'N/A'} | Duration: ${v.duration?.text || 'N/A'}`);
    });
  } catch(e) {
    console.error('Error:', e.message.substring(0, 500));
  }
})();
