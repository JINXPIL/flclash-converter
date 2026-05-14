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

<h1 align="center">⚡ Network Builder v17.00 ULTRA</h1>

<p align="center">
  <b>專業級 100% 在地化網頁工具，用於管理、深度清理與轉換海量代理伺服器資料庫。</b><br>
  <i>適用於 FlClash、Nekobox (Xray)、Sing-box 與 Clash Meta 配置的一體化生態系統。</i>
</p>

<p align="center">
  <a href="https://jinxpil.github.io/flclash-converter/">
    <img src="https://img.shields.io/badge/🚀_開啟_ULTRA_版本-0052FF?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Open Web Version">
  </a>
</p>

> [!IMPORTANT]
> **零信任安全 (Zero-Trust Security)。** 本專案無後端服務。所有操作（從解析到生成二維碼）均在您的瀏覽器記憶體中執行。任何 UUID、金鑰或 IP 地址均不會上傳至第三方伺服器。

---

### 📸 介面展示 (ULTRA 設計)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/JSON%20to%20YAML%20Converter.jpg">
    <img alt="JSON to YAML" src="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/JSON%20to%20YAML%20Converter.jpg" width="48%">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/Yaml%20Code%20Formatter.jpg">
    <img alt="YAML Formatter" src="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/Yaml%20Code%20Formatter.jpg" width="48%">
  </picture>
</p>

---

### 🔥 v17.00 ULTRA 有什麼新功能？

- 🚀 **極限解析引擎 (Extreme Parser Engine)：** 解析引擎經過深度優化，可同時處理 **10,000+ 個節點**。即使面對超大型資料庫，介面依然流暢，搜尋瞬時響應。
- 🌍 **ULTRA 全球在地化：** 全面支援 6 種語言 (RU, EN, ZH, ZH-TW, FA, ES)。針對各個地區優化了使用者介面與系統通知。
- 🛡️ **QuotaGuard 記憶體防護：** 智慧型瀏覽器記憶體控制系統。防止在導入體積巨大的訂閱檔案時發生應用程式崩潰 (QuotaExceededError)。
- 🧠 **智慧型去重過濾：** 基於 IP:Port 對的自動節點比對。程式可瞬時識別並刪除冗餘節點，確保節點列表精簡唯一。
- 🛠️ **極致穩定性：** 修復了彈窗介面的關鍵語法錯誤 (SyntaxError)，並優化了行動裝置的剪貼簿效能。

---

### 🔌 支援通訊協定

<table align="center" width="100%">
  <tr>
    <td align="center">🛡️ <b>VLESS / VMess</b><br>Reality, Vision, gRPC</td>
    <td align="center">⚡ <b>Hysteria 1/2</b><br>極速傳輸與跳港</td>
    <td align="center">🐎 <b>Trojan</b><br>隱身 TLS 與密碼驗證</td>
  </tr>
  <tr>
    <td align="center">🔒 <b>WireGuard</b><br>原生 VPN 與 AmneziaWG</td>
    <td align="center">🌐 <b>Shadowsocks / RR</b><br>經典與 AEAD 加密</td>
    <td align="center">🔌 <b>TUIC / Socks5 / HTTP</b><br>完整通訊協定相容性</td>
  </tr>
</table>

---

### 🔥 核心功能

- 🧩 **全能解析器 (Omni-Parser)：** 瞬時 Base64 訂閱解碼，從文本中提取原始連結，以及對複雜 JSON/YAML 配置的深度逆向工程。
- 🌍 **批量編輯器 (Mass Editor)：** 一鍵為數千個選定節點批量修改參數（如 SNI, Fingerprint, Flow, Public Key）。
- 🌍 **智慧型 GeoIP：** 自動檢測伺服器所在的國家與城市，並自動為名稱添加對應的國旗標誌 (🇫🇮, 🇩🇪, 🇺🇸)。
- ⚙️ **自動優化：** 測試後自動刪除「失效」節點，支援列表隨機打亂 (Shuffle)，並自動修復損壞的 URI 連結。
- 🐛 **診斷日誌系統 (Diagnostic Logger)：** 內建即時事件監控系統，用於追蹤配置問題與網路連線狀態。

---

### 📥 推薦用戶端 (ULTRA 相容)

<details>
<summary><b>🤖 Android 平台</b></summary>

- [FlClash](https://github.com/chen08209/FlClash) — 推薦用戶端
- [Karing](https://github.com/KaringX/karing) — 進階使用者介面
- [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
</details>

<details>
<summary><b>🍏 iOS 平台</b></summary>

- [Karing](https://apps.apple.com/us/app/karing/id6472431552)
- [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
- [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)
</details>

<details>
<summary><b>💻 桌面端 (Win/Mac/Linux)</b></summary>

- [Karing](https://github.com/KaringX/karing)
- [FlClash](https://github.com/chen08209/FlClash)
- [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)
</details>

---

### ⭐ 支持專案

**如果 Network Builder ULTRA 對您有所幫助，請不要忘記給予一個 Star！這是我持續開發與改進的最大動力。** :star2:

[![Stargazers over time](https://starchart.cc/jinxpil/flclash-converter.svg?variant=adaptive)](https://starchart.cc/jinxpil/flclash-converter)
