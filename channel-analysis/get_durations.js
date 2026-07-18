const { Innertube } = require('youtubei.js');
async function run() {
  const yt = await Innertube.create();
  for (const id of ['SkcfKqa7o0g','m1NGNtWIB1A','9yzxYYmGZXU','xoaMkvl979s','lWikW4oFOf8']) {
    try {
      const info = await yt.getInfo(id);
      const dur = info.basic_info?.duration || info.video_details?.duration || 0;
      const mins = Math.floor(dur/60);
      const secs = dur % 60;
      console.log(id + ': ' + mins + ':' + String(secs).padStart(2,'0'));
    } catch(e) { console.log(id + ': error ' + e.message); }
  }
}
run();
