const fs=require('fs');
const LEGAL='Free plan available · Paid plans from $96/year';
const RISK='Research tool, not a broker. Not investment advice.';
const foot=`<div class="foot"><div class="row" style="gap:10px;flex-wrap:wrap"><span class="pill">${LEGAL}</span></div><div class="fine" style="margin-top:14px">${RISK}</div></div>`;
const wrap=(title,css,text,vis)=>`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"><style>${css}</style></head><body><div class="ad" id="ad"><div class="col text">${text}</div><div class="col vis">${vis}</div></div><script>document.getElementById('ad').classList.add(location.hash.slice(1)||'wide')</script></body></html>`;
const brand='<div class="brand"><i></i>Finsera Themes</div>';
const out={};

// 1 product
const rows=[['Artificial Intelligence','AI'],['AI Infrastructure','AII'],['Cyber Security','CYB'],['Robotics and Automation','ROB'],['Optical Networking','OPN'],['Genomic Revolution','GER'],['Critical Energy Materials','CEM'],['Aging Population','AGE']];
out.product_v1=wrap('product',`
.tbl{padding:0;overflow:hidden;width:100%}
.bar{padding:16px 20px;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;align-items:center}
.bar b{font-weight:600;font-size:17px}.sq .bar b{font-size:24px}
.srch{border:1px solid var(--line);border-radius:8px;padding:7px 14px;font-size:14px;color:var(--muted);background:var(--bg)}.sq .srch{font-size:20px;padding:10px 18px}
.r{display:flex;align-items:center;gap:14px;padding:13px 20px;border-bottom:1px solid var(--line);font-size:17px;font-weight:500}
.sq .r{padding:16px 28px;font-size:25px;gap:20px}.sq .r:nth-child(n+8){display:none}
.r:last-child{border:0}
.ck{width:18px;height:18px;border:1px solid #B9C2D3;border-radius:5px;flex:none}.sq .ck{width:26px;height:26px}
.ck.on{background:var(--blue);border-color:var(--blue)}
.ab{width:44px;text-align:center;font-size:12px;font-weight:700;color:var(--blue);background:var(--blue-l);border-radius:6px;padding:4px 0}.sq .ab{width:62px;font-size:17px}
.r span.n{flex:1}
.r em{font-style:normal;font-size:14px;color:var(--muted)}.sq .r em{font-size:20px}
`,`${brand}<div><h1>Browse investing themes, not just tickers.</h1><p class="sub">See what each theme covers, compare them, and build your own.</p></div>${foot}`,
`<div class="card tbl"><div class="bar"><b>Explore themes</b><span class="srch">Search themes…</span></div>${rows.map((r,i)=>`<div class="r"><span class="ck ${i<3?'on':''}"></span><span class="ab">${r[1]}</span><span class="n">${r[0]}</span><em>Details ›</em></div>`).join('')}</div>`);

// 2 explainer
const seg=[['Chips & hardware','Specialized processors and the equipment behind them'],['Cloud computing','Where models are trained and run'],['Data & analytics','Tools that turn data into decisions'],['Software','Applications built on top of AI'],['Humanoid robotics','AI moving into the physical world']];
out.explainer_ai_v1=wrap('explainer',`
.list{display:flex;flex-direction:column;gap:12px;width:100%}
.s{padding:16px 20px;display:flex;gap:16px;align-items:center}.sq .sub{display:none}.sq .s{padding:13px 24px;gap:20px}.sq .num{width:44px;height:44px}
.num{width:34px;height:34px;border-radius:50%;background:var(--blue-l);color:var(--blue);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:15px;flex:none}.sq .num{width:50px;height:50px;font-size:22px}
.s b{display:block;font-weight:600;font-size:19px}.sq .s b{font-size:27px}
.s div span{display:block;font-size:15px;color:var(--muted);margin-top:3px}.sq .s div span{font-size:21px;margin-top:2px}
.hd{display:flex;gap:10px;align-items:center;margin-bottom:4px}
`,`${brand}<div><h1>What's actually inside an “AI stocks” theme?</h1><p class="sub">Five parts of the AI economy, grouped in one place so you can research each one.</p></div>${foot}`,
`<div class="list"><div class="hd"><span class="tag">THEME</span><b style="font-size:20px" class="hb">Artificial Intelligence</b></div>${seg.map((s,i)=>`<div class="card s"><span class="num">${i+1}</span><div><b>${s[0]}</b><span>${s[1]}</span></div></div>`).join('')}</div>`);

// 3 question hook (native/plain)
out.question_v1=`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"><style>
.ad{background:#fff;flex-direction:column;justify-content:space-between}
.wide{padding:60px 80px}.sq{padding:100px 90px}
.q{font-family:'InterL';font-weight:700;letter-spacing:-.02em;line-height:1.18;font-size:56px}.sq .q{font-size:84px}
.body{font-size:26px;line-height:1.45;color:#3A4359;margin-top:28px;max-width:900px}.sq .body{font-size:36px;margin-top:40px}
.wide .body{font-size:24px}
.bt{display:flex;justify-content:space-between;align-items:flex-end;border-top:1px solid var(--line);padding-top:24px}
</style></head><body><div class="ad" id="ad"><div><div class="q">How do you research a theme like AI or cybersecurity?</div><p class="body">Most people start with a single ticker. We start with the theme, then go company by company. Free to try.</p></div><div class="bt"><div><div class="brand"><i></i>Finsera Themes</div><div class="fine" style="margin-top:10px">${LEGAL}<br>${RISK}</div></div></div></div><script>document.getElementById('ad').classList.add(location.hash.slice(1)||'wide')</script></body></html>`;

// 4 compare
const th=[['Artificial Intelligence','ai','Specialized hardware, software and infrastructure, including cloud computing and analytics.','Tech'],['Robotics and Automation','robotics','Sensors, actuators, autonomous mobile robots and industrial automation systems.','Industrials'],['Cyber Security','cyber-security','Cloud and endpoint protection, threat detection and regulatory compliance.','Security']];
out.compare_v1=wrap('compare',`
.cmp{display:flex;gap:14px;width:100%}.sq .sub{display:none}.sq .cmp{flex-direction:column;gap:16px}
.t{flex:1;padding:14px;display:flex;flex-direction:column;gap:12px;overflow:hidden}.sq .t{flex-direction:row;padding:16px;gap:24px;align-items:center}
.t img{width:100%;aspect-ratio:1/1;object-fit:cover;border-radius:10px;border:1px solid var(--line);display:block}.sq .t img{width:128px;flex:none}
.t b{font-size:17px;font-weight:600;line-height:1.2;display:block}.sq .t b{font-size:28px}
.t p{font-size:13px;color:var(--muted);line-height:1.4;margin:6px 0 10px}.sq .t p{font-size:21px;margin:6px 0 10px}
.t .tag{white-space:nowrap}
`,`${brand}<div><h1>AI, robotics or cybersecurity? Compare themes side by side.</h1><p class="sub">Look at what each one covers before you decide where to dig in.</p></div>${foot}`,
`<div class="cmp">${th.map(t=>`<div class="card t"><img src="assets/${t[1]}.webp"><div><b>${t[0]}</b><p>${t[2]}</p><span class="tag">${t[3].toUpperCase()}</span></div></div>`).join('')}</div>`);

// 5 build
out.build_v1=wrap('build',`
.col.vis{justify-content:center}.bld{width:100%;padding:24px;display:flex;flex-direction:column;gap:18px}.sq .sub{display:none}.sq .bld{padding:44px;gap:34px}
.lb{font-size:13px;font-weight:600;color:var(--muted);letter-spacing:.04em;margin-bottom:8px}.sq .lb{font-size:19px;margin-bottom:12px}
.inp{border:1px solid var(--line);border-radius:10px;padding:13px 16px;font-size:19px;font-weight:500;background:var(--bg)}.sq .inp{font-size:29px;padding:20px 24px;border-radius:14px}
.chips{display:flex;flex-wrap:wrap;gap:8px}.sq .chips{gap:12px}
.chip{border:1px solid var(--line);border-radius:999px;padding:8px 14px;font-size:16px;font-weight:500;background:#fff}.sq .chip{font-size:24px;padding:12px 22px}
.chip.b{background:var(--blue-l);border-color:#C9D7EC;color:var(--blue)}
.steps{display:flex;gap:10px}.st{flex:1;border:1px solid var(--line);border-radius:10px;padding:12px;font-size:14px;color:var(--muted);font-weight:500}.sq .st{font-size:21px;padding:18px;border-radius:14px}
.st b{display:block;color:var(--navy);font-size:15px}.sq .st b{font-size:23px}
`,`${brand}<div><h1>Can't find your theme? Build your own.</h1><p class="sub">Humanoid robots, grid storage, longevity. Name it, add companies, and track it in one place.</p></div>${foot}`,
`<div class="card bld"><div><div class="lb">THEME NAME</div><div class="inp">Humanoid robots</div></div><div><div class="lb">COMPANIES</div><div class="chips"><span class="chip b">Company A</span><span class="chip b">Company B</span><span class="chip b">Company C</span><span class="chip">+ Add company</span></div></div><div class="steps"><div class="st"><b>1</b>Pick an idea</div><div class="st"><b>2</b>Add companies</div><div class="st"><b>3</b>Track it</div></div></div>`);

// 6 statement
out.statement_v1=`<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"><style>
.ad{background:var(--navy);color:#fff;flex-direction:column;justify-content:space-between}
.wide{padding:56px 72px}.sq{padding:90px 86px}
.big{font-family:'Caslon',serif;font-weight:600;line-height:1;letter-spacing:-.015em;font-size:104px}.sq .big{font-size:150px}
.big em{font-style:italic;color:#8FB1E6}
.sub2{font-size:24px;color:#B9C3DA;margin-top:24px;line-height:1.4}.sq .sub2{font-size:36px;margin-top:36px}
.pill2{display:inline-flex;border:1px solid rgba(255,255,255,.22);border-radius:999px;padding:9px 16px;font-size:16px}.sq .pill2{font-size:23px;padding:12px 22px}
.brand i{background:#8FB1E6}.sq .brand{order:0}
</style></head><body><div class="ad" id="ad"><div class="brand"><i></i>Finsera Themes</div><div><div class="big">Start with a theme, <em>not a ticker.</em></div><p class="sub2">Research AI, robotics, cybersecurity and 90+ more ideas.</p></div><div><span class="pill2">${LEGAL}</span><div class="fine" style="margin-top:14px;color:#9AA6C2">${RISK}</div></div></div><script>document.getElementById('ad').classList.add(location.hash.slice(1)||'wide')</script></body></html>`;

// 7 vs schwab (message match: "Look before you buy a theme.")
out.vs_schwab_v1=wrap('vs_schwab',`
.col.vis{justify-content:center}.vs{width:100%;padding:24px;display:flex;flex-direction:column;gap:18px}.sq .vs{padding:44px;gap:32px}.sq .sub{display:none}
.lb{font-size:13px;font-weight:600;color:var(--muted);letter-spacing:.04em;margin-bottom:8px}.sq .lb{font-size:19px;margin-bottom:12px}
.inp{border:1px solid var(--line);border-radius:10px;padding:14px 16px;font-size:18px;font-weight:500;line-height:1.35;background:var(--bg)}.sq .inp{font-size:28px;padding:22px 26px;border-radius:14px}
.steps{display:flex;gap:10px}.st{flex:1;border:1px solid var(--line);border-radius:10px;padding:12px;font-size:14px;color:var(--muted);font-weight:500}.sq .st{font-size:21px;padding:18px;border-radius:14px}
.st b{display:block;color:var(--navy);font-size:15px}.sq .st b{font-size:23px}
.note{border-top:1px solid var(--line);padding-top:16px;font-size:15px;color:var(--muted);line-height:1.4}.sq .note{font-size:22px;padding-top:26px}
`,`${brand}<div><h1>Look before you buy a theme.</h1><p class="sub">Type an idea, see the companies behind it, and compare it with the S&amp;P&nbsp;500. Research only.</p></div>${foot}`,
`<div class="card vs"><div><div class="lb">DESCRIBE YOUR IDEA</div><div class="inp">Mid- and large-cap defense companies with exposure to drones and autonomous systems</div></div><div class="steps"><div class="st"><b>1</b>Type an idea</div><div class="st"><b>2</b>See the companies</div><div class="st"><b>3</b>Compare with the S&amp;P&nbsp;500</div></div><div class="note">Schwab Investing Themes lets you buy a theme. Finsera lets you study one first. You can use both.</div></div>`);

for(const k in out)fs.writeFileSync(k+'.html',out[k]);
