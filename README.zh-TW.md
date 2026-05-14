[🇺🇸 English](/README.en.md) | [🇷🇺 Русский](/README.md) | [🇨🇳 简体中文](/README.zh.md) | [🇹🇼 繁體中文](/README.zh-TW.md) | [🇮🇷 فارسی](/README.fa.md) | [🇪🇸 Español](/README.es.md)

<p align="center">
  <a href="https://github.com/jinxpil/flclash-converter/releases">
    <img src="https://img.shields.io/github/v/release/jinxpil/flclash-converter.svg?style=flat-square" alt="Release">
  </a>
  <a href="https://github.com/jinxpil/flclash-converter/releases/latest">
    <img src="https://img.shields.io/github/downloads/jinxpil/flclash-converter/total.svg?style=flat-square" alt="Downloads">
  </a>
  <a href="#">
    <img src="https://img.shields.io/github/languages/top/jinxpil/flclash-converter.svg?style=flat-square" alt="Language">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License">
  </a>
  <a href="https://github.com/jinxpil/flclash-converter/stargazers">
    <img src="https://img.shields.io/github/stars/jinxpil/flclash-converter.svg?style=flat-square" alt="Stars">
  </a>
</p>

**Network Builder** 是一款高級的 100% 本地 Web 工具（單文件 HTML / Vanilla JS），用於管理、測試和轉換代理伺服器。它提供了便捷的介面，可解析來自任何來源的節點，並為 FlClash、Nekobox (Xray) 和 Sing-box 即時生成優化的路由設定檔。

> [!IMPORTANT]
> **僅供學習交流。** 本項目僅為研究目的而創建。請勿將其用於非法用途。作者對本工具的濫用不承擔任何責任。所有計算均在您的瀏覽器中嚴格本地進行（零信任）。

作為一款強大的網路工具，Network Builder 無需後端伺服器即可提供最高效能，支援 10 多種協定，並提供深度的 UI 自訂。

### 📸 介面

<p align="center">
  <img src="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/JSON%20to%20YAML%20Converter.jpg" alt="JSON to YAML" width="48%">
  <img src="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/Yaml%20Code%20Formatter.jpg" alt="YAML Formatter" width="48%">
</p>

## 🚀 快速開始

👉 **[打開網頁版](https://jinxpil.github.io/flclash-converter/)** *（支援 PWA，可新增至智慧型手機主畫面）*

或者從 [Releases](https://github.com/jinxpil/flclash-converter/releases) 區塊下載最新的 `index.html` 並在瀏覽器中打開。完全離線運作。

## 📥 推薦客戶端

為了使用生成的設定檔和路由，我們建議使用以下應用程式：

### 🤖 Android
- [FlClash](https://github.com/chen08209/FlClash)
- [Karing](https://github.com/KaringX/karing)
- [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
- [FlClashX](https://github.com/pluralplay/FlClashX)

### 🍏 iOS
- [Karing](https://apps.apple.com/us/app/karing/id6472431552)
- [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
- [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)

### 💻 PC (Windows / macOS / Linux)
- [Karing](https://github.com/KaringX/karing)
- [FlClash](https://github.com/chen08209/FlClash)
- [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)

## 🔥 核心功能

- **零信任安全 (Zero-Trust Security):** 無第三方伺服器。資料在記憶體中處理，關閉分頁後即銷毀。
- **全能解析器 (Omni-Parser):** 即時解碼 Base64 訂閱，逆向工程 JSON 設定，並支援拖曳 (Drag & Drop)。
- **批量編輯器 & 智能 GeoIP:** 批量修改參數（SNI、Flow、Fingerprint），並自動識別節點地理位置添加國旗（🇫🇮, 🇩🇪）。
- **診斷日誌 (Diagnostic Logger):** 內建後台除錯系統，記錄互動、錯誤和網路事件，便於排查問題。
- **主題引擎 (Theme Engine):** 全面的介面自訂，支援匯入/匯出 `.json` 設計。
- **自動優化:** 按 IP/連接埠清理重複項目，TCP/HTTP 延遲測試後移除失效節點，並自動修復損壞的連結。

## 🔌 支援的協定

`VLESS` (Reality/Vision) • `VMess` • `Trojan` • `Hysteria2` • `SS/SSR` • `WireGuard` • `TUIC` • `Socks5` • `HTTP`

## ⭐ 支持項目

**如果這個項目對您有幫助，請給它點個 Star！** :star2:

## 📈 Star 歷史

[![Stargazers over time](https://starchart.cc/jinxpil/flclash-converter.svg?variant=adaptive)](https://starchart.cc/jinxpil/flclash-converter)
