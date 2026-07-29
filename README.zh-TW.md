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
  <b>極度強大且 100% 本機的 Web 工具，專為管理超大型代理節點清單設計。</b><br>
  <i>為 FlClash、Exclave、Sing-box、Clash Meta 提供解析、轉換與深度優化，並包含適用於 INCY / HAPP 的行動端 PWA 開發環境。</i>
</p>

<p align="center">
  <a href="https://jinxpil.github.io/flclash-converter/">
    <img src="https://img.shields.io/badge/🚀_打開_ULTRA_版本-0052FF?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Open Web Version">
  </a>
  <a href="https://jinxpil.github.io/flclash-converter/INCY_Tool.html">
    <img src="https://img.shields.io/badge/🔮_INCY_CONFIG_TOOL-8A2BE2?style=for-the-badge&logo=pwa&logoColor=white" alt="Open INCY Tool">
  </a>
</p>

<p align="center">
  🤖 <b>同時推薦我的第二個專案：</b><br>
  👉 <a href="https://github.com/JINXPIL/json-yaml-ai"><b>JSON-YAML-AI</b></a> 👈
</p>

> [!IMPORTANT]
> **零信任與隱私至上。** 所有運算均在您的瀏覽器內部完全本機執行，不會上傳任何資料。本工具專為深入學習網路協定的教育目的建立。遇到 ISP 面向更新訂閱引發的「超時 (Timeout)」時，利用此工具即可手動繞過限制，極速本機處理配置。

---

### 🔮 全新推出：INCY Config Tool (終極 PWA)

除了全局的轉換系統，目前專案加入了一套 **專屬於行動裝置的獨立編輯環境 (IDE)**，能夠讓您在各種情境下手動修剪 `incy://` 以及 `happ://` 的分流設定檔。

* 📱 **零外部依賴 & PWA：** 由 1 個純 HTML 檔案組成。支援 100% 離線執行（可如原生應用程式般釘選到手機首頁）。
* 🪄 **INCY-MINI 壓縮演算法：** 採用隱藏壓縮技術，將訂閱長度激減 5 倍，讓超長的設定不被 Telegram/WhatsApp 半途裁斷！
* 🚀 **深度連結直達：** 改完配置檔，即可直接一鍵導向您的手機代理端 APP 完成匯入。
* 🧠 **行動版智慧編輯器：** 與 VS Code 相似的智慧縮排功能，精準識別 JSON 語法錯誤並自動捲動，支援一站式復原 (Undo)。

👉 **[啟動 INCY Config Tool](https://jinxpil.github.io/flclash-converter/INCY_Tool.html)**

---

### 🔥 17.05 ULTRA 版本的亮點？ (極致高並發)

* 🌐 **新增協議廣泛支援：** 全面覆蓋 **VMess, Hysteria2 (hy2), Shadowsocks (SS), 以及 ShadowsocksR (SSR)**。
* 🚀 **極限效能解析：** 透過非同步加載以及 DOM 虛擬化，能在毫秒級單位清洗和去重 **250,000+** 筆節點且不卡死瀏覽器。
* 🛡️ **YAML 裝甲淨化：** 優化至工業標準。自動捨棄無效的 `2022-blake3` 協定、不法 ASCII 字元等垃圾數據，保障 Mihomo 用戶無痛無錯導入。
* ⚙️ **全新 UI 與功能：** 新增明暗雙重主題、以及能直接無縫把 RAW 來源打包至 `proxy-providers` 區塊的「訂閱切換鈕」。

---

### 🤝 社群替代路由資料庫

如果需要來自社群其它分流路由方案：
* [Roscomvpn-routing](https://github.com/hydraponique/roscomvpn-routing) — 此專案由 *hydraponique* 維護，時常為 **INCY、HAPP** 和 **Clash Meta** 提供精準修訂過的規則配置檔案。

---

### 🛡️ 其它審查繞過與代理工具 (DPI Bypass)

*如果一般 VPN 協議遭受防火牆深度封阻，可嘗試採用各類封包繞過及偽裝方案:*

* [Zapret](https://github.com/bol-van/zapret) — 系統級、高自定義的防 DPI 分析與破解工具。
* [Zapret2](https://github.com/bol-van/zapret2) — 由 `bol-van` 主導的實驗性黑科技新版本。
* [Zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) — 立刻解決 Discord 或 Youtube 嚴重掉包的自動腳本封裝。
* [ByeByeDPI](https://github.com/romanvht/ByeByeDPI) — 面向 Windows 環境穩定且強大的深度驗證繞行方案。
* [tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) — 將 Telegram 以 WebSocket 協定反向代理的優質對策。

---

### ⭐ 支持這個專案

**若 Network Builder ULTRA 或 INCY Tool 幫到了您，請不吝於為專案點下一顆 Star ⭐！**

[![Star History Chart](https://api.star-history.com/svg?repos=JINXPIL/flclash-converter&type=Date)](https://star-history.com/#JINXPIL/flclash-converter&Date)