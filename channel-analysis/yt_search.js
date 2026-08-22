const { Innertube } = require('youtubei.js');
async function main() {
  const yt = await Innertube.create();
  const ids = ['z9bTzjy4SCg', 'c6FlpordfDk', 'OeynencPfpg', 'KCSZ4QhOw0I'];
  for (const id of ids) {
    try {
      const info = await yt.getInfo(id);
      const v = info.basic_info;
      console.log(JSON.stringify({
        id,
        title: v.title,
        views: v.view_count,
        duration: v.duration,
        channel: info.channel?.name,
        subscribers: info.channel?.subscriber_count,
        published: v.published_text || v.publish_date,
        description: (v.short_description || '').substring(0, 300),
      }));
    } catch(e) { console.error('Error for', id, e.message); }
  }
}
main().catch(e=>console.error(e.message));
