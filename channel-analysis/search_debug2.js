const { Innertube } = require('youtubei.js');
async function search() {
  const yt = await Innertube.create();
  const results = await yt.search('Lp spaces introduction pth power summable');
  const items = results.data?.contents || [];
  console.log('Total items:', items.length);
  for (let i = 0; i < Math.min(3, items.length); i++) {
    console.log('\n--- Item', i, '---');
    console.log('Top keys:', Object.keys(items[i]).join(', '));
    // Look for lockupViewModel or similar
    const lockup = items[i]?.lockupViewModel;
    if (lockup) {
      console.log('lockup contentId:', lockup.contentId);
      console.log('lockup title:', lockup.title?.content);
      console.log('lockup metadata:', JSON.stringify(lockup.metadata?.metadataContent?.compact)?.substring(0, 200));
    } else {
      console.log('No lockup. Data:', JSON.stringify(items[i]).substring(0, 500));
    }
  }
}
search().catch(e => console.error(e.message));
