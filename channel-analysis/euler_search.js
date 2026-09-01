const { Innertube } = require("youtubei.js");
(async () => {
  try {
    const yt = await Innertube.create();
    console.log("Searching Euler theorem...");
    const r = await yt.search("Euler theorem number theory proof");
    const items = r.videos || r.results || r;
    if (Array.isArray(items)) {
      items.slice(0, 4).forEach((v) => {
        console.log(JSON.stringify({ id: v.id, title: (v.title?.text || v.title || "").substring(0, 80), views: v.view_count }));
      });
    }
  } catch (e) { console.error("ERR:", e.message); }
})();