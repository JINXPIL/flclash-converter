<p align="center">
  <a href="/README.en.md">🇺🇸 English</a> •
  <a href="/README.md">🇷🇺 Русский</a> •
  <a href="/README.zh.md">🇨🇳 简体中文</a> •
  <a href="/README.zh-TW.md"><b>🇹🇼 繁體中文</b></a> •
  <a href="/README.fa.md">🇮🇷 فارسی</a> •
  <a href="/README.es.md">🇪🇸 Español</a>
</p>

<p align="center">
  <a href="https://github.com/JINXPIL/flclash-converter/releases">
    <img src="https://img.shields.io/github/v/release/JINXPIL/flclash-converter?style=for-the-badge&logo=github&color=181717" alt="Release">
  </a>
  <a href="https://github.com/JINXPIL/flclash-converter/releases/latest">
    <img src="https://img.shields.io/github/downloads/JINXPIL/flclash-converter/total?style=for-the-badge&color=brightgreen" alt="Downloads">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License">
  </a>
  <a href="https://github.com/JINXPIL/flclash-converter/stargazers">
    <img src="https://img.shields.io/github/stars/JINXPIL/flclash-converter?style=for-the-badge&color=yellow" alt="Stars">
  </a>
</p>

<h1 align="center">⚡ Network Builder v17.05 ULTRA</h1>

<p align="center">
  <b>極其強大的 100% 本地 Web 工具，用於管理海量代理伺服器資料庫。</b><br>
  <i>為 FlClash、Exclave、Sing-box 和 Clash Meta 提供配置解析、轉換和深度優化。</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white" alt="JSON">
  <img src="https://img.shields.io/badge/YAML-CB171E?style=for-the-badge&logo=yaml&logoColor=white" alt="YAML">
</p>

<p align="center">
  <a href="https://jinxpil.github.io/flclash-converter/">
    <img src="https://img.shields.io/badge/🚀_打開_ULTRA_版本-0052FF?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Open Web Version">
  </a>
</p>

<p align="center">
  🤖 <b>另請關注我的第二個專案：</b><br>
  👉 <a href="https://github.com/JINXPIL/json-yaml-ai"><b>JSON-YAML-AI</b></a> 👈
</p>

> [!IMPORTANT]
> **零信任與隱私至上。** 所有計算嚴格在您的瀏覽器本地進行。沒有任何資料會離開您的裝置。該工具專為教育目的和深度網路協議分析而建立。

> [!WARNING]
> **關於 YAML 訂閱和超時 (Timeout) 的警告：**
> 許多 VPN 供應商在匯出訂閱時故意（或由於 API 設定不當）限制第三方客戶端。伺服器可能成功載入您的列表中，但在嘗試連線時會導致無限超時。
> 💡 **如何檢查問題所在：** 如果您獲取同一節點的「原始」連結（例如 `vless://...` 或 JSON 程式碼），將其作為本地設定檔手動新增，並且 **它可以正常運作** — 那麼問題 100% 出在供應商那邊。這意味著他們的伺服器在嘗試更新訂閱時透過 `User-Agent` 阻止了您的客戶端請求。在其他情況下，超時可能是由於您的 ISP (DPI) 針對協議簽名進行了定向封鎖。

---

### 📸 介面 (ULTRA Design)

<p align="center">
  <a href="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/Gemini_Generated_Image_w0ysv7w0ysv7w0ys.png" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/Gemini_Generated_Image_w0ysv7w0ysv7w0ys.png">
      <img alt="JSON to YAML" src="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/Gemini_Generated_Image_w0ysv7w0ysv7w0ys.png" width="48%">
    </picture>
  </a>
  
  <a href="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/firefox_DHEZPiG4oz.png" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/firefox_DHEZPiG4oz.png">
      <img alt="Converter" src="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/firefox_DHEZPiG4oz.png" width="48%">
    </picture>
  </a>
</p>

---

### 🔥 17.05 ULTRA 版本有什麼新功能？ (The HighLoad Perfection)

* 🌐 **全球協議擴展：** 增加了對 **VMess, Hysteria2 (hy2), Shadowsocks (SS) 和 ShadowsocksR (SSR)** 的完整解析支援。
* 🚀 **極限性能 (HighLoad)：** 引入了非同步分塊和 `Set` 字典。DOM 虛擬化允許在幾毫秒內載入和去重 **250,000+ 個節點**，而不會使瀏覽器崩潰！
* 🛡️ **穿甲級 YAML 淨化器：** 工業級面部識別控制。腳本自動銷毀公共列表中的垃圾（不可見的 ASCII 字元，偽造的 `2022-blake3` 密碼，空密碼），並保證 100% 穩定匯入 Mihomo。
* ⚙️ **戰勝超時：** YAML 生成器已被重寫以滿足嚴格的 Mihomo 標準（新增了 `alpn`, `skip-cert-verify: true`, `servername` 和增強的 Fake-IP DNS）。
* 🎨 **全新的 UI/UX：** 獨立的淺色/深色主題以及獨立的顏色儲存，以及一個 **「訂閱模式」切換開關**，用於將 RAW 連結（Pastebin/GitHub）直接嵌入到 `proxy-providers` 區塊中。

---

### 🔌 支援的協議

<table align="center" width="100%">
  <tr>
    <td align="center">🛡️ <b>VLESS / VMess</b><br>Reality & Vision</td>
    <td align="center">⚡ <b>Hysteria 2</b><br>Brutal Speed</td>
    <td align="center">🐎 <b>Trojan</b><br>Stealth Protocol</td>
  </tr>
  <tr>
    <td align="center">🔒 <b>WireGuard</b><br>Native VPN</td>
    <td align="center">🌐 <b>SS / SSR</b><br>Shadowsocks</td>
    <td align="center">🔌 <b>TUIC / Socks5 / HTTP</b><br>Full Support</td>
  </tr>
</table>

---

### 🎯 開箱即用的預設

為了避免頁面充滿程式碼，所有現成的預設都已移至以客戶端命名的單獨資料夾中。

<table width="100%">
<thead><tr><th align="left">平台</th><th align="left">配置</th><th align="left">匯入連結</th></tr></thead>
<tbody>
<tr>
  <td><b>Happ (Routing)</b></td>
  <td>專為俄羅斯地區優化，內建廣告攔截</td>
  <td>
    <a href="https://jinxpil.github.io/flclash-converter/happ.html">⚡ 快速安裝 (一鍵)</a><br>
    <a href="https://raw.githubusercontent.com/JINXPIL/flclash-converter/main/HAPP/DEFAULT.json">📄 查看程式碼 (JSON)</a>
  </td>
</tr>
<tr>
  <td><b>INCY (Routing)</b></td>
  <td>專為俄羅斯地區優化，內建廣告攔截</td>
  <td>
    <a href="https://jinxpil.github.io/flclash-converter/incy.html">⚡ 快速安裝 (一鍵)</a><br>
    <a href="https://raw.githubusercontent.com/JINXPIL/flclash-converter/main/INCY/DEFAULT.json">📄 查看程式碼 (JSON)</a>
  </td>
</tr>
<tr>
  <td><b>Mihomo / Clash Meta</b></td>
  <td>v79.0 Ultimate (DPI 規避, 嚴格的 TLS)</td>
  <td><a href="https://raw.githubusercontent.com/JINXPIL/flclash-converter/main/MIHOMO/ULTIMATE.yml">🔗 匯入 YML 配置</a></td>
</tr>
</tbody>
</table>

---

### 🚦 路由規則內部邏輯

可靠的「外科手術式」分流，以便所需資源無延遲載入，而受阻的資源變得可存取。

<table width="100%">
<tbody>
<tr>
  <td>🔴 <b>BLOCK (阻止)</b></td>
  <td>廣告，追蹤器，遙測（節省伺服器流量和設備電池）。</td>
</tr>
<tr>
  <td>🟢 <b>DIRECT (直連)</b></td>
  <td>本地 ISP，國內銀行，政府服務（理想的低延遲，銀行不會因可疑 IP 封禁）。</td>
</tr>
<tr>
  <td>🔵 <b>PROXY (代理)</b></td>
  <td>YouTube, Instagram, ChatGPT, 國外 CDN 和所有其他被封鎖的流量。</td>
</tr>
</tbody>
</table>

---

### 🛡️ DNS 設定

<table width="100%">
<thead><tr><th align="center">目的</th><th align="left">伺服器</th><th align="left">原因</th></tr></thead>
<tbody>
<tr>
  <td align="center">🏠 <b>DIRECT (國內)</b></td>
  <td><a href="https://dns.yandex.ru/">Yandex DNS</a> <code>77.88.8.8</code></td>
  <td>快速解析內部資源，本地延遲低，無需啟動 VPN 即可運作。</td>
</tr>
<tr>
  <td align="center">🌍 <b>PROXY (國外)</b></td>
  <td><a href="https://developers.cloudflare.com/1.1.1.1/">Cloudflare</a> / <a href="https://developers.google.com/speed/public-dns/">Google</a></td>
  <td>代理流量的可靠解析，防止本地 ISP 的 DNS 欺騙。</td>
</tr>
</tbody>
</table>

---
> [!NOTE]
> 諸如 **NekoBox** 和 **NekoRay** 之類的流行客戶端目前已被視為過時。建議切換到基於最新 **sing-box** 和 **Xray** 核心的現代和優化替代方案（例如，完全複製 NekoBox 介面的 **Exclave**，或 **Incy**）。

<details>
<summary><b>🤖 Android</b></summary>

* [v2RayTun](https://v2raytun.com/) — 基於 Xray Core 的高速安全客戶端。
* [FlClash](https://github.com/chen08209/FlClash) — 主要的跨平台客戶端。
* [Incy](https://incy.cc/) — 現代，快速的客戶端，支援一鍵匯入。
* [Happ](https://www.happ.su/main) — 用於方便管理伺服器列表的代理實用程式。
* [Exclave](https://github.com/ExclaveNetwork/Exclave) — NekoBox 的現代替代品，具有熟悉的 UI。
* [Sing-box](https://github.com/SagerNet/sing-box) — 官方純淨核心，用於高級配置。
* [Hiddify App](https://github.com/hiddify/hiddify-app) — 適用於任何配置類型的通用客戶端。
* [v2rayNG](https://github.com/2dust/v2rayNG) — Xray 核心的穩定經典解決方案。
* [Karing](https://github.com/KaringX/karing) — 功能豐富的 GUI。
* [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
* ~~[NekoBox For Android](https://github.com/MatsuriDayo/NekoBoxForAndroid)~~ *(已棄用)*
</details>

<details>
<summary><b>🍏 iOS</b></summary>

* [v2RayTun](https://v2raytun.com/) — 基於 Xray Core 的高速安全客戶端。
* [Incy](https://incy.cc/) — App Store 中優秀的現代客戶端。
* [Happ](https://www.happ.su/main) — 舒適的代理實用程式。
* [Karing](https://apps.apple.com/us/app/karing/id6472431552)
* [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
* [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)
* [Clash Lite](https://apps.apple.com/us/app/clash-lite/id6761357475)
* [V2Lite VPN](https://apps.apple.com/us/app/v2lite-vpn-super-vpn-proxy/id6444585377)
</details>

<details>
<summary><b>💻 Desktop (Win/Mac/Linux)</b></summary>

* [v2RayTun](https://v2raytun.com/) — 基於 Xray Core 的高速安全客戶端。
* [Happ](https://www.happ.su/main) — 跨平台桌面版本。
* [v2rayN](https://github.com/2dust/v2rayN) — 適用於 Windows 的強大可客製化客戶端。
* [FlClash](https://github.com/chen08209/FlClash) — 極簡且快速的 GUI。
* [Karing](https://github.com/KaringX/karing)
* [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)
* ~~[NekoRay](https://github.com/MatsuriDayo/nekoray)~~ *(已棄用)*
</details>

---

### 🛡️ 替代工具 (DPI 繞過)

*如果標準 VPN 協議被您的 ISP 或 DPI 完全封鎖，請使用本地深度封包檢測繞過工具：*

* [Zapret](https://github.com/bol-van/zapret) — 在系統層面進行深度 DPI 繞過的最強大，最靈活的工具。
* [Zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) — 針對特定熱門服務優化和配置的現成腳本。
* [ByeByeDPI](https://github.com/romanvht/ByeByeDPI) — 在 Android 上本地執行的經過驗證的經典解決方案。

---

### ⭐ 支援該專案

**如果 Network Builder ULTRA 幫助了您，請不要忘記留下一顆星！這會激發該專案的進一步發展。** :star2:

[![Star History Chart](https://api.star-history.com/svg?repos=JINXPIL/flclash-converter&type=Date)](https://star-history.com/#JINXPIL/flclash-converter&Date)