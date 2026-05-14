<p align="center">
  <a href="/README.en.md">🇺🇸 English</a> •
  <a href="/README.md">🇷🇺 Русский</a> •
  <a href="/README.zh.md">🇨🇳 简体中文</a> •
  <a href="/README.zh-TW.md">🇹🇼 繁體中文</a> •
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

<h1 align="center">🌐 Network Builder</h1>

<p align="center">
  <b>高級的 100% 本地 Web 工具（單文件 HTML / Vanilla JS），用於管理、測試和轉換代理伺服器。</b><br>
  <i>提供便捷的介面，可解析來自任何來源的節點，並為 FlClash、Nekobox (Xray) 和 Sing-box 即時生成優化的路由設定檔。</i>
</p>

<p align="center">
  <a href="https://jinxpil.github.io/flclash-converter/">
    <img src="https://img.shields.io/badge/🚀_打開網頁版-0052FF?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Open Web Version">
  </a>
</p>

> [!IMPORTANT]
> **僅供學習交流。** 本項目僅為研究目的而創建。請勿將其用於非法用途。作者對本工具的濫用不承擔任何責任。所有計算均在您的瀏覽器中嚴格本地進行（零信任）。

---

### 📸 介面 (自適應)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/JSON%20to%20YAML%20Converter.jpg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/JSON%20to%20YAML%20Converter.jpg">
    <img alt="JSON to YAML" src="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/JSON%20to%20YAML%20Converter.jpg" width="48%">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/Yaml%20Code%20Formatter.jpg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/Yaml%20Code%20Formatter.jpg">
    <img alt="YAML Formatter" src="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/Yaml%20Code%20Formatter.jpg" width="48%">
  </picture>
</p>

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
    <td align="center">🔌 <b>TUIC / Socks5 / HTTP</b><br>Other Protocols</td>
  </tr>
</table>

---

### 📥 推薦客戶端

<details>
<summary><b>🤖 顯示 Android 客戶端</b></summary>

- [FlClash](https://github.com/chen08209/FlClash)
- [Karing](https://github.com/KaringX/karing)
- [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
- [FlClashX](https://github.com/pluralplay/FlClashX)
</details>

<details>
<summary><b>🍏 顯示 iOS 客戶端</b></summary>

- [Karing](https://apps.apple.com/us/app/karing/id6472431552)
- [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
- [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)
</details>

<details>
<summary><b>💻 顯示 PC (Windows / macOS / Linux) 客戶端</b></summary>

- [Karing](https://github.com/KaringX/karing)
- [FlClash](https://github.com/chen08209/FlClash)
- [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)
</details>

---

### 🔥 核心功能

- 🛡️ **零信任安全 (Zero-Trust Security):** 無第三方伺服器。資料在記憶體中處理，關閉分頁後即銷毀。
- 🧩 **全能解析器 (Omni-Parser):** 即時解碼 Base64 訂閱，逆向工程 JSON 設定，並支援拖曳 (Drag & Drop)。
- 🌍 **批量編輯器 & 智能 GeoIP:** 批量修改參數（SNI、Flow、Fingerprint），並自動識別節點地理位置添加國旗（🇫🇮, 🇩🇪）。
- 🐛 **診斷日誌 (Diagnostic Logger):** 內建後台除錯系統，記錄互動、錯誤和網路事件，便於排查問題。
- 🎨 **主題引擎 (Theme Engine):** 全面的介面自訂，支援匯入/匯出 `.json` 設計。
- ⚙️ **自動優化:** 按 IP/連接埠清理重複項目，TCP/HTTP 延遲測試後移除失效節點，並自動修復損壞的連結。

---

### ⭐ 支持項目

**如果這個項目對您有幫助，請給它點個 Star！** :star2:

[![Stargazers over time](https://starchart.cc/jinxpil/flclash-converter.svg?variant=adaptive)](https://starchart.cc/jinxpil/flclash-converter)
