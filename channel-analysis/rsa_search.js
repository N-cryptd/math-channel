const { Innertube } = require("youtubei.js");
async function main() {
 const yt = await Innertube.create();
 const results = await yt.search("RSA encryption explained animation");
 for (let i = 0; i < Math.min(5, results.length); i++) {
   const v = results[i];
   console.log(v.id || v.video_id, "|", (v.title?.text || "").substring(0, 80), "|", v.view_count || 0);
 }
}
main().catch(e=>console.error(e.message));
