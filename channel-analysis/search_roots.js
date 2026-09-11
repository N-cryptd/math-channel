const { Innertube } = require('youtubei.js');
async function main() {
  const yt = await Innertube.create();
  const queries = [
    'what are square roots explained',
    'square roots and radicals visual intuition',
    'cube roots for beginners',
    'simplifying radicals explained',
    'math antics square roots',
  ];
  const all = [];
  for (const q of queries) {
    try {
      const res = await yt.search(q);
      const items = [];
      for (const it of (res.results || [])) {
        if (!it.video_id) continue;
        items.push({
          id: it.video_id,
          title: it.title?.text ?? null,
          channel: it.author?.name ?? null,
          views: it.short_view_count?.text ?? null,
          published: it.published?.text ?? null,
          length: it.length_text?.text ?? null,
        });
      }
      console.error(`[${q}] -> ${items.length} results`);
      all.push({ query: q, results: items.slice(0, 8) });
    } catch (e) { console.error('Search error for', q, e.message); }
  }
  console.log(JSON.stringify(all, null, 1));
}
main().catch(e => console.error(e.message));
