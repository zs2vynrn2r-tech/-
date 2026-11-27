const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(500);
await p.pdf({path:process.argv[3],format:'A4',printBackground:true,preferCSSPageSize:true,displayHeaderFooter:true,headerTemplate:'<div></div>',footerTemplate:'<div style="width:100%;font-size:8px;color:#888;text-align:center">- <span class="pageNumber"></span> / <span class="totalPages"></span> -</div>'});
await b.close();})();
