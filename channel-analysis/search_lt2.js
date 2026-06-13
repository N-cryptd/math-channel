const { Innertube } = require('youtubei.js');

async function main() {
  const yt = await Innertube.create();
  
  // Search for Trefor Bazett Laplace
  console.log("=== Trefor Bazett ===");
  const s1 = await yt.search('Laplace Transform Dr Trefor Bazett');
  for (const v of s1.videos.slice(0,3)) {
    console.log(v.id, '|', v.title?.text || v.title);
  }
  
  // Search for general Laplace explained
  console.log("\n=== General ===");
  const s2 = await yt.search('Laplace Transform explained animation');
  for (const v of s2.videos.slice(0,5)) {
    console.log(v.id, '|', v.title?.text || v.title, '|', v.channel?.name || 'N/A');
  }
  
  // Search for blackpenredpen
  console.log("\n=== blackpenredpen ===");
  const s3 = await yt.search('Laplace transform blackpenredpen');
  for (const v of s3.videos.slice(0,3)) {
    console.log(v.id, '|', v.title?.text || v.title);
  }
  
  // Steve Brunton
  console.log("\n=== Steve Brunton ===");
  const s4 = await yt.search('Laplace transform Steve Brunton');
  for (const v of s4.videos.slice(0,3)) {
    console.log(v.id, '|', v.title?.text || v.title);
  }
}
main().catch(e => console.error(e.message));
