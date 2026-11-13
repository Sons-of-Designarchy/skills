const {chromium}=require('/Users/danielpliego/projects/fin/finsera/e2e/node_modules/playwright-core');
(async()=>{const b=await chromium.launch({executablePath:process.env.HOME+'/Library/Caches/ms-playwright/chromium_headless_shell-1234/chrome-headless-shell-mac-arm64/chrome-headless-shell'});
const names=['product_v1','explainer_ai_v1','question_v1','compare_v1','build_v1','statement_v1','vs_schwab_v1'];
for(const n of names)for(const [f,w,h] of [['1200x628',1200,628],['1080x1080',1080,1080]]){
 const p=await b.newPage({viewport:{width:w,height:h}});
 await p.goto(`file://${__dirname}/${n}.html#${w==1200?'wide':'sq'}`);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
 await p.screenshot({path:`${__dirname}/../${n}_${f}.png`});await p.close();}
await b.close()})();
