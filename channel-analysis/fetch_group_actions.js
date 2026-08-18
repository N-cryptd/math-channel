const { Innertube } = require('youtubei.js');

(async () => {
  const yt = await Innertube.create();
  const ids = [
    'sNX3txN9zc4',  // Essence of Group Theory - Group Actions
    'mH0oCDa74tE',  // 3B1B - monster group (mentions group actions)
    '72-lcTwM2II',  // Visual Algebra - Five features of group actions
  ];
  for (const id of ids) {
    try {
      const info = await yt.getInfo(id);
      const basic = info.basic_info || {};
      console.log('--- ' + id + ' ---');
      console.log('Title:', basic.title || info.title || 'N/A');
      console.log('Channel:', basic.channel?.name || 'N/A');
      console.log('Views:', basic.view_count || 'N/A');
      console.log('Duration:', basic.duration || 'N/A');
      console.log('Published:', basic.publish_date || 'N/A');
      console.log('Subs:', basic.channel?.subscriber_count || 'N/A');
      console.log('Desc:', (basic.short_description || '').slice(0, 300));
      console.log();
    } catch(e) { console.error(id + ': ' + e.message); }
  }
})();
