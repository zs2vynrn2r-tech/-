const { chromium } = require('playwright');
(async () => {
  const [src, dst] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + src);
  await p.waitForFunction(() => document.body.dataset.done === '1', null, { timeout: 60000 });
  await p.pdf({ path: dst, format: 'A4', printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 } });
  const n = await p.evaluate(() => document.querySelectorAll('.page').length);
  console.log('pages', n, dst);
  await b.close();
})();
