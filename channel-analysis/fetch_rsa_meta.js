const { Innertube } = require("youtubei.js");
async function main() {
  const yt = await Innertube.create();
  const ids = [
    "4zahvcJ9glg",  // RSA Algorithm example - 1.27M views
    "wXB-V_Keiu8",  // Public Key Cryptography RSA - 990K views
    "5pswKNgVZSg",  // Euler's Totient Theorem & FLT proof - 91K
    "ijT3pmmal00",  // Euler's Theorem proof - 55K
    "hm8s6FAc4pg",  // RSA How Does It Actually Work - 62K
  ];
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
        has_captions: !!(v.captions && v.captions.length > 0),
      }));
    } catch(e) { console.error('Error for', id, e.message); }
  }
}
main().catch(e=>console.error(e.message));
