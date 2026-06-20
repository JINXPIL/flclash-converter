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

<h1 align="center">⚡ Network Builder v17.04 ULTRA</h1>

<p align="center">
  <b>極其強大且 100% 本地的 Web 工具，用於管理龐大的代理伺服器資料庫。</b><br>
  <i>解析、轉換並深度優化 FlClash、Exclave、Sing-box 和 Clash Meta 的配置。</i>
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

> [!IMPORTANT]
> **零信任與隱私至上。** 所有計算均在您的瀏覽器中嚴格本地執行。沒有任何資料會離開您的裝置。該工具僅用於深入研究網路協議和路由原理的教育目的。

> [!WARNING]
> **注意：YAML 訂閱和超時 (Timeout) 問題：**
> 許多 VPN 提供商在匯出訂閱時故意（或由於 API 配置不當）限制第三方客戶端的操作。節點可能會成功載入到您的列表中，但在嘗試連接時，它們會進入無限超時。
> 💡 **如何排查問題：** 如果您獲取同一節點的「原始」連結（例如，`vless://...` 或 JSON 代碼），將其作為本地設定檔手動添加，並且**它可以正常工作** — 則問題 100% 出在提供商端。這意味著當嘗試更新訂閱時，他們的伺服器透過 `User-Agent` 攔截了客戶端的請求。在其他情況下，超時可能是由審查防火牆 (DPI) 針對協議特徵的定向攔截引起的。

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

### 🔥 版本 17.02 ULTRA 有什麼新功能？

* 🚀 **極限解析引擎：** 全面優化程式碼，可同時處理 **10,000 多個節點**。即使在海量資料下也能保持流暢的介面。
* 🌍 **ULTRA 本地化：** 深度支援 6 種語言。介面和系統通知現已完全適配。
* 🛡️ **QuotaGuard 系統：** 防止瀏覽器記憶體溢出的智能保護。處理任何體積的配置都不會導致分頁崩潰。
* 🧠 **智能去重過濾器：** 透過 `IP:Port` 自動比較伺服器並刪除垃圾和重複項，僅保留唯一節點。
* 🛠️ **精細診斷：** 更新的事件日誌並修復了語法錯誤 (SyntaxError fix)，確保完美穩定運行。

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

### 🎯 配置與路由規則 (預設)

為了不讓頁面堆滿代碼，所有現成的預設配置都已提取到獨立的倉庫檔案中。

* 🌐 **Happ 分流規則** — 優化的規則預設（克里米亞、SevSU、繞過限制、AdBlock），透過 `routing.happ.su` 構建。**嚴格**僅供 Happ 客戶端使用。
    * 📄 配置檔案連結：[`./rus_vp_happ.json`](./rus_vp_happ.json)
    * 🔗 客戶端導入連結：`https://raw.githubusercontent.com/JINXPIL/flclash-converter/refs/heads/main/rus_vp_happ.json`
* 🛠️ **Mihomo/Clash 優化配置 (YAML)** — v79.0 Ultimate，具有嚴格的瀏覽器 TLS 指紋和防 DPI 分析保護。
    * 📄 配置檔案連結：[`./GL_Crimea_ipv6_yan(9.35).yml`](./GL_Crimea_ipv6_yan(9.35).yml)
    * 🔗 客戶端導入連結：`https://raw.githubusercontent.com/JINXPIL/flclash-converter/refs/heads/main/GL_Crimea_ipv6_yan(9.35).yml`

---

### 📥 推薦客戶端 (ULTRA 兼容)

> [!NOTE]
> 注意：**NekoBox** 和 **NekoRay** 等流行客戶端目前被視為已過時。強烈建議切換到基於 **sing-box** 和 **Xray** 核心的現代優化替代方案。

<details>
<summary><b>🤖 Android</b></summary>

* [v2RayTun](https://v2raytun.com/) — 基於 Xray Core 的高速安全客戶端。
* [FlClash](https://github.com/chen08209/FlClash) — 跨平台客戶端。
* [Incy](https://incy.cc/) — 具有一鍵匯入功能的現代快速客戶端。
* [Happ](https://www.happ.su/main) — 用於方便管理伺服器列表的代理實用程式。
* [Exclave](https://github.com/ExclaveNetwork/Exclave) — NekoBox 的現代替代品。
* [Sing-box](https://github.com/SagerNet/sing-box) — 官方純淨核心，適合高級配置。
* [Hiddify App](https://github.com/hiddify/hiddify-app) — 通用客戶端。
* [v2rayNG](https://github.com/2dust/v2rayNG) — 經典穩定的 Xray 解決方案。
* [Karing](https://github.com/KaringX/karing) — 功能豐富的 GUI。
* [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
* ~~[NekoBox For Android](https://github.com/MatsuriDayo/NekoBoxForAndroid)~~ *(已過時)*
</details>

<details>
<summary><b>🍏 iOS</b></summary>

* [v2RayTun](https://v2raytun.com/) — 基於 Xray Core 的高速安全客戶端。
* [Incy](https://incy.cc/) — App Store 中的優秀現代客戶端。
* [Happ](https://www.happ.su/main) — 舒適的代理工具。
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
* [v2rayN](https://github.com/2dust/v2rayN) — 適用於 Windows 的強大可定制客戶端。
* [FlClash](https://github.com/chen08209/FlClash) — 極簡快速的 GUI。
* [Karing](https://github.com/KaringX/karing)
* [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)
* ~~[NekoRay](https://github.com/MatsuriDayo/nekoray)~~ *(已過時)*
</details>

---

### 🛡️ 替代工具 (DPI 繞過)

*如果標準 VPN 協議被您的 ISP 或防火牆完全封鎖，請使用本地深度封包檢測繞過工具：*

* [Zapret](https://github.com/bol-van/zapret) — 系統級最強大靈活的深度繞過 DPI 工具。
* [Zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) — 針對特定流行服務的優化腳本。
* [ByeByeDPI](https://github.com/romanvht/ByeByeDPI) — 適用於 Windows 的成熟本地執行解決方案。

---

### ⭐ 支持項目

**如果 Network Builder ULTRA 對您有幫助，請不要忘記點個星 (Star)！這能激勵項目進一步發展。** :star2:

[![Stargazers over time](https://starchart.cc/jinxpil/flclash-converter.svg?variant=adaptive)](https://starchart.cc/jinxpil/flclash-converter)
