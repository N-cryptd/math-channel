const { Innertube } = require('youtubei.js');
async function main() {
  const yt = await Innertube.create();
  // Try fetching TBSOM channel videos to find Lp spaces
  const results = await yt.search('@brightsideofmaths Lp spaces');
  
  // Try to extract from different possible structures
  const allContents = results?.on_response_received_endpoints?.[0]?.append_continuation_items_action?.continuationItems
    || results?.data?.contents
    || results?.contents
    || [];
  
  console.log('allContents length:', allContents.length);
  
  // Also dump the top-level keys
  console.log('Results keys:', Object.keys(results).join(', '));
  if (results.data) console.log('data keys:', Object.keys(results.data).join(', '));
  
  // Try the raw page
  const page = results.page;
  if (page) {
    console.log('page keys:', Object.keys(page).join(', '));
  }
}
main().catch(e => console.error(e.message));
