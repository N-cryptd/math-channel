const { Innertube } = require("youtubei.js");
(async () => {
  try {
    const yt = await Innertube.create();
    console.log("Searching...");
    const r = await yt.search("RSA encryption explained math");
    const items = r.videos || r.results || r;
    if (Array.isArray(items)) {
      items.slice(0, 6).forEach((v) => {
        console.log(JSON.stringify({ id: v.id, title: (v.title?.text || v.title || "").substring(0, 80), views: v.view_count }));
      });
    } else {
      console.log("Type:", typeof items);
      console.log("Keys:", Object.keys(items).slice(0, 10));
    }
  } catch (e) { console.error("ERR:", e.message); }
})();