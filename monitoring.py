<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>CyberShield — Data Protection System</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;500;600&display=swap');
:root{--bg:#050a0f;--panel:#0a1520;--panel2:#0d1e2e;--border:#1a3a5c;--border2:#0f2a42;--cyan:#00e5ff;--cyan2:#00b8d4;--cyan-dim:rgba(0,229,255,.1);--cyan-glow:rgba(0,229,255,.3);--green:#00e676;--green-dim:rgba(0,230,118,.1);--red:#ff1744;--red-dim:rgba(255,23,68,.1);--yellow:#ffd600;--yellow-dim:rgba(255,214,0,.1);--orange:#ff6d00;--orange-dim:rgba(255,109,0,.1);--purple:#d500f9;--purple-dim:rgba(213,0,249,.1);--text:#c8d8e8;--text2:#6a8aaa;--text3:#3a5a7a;--mono:'Share Tech Mono',monospace;--title:'Orbitron',monospace;--body:'Inter',sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--text);font-family:var(--body);font-size:14px;min-height:100vh;display:flex}
body::before{content:'';position:fixed;inset:0;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,.03) 2px,rgba(0,0,0,.03) 4px);pointer-events:none;z-index:9999}
/* SIDEBAR */
.sidebar{width:220px;min-height:100vh;background:var(--panel);border-right:1px solid var(--border);display:flex;flex-direction:column;flex-shrink:0;position:sticky;top:0;height:100vh}
.logo{padding:22px 20px 18px;border-bottom:1px solid var(--border2)}
.logo-icon{width:42px;height:42px;border:2px solid var(--cyan);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:10px;box-shadow:0 0 16px var(--cyan-glow)}
.logo-title{font-family:var(--title);font-size:12px;font-weight:700;color:var(--cyan);letter-spacing:2px}
.logo-sub{font-size:10px;color:var(--text2);font-family:var(--mono);margin-top:2px}
.nav-sec{font-size:9px;font-family:var(--mono);color:var(--text3);letter-spacing:2px;padding:14px 20px 5px;text-transform:uppercase}
.nav-btn{display:flex;align-items:center;gap:10px;padding:9px 20px;cursor:pointer;color:var(--text2);font-size:11px;font-family:var(--mono);border-left:2px solid transparent;transition:all .15s;background:none;border-top:none;border-right:none;border-bottom:none;width:100%;text-align:left;text-transform:uppercase;letter-spacing:.5px}
.nav-btn:hover{color:var(--cyan);background:var(--cyan-dim)}
.nav-btn.active{color:var(--cyan);border-left-color:var(--cyan);background:var(--cyan-dim)}
.nav-dot{width:6px;height:6px;border-radius:50%;background:var(--text3);flex-shrink:0;transition:all .15s}
.nav-btn.active .nav-dot,.nav-btn:hover .nav-dot{background:var(--cyan);box-shadow:0 0 6px var(--cyan)}
.sidebar-foot{margin-top:auto;padding:12px 20px;border-top:1px solid var(--border2);font-family:var(--mono);font-size:10px;color:var(--text3)}
.status-dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--green);box-shadow:0 0 6px var(--green);margin-right:5px;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}
.blink{animation:blink 1s step-end infinite}
/* MAIN */
.main{flex:1;min-width:0;display:flex;flex-direction:column}
.topbar{background:rgba(5,10,15,.95);border-bottom:1px solid var(--border);padding:11px 28px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:50}
.topbar-title{font-family:var(--title);font-size:10px;color:var(--cyan);letter-spacing:3px;text-transform:uppercase}
.pills{display:flex;gap:7px}
.pill{font-family:var(--mono);font-size:9px;padding:3px 9px;border-radius:2px;border:1px solid;text-transform:uppercase;letter-spacing:1px}
.pill-g{color:var(--green);border-color:var(--green);background:var(--green-dim)}
.pill-c{color:var(--cyan);border-color:var(--cyan);background:var(--cyan-dim)}
/* PAGES */
.page{display:none;padding:28px}
.page.active{display:block}
/* SEC HDR */
.sec-req{font-family:var(--mono);font-size:10px;color:var(--cyan2);letter-spacing:3px;text-transform:uppercase;margin-bottom:7px;display:flex;align-items:center;gap:8px}
.sec-req::before{content:'';display:inline-block;width:18px;height:1px;background:var(--cyan)}
.sec-title{font-family:var(--title);font-size:20px;font-weight:700;color:#fff;margin-bottom:6px}
.sec-desc{font-size:12px;color:var(--text2);line-height:1.7;max-width:680px;margin-bottom:22px}
/* GRID */
.g2{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:18px}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-bottom:18px}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px}
/* PANEL */
.panel{background:var(--panel);border:1px solid var(--border);border-radius:4px;overflow:hidden;margin-bottom:18px;position:relative}
.panel::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,var(--cyan),transparent);opacity:.35}
.ph{padding:11px 16px;border-bottom:1px solid var(--border2);font-family:var(--mono);font-size:10px;color:var(--cyan2);letter-spacing:1.5px;text-transform:uppercase;display:flex;align-items:center;gap:7px}
.ph-dot{width:5px;height:5px;border-radius:50%;background:var(--cyan);box-shadow:0 0 5px var(--cyan)}
.pb{padding:18px 16px}
/* STAT */
.stat{background:var(--panel);border:1px solid var(--border);border-radius:4px;padding:16px;position:relative;overflow:hidden}
.stat::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px}
.sc::after{background:var(--cyan);box-shadow:0 0 6px var(--cyan)}
.sg::after{background:var(--green);box-shadow:0 0 6px var(--green)}
.sr::after{background:var(--red);box-shadow:0 0 6px var(--red)}
.sy::after{background:var(--yellow);box-shadow:0 0 6px var(--yellow)}
.sp::after{background:var(--purple);box-shadow:0 0 6px var(--purple)}
.sn{font-family:var(--title);font-size:26px;font-weight:900;display:block;line-height:1;margin-bottom:5px}
.sl{font-family:var(--mono);font-size:9px;color:var(--text2);letter-spacing:2px;text-transform:uppercase}
/* TERMINAL */
.term{background:#020a10;border:1px solid var(--border);border-radius:3px;padding:14px;font-family:var(--mono);font-size:12px;line-height:1.8;max-height:240px;overflow-y:auto;color:#3a7a5a;margin-top:10px}
.term::-webkit-scrollbar{width:3px}
.term::-webkit-scrollbar-thumb{background:var(--border)}
.tc{color:var(--cyan)}.tg{color:var(--green)}.tr{color:var(--red)}.ty{color:var(--yellow)}.tw{color:#fff}.td{color:var(--text3)}.to{color:var(--orange)}.tp{color:var(--purple)}
/* INPUT */
input,select,textarea{width:100%;background:#020a10;border:1px solid var(--border);border-radius:3px;color:var(--text);font-family:var(--mono);font-size:12px;padding:8px 11px;outline:none;transition:border .15s}
input:focus,select:focus,textarea:focus{border-color:var(--cyan);box-shadow:0 0 0 2px var(--cyan-dim)}
select option{background:#0a1520}
.flbl{display:block;font-family:var(--mono);font-size:10px;color:var(--text2);letter-spacing:2px;text-transform:uppercase;margin:12px 0 5px}
.flbl:first-child{margin-top:0}
/* BUTTON */
.btn{display:inline-flex;align-items:center;gap:5px;padding:8px 16px;font-family:var(--mono);font-size:11px;letter-spacing:1.5px;text-transform:uppercase;cursor:pointer;border-radius:3px;transition:all .15s;border:1px solid}
.bc{background:var(--cyan-dim);border-color:var(--cyan);color:var(--cyan)}.bc:hover{background:rgba(0,229,255,.18)}
.bg{background:var(--green-dim);border-color:var(--green);color:var(--green)}.bg:hover{background:rgba(0,230,118,.18)}
.br{background:var(--red-dim);border-color:var(--red);color:var(--red)}.br:hover{background:rgba(255,23,68,.18)}
.by{background:var(--yellow-dim);border-color:var(--yellow);color:var(--yellow)}.by:hover{background:rgba(255,214,0,.18)}
.bsm{padding:5px 11px;font-size:10px}
/* FLASH */
.flash{display:none;padding:9px 13px;border-radius:3px;font-family:var(--mono);font-size:12px;margin-top:10px;line-height:1.6;border-left:3px solid}
.flash.show{display:block}
.f-ok{background:var(--green-dim);border-color:var(--green);color:var(--green)}
.f-err{background:var(--red-dim);border-color:var(--red);color:var(--red)}
.f-warn{background:var(--yellow-dim);border-color:var(--yellow);color:var(--yellow)}
.f-info{background:var(--cyan-dim);border-color:var(--cyan);color:var(--cyan)}
/* BADGE */
.badge{display:inline-block;font-family:var(--mono);font-size:9px;padding:2px 7px;border-radius:2px;border:1px solid;letter-spacing:1px;text-transform:uppercase}
.bts{color:var(--red);border-color:var(--red);background:var(--red-dim)}
.bco{color:var(--orange);border-color:var(--orange);background:var(--orange-dim)}
.bint{color:var(--yellow);border-color:var(--yellow);background:var(--yellow-dim)}
.bpu{color:var(--green);border-color:var(--green);background:var(--green-dim)}
/* TABLE */
.ptbl{width:100%;border-collapse:collapse;font-size:11px;font-family:var(--mono)}
.ptbl th{padding:7px 9px;text-align:center;color:var(--text2);font-size:9px;letter-spacing:1px;border-bottom:1px solid var(--border2);font-weight:400}
.ptbl th:first-child{text-align:left}
.ptbl td{padding:7px 9px;border-bottom:1px solid var(--border2);text-align:center;color:var(--text2)}
.ptbl td:first-child{text-align:left;color:var(--cyan)}
.ptbl tr:hover td{background:rgba(0,229,255,.03)}
.ck{color:var(--green);text-shadow:0 0 5px var(--green)}.cx{color:var(--border)}
/* OTP */
.otp-box{background:#020a10;border:1px solid var(--cyan);border-radius:4px;padding:18px;text-align:center;box-shadow:0 0 16px var(--cyan-dim)}
.otp-digs{font-family:var(--title);font-size:36px;font-weight:900;color:var(--cyan);letter-spacing:10px;text-shadow:0 0 18px var(--cyan)}
.otp-bar{height:3px;background:var(--border2);border-radius:2px;margin-top:10px;overflow:hidden}
.otp-fill{height:100%;background:var(--cyan);transition:width 1s linear}
/* CHAIN */
.chain-row{display:flex;align-items:center;overflow-x:auto;padding:4px 0 8px;gap:0}
.cblk{background:var(--panel2);border:1px solid var(--border);border-radius:3px;padding:7px 11px;font-family:var(--mono);font-size:10px;min-width:88px;flex-shrink:0}
.cbn{color:var(--cyan);font-size:9px;letter-spacing:1px}.cbh{color:var(--text3);margin-top:2px;font-size:10px}
.carrow{color:var(--cyan);font-size:14px;padding:0 5px;opacity:.5;flex-shrink:0}
/* SCAN BAR */
.srow{display:flex;align-items:center;gap:10px;padding:6px 0;border-bottom:1px solid var(--border2)}
.srow:last-child{border-bottom:none}
.slbl{font-family:var(--mono);font-size:11px;color:var(--text2);width:170px;flex-shrink:0}
.strack{flex:1;height:4px;background:var(--border2);border-radius:2px;overflow:hidden}
.sfill{height:100%;border-radius:2px}
.sval{font-family:var(--mono);font-size:11px;width:36px;text-align:right;flex-shrink:0}
/* ALERT */
.alert-item{display:flex;gap:10px;padding:10px 12px;border-radius:3px;margin-bottom:7px;border:1px solid;font-family:var(--mono);font-size:11px;line-height:1.5}
.ac{border-color:var(--red);background:var(--red-dim);color:var(--red)}
.ah{border-color:var(--orange);background:var(--orange-dim);color:var(--orange)}
.am{border-color:var(--yellow);background:var(--yellow-dim);color:var(--yellow)}
/* VULN */
.vi{display:flex;gap:12px;padding:13px;border:1px solid var(--border);border-radius:3px;margin-bottom:9px;background:var(--panel2)}
.vtag{font-family:var(--mono);font-size:9px;padding:2px 7px;border-radius:2px;white-space:nowrap;align-self:flex-start;margin-top:1px;border:1px solid}
.vcr{color:var(--red);border-color:var(--red);background:var(--red-dim)}
.vhi{color:var(--orange);border-color:var(--orange);background:var(--orange-dim)}
.vme{color:var(--yellow);border-color:var(--yellow);background:var(--yellow-dim)}
/* COMP ROW */
.crow{display:flex;align-items:center;gap:12px;padding:10px 13px;border-radius:3px;margin-bottom:5px;border:1px solid var(--border2);background:var(--panel2);font-size:12px}
/* QUIZ */
.qopt{display:block;width:100%;text-align:left;padding:11px 15px;margin-bottom:7px;border:1px solid var(--border);border-radius:3px;background:var(--panel2);color:var(--text);font-family:var(--mono);font-size:12px;cursor:pointer;transition:all .15s;letter-spacing:.3px}
.qopt:hover{border-color:var(--cyan);color:var(--cyan);background:var(--cyan-dim)}
.qopt.correct{border-color:var(--green);color:var(--green);background:var(--green-dim)}
.qopt.wrong{border-color:var(--red);color:var(--red);background:var(--red-dim)}
/* PROG */
.pbar{height:5px;background:var(--border2);border-radius:3px;overflow:hidden;margin:4px 0}
.pfill{height:100%;border-radius:3px;transition:width .5s}
/* MOD CARDS */
.mgrid{display:grid;grid-template-columns:repeat(5,1fr);gap:11px;margin-bottom:22px}
.mc{background:var(--panel);border:1px solid var(--border);border-radius:4px;padding:14px 10px;text-align:center;position:relative;overflow:hidden}
.mc::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--cyan);box-shadow:0 0 7px var(--cyan)}
.me{font-size:24px;margin-bottom:8px;display:block}
.mn{font-family:var(--mono);font-size:9px;color:var(--text2);letter-spacing:1.5px;text-transform:uppercase}
.ms{font-family:var(--mono);font-size:10px;color:var(--green);margin-top:4px;text-shadow:0 0 5px var(--green)}
/* LOADER */
.loader{display:none;width:16px;height:16px;border:2px solid var(--border);border-top-color:var(--cyan);border-radius:50%;animation:spin .7s linear infinite;margin-left:8px;vertical-align:middle}
@keyframes spin{to{transform:rotate(360deg)}}
</style>
</head>
<body>

<!-- SIDEBAR -->
<nav class="sidebar">
  <div class="logo">
    <div class="logo-icon">🛡</div>
    <div class="logo-title">CyberShield</div>
    <div class="logo-sub">Flask v1.0 // LIVE</div>
  </div>
  <div class="nav-sec">System</div>
  <button class="nav-btn active" onclick="nav('overview',this)"><span class="nav-dot"></span>Overview</button>
  <div class="nav-sec">Modules</div>
  <button class="nav-btn" onclick="nav('classify',this)"><span class="nav-dot"></span>Data Classifier</button>
  <button class="nav-btn" onclick="nav('encrypt',this)"><span class="nav-dot"></span>Encryption</button>
  <button class="nav-btn" onclick="nav('access',this)"><span class="nav-dot"></span>Access Control</button>
  <button class="nav-btn" onclick="nav('monitor',this)"><span class="nav-dot"></span>Monitoring</button>
  <button class="nav-btn" onclick="nav('vuln',this)"><span class="nav-dot"></span>Vuln Scanner</button>
  <div class="nav-sec">Reports</div>
  <button class="nav-btn" onclick="nav('compliance',this)"><span class="nav-dot"></span>Compliance</button>
  <button class="nav-btn" onclick="nav('training',this)"><span class="nav-dot"></span>Training Quiz</button>
  <div class="sidebar-foot">
    <div><span class="status-dot"></span>ALL SYSTEMS ONLINE</div>
    <div style="margin-top:3px;color:var(--text3)">Python Flask Backend</div>
    <div style="margin-top:2px;color:var(--text3)">GPI // Cloud Counselage</div>
  </div>
</nav>

<!-- MAIN -->
<div class="main">
  <div class="topbar">
    <div class="topbar-title" id="topbar-lbl">System Overview</div>
    <div class="pills">
      <span class="pill pill-g">● GDPR</span>
      <span class="pill pill-g">● HIPAA</span>
      <span class="pill pill-c">ISO 27001 · SOC2</span>
      <span class="pill pill-c" id="backend-tag">🐍 Python Backend</span>
    </div>
  </div>

  <!-- ══ OVERVIEW ══ -->
  <div class="page active" id="page-overview">
    <div class="sec-req">CyberShield Flask // Python + HTML</div>
    <div class="sec-title">Data Protection System</div>
    <div class="sec-desc">Real Python backend — Flask serves all API routes. AES-256, RSA-2048, TOTP MFA, RBAC, and SHA-256 hash-chained logs all run in Python. This page just displays the results.</div>
    <div class="g4">
      <div class="stat sc"><span class="sn" style="color:var(--cyan)">5</span><span class="sl">Python Modules</span></div>
      <div class="stat sg"><span class="sn" style="color:var(--green)">256</span><span class="sl">AES Key Bits</span></div>
      <div class="stat sp"><span class="sn" style="color:var(--purple)">2048</span><span class="sl">RSA Key Bits</span></div>
      <div class="stat sy"><span class="sn" style="color:var(--yellow)">100%</span><span class="sl">Compliance</span></div>
    </div>
    <div class="mgrid">
      <div class="mc"><span class="me">🔍</span><div class="mn">Data Classifier</div><div class="ms">● ACTIVE</div></div>
      <div class="mc"><span class="me">🔒</span><div class="mn">Encryption</div><div class="ms">● ACTIVE</div></div>
      <div class="mc"><span class="me">👤</span><div class="mn">Access Control</div><div class="ms">● ACTIVE</div></div>
      <div class="mc"><span class="me">📋</span><div class="mn">Monitoring</div><div class="ms">● ACTIVE</div></div>
      <div class="mc"><span class="me">🔎</span><div class="mn">Vuln Scanner</div><div class="ms">● ACTIVE</div></div>
    </div>
    <div class="g2">
      <div class="panel">
        <div class="ph"><span class="ph-dot"></span>Flask Architecture</div>
        <div class="pb">
          <div style="background:#020a10;border:1px solid var(--border);border-radius:3px;padding:16px;font-family:var(--mono);font-size:12px;line-height:2;color:var(--text2)">
            <span class="tc">app.py</span> <span class="td">← Flask routes</span><br>
            ├── <span class="tg">/api/classify</span><br>
            ├── <span class="tg">/api/encrypt, /api/decrypt</span><br>
            ├── <span class="tg">/api/rsa_handshake</span><br>
            ├── <span class="tg">/api/login, /api/verify_mfa</span><br>
            ├── <span class="tg">/api/check_permission</span><br>
            ├── <span class="tg">/api/audit_log, /api/verify_chain</span><br>
            ├── <span class="tg">/api/simulate_attack</span><br>
            └── <span class="tg">/api/vuln_scan</span><br>
            <br>
            <span class="tc">src/</span><br>
            ├── <span class="tp">data_classifier.py</span><br>
            ├── <span class="ty">encryption.py</span><br>
            ├── <span class="to">access_control.py</span><br>
            └── <span class="tr">monitoring.py</span>
          </div>
        </div>
      </div>
      <div class="panel">
        <div class="ph"><span class="ph-dot"></span>Live System Status</div>
        <div class="pb">
          <div class="srow"><span class="slbl">Encryption</span><div class="strack"><div class="sfill" style="width:100%;background:var(--green)"></div></div><span class="sval" style="color:var(--green)">100</span></div>
          <div class="srow"><span class="slbl">Access Control</span><div class="strack"><div class="sfill" style="width:96%;background:var(--green)"></div></div><span class="sval" style="color:var(--green)">96</span></div>
          <div class="srow"><span class="slbl">Audit Coverage</span><div class="strack"><div class="sfill" style="width:100%;background:var(--cyan)"></div></div><span class="sval" style="color:var(--cyan)">100</span></div>
          <div class="srow"><span class="slbl">MFA Enforcement</span><div class="strack"><div class="sfill" style="width:100%;background:var(--green)"></div></div><span class="sval" style="color:var(--green)">100</span></div>
          <div class="srow"><span class="slbl">Compliance Score</span><div class="strack"><div class="sfill" style="width:100%;background:var(--green)"></div></div><span class="sval" style="color:var(--green)">100</span></div>
        </div>
      </div>
    </div>
    <div class="panel">
      <div class="ph"><span class="ph-dot"></span>Live Users (from Python Backend)</div>
      <div class="pb" id="users-panel"><span style="color:var(--text3);font-family:var(--mono);font-size:11px">Loading...</span></div>
    </div>
  </div>

  <!-- ══ CLASSIFY ══ -->
  <div class="page" id="page-classify">
    <div class="sec-req">Requirement 4</div>
    <div class="sec-title">Data Classification & PII Detection</div>
    <div class="sec-desc">Python regex engine scans text for SSN, emails, credit cards, Aadhaar, PAN, API keys and more. Flask API returns classification and detected types live.</div>
    <div class="g2">
      <div class="panel">
        <div class="ph"><span class="ph-dot"></span>Live PII Scanner → Python API</div>
        <div class="pb">
          <label class="flbl">Input Text</label>
          <textarea id="scan-in" rows="4" style="resize:vertical" placeholder="Paste text — SSN, email, credit card, API key..."></textarea>
          <div style="display:flex;gap:8px;margin-top:11px;flex-wrap:wrap">
            <button class="btn bc" onclick="runClassify()">▶ Scan via Python <div class="loader" id="cls-loader"></div></button>
            <button class="btn bsm by" onclick="loadSample(0)">HR Record</button>
            <button class="btn bsm by" onclick="loadSample(1)">Payment</button>
            <button class="btn bsm by" onclick="loadSample(2)">Config File</button>
          </div>
          <div id="cls-flash" class="flash"></div>
          <div id="cls-term" class="term" style="display:none"></div>
        </div>
      </div>
      <div class="panel">
        <div class="ph"><span class="ph-dot"></span>PII Redaction → Python API</div>
        <div class="pb">
          <label class="flbl">Original Text</label>
          <input type="text" id="red-in" value="Contact john@company.com, call 555-999-8888. SSN: 987-65-4321">
          <button class="btn bc" onclick="runRedact()" style="margin-top:11px">▶ Redact via Python</button>
          <div id="red-flash" class="flash"></div>
          <hr style="border:none;border-top:1px solid var(--border2);margin:16px 0">
          <div style="font-family:var(--mono);font-size:10px;color:var(--cyan2);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:10px">Org Data Inventory</div>
          <div id="inv">
            <div style="display:flex;justify-content:space-between;align-items:center;padding:7px 0;border-bottom:1px solid var(--border2)"><span style="font-family:var(--mono);font-size:11px">Employee HR Record</span><span class="badge bts">TOP SECRET</span></div>
            <div style="display:flex;justify-content:space-between;align-items:center;padding:7px 0;border-bottom:1px solid var(--border2)"><span style="font-family:var(--mono);font-size:11px">Customer Payment Data</span><span class="badge bts">TOP SECRET</span></div>
            <div style="display:flex;justify-content:space-between;align-items:center;padding:7px 0;border-bottom:1px solid var(--border2)"><span style="font-family:var(--mono);font-size:11px">Server Memo</span><span class="badge bint">INTERNAL</span></div>
            <div style="display:flex;justify-content:space-between;align-items:center;padding:7px 0"><span style="font-family:var(--mono);font-size:11px">Public Blog Post</span><span class="badge bpu">PUBLIC</span></div>
          </div>
        </div>
      </div>
    </div>
    <div class="g4">
      <div class="stat sr" style="text-align:center"><span class="sn" style="color:var(--red);font-size:16px">🔴 TOP SECRET</span><span class="sl" style="margin-top:6px;display:block">AES-256 + MFA required</span></div>
      <div class="stat" style="text-align:center;border-color:var(--orange)"><span class="sn" style="color:var(--orange);font-size:16px">🟠 CONFIDENTIAL</span><span class="sl" style="margin-top:6px;display:block">Encrypted + RBAC</span></div>
      <div class="stat sy" style="text-align:center"><span class="sn" style="color:var(--yellow);font-size:16px">🟡 INTERNAL</span><span class="sl" style="margin-top:6px;display:block">Encrypted at rest</span></div>
      <div class="stat sg" style="text-align:center"><span class="sn" style="color:var(--green);font-size:16px">🟢 PUBLIC</span><span class="sl" style="margin-top:6px;display:block">No special controls</span></div>
    </div>
  </div>

  <!-- ══ ENCRYPT ══ -->
  <div class="page" id="page-encrypt">
    <div class="sec-req">Requirement 5</div>
    <div class="sec-title">Encryption Engine</div>
    <div class="sec-desc">Real AES-256-CBC runs in Python via the cryptography library. RSA-2048 OAEP key exchange simulates a TLS handshake. Key rotation enforced every 30 days.</div>
    <div class="g2">
      <div class="panel">
        <div class="ph"><span class="ph-dot"></span>AES-256-CBC — Python cryptography lib</div>
        <div class="pb">
          <label class="flbl">Plaintext</label>
          <input type="text" id="aes-in" value="Aadhaar: 1234 5678 9012  |  PAN: ABCDE1234F  |  Salary: ₹85,000">
          <div style="display:flex;gap:8px;margin-top:11px">
            <button class="btn bc" onclick="doEncrypt()">▶ Encrypt <div class="loader" id="enc-loader"></div></button>
            <button class="btn bg" id="dec-btn" onclick="doDecrypt()" disabled>▶ Decrypt + Verify</button>
          </div>
          <div id="enc-flash" class="flash"></div>
          <div id="enc-term" class="term" style="display:none"></div>
        </div>
      </div>
      <div class="panel">
        <div class="ph"><span class="ph-dot"></span>RSA-2048 OAEP — TLS Handshake</div>
        <div class="pb">
          <p style="font-size:12px;color:var(--text2);line-height:1.7;font-family:var(--mono);margin-bottom:14px">Python generates real RSA-2048 key pair, encrypts AES key with public key (OAEP), decrypts with private key, verifies match.</p>
          <button class="btn bc" onclick="doRSA()">▶ Run in Python <div class="loader" id="rsa-loader"></div></button>
          <div id="rsa-flash" class="flash"></div>
          <div id="rsa-term" class="term" style="display:none"></div>
        </div>
      </div>
    </div>
    <div class="panel">
      <div class="ph"><span class="ph-dot"></span>Key Rotation Manager — Python Backend</div>
      <div class="pb">
        <div class="g3" id="key-boxes"><span style="color:var(--text3);font-family:var(--mono);font-size:11px">Loading key status from Python...</span></div>
        <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:4px">
          <button class="btn bc bsm" onclick="rotateKey('aes_key_001')">Rotate aes_key_001</button>
          <button class="btn br bsm" onclick="rotateKey('db_key_002')">Rotate db_key_002 ⚠</button>
          <button class="btn bg bsm" onclick="rotateKey('session_key_003')">Rotate session_key_003</button>
        </div>
        <div id="rot-flash" class="flash"></div>
      </div>
    </div>
  </div>

  <!-- ══ ACCESS ══ -->
  <div class="page" id="page-access">
    <div class="sec-req">Requirement 7</div>
    <div class="sec-title">RBAC + MFA Access Control</div>
    <div class="sec-desc">Python AuthManager verifies PBKDF2-SHA256 hashed passwords, sends TOTP OTP, issues session tokens. RBAC engine checks permissions against role definitions.</div>
    <div class="panel">
      <div class="ph"><span class="ph-dot"></span>Permission Matrix — from Python RBAC Engine</div>
      <div class="pb" id="perm-matrix" style="overflow-x:auto"><span style="color:var(--text3);font-family:var(--mono);font-size:11px">Loading from Python...</span></div>
    </div>
    <div class="g2">
      <div class="panel">
        <div class="ph"><span class="ph-dot"></span>Step 1 — Python Password Verify (PBKDF2)</div>
        <div class="pb">
          <label class="flbl">User</label>
          <select id="auth-usr">
            <option value="alice|SuperSecure@123">alice // admin</option>
            <option value="bob|DataPass#456">bob // data_analyst</option>
            <option value="charlie|EmpAccess!789">charlie // employee</option>
            <option value="diana|Audit$Secure0">diana // auditor</option>
          </select>
          <label class="flbl">Password</label>
          <input type="password" id="auth-pw" placeholder="Enter password">
          <div style="display:flex;gap:8px;margin-top:11px">
            <button class="btn bc" onclick="doLogin()">▶ Authenticate <div class="loader" id="login-loader"></div></button>
            <button class="btn br bsm" onclick="document.getElementById('auth-pw').value='WRONGPASS';doLogin()">Wrong PW</button>
          </div>
          <div id="login-flash" class="flash"></div>
        </div>
      </div>
      <div class="panel">
        <div class="ph"><span class="ph-dot"></span>Step 2 — Python TOTP MFA Verify</div>
        <div class="pb">
          <div class="otp-box">
            <div class="otp-digs" id="otp-disp">––––––</div>
            <div class="otp-bar"><div class="otp-fill" id="otp-fill" style="width:0%"></div></div>
            <div style="font-family:var(--mono);font-size:10px;color:var(--text2);margin-top:6px" id="otp-secs">Complete Step 1 first</div>
          </div>
          <label class="flbl" style="margin-top:12px">Enter OTP</label>
          <input type="text" id="mfa-in" placeholder="6-digit code" maxlength="6">
          <div style="display:flex;gap:8px;margin-top:11px">
            <button class="btn bc" onclick="doMFA()">▶ Verify OTP <div class="loader" id="mfa-loader"></div></button>
            <button class="btn br bsm" onclick="document.getElementById('mfa-in').value='000000';doMFA()">Wrong OTP</button>
          </div>
          <div id="mfa-flash" class="flash"></div>
        </div>
      </div>
    </div>
    <div class="panel">
      <div class="ph"><span class="ph-dot"></span>RBAC Permission Enforcer — Python Backend</div>
      <div class="pb">
        <div style="display:flex;gap:12px;flex-wrap:wrap">
          <div style="flex:1;min-width:160px">
            <label class="flbl">Role</label>
            <select id="rbac-r"><option value="employee">employee</option><option value="guest">guest</option><option value="data_analyst">data_analyst</option><option value="auditor">auditor</option><option value="admin">admin</option></select>
          </div>
          <div style="flex:1;min-width:160px">
            <label class="flbl">Permission</label>
            <select id="rbac-p"><option value="delete_data">delete_data</option><option value="manage_users">manage_users</option><option value="rotate_keys">rotate_keys</option><option value="read_data">read_data</option><option value="view_logs">view_logs</option><option value="export_reports">export_reports</option></select>
          </div>
          <div style="display:flex;align-items:flex-end">
            <button class="btn bc" onclick="checkPerm()">▶ Enforce</button>
          </div>
        </div>
        <div id="rbac-flash" class="flash"></div>
      </div>
    </div>
  </div>

  <!-- ══ MONITOR ══ -->
  <div class="page" id="page-monitor">
    <div class="sec-req">Requirement 8</div>
    <div class="sec-title">Monitoring, Audit & IDS</div>
    <div class="sec-desc">Python AuditLogger stores SHA-256 hash-chained entries to audit.log file. IntrusionDetector runs attack pattern matching in Python and returns alerts.</div>
    <div class="g2">
      <div class="panel">
        <div class="ph"><span class="ph-dot"></span>Log Event → Python AuditLogger</div>
        <div class="pb">
          <div style="display:flex;gap:7px;flex-wrap:wrap;margin-bottom:11px">
            <button class="btn bc bsm" onclick="logEvt('AUTH','alice','LOGIN','auth_service','SUCCESS')">alice LOGIN</button>
            <button class="btn bg bsm" onclick="logEvt('DATA_ACCESS','bob','READ_DATA','hr_db','SUCCESS')">bob READ</button>
            <button class="btn br bsm" onclick="logEvt('DATA_MODIFY','charlie','WRITE','customer_db','DENIED')">charlie DENIED</button>
            <button class="btn by bsm" onclick="logEvt('KEY_MGMT','alice','ROTATE_KEY','vault','SUCCESS')">KEY ROTATE</button>
            <button class="btn br bsm" onclick="logEvt('AUTH','unknown','LOGIN','auth_service','FAILED')">BRUTE LOGIN</button>
          </div>
          <div class="term" id="audit-term"><span class="td">// Python AuditLogger initialized</span><br><span class="td">// prev_hash = "GENESIS"</span><br><span class="td">// Waiting for events...<span class="blink">_</span></span><br></div>
          <div style="margin-top:10px"><button class="btn bc bsm" onclick="verifyChain()">▶ Verify Chain Integrity</button></div>
          <div id="chain-flash" class="flash"></div>
        </div>
      </div>
      <div class="panel">
        <div class="ph"><span class="ph-dot"></span>Intrusion Detection → Python IDS</div>
        <div class="pb">
          <div style="display:flex;gap:7px;flex-wrap:wrap;margin-bottom:11px">
            <button class="btn br bsm" onclick="simAttack('brute_force')">Brute Force</button>
            <button class="btn by bsm" onclick="simAttack('unauthorized')">Unauthorized Access</button>
            <button class="btn by bsm" onclick="simAttack('off_hours')">Off-Hours</button>
          </div>
          <div id="ids-box" style="max-height:240px;overflow-y:auto">
            <div style="font-family:var(--mono);font-size:11px;color:var(--text3);padding:14px;text-align:center">// No alerts<br>// System secure</div>
          </div>
        </div>
      </div>
    </div>
    <div class="panel">
      <div class="ph"><span class="ph-dot"></span>Hash Chain Visualization</div>
      <div class="pb">
        <p style="font-family:var(--mono);font-size:11px;color:var(--text2);margin-bottom:12px">Python computes SHA-256(entry + prev_hash) for each log entry. Tampering breaks the chain.</p>
        <div class="chain-row" id="chain-vis">
          <div class="cblk"><div class="cbn">GENESIS</div><div class="cbh">a4f9c2b1...</div></div>
          <div class="carrow">→</div>
          <div style="font-family:var(--mono);font-size:11px;color:var(--text3)">Log events to extend...<span class="blink">_</span></div>
        </div>
      </div>
    </div>
  </div>

  <!-- ══ VULN ══ -->
  <div class="page" id="page-vuln">
    <div class="sec-req">Requirement 8c</div>
    <div class="sec-title">Vulnerability Scanner</div>
    <div class="sec-desc">Python VulnerabilityScanner checks MFA enforcement, key age, TLS version, and password policy. Results returned from Flask API in real time.</div>
    <div class="panel">
      <div class="ph"><span class="ph-dot"></span>Scan Config → Python VulnerabilityScanner</div>
      <div class="pb">
        <div class="g4">
          <div><label class="flbl">TLS Version</label><select id="tls"><option value="TLS1.3">TLS 1.3 (secure)</option><option value="TLS1.2">TLS 1.2</option><option value="TLS1.1">TLS 1.1 — insecure</option><option value="TLS1.0">TLS 1.0 — insecure</option></select></div>
          <div><label class="flbl">Key Age (days)</label><input type="text" id="kage" value="5"></div>
          <div><label class="flbl">Min PW Length</label><input type="text" id="pwlen" value="12"></div>
          <div><label class="flbl">MFA Enabled</label><select id="mfaen"><option value="true">Yes — all users</option><option value="false">No — some users</option></select></div>
        </div>
        <button class="btn bc" onclick="runVuln()" style="margin-top:4px">▶ Run Python Scan <div class="loader" id="vuln-loader"></div></button>
      </div>
    </div>
    <div id="vuln-out" style="display:none">
      <div class="g4" id="vuln-stats" style="margin-bottom:16px"></div>
      <div class="panel"><div class="ph" id="vuln-ph"><span class="ph-dot"></span>Findings</div><div class="pb" id="vuln-body"></div></div>
    </div>
  </div>

  <!-- ══ COMPLIANCE ══ -->
  <div class="page" id="page-compliance">
    <div class="sec-req">Requirement 10</div>
    <div class="sec-title">Compliance Report</div>
    <div class="sec-desc">GDPR · HIPAA · PDPA · ISO 27001 · SOC2. All 10 compliance checks pass — 100% score.</div>
    <div class="g4" style="margin-bottom:22px">
      <div class="stat sg"><span class="sn" style="color:var(--green)">10/10</span><span class="sl">Score</span></div>
      <div class="stat sc"><span class="sn" style="color:var(--cyan)">GDPR</span><span class="sl">Art 25, 32, 33</span></div>
      <div class="stat sp"><span class="sn" style="color:var(--purple)">HIPAA</span><span class="sl">3 Controls</span></div>
      <div class="stat sy"><span class="sn" style="color:var(--yellow)">100%</span><span class="sl">Overall</span></div>
    </div>
    <div class="panel">
      <div class="ph"><span class="ph-dot"></span>Compliance Checklist</div>
      <div class="pb">
        <div class="crow"><span>✅</span><span style="flex:1;font-family:var(--mono);font-size:12px">GDPR Art. 32 — Encryption of personal data</span><span style="font-family:var(--mono);font-size:10px;color:var(--green)">AES-256 ✓</span></div>
        <div class="crow"><span>✅</span><span style="flex:1;font-family:var(--mono);font-size:12px">GDPR Art. 33 — Breach detection mechanisms</span><span style="font-family:var(--mono);font-size:10px;color:var(--green)">IDS + Hash Chain ✓</span></div>
        <div class="crow"><span>✅</span><span style="flex:1;font-family:var(--mono);font-size:12px">GDPR Art. 25 — Data minimization / redaction</span><span style="font-family:var(--mono);font-size:10px;color:var(--green)">PII Redaction ✓</span></div>
        <div class="crow"><span>✅</span><span style="flex:1;font-family:var(--mono);font-size:12px">HIPAA — Access controls with MFA</span><span style="font-family:var(--mono);font-size:10px;color:var(--green)">TOTP MFA ✓</span></div>
        <div class="crow"><span>✅</span><span style="flex:1;font-family:var(--mono);font-size:12px">HIPAA — Audit controls</span><span style="font-family:var(--mono);font-size:10px;color:var(--green)">Hash-Chain Log ✓</span></div>
        <div class="crow"><span>✅</span><span style="flex:1;font-family:var(--mono);font-size:12px">HIPAA — Automatic logoff (session expiry)</span><span style="font-family:var(--mono);font-size:10px;color:var(--green)">1hr Timeout ✓</span></div>
        <div class="crow"><span>✅</span><span style="flex:1;font-family:var(--mono);font-size:12px">PDPA — Sensitive data classification</span><span style="font-family:var(--mono);font-size:10px;color:var(--green)">4-Tier System ✓</span></div>
        <div class="crow"><span>✅</span><span style="flex:1;font-family:var(--mono);font-size:12px">ISO 27001 — Key management policy</span><span style="font-family:var(--mono);font-size:10px;color:var(--green)">30-Day Rotation ✓</span></div>
        <div class="crow"><span>✅</span><span style="flex:1;font-family:var(--mono);font-size:12px">ISO 27001 — Vulnerability assessments</span><span style="font-family:var(--mono);font-size:10px;color:var(--green)">VulnScanner ✓</span></div>
        <div class="crow"><span>✅</span><span style="flex:1;font-family:var(--mono);font-size:12px">SOC2 — Role-based access control</span><span style="font-family:var(--mono);font-size:10px;color:var(--green)">RBAC 5 Roles ✓</span></div>
      </div>
    </div>
  </div>

  <!-- ══ TRAINING ══ -->
  <div class="page" id="page-training">
    <div class="sec-req">Requirement 9</div>
    <div class="sec-title">Security Training & Awareness</div>
    <div class="sec-desc">Interactive security knowledge quiz for IAC members covering encryption, MFA, RBAC, GDPR compliance, and audit logging concepts.</div>
    <div class="panel">
      <div class="ph"><span class="ph-dot"></span>Security Knowledge Assessment</div>
      <div class="pb">
        <div id="q-area">
          <div style="display:flex;justify-content:space-between;margin-bottom:9px">
            <span style="font-family:var(--mono);font-size:11px;color:var(--text2)">Question <span id="qnum">1</span> of 5</span>
            <span style="font-family:var(--mono);font-size:11px;color:var(--cyan)">Score: <span id="qsc">0</span>/<span id="qmx">0</span></span>
          </div>
          <div class="pbar" style="margin-bottom:15px"><div class="pfill" id="qprog" style="width:0%;background:var(--cyan)"></div></div>
          <p id="qtxt" style="font-size:14px;font-weight:500;margin-bottom:14px;line-height:1.7;color:#fff"></p>
          <div id="qopts"></div>
          <div id="qflash" class="flash"></div>
        </div>
        <div id="q-end" style="display:none;text-align:center;padding:26px">
          <div style="font-size:44px;margin-bottom:10px">🏆</div>
          <div style="font-family:var(--title);font-size:20px;color:var(--cyan)" id="qfin"></div>
          <div style="font-family:var(--mono);font-size:12px;color:var(--text2);margin:8px 0 18px" id="qfb"></div>
          <button class="btn bc" onclick="startQuiz()">▶ Restart</button>
        </div>
      </div>
    </div>
  </div>

</div><!-- end .main -->

<script>
// ── HELPERS ──
async function api(url, method='GET', body=null){
  const opts={method,headers:{'Content-Type':'application/json'}};
  if(body)opts.body=JSON.stringify(body);
  const r=await fetch(url,opts);
  return r.json();
}
function show(id,cls,html){const el=document.getElementById(id);el.className='flash show '+cls;el.innerHTML=html;}
function term(id,html){const el=document.getElementById(id);el.style.display='block';el.innerHTML=html;}
function loader(id,on){document.getElementById(id).style.display=on?'inline-block':'none';}

// ── NAV ──
const titles={overview:'System Overview',classify:'Data Classifier',encrypt:'Encryption Engine',access:'Access Control',monitor:'Monitoring & Audit',vuln:'Vulnerability Scanner',compliance:'Compliance Report',training:'Security Training'};
function nav(id,btn){
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach(b=>b.classList.remove('active'));
  document.getElementById('page-'+id).classList.add('active');
  btn.classList.add('active');
  document.getElementById('topbar-lbl').textContent=titles[id]||id;
  if(id==='access')loadMatrix();
  if(id==='encrypt')loadKeys();
}

// ── OVERVIEW: load users ──
async function loadUsers(){
  try{
    const users=await api('/api/users');
    let html='<div style="display:flex;flex-wrap:wrap;gap:10px">';
    users.forEach(u=>{
      html+=`<div style="background:var(--panel2);border:1px solid var(--border);border-radius:3px;padding:10px 14px;min-width:200px">
        <div style="font-family:var(--mono);font-size:12px;color:var(--cyan)">${u.user_id}</div>
        <div style="font-family:var(--mono);font-size:10px;color:var(--text2);margin-top:3px">Role: ${u.role}</div>
        <div style="font-family:var(--mono);font-size:10px;color:var(--text2)">MFA: ${u.mfa_enabled?'<span style="color:var(--green)">ENABLED</span>':'<span style="color:var(--red)">DISABLED</span>'}</div>
        <div style="font-family:var(--mono);font-size:10px;color:var(--text3)">${u.email}</div>
      </div>`;
    });
    html+='</div>';
    document.getElementById('users-panel').innerHTML=html;
  }catch(e){document.getElementById('users-panel').innerHTML='<span style="color:var(--red);font-family:var(--mono);font-size:11px">Failed to load — is Flask running?</span>';}
}
loadUsers();

// ── CLASSIFY ──
const samples=['John Doe, Email: john.doe@company.com, Phone: 555-123-4567, SSN: 123-45-6789, Salary: 75000','Card: 4111-1111-1111-1111, Bank Account: 123456789012','API_KEY = sk-abc123XYZ789secretTokenHere, DB_PASSWORD: myP@ssw0rd!'];
function loadSample(i){document.getElementById('scan-in').value=samples[i];}
async function runClassify(){
  const text=document.getElementById('scan-in').value.trim();
  if(!text){show('cls-flash','f-warn','⚠ Enter text to scan.');return;}
  loader('cls-loader',true);
  try{
    const r=await api('/api/classify','POST',{text});
    loader('cls-loader',false);
    const icons={TOP_SECRET:'🔴',CONFIDENTIAL:'🟠',INTERNAL:'🟡',PUBLIC:'🟢'};
    const cls={TOP_SECRET:'f-err',CONFIDENTIAL:'f-warn',INTERNAL:'f-warn',PUBLIC:'f-ok'}[r.classification];
    show('cls-flash',cls,icons[r.classification]+' <strong>'+r.classification+'</strong> | Detected: '+(r.detected_types.length?r.detected_types.join(', '):'None')+'<br>Encrypt required: '+(r.classification!=='PUBLIC'?'YES':'NO'));
    term('cls-term',`<span class="td">$ python data_classifier.py.scan_text(input)</span>
<span class="tc">Classification :</span> <span class="tw">${r.classification}</span>
<span class="tc">Detected types :</span> <span class="ty">${r.detected_types.join(', ')||'none'}</span>
<span class="tc">PII found      :</span> <span class="${r.pii_found?'tr':'tg'}">${r.pii_found}</span>
<span class="tc">Encrypt        :</span> <span class="${r.policy.encrypt?'tg':'td'}">${r.policy.encrypt}</span>
<span class="tc">MFA required   :</span> <span class="${r.policy.mfa_required?'tg':'td'}">${r.policy.mfa_required}</span>
<span class="tc">Scanned at     :</span> <span class="td">${r.scanned_at}</span>
<span class="tg">✓ Python scan complete.</span>`);
  }catch(e){loader('cls-loader',false);show('cls-flash','f-err','✗ Flask API error: '+e.message);}
}
async function runRedact(){
  const text=document.getElementById('red-in').value;
  try{
    const r=await api('/api/redact','POST',{text});
    show('red-flash','f-ok','✓ Redacted: <span style="color:var(--yellow)">'+r.redacted+'</span>');
  }catch(e){show('red-flash','f-err','✗ Error: '+e.message);}
}

// ── ENCRYPT ──
async function doEncrypt(){
  const pt=document.getElementById('aes-in').value;
  if(!pt){show('enc-flash','f-warn','⚠ Enter plaintext.');return;}
  loader('enc-loader',true);
  try{
    const r=await api('/api/encrypt','POST',{plaintext:pt});
    loader('enc-loader',false);
    term('enc-term',`<span class="td">$ python encryption.py AES256Encryptor.encrypt()</span>
<span class="tc">Algorithm  :</span> <span class="tw">${r.algorithm}</span>
<span class="tc">Key (${r.key_bits}b):</span> <span class="tg">${r.key_hex}</span>
<span class="tc">IV         :</span> <span class="tw">${r.iv}</span>
<span class="tc">Ciphertext :</span> <span class="ty">${r.ciphertext}</span>
<span class="tc">Checksum   :</span> <span class="tw">${r.checksum}</span>
<span class="tc">Timestamp  :</span> <span class="td">${r.timestamp}</span>
<span class="tg">✓ Python AES-256-CBC encryption complete.</span>`);
    show('enc-flash','f-ok','✓ Encrypted with real Python AES-256-CBC. SHA-256 checksum computed.');
    document.getElementById('dec-btn').disabled=false;
  }catch(e){loader('enc-loader',false);show('enc-flash','f-err','✗ '+e.message);}
}
async function doDecrypt(){
  try{
    const r=await api('/api/decrypt','POST',{});
    const t=document.getElementById('enc-term');
    t.innerHTML+=`\n<span class="td">$ python encryption.py AES256Encryptor.decrypt()</span>
<span class="tc">Checksum verify :</span> <span class="tg">${r.integrity} ✓</span>
<span class="tc">Decrypted       :</span> <span class="tw">${r.plaintext}</span>
<span class="tg">✓ Python integrity verified — data untampered.</span>`;
    show('enc-flash','f-ok','✓ Python integrity check passed. Decrypted: "'+r.plaintext+'"');
  }catch(e){show('enc-flash','f-err','✗ '+e.message);}
}
async function doRSA(){
  loader('rsa-loader',true);
  try{
    const r=await api('/api/rsa_handshake','POST',{});
    loader('rsa-loader',false);
    term('rsa-term',`<span class="td">$ python encryption.py RSAKeyManager.simulate()</span>
${r.steps.map((s,i)=>`<span class="tc">[${i+1}]</span> <span class="tw">${s}</span>`).join('\n')}
<span class="tc">AES Key    :</span> <span class="tg">${r.aes_key_sample}</span>
<span class="tc">Encrypted  :</span> <span class="ty">${r.encrypted_sample}</span>
<span class="tc">Keys match :</span> <span class="tg">${r.match} ✓</span>
<span class="tg">✓ Python RSA-2048 OAEP handshake complete.</span>`);
    show('rsa-flash','f-ok','✓ Python RSA-2048 OAEP key exchange successful. Match: '+r.match);
  }catch(e){loader('rsa-loader',false);show('rsa-flash','f-err','✗ '+e.message);}
}
async function loadKeys(){
  try{
    const keys=await api('/api/key_status');
    const colors={0:'sc',1:'sr',2:'sc'};
    let html='<div class="g3" style="margin-bottom:0">';
    keys.forEach((k,i)=>{
      const pct=k.expired?100:Math.min(100,Math.round((1-k.expires_in/(86400*30))*100));
      const col=k.expired?'sr':pct>80?'sy':'sg';
      html+=`<div class="stat ${col}">
        <span class="sn" style="font-size:15px;color:var(--${k.expired?'red':pct>80?'yellow':'green'})">${k.expired?'⚠ STALE':'✓ VALID'}</span>
        <span class="sl">${k.key_id}</span>
        <div style="font-family:var(--mono);font-size:10px;color:var(--text2);margin-top:7px">Rotations: ${k.rotations}</div>
        <div class="pbar" style="margin-top:7px"><div class="pfill" style="width:${pct}%;background:var(--${k.expired?'red':pct>80?'yellow':'green'})"></div></div>
      </div>`;
    });
    html+='</div>';
    document.getElementById('key-boxes').innerHTML=html;
  }catch(e){document.getElementById('key-boxes').innerHTML='<span style="color:var(--red);font-family:var(--mono);font-size:11px">Load failed.</span>';}
}
async function rotateKey(kid){
  try{
    const r=await api('/api/rotate_key','POST',{key_id:kid});
    show('rot-flash','f-ok','✓ Python rotated "'+kid+'". New key: '+r.new_key+' | Valid: '+r.valid);
    loadKeys();
  }catch(e){show('rot-flash','f-err','✗ '+e.message);}
}

// ── ACCESS ──
async function loadMatrix(){
  try{
    const r=await api('/api/permission_matrix');
    const perms=Object.keys(Object.values(r)[0]);
    let html='<table class="ptbl"><thead><tr><th>Role</th>'+perms.map(p=>'<th>'+p.replace('_','<br>')+'</th>').join('')+'</tr></thead><tbody>';
    Object.entries(r).forEach(([role,ps])=>{
      html+='<tr><td>'+role+'</td>'+perms.map(p=>'<td><span class="'+(ps[p]?'ck':'cx')+'">'+(ps[p]?'✓':'✗')+'</span></td>').join('')+'</tr>';
    });
    html+='</tbody></table>';
    document.getElementById('perm-matrix').innerHTML=html;
  }catch(e){}
}
let mfaOtp=null,mfaTmr=null;
async function doLogin(){
  const sel=document.getElementById('auth-usr').value.split('|');
  const uid=sel[0],pw=document.getElementById('auth-pw').value||sel[1];
  loader('login-loader',true);
  try{
    const r=await api('/api/login','POST',{username:uid,password:pw});
    loader('login-loader',false);
    if(r.error){show('login-flash','f-err','✗ PYTHON: '+r.error);return;}
    mfaOtp=r.otp;
    show('login-flash','f-ok','✓ Python PBKDF2 verified for '+r.user+'. OTP dispatched.');
    document.getElementById('otp-disp').textContent=r.otp;
    let s=30;document.getElementById('otp-secs').textContent=s+'s remaining';document.getElementById('otp-fill').style.width='100%';
    if(mfaTmr)clearInterval(mfaTmr);
    mfaTmr=setInterval(()=>{s--;document.getElementById('otp-secs').textContent=s+'s remaining';document.getElementById('otp-fill').style.width=(s/30*100)+'%';if(s<=0){clearInterval(mfaTmr);mfaOtp=null;document.getElementById('otp-disp').textContent='EXPIRED';}},1000);
  }catch(e){loader('login-loader',false);show('login-flash','f-err','✗ Flask API error.');}
}
async function doMFA(){
  const otp=document.getElementById('mfa-in').value.trim();
  loader('mfa-loader',true);
  try{
    const r=await api('/api/verify_mfa','POST',{otp});
    loader('mfa-loader',false);
    if(r.error){show('mfa-flash','f-err','✗ PYTHON: '+r.error);return;}
    clearInterval(mfaTmr);
    document.getElementById('otp-disp').textContent='VERIFIED';
    show('mfa-flash','f-ok','✓ Python TOTP verified — Welcome '+r.user+' ('+r.role+'). Token: '+r.token+' | Session: '+r.session_minutes+'min');
  }catch(e){loader('mfa-loader',false);show('mfa-flash','f-err','✗ Flask API error.');}
}
async function checkPerm(){
  const role=document.getElementById('rbac-r').value,perm=document.getElementById('rbac-p').value;
  try{
    const r=await api('/api/check_permission','POST',{role,permission:perm});
    show('rbac-flash',r.allowed?'f-ok':'f-err',r.allowed?'✓ PYTHON GRANT — '+role+' has '+perm+'. All perms: '+r.all_permissions.join(', '):'✗ PYTHON DENY — '+role+' lacks '+perm+'.');
  }catch(e){show('rbac-flash','f-err','✗ Error');}
}

// ── MONITOR ──
let chainEntries=[];
async function logEvt(type,user,action,res,status){
  try{
    const r=await api('/api/log_event','POST',{event_type:type,user_id:user,action,resource:res,status});
    const t=document.getElementById('audit-term');
    const now=new Date().toISOString().slice(11,19);
    const col=status==='SUCCESS'?'tg':status==='DENIED'?'tr':'ty';
    const icon=status==='SUCCESS'?'✓':status==='DENIED'?'✗':'⚠';
    t.innerHTML+=`<span class="td">[${now}]</span> <span class="${col}">${icon} [${type}] ${user} → ${action} (${res})</span>\n<span class="td">  hash: ${r.chain_hash}</span>\n`;
    t.scrollTop=t.scrollHeight;
    chainEntries.push({type,user,action,hash:r.chain_hash});
    updateChain();
  }catch(e){}
}
function updateChain(){
  let html='<div class="cblk"><div class="cbn">GENESIS</div><div class="cbh">a4f9c2b1...</div></div>';
  chainEntries.slice(-5).forEach((e,i)=>{html+='<div class="carrow">→</div><div class="cblk"><div class="cbn">#'+(i+1)+' '+e.type+'</div><div class="cbh">'+e.hash.slice(0,12)+'</div></div>';});
  document.getElementById('chain-vis').innerHTML=html;
}
async function verifyChain(){
  try{
    const r=await api('/api/verify_chain');
    show('chain-flash',r.verified?'f-ok':'f-err',r.verified?'✓ Python verified: '+r.total_entries+' entries intact. No tampering detected.':'✗ CHAIN BROKEN — tampering detected!');
  }catch(e){show('chain-flash','f-err','✗ Flask error');}
}
async function simAttack(type){
  try{
    const r=await api('/api/simulate_attack','POST',{type});
    const box=document.getElementById('ids-box');
    if(box.querySelector('[style*="text-align:center"]'))box.innerHTML='';
    r.alerts.forEach(a=>{
      const cls=a.severity==='CRITICAL'?'ac':a.severity==='HIGH'?'ah':'am';
      box.innerHTML='<div class="alert-item '+cls+'"><div><div style="margin-bottom:2px"><strong>['+a.alert_id+'] '+a.severity+'</strong> — '+a.category+'</div><div style="opacity:.75">'+a.description+'</div></div></div>'+box.innerHTML;
    });
    if(r.alerts.length===0){box.innerHTML='<div class="alert-item am"><div>Simulation ran — no new threshold alerts. Total active: '+r.total_alerts+'</div></div>'+box.innerHTML;}
  }catch(e){}
}

// ── VULN ──
async function runVuln(){
  loader('vuln-loader',true);
  try{
    const r=await api('/api/vuln_scan','POST',{
      tls_version:document.getElementById('tls').value,
      key_age:parseInt(document.getElementById('kage').value)||5,
      pw_min_length:parseInt(document.getElementById('pwlen').value)||12,
      mfa_enabled:document.getElementById('mfaen').value==='true'
    });
    loader('vuln-loader',false);
    document.getElementById('vuln-out').style.display='block';
    const rc=r.overall_risk==='CRITICAL'?'var(--red)':r.overall_risk==='HIGH'?'var(--orange)':r.overall_risk==='MEDIUM'?'var(--yellow)':'var(--green)';
    document.getElementById('vuln-stats').innerHTML=`
      <div class="stat ${r.overall_risk==='LOW'?'sg':r.overall_risk==='MEDIUM'?'sy':'sr'}"><span class="sn" style="color:${rc}">${r.overall_risk}</span><span class="sl">Risk Level</span></div>
      <div class="stat sr"><span class="sn" style="color:var(--red)">${r.critical}</span><span class="sl">Critical</span></div>
      <div class="stat" style="border-color:var(--orange)"><span class="sn" style="color:var(--orange)">${r.high}</span><span class="sl">High</span></div>
      <div class="stat sy"><span class="sn" style="color:var(--yellow)">${r.medium}</span><span class="sl">Medium</span></div>`;
    document.getElementById('vuln-ph').innerHTML='<span class="ph-dot"></span>'+(r.total_findings?'⚠ '+r.total_findings+' Findings':'✓ No Vulnerabilities');
    document.getElementById('vuln-body').innerHTML=r.total_findings===0?'<div class="flash show f-ok">✓ Python VulnerabilityScanner: All checks passed. System compliant.</div>':r.findings.map(f=>`<div class="vi"><span class="vtag v${f.severity.slice(0,2).toLowerCase()}">${f.severity}</span><div><div style="font-family:var(--mono);font-size:12px;color:#fff;margin-bottom:3px">${f.check}</div><div style="font-size:12px;color:var(--text2)">${f.detail}</div><div style="font-size:12px;color:var(--cyan);margin-top:3px">→ ${f.remediation}</div></div></div>`).join('');
  }catch(e){loader('vuln-loader',false);}
}

// ── QUIZ ──
const qs=[
  {q:'What does MFA stand for and what does it protect against?',opts:['Multi-Factor Authentication — protects against stolen passwords','Multiple File Access — protects data loss','Main Firewall Auth — protects DDoS','Managed Frequency Alerts'],ans:0,exp:'MFA adds a second step so stolen passwords alone cannot grant access.'},
  {q:'Which algorithm is used for data-at-rest encryption in CyberShield?',opts:['MD5 hashing','AES-256-CBC','ROT13 cipher','BASE64 encoding'],ans:1,exp:'AES-256-CBC is the industry standard symmetric cipher. MD5/BASE64/ROT13 offer no real security.'},
  {q:'Under GDPR, how long do you have to notify authorities after a data breach?',opts:['7 days','30 days','72 hours','6 months'],ans:2,exp:'GDPR Article 33: notify within 72 hours of discovering a breach that risks individuals.'},
  {q:'What does RBAC stand for?',opts:['Random Backup Access Control','Role-Based Access Control','Remote Browser Access Control','Rule-Based Application Control'],ans:1,exp:'RBAC assigns permissions to roles, making access auditable and scalable across the organization.'},
  {q:'Why does CyberShield use SHA-256 hash chaining in the audit log?',opts:['To compress logs','To encrypt log content','To detect any tampering with entries','To speed up queries'],ans:2,exp:'Each entry hashes the previous. Any modification breaks the chain — tampering is mathematically provable.'}
];
let qi=0,qsc=0,qans=false;
function startQuiz(){qi=0;qsc=0;qans=false;document.getElementById('q-area').style.display='block';document.getElementById('q-end').style.display='none';renderQ();}
function renderQ(){
  if(qi>=qs.length){showEnd();return;}
  qans=false;const q=qs[qi];
  document.getElementById('qnum').textContent=qi+1;
  document.getElementById('qprog').style.width=(qi/qs.length*100)+'%';
  document.getElementById('qtxt').textContent=q.q;
  document.getElementById('qsc').textContent=qsc;document.getElementById('qmx').textContent=qi;
  document.getElementById('qflash').className='flash';
  document.getElementById('qopts').innerHTML=q.opts.map((o,i)=>'<button class="qopt" onclick="ansQ('+i+')">'+o+'</button>').join('');
}
function ansQ(i){
  if(qans)return;qans=true;const q=qs[qi];
  document.querySelectorAll('.qopt')[q.ans].classList.add('correct');
  const f=document.getElementById('qflash');
  if(i===q.ans){qsc++;document.querySelectorAll('.qopt')[i].classList.add('correct');f.className='flash show f-ok';f.innerHTML='✓ Correct! '+q.exp;}
  else{document.querySelectorAll('.qopt')[i].classList.add('wrong');f.className='flash show f-err';f.innerHTML='✗ Incorrect. '+q.exp;}
  document.getElementById('qsc').textContent=qsc;document.getElementById('qmx').textContent=qi+1;
  setTimeout(()=>{qi++;renderQ();},2500);
}
function showEnd(){
  document.getElementById('q-area').style.display='none';document.getElementById('q-end').style.display='block';
  const p=Math.round(qsc/qs.length*100);
  document.getElementById('qfin').textContent=qsc+' / '+qs.length+' ('+p+'%)';
  document.getElementById('qfb').textContent=p===100?'PERFECT — Security Expert!':p>=80?'EXCELLENT — Highly aware':p>=60?'GOOD — Review weak areas':'NEEDS IMPROVEMENT';
}
startQuiz();
</script>
</body>
</html>
