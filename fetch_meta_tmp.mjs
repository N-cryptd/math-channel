import { Innertube } from '/root/math-channel/node_modules/youtubei.js/dist/src/platform/node.js';

async function main() {
  const yt = await Innertube.create();
  const videos = [
    'kVQNhAIFZYc', // Epsilon-Delta Definition of Functional Limits | Real Analysis
    'PzsWhDlTcqY', // Real Analysis | Precise definition of a limit (Michael Penn)
    'aVeKuMPFv8s', // Real Analysis | Sequential limits in functions (Michael Penn)
    '7svyCaVjH6w', // Connecting Function Limits and Sequence Limits | Real Analysis (Wrath of Math)
    'vIRvEvjKM58', // Limits of Oscillating Functions and the Squeeze Theorem (Trefor)
    'Qspc6uBMdEY', // A Tale of Three Functions | Intro to Limits Part I (Trefor)
  ];
  for (const id of videos) {
    try {
      const info = await yt.getInfo(id);
      const vd = info.basic_info;
      console.log(id, '|', vd.title, '|', vd.view_count, '|', vd.duration);
      if (vd.channel) console.log('  Channel:', vd.channel.name);
    } catch(e) { console.error(id, 'ERROR:', e.message?.substring(0,100)); }
  }
}
main().catch(e => console.error(e.message));
