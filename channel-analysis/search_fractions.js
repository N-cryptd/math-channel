const { Innertube } = require('youtubei.js');
async function main() {
  const yt = await Innertube.create();
  const queries = ['what are fractions explained', 'fractions visual intuition animation'];
  for (const q of queries) {
    try {
      const res = await yt.search(q);
      const items = [];
      for (const it of res.contents || []) {
        // lockupViewModel format
        const c = it.content;
        if (c && c.lockupViewModel) {
          const lv = c.lockupViewModel;
          const id = lv.contentId;
          const title = lv.metadata?.lockupMetadataViewModel?.title?.content;
          const metaLines = lv.metadata?.lockupMetadataViewModel?.metadata?.contentMetadataViewModel?.metadataRows || [];
          let views = '', channel = '', date = '';
          for (const row of metaLines) {
            for (const part of (row.metadataParts || [])) {
              const t = part?.text?.content || '';
              if (t.includes('views')) views = t;
              else if (t.includes('ago')) date = t;
              else if (!channel) channel = t;
            }
          }
          if (title) items.push({ id, title, views, date, channel });
        }
      }
      console.log(JSON.stringify({ query: q, results: items.slice(0, 10) }, null, 1));
    } catch (e) { console.error('Search error for', q, e.message); }
  }
}
main().catch(e => console.error(e.message));
