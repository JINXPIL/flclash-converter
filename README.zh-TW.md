<p align="center">
  <a href="/README.en.md">🇺🇸 English</a> •
  <a href="/README.md">🇷🇺 Русский</a> •
  <a href="/README.zh.md">🇨🇳 简体中文</a> •
  <a href="/README.zh-TW.md"><b>🇹🇼 繁體中文</b></a> •
  <a href="/README.fa.md">🇮🇷 فارسی</a> •
  <a href="/README.es.md">🇪🇸 Español</a>
</p>

<p align="center">
  <a href="https://github.com/jinxpil/flclash-converter/releases">
    <img src="https://img.shields.io/github/v/release/jinxpil/flclash-converter?style=for-the-badge&logo=github&color=181717" alt="Release">
  </a>
  <a href="https://github.com/jinxpil/flclash-converter/releases/latest">
    <img src="https://img.shields.io/github/downloads/jinxpil/flclash-converter/total?style=for-the-badge&color=brightgreen" alt="Downloads">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License">
  </a>
  <a href="https://github.com/jinxpil/flclash-converter/stargazers">
    <img src="https://img.shields.io/github/stars/jinxpil/flclash-converter?style=for-the-badge&color=yellow" alt="Stars">
  </a>
</p>

<h1 align="center">⚡ Network Builder v17.05 ULTRA</h1>

<p align="center">
  <b>一款極其強大且 100% 本地運行的 Web 工具，用於管理海量代理伺服器資料庫。</b><br>
  <i>為 FlClash、Exclave、Sing-box 和 Clash Meta 提供解析、轉換和深度優化的配置。</i>
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
  🤖 <b>也請關注我的第二個專案：</b><br>
  👉 <a href="https://github.com/JINXPIL/json-yaml-ai"><b>JSON-YAML-AI</b></a> 👈
</p>

> [!IMPORTANT]
> **零信任與隱私優先。** 所有運算均在您的瀏覽器中嚴格本地執行。沒有任何數據會離開您的裝置。本工具僅為教育目的而創建，用於深入研究網路協議。

> [!WARNING]
> **注意：YAML 訂閱和超時 (Timeout) 問題：**
> 許多 VPN 提供商故意（或由於 API 設定不當）限制第三方客戶端匯出訂閱。伺服器可能成功加載到您的列表中，但在嘗試連線時會進入無限超時。
> 💡 **如何排查原因：** 如果您獲取同一個節點的「原始」連結（例如 `vless://...` 或 JSON 程式碼），將其手動添加為本地設定檔，並且 **它可以正常運作** —— 那麼問題 100% 出在提供商那邊。這意味著在嘗試更新訂閱時，他們的伺服器根據 `User-Agent` 攔截了客戶端的請求。在其他情況下，超時可能是由於防火牆對協議特徵進行了精準封鎖。

---

### 📸 介面展示 (ULTRA Design)

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

### 🔥 17.05 ULTRA 版本更新了什麼？ (高併發完美版)

* 🌐 **全面協議擴展：** 增加對 **VMess、Hysteria2 (hy2)、Shadowsocks (SS) 和 ShadowsocksR (SSR)** 的完整解析支援。
* 🚀 **極限效能 (HighLoad)：** 引入非同步分塊處理與 `Set` 字典。DOM 虛擬化技術讓您在毫秒內加載並去重 **250,000+ 個節點**，瀏覽器絲滑不卡頓！
* 🛡️ **防彈級 YAML 淨化器：** 工業級準入控制。腳本會自動清理公共節點庫中的垃圾（不可見 ASCII 字元、虛假的 `2022-blake3` 加密、空密碼），確保 100% 穩定匯入 Mihomo。
* ⚙️ **徹底解決超時問題：** YAML 生成器已根據 Mihomo 嚴格標準重寫（添加了 `alpn`、`skip-cert-verify: true`、`servername` 以及改進的 Fake-IP DNS 路由）。
* 🎨 **全新 UI/UX：** 獨立的明/暗主題（支援分別儲存自訂顏色），以及**「訂閱模式」開關**，可將 RAW 連結（Pastebin/GitHub）直接嵌入到 `proxy-providers` 模組中。

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

### 🎯 配置與路由 (預設)

為了避免在頁面上堆砌大量程式碼，所有現成的預設配置都已提取到獨立的儲存庫文件中。

* 🌐 **Happ 分流配置** — 透過 `routing.happ.su` 建構的優化規則預設（繞過限制、AdBlock等）。**嚴格**專為 Happ 客戶端設計。
    * 📄 配置文件連結：[`./rus_vp_happ.json`](./rus_vp_happ.json)
    * 🔗 客戶端匯入連結：`https://raw.githubusercontent.com/JINXPIL/flclash-converter/refs/heads/main/rus_vp_happ.json`
* 🛠️ **優化的 YAML 配置 (Mihomo/Clash)** — v79.0 Ultimate，具備嚴格的 TLS 瀏覽器指紋和防 DPI 嗅探保護。
    * 📄 配置文件連結：[`./GL_Crimea_ipv6_yan(9.35).yml`](./GL_Crimea_ipv6_yan(9.35).yml)
    * 🔗 客戶端匯入連結：`https://raw.githubusercontent.com/JINXPIL/flclash-converter/refs/heads/main/GL_Crimea_ipv6_yan(9.35).yml`

---
> [!NOTE]
> 目前，像 **NekoBox** 和 **NekoRay** 這類熱門客戶端已被認為是過時的。建議遷移到基於最新的 **sing-box** 和 **Xray** 核心的現代優化替代方案（例如 **Exclave**，它完全復刻了 NekoBox 的介面，或者 **Incy**）。

<details>
<summary><b>🤖 Android</b></summary>

* [v2RayTun](https://v2raytun.com/) — 基於 Xray Core 的高速、安全客戶端。
* [FlClash](https://github.com/chen08209/FlClash) — 優秀的跨平台客戶端。
* [Incy](https://incy.cc/) — 支援一鍵匯入的現代快速客戶端。
* [Happ](https://www.happ.su/main) — 方便管理伺服器列表的代理工具。
* [Exclave](https://github.com/ExclaveNetwork/Exclave) — NekoBox 的現代替代品，介面熟悉。
* [Sing-box](https://github.com/SagerNet/sing-box) — 用於高級配置的官方純淨核心。
* [Hiddify App](https://github.com/hiddify/hiddify-app) — 適用於任何配置類型的通用客戶端。
* [v2rayNG](https://github.com/2dust/v2rayNG) — 基於 Xray 核心的穩定經典方案。
* [Karing](https://github.com/KaringX/karing) — 功能豐富的圖形介面。
* [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
* ~~[NekoBox For Android](https://github.com/MatsuriDayo/NekoBoxForAndroid)~~ *(已過時)*
</details>

<details>
<summary><b>🍏 iOS</b></summary>

* [v2RayTun](https://v2raytun.com/) — 基於 Xray Core 的高速、安全客戶端。
* [Incy](https://incy.cc/) — App Store 上出色的現代客戶端。
* [Happ](https://www.happ.su/main) — 舒適的代理工具。
* [Karing](https://apps.apple.com/us/app/karing/id6472431552)
* [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
* [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)
* [Clash Lite](https://apps.apple.com/us/app/clash-lite/id6761357475)
* [V2Lite VPN](https://apps.apple.com/us/app/v2lite-vpn-super-vpn-proxy/id6444585377)
</details>

<details>
<summary><b>💻 Desktop (Win/Mac/Linux)</b></summary>

* [v2RayTun](https://v2raytun.com/) — 基於 Xray Core 的高速、安全客戶端。
* [Happ](https://www.happ.su/main) — 跨平台桌面版本。
* [v2rayN](https://github.com/2dust/v2rayN) — Windows 上強大的可定制客戶端。
* [FlClash](https://github.com/chen08209/FlClash) — 極簡快速的 GUI。
* [Karing](https://github.com/KaringX/karing)
* [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)
* ~~[NekoRay](https://github.com/MatsuriDayo/nekoray)~~ *(已過時)*
</details>

---

### 🛡️ 替代工具 (DPI 繞過)

*如果標準 VPN 協議被您的 ISP 完全封鎖，請使用本地的深度包檢測繞過工具：*

* [Zapret](https://github.com/bol-van/zapret) — 系統級別最強大、最靈活的深度 DPI 繞過工具。
* [Zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) — 針對特定流行服務優化的現成腳本。
* [ByeByeDPI](https://github.com/romanvht/ByeByeDPI) — 久經考驗的經典 Android 本地運行方案。

---

### ⭐ 支援項目

**如果 Network Builder ULTRA 幫助到了您，請不要忘記點個 Star！這將激勵我們繼續開發。** :star2:

[![Star History Chart](https://api.star-history.com/svg?repos=jinxpil/flclash-converter&type=Date)](https://star-history.com/#jinxpil/flclash-converter&Date)
