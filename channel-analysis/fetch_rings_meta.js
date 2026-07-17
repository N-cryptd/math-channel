const { Innertube } = require('youtubei.js');

async function fetchMetadata() {
  const yt = await Innertube.create();
  const ids = [
    'j_f7O-4Rb9U',  // Ring Definition (expanded) - Abstract Algebra
    'vfyUU_prh9s',  // Algebraic Structures: Groups, Rings, and Fields
    '6RC70C9FNXI',  // Abstract Algebra: The definition of a Ring
    '1oqqpqaDgfI',  // Lord of the Commutative Rings - Numberphile
  ];
  for (const id of ids) {
    try {
      const info = await yt.getInfo(id);
      const basic = info.basic_info;
      console.log('---');
      console.log('ID:', id);
      console.log('Title:', basic?.title || 'N/A');
      console.log('Views:', basic?.view_count || 'N/A');
      console.log('Channel:', basic?.channel?.name || 'N/A');
      console.log('Duration:', basic?.duration || 'N/A');
      console.log('Has captions:', info.captions ? 'yes' : 'no');
    } catch (e) {
      console.log('Error for ' + id + ': ' + e.message);
    }
  }
}
fetchMetadata().catch(e => console.error(e.message));
