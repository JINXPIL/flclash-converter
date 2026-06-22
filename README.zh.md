<p align="center">
  <a href="/README.en.md">🇺🇸 English</a> •
  <a href="/README.md">🇷🇺 Русский</a> •
  <a href="/README.zh.md"><b>🇨🇳 简体中文</b></a> •
  <a href="/README.zh-TW.md">🇹🇼 繁體中文</a> •
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
  <b>一款极其强大且 100% 本地运行的 Web 工具，用于管理海量代理服务器数据库。</b><br>
  <i>为 FlClash、Exclave、Sing-box 和 Clash Meta 提供解析、转换和深度优化的配置。</i>
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
    <img src="https://img.shields.io/badge/🚀_打开_ULTRA_版本-0052FF?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Open Web Version">
  </a>
</p>

<p align="center">
  🤖 <b>也请关注我的第二个项目：</b><br>
  👉 <a href="https://github.com/JINXPIL/json-yaml-ai"><b>JSON-YAML-AI</b></a> 👈
</p>

> [!IMPORTANT]
> **零信任与隐私优先。** 所有计算均在您的浏览器中严格本地执行。没有任何数据会离开您的设备。本工具仅为教育目的而创建，用于深入研究网络协议。

> [!WARNING]
> **注意：YAML 订阅和超时 (Timeout) 问题：**
> 许多 VPN 提供商故意（或由于 API 设置不当）限制第三方客户端导出订阅。服务器可能成功加载到您的列表中，但在尝试连接时会进入无限超时。
> 💡 **如何排查原因：** 如果您获取同一个节点的“原始”链接（例如 `vless://...` 或 JSON 代码），将其手动添加为本地配置文件，并且 **它可以正常工作** —— 那么问题 100% 出在提供商那边。这意味着在尝试更新订阅时，他们的服务器根据 `User-Agent` 拦截了客户端的请求。在其他情况下，超时可能是由于防火墙（如 GFW）对协议特征进行了精准封锁。

---

### 📸 界面展示 (ULTRA Design)

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

### 🔥 17.05 ULTRA 版本更新了什么？ (高并发完美版)

* 🌐 **全面协议扩展：** 增加对 **VMess、Hysteria2 (hy2)、Shadowsocks (SS) 和 ShadowsocksR (SSR)** 的完整解析支持。
* 🚀 **极限性能 (HighLoad)：** 引入异步分块处理与 `Set` 字典。DOM 虚拟化技术让您在毫秒内加载并去重 **250,000+ 个节点**，浏览器丝滑不卡顿！
* 🛡️ **防弹级 YAML 净化器：** 工业级准入控制。脚本会自动清理公共节点库中的垃圾（不可见 ASCII 字符、虚假的 `2022-blake3` 加密、空密码），确保 100% 稳定导入 Mihomo。
* ⚙️ **彻底解决超时问题：** YAML 生成器已根据 Mihomo 严格标准重写（添加了 `alpn`、`skip-cert-verify: true`、`servername` 以及改进的 Fake-IP DNS 路由）。
* 🎨 **全新 UI/UX：** 独立的明/暗主题（支持分别保存自定义颜色），以及**“订阅模式”开关**，可将 RAW 链接（Pastebin/GitHub）直接嵌入到 `proxy-providers` 模块中。

---

### 🔌 支持的协议

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

### 🎯 配置与路由 (预设)

为了避免在页面上堆砌大量代码，所有现成的预设配置都已提取到独立的仓库文件中。

* 🌐 **Happ 分流配置** — 通过 `routing.happ.su` 构建的优化规则预设（绕过限制、AdBlock等）。**严格**专为 Happ 客户端设计。
    * 📄 配置文件链接：[`./rus_vp_happ.json`](./rus_vp_happ.json)
    * 🔗 客户端导入链接：`https://raw.githubusercontent.com/JINXPIL/flclash-converter/refs/heads/main/rus_vp_happ.json`
* 🛠️ **优化的 YAML 配置 (Mihomo/Clash)** — v79.0 Ultimate，具备严格的 TLS 浏览器指纹和防 DPI 嗅探保护。
    * 📄 配置文件链接：[`./GL_Crimea_ipv6_yan(9.35).yml`](./GL_Crimea_ipv6_yan(9.35).yml)
    * 🔗 客户端导入链接：`https://raw.githubusercontent.com/JINXPIL/flclash-converter/refs/heads/main/GL_Crimea_ipv6_yan(9.35).yml`

---
> [!NOTE]
> 目前，像 **NekoBox** 和 **NekoRay** 这类热门客户端已被认为是过时的。建议迁移到基于最新的 **sing-box** 和 **Xray** 内核的现代优化替代方案（例如 **Exclave**，它完全复刻了 NekoBox 的界面，或者 **Incy**）。

<details>
<summary><b>🤖 Android</b></summary>

* [v2RayTun](https://v2raytun.com/) — 基于 Xray Core 的高速、安全客户端。
* [FlClash](https://github.com/chen08209/FlClash) — 优秀的跨平台客户端。
* [Incy](https://incy.cc/) — 支持一键导入的现代快速客户端。
* [Happ](https://www.happ.su/main) — 方便管理服务器列表的代理工具。
* [Exclave](https://github.com/ExclaveNetwork/Exclave) — NekoBox 的现代替代品，界面熟悉。
* [Sing-box](https://github.com/SagerNet/sing-box) — 用于高级配置的官方纯净内核。
* [Hiddify App](https://github.com/hiddify/hiddify-app) — 适用于任何配置类型的通用客户端。
* [v2rayNG](https://github.com/2dust/v2rayNG) — 基于 Xray 内核的稳定经典方案。
* [Karing](https://github.com/KaringX/karing) — 功能丰富的图形界面。
* [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
* ~~[NekoBox For Android](https://github.com/MatsuriDayo/NekoBoxForAndroid)~~ *(已过时)*
</details>

<details>
<summary><b>🍏 iOS</b></summary>

* [v2RayTun](https://v2raytun.com/) — 基于 Xray Core 的高速、安全客户端。
* [Incy](https://incy.cc/) — App Store 上出色的现代客户端。
* [Happ](https://www.happ.su/main) — 舒适的代理工具。
* [Karing](https://apps.apple.com/us/app/karing/id6472431552)
* [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
* [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)
* [Clash Lite](https://apps.apple.com/us/app/clash-lite/id6761357475)
* [V2Lite VPN](https://apps.apple.com/us/app/v2lite-vpn-super-vpn-proxy/id6444585377)
</details>

<details>
<summary><b>💻 Desktop (Win/Mac/Linux)</b></summary>

* [v2RayTun](https://v2raytun.com/) — 基于 Xray Core 的高速、安全客户端。
* [Happ](https://www.happ.su/main) — 跨平台桌面版本。
* [v2rayN](https://github.com/2dust/v2rayN) — Windows 上强大的可定制客户端。
* [FlClash](https://github.com/chen08209/FlClash) — 极简快速的 GUI。
* [Karing](https://github.com/KaringX/karing)
* [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)
* ~~[NekoRay](https://github.com/MatsuriDayo/nekoray)~~ *(已过时)*
</details>

---

### 🛡️ 替代工具 (DPI 绕过)

*如果标准 VPN 协议被您的 ISP 完全封锁，请使用本地的深度包检测绕过工具：*

* [Zapret](https://github.com/bol-van/zapret) — 系统级别最强大、最灵活的深度 DPI 绕过工具。
* [Zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) — 针对特定流行服务优化的现成脚本。
* [ByeByeDPI](https://github.com/romanvht/ByeByeDPI) — 久经考验的经典 Android 本地运行方案。

---

### ⭐ 支持项目

**如果 Network Builder ULTRA 帮助到了您，请不要忘记点个 Star！这将激励我们继续开发。** :star2:

[![Star History Chart](https://api.star-history.com/svg?repos=jinxpil/flclash-converter&type=Date)](https://star-history.com/#jinxpil/flclash-converter&Date)
