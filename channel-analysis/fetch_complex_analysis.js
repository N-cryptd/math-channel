const { Innertube } = require('youtubei.js');

const fs = require('fs');

// Key competitor video IDs found from search
const videoIds = [
  // "Essence of complex analysis" series (most relevant - appears in many queries)
  'LoTaJE16uLk', // Why care about complex analysis? | Essence of complex analysis #1
  'NtoIXhUgqSk', // The 5 ways to visualize complex functions | Essence of complex analysis #3
  '0CHZMY02Dhk', // What does it mean to take a complex derivative? (visually explained)
  'TaWBXRaNEcc', // What do complex functions look like? | Essence of complex analysis #4
  'EyBDtUtyshk', // Complex integration, Cauchy and residue theorems | Essence of complex analysis #6

  // Complex Analysis Lxx series
  '_mv0q7-WF4E', // Complex Analysis L01: Overview & Motivation
  'pAq_dilfB_0', // Complex Analysis L06: Analytic Functions and Cauchy-Riemann Conditions
  'phbO46YJ1U0Q', // Complex Analysis L10: Cauchy Integral Formula

  // "Complex Analysis #N" series (possibly Michael Penn or similar)
  'dEu5ie25U0Y', // Complex Analysis 1 | Introduction
  'qXWRL6NHlWc', // Complex analysis: Introduction
  '_Q4pGe6GyR4', // Complex Analysis 3 | Complex Derivative and Examples

  // Complex Analysis by a Physicist
  'OfN9QG0zCXg', // The Cauchy-Riemann Equations - Complex Analysis By A Physicist

  // Laurent series
  'RC15R-ktnUI', // Laurent Series Explained | How to Determine Laurent Series

  // Contour integrals
  'cVCd9dnttfw', // Contour Integration Explained

  // Cauchy-Riemann
  'Ico7k2QlPH8', // Cauchy-Riemann Equations Explained (with Proof) | Complex Analysis #1

  // Residue theorem
  'UXMy5zEEEaU', // Complex Analysis 34 | Residue theorem

  // Analytic functions
  'QjJ2XzdXdEI', // Complex Analysis: what is an analytic function?
];

(async () => {
  const yt = await Innertube.create();
  const results = [];

  for (const id of videoIds) {
    try {
      const info = await yt.getInfo(id);
      const basicInfo = info.basic_info || info;
      const channel = info.basic_info?.channel || info.channel;
      const title = basicInfo.title || '';
      const views = basicInfo.view_count || basicInfo.viewCount || 0;
      const duration = basicInfo.duration || basicInfo.length_seconds || 0;
      const description = (basicInfo.short_description || basicInfo.description || '').slice(0, 300);
      const subs = channel?.subscriber_count || channel?.subscriberCount || 0;
      const chName = basicInfo.channel?.name || channel?.name || '';
      const published = basicInfo.publish_date || basicInfo.publishedDate || '';

      results.push({
        id,
        title: typeof title === 'string' ? title : (title?.text || ''),
        channel: typeof chName === 'string' ? chName : (chName?.text || ''),
        views: typeof views === 'number' ? views : parseInt(views) || 0,
        duration_seconds: typeof duration === 'number' ? duration : parseInt(duration) || 0,
        description: typeof description === 'string' ? description : (description?.text || ''),
        subscribers: typeof subs === 'number' ? subs : parseInt(subs) || 0,
        published: typeof published === 'string' ? published : (published?.text || ''),
      });

      console.log(`OK: ${id} | ${chName} | views=${views} | dur=${duration}s`);
    } catch(e) {
      console.error(`FAIL: ${id} | ${e.message}`);
      results.push({ id, error: e.message });
    }
  }

  // Write results to JSON
  fs.writeFileSync('/root/.hermes/kanban/workspaces/t_c79f8d6d/competitor_metadata.json', JSON.stringify(results, null, 2));
  console.log(`\nTotal: ${results.length} videos fetched, saved to competitor_metadata.json`);
})();
