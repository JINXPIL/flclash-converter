
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
    <img src="https://img.shields.io/github/v/release/jinxpil/flclash-converter.svg?style=for-the-badge&color=blue" alt="Release">
  </a>
  <a href="https://github.com/jinxpil/flclash-converter/releases/latest">
    <img src="https://img.shields.io/github/downloads/jinxpil/flclash-converter/total.svg?style=for-the-badge&color=brightgreen" alt="Downloads">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge" alt="License">
  </a>
  <a href="https://github.com/jinxpil/flclash-converter/stargazers">
    <img src="https://img.shields.io/github/stars/jinxpil/flclash-converter.svg?style=for-the-badge&color=yellow" alt="Stars">
  </a>
</p>

<h1 align="center">⚡ Network Builder v17.02 ULTRA</h1>

<p align="center">
  <b>極其強大且 100% 本地化的網路工具，用於管理龐大的代理伺服器資料庫。</b><br>
  <i>解析、轉換並深度優化 FlClash、Exclave、Sing-box 和 Clash Meta 的配置。</i>
</p>

<p align="center">
  <a href="https://jinxpil.github.io/flclash-converter/">
    <img src="https://img.shields.io/badge/🚀_打開_ULTRA--版本-0052FF?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Open Web Version">
  </a>
</p>

> [!IMPORTANT]
> **零信任與隱私至上。** 所有計算均在您的瀏覽器中嚴格本地執行。任何資料都不會離開您的設備。該工具僅用於教育目的，旨在深度研究網路協定。

> [!WARNING]
> **注意：YAML 訂閱與連線逾時 (Timeout) 問題：**
> 許多 VPN 提供商在匯出訂閱時，會故意（或由於 API 設定不當）限制第三方用戶端的使用。伺服器可以成功載入到您的清單中，但在嘗試連線時會進入無限逾時狀態。
> 💡 **如何排查原因：** 如果您獲取該節點的「原生」連結（例如 `vless://...` 或 JSON 程式碼）並將其作為本地設定檔手動新增，且**可以正常運作** —— 那麼問題 100% 出在提供商端。這代表他們的伺服器在嘗試更新訂閱時，透過 `User-Agent` 攔截了您用戶端的請求。在其他情況下，逾時可能是由於審查防火牆（DPI）對協定特徵實施的精準攔截造成的。

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

### 🔥 17.01 ULTRA 版本有什麼新功能？

- 🚀 **Extreme Parser Engine:** 極速解析引擎，程式碼全面優化，支援同時處理 **10,000+ 節點**。即使資料量巨大，介面依然流暢。
- 🌍 **ULTRA Localization:** 深度支援 6 种語言 (RU, EN, ZH, FA, ES)。介面和系統通知現已完全適配。
- 🛡️ **QuotaGuard 系統:** 智能防止瀏覽器記憶體溢出。處理任何大小的配置都不會導致分頁崩潰。
- 🧠 **Smart Duplicate Filter:** 智能去重，透過 IP:端口 自動比對伺服器。程式自動清理垃圾和重複項，僅保留唯一的節點。
- 🛠️ **Refined Diagnostics:** 更新了事件日誌並修復了語法錯誤 (SyntaxError fix)，確保完美穩定性。

---

### 🔌 支援的協定

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

### 📥 推薦用戶端 (ULTRA 兼容)

> [!NOTE]
> 流行的用戶端如 **NekoBox** 和 **NekoRay** 目前已被視為過時。強烈建議切換到基於 **sing-box** 和 **Xray** 核心的現代優化替代品（例如，完全還原 NekoBox 介面的 **Exclave**，或者 **Incy**）。

<details>
<summary><b>🤖 Android (安卓)</b></summary>

- [v2RayTun](https://v2raytun.com/) — 基於 Xray Core 的高速安全用戶端。
- [FlClash](https://github.com/chen08209/FlClash) — 主要的跨平台用戶端。
- [Incy](https://incy.cc/) — 支援一鍵導入的現代快速用戶端。
- [Happ](https://www.happ.su/main) — 便捷管理伺服器列表的代理工具。
- [Exclave](https://github.com/ExclaveNetwork/Exclave) — 現代化且保持更新的 NekoBox 替代品，介面熟悉。
- [Sing-box](https://github.com/SagerNet/sing-box) — 官方純淨核心，適合高級配置。
- [Hiddify App](https://github.com/hiddify/hiddify-app) — 支援所有配置類型的通用用戶端。
- [v2rayNG](https://github.com/2dust/v2rayNG) — 基於 Xray 核心的穩定經典解決方案。
- [Karing](https://github.com/KaringX/karing) — 功能豐富的圖形介面。
- [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
- ~~[NekoBox For Android](https://github.com/MatsuriDayo/NekoBoxForAndroid)~~ *(已過時)*
</details>

<details>
<summary><b>🍏 iOS (蘋果)</b></summary>

- [v2RayTun](https://v2raytun.com/) — 基於 Xray Core 的高速安全用戶端.
- [Incy](https://incy.cc/) — App Store 中優秀的現代用戶端。
- [Happ](https://www.happ.su/main) — 舒適的代理工具。
- [Karing](https://apps.apple.com/us/app/karing/id6472431552)
- [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
- [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)
- [Clash Lite](https://apps.apple.com/us/app/clash-lite/id6761357475)
- [V2Lite VPN](https://apps.apple.com/us/app/v2lite-vpn-super-vpn-proxy/id6444585377)
</details>

<details>
<summary><b>💻 Desktop (電腦端 Win/Mac/Linux)</b></summary>

- [v2RayTun](https://v2raytun.com/) — 基於 Xray Core 的高速安全用戶端。
- [Happ](https://www.happ.su/main) — 跨平台桌面版本。
- [v2rayN](https://github.com/2dust/v2rayN) — 強大的 Windows 可自定義用戶端。
- [FlClash](https://github.com/chen08209/FlClash) — 極簡快速的 GUI。
- [Karing](https://github.com/KaringX/karing)
- [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)
- ~~[NekoRay](https://github.com/MatsuriDayo/nekoray)~~ *(已過時)*
</details>

---

### 🛡️ 替代工具 (DPI 繞過 / 防火牆穿透)

*如果標準 VPN 協定被您的運營商或審查防火牆完全封鎖，請使用本地的深度封包檢測 (DPI) 繞過工具：*

* [Zapret](https://github.com/bol-van/zapret) — 系統級深度繞過 DPI 最強大、最靈活的工具。
* [Zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) — 針對特定熱門服務預先配置好的優化腳本。
* [ByeByeDPI](https://github.com/romanvht/ByeByeDPI) — 在 Windows 上本地運行的成熟經典解決方案。

---

### ⭐ 支持項目

**如果 Network Builder ULTRA 幫助了您，請不要忘記點個 Star ⭐️！這能激勵項目進一步發展。**

[![Stargazers over time](https://starchart.cc/jinxpil/flclash-converter.svg?variant=adaptive)](https://starchart.cc/jinxpil/flclash-converter)
