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

<h1 align="center">⚡ Network Builder v17.02 ULTRA</h1>

<p align="center">
  <b>极其强大且 100% 本地的 Web 工具，用于管理庞大的代理服务器数据库。</b><br>
  <i>解析、转换并深度优化 FlClash、Exclave、Sing-box 和 Clash Meta 的配置。</i>
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

> [!IMPORTANT]
> **零信任与隐私至上。** 所有计算均在您的浏览器中严格本地执行。没有任何数据会离开您的设备。该工具仅用于深入研究网络协议和路由原理的教育目的。

> [!WARNING]
> **注意：YAML 订阅和超时 (Timeout) 问题：**
> 许多 VPN 提供商在导出订阅时故意（或由于 API 配置不当）限制第三方客户端的操作。节点可能会成功加载到您的列表中，但在尝试连接时，它们会进入无限超时。
> 💡 **如何排查问题：** 如果您获取同一节点的“原始”链接（例如，`vless://...` 或 JSON 代码），将其作为本地配置文件手动添加，并且**它可以正常工作** — 则问题 100% 出在提供商端。这意味着当尝试更新订阅时，他们的服务器通过 `User-Agent` 拦截了客户端的请求。在其他情况下，超时可能是由审查防火墙 (DPI) 针对协议特征的定向拦截引起的。

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

### 🔥 版本 17.02 ULTRA 有什么新功能？

* 🚀 **极限解析引擎：** 全面优化代码，可同时处理 **10,000 多个节点**。即使在海量数据下也能保持流畅的界面。
* 🌍 **ULTRA 本地化：** 深度支持 6 种语言（俄语、英语、中文、波斯语、西班牙语）。界面和系统通知现已完全适配。
* 🛡️ **QuotaGuard 系统：** 防止浏览器内存溢出的智能保护。处理任何体积的配置都不会导致标签页崩溃。
* 🧠 **智能去重过滤器：** 通过 `IP:Port` 自动比较服务器并删除垃圾和重复项，仅保留唯一节点。
* 🛠️ **精细诊断：** 更新的事件日志并修复了语法错误 (SyntaxError fix)，确保完美稳定运行。

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

### 🎯 配置与路由规则 (预设)

为了不让页面堆满代码，所有现成的预设配置都已提取到独立的仓库文件中。

* 🌐 **Happ 分流规则** — 优化的规则预设（克里米亚、SevSU、绕过限制、AdBlock），通过 `routing.happ.su` 构建。**严格**仅供 Happ 客户端使用。
    * 📄 配置文件链接：[`./rus_vp_happ.json`](./rus_vp_happ.json)
    * 🔗 客户端导入链接：`https://raw.githubusercontent.com/JINXPIL/flclash-converter/refs/heads/main/rus_vp_happ.json`
* 🛠️ **Mihomo/Clash 优化配置 (YAML)** — v79.0 Ultimate，具有严格的浏览器 TLS 指纹和防 DPI 分析保护。
    * 📄 配置文件链接：[`./GL_Crimea_ipv6_yan(9.35).yml`](./GL_Crimea_ipv6_yan(9.35).yml)
    * 🔗 客户端导入链接：`https://raw.githubusercontent.com/JINXPIL/flclash-converter/refs/heads/main/GL_Crimea_ipv6_yan(9.35).yml`

---

### 📥 推荐客户端 (ULTRA 兼容)

> [!NOTE]
> 注意：**NekoBox** 和 **NekoRay** 等流行客户端目前被视为已过时。强烈建议切换到基于 **sing-box** 和 **Xray** 内核的现代优化替代方案（例如，完全复制 NekoBox 界面的 **Exclave**，或 **Incy**）。

<details>
<summary><b>🤖 Android</b></summary>

* [v2RayTun](https://v2raytun.com/) — 基于 Xray Core 的高速安全客户端。
* [FlClash](https://github.com/chen08209/FlClash) — 跨平台客户端。
* [Incy](https://incy.cc/) — 具有一键导入功能的现代快速客户端。
* [Happ](https://www.happ.su/main) — 用于方便管理服务器列表的代理实用程序。
* [Exclave](https://github.com/ExclaveNetwork/Exclave) — NekoBox 的现代替代品。
* [Sing-box](https://github.com/SagerNet/sing-box) — 官方纯净内核，适合高级配置。
* [Hiddify App](https://github.com/hiddify/hiddify-app) — 通用客户端。
* [v2rayNG](https://github.com/2dust/v2rayNG) — 经典稳定的 Xray 解决方案。
* [Karing](https://github.com/KaringX/karing) — 功能丰富的 GUI。
* [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
* ~~[NekoBox For Android](https://github.com/MatsuriDayo/NekoBoxForAndroid)~~ *(已过时)*
</details>

<details>
<summary><b>🍏 iOS</b></summary>

* [v2RayTun](https://v2raytun.com/) — 基于 Xray Core 的高速安全客户端。
* [Incy](https://incy.cc/) — App Store 中的优秀现代客户端。
* [Happ](https://www.happ.su/main) — 舒适的代理工具。
* [Karing](https://apps.apple.com/us/app/karing/id6472431552)
* [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
* [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)
* [Clash Lite](https://apps.apple.com/us/app/clash-lite/id6761357475)
* [V2Lite VPN](https://apps.apple.com/us/app/v2lite-vpn-super-vpn-proxy/id6444585377)
</details>

<details>
<summary><b>💻 Desktop (Win/Mac/Linux)</b></summary>

* [v2RayTun](https://v2raytun.com/) — 基于 Xray Core 的高速安全客户端。
* [Happ](https://www.happ.su/main) — 跨平台桌面版本。
* [v2rayN](https://github.com/2dust/v2rayN) — 适用于 Windows 的强大可定制客户端。
* [FlClash](https://github.com/chen08209/FlClash) — 极简快速的 GUI。
* [Karing](https://github.com/KaringX/karing)
* [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)
* ~~[NekoRay](https://github.com/MatsuriDayo/nekoray)~~ *(已过时)*
</details>

---

### 🛡️ 替代工具 (DPI 绕过)

*如果标准 VPN 协议被您的 ISP 或防火墙完全封锁，请使用本地深度包检测绕过工具：*

* [Zapret](https://github.com/bol-van/zapret) — 系统级最强大灵活的深度绕过 DPI 工具。
* [Zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) — 针对特定流行服务的优化脚本。
* [ByeByeDPI](https://github.com/romanvht/ByeByeDPI) — 适用于 Windows 的成熟本地执行解决方案。

---

### ⭐ 支持项目

**如果 Network Builder ULTRA 对您有帮助，请不要忘记点个星 (Star)！这能激励项目进一步发展。** :star2:

[![Stargazers over time](https://starchart.cc/jinxpil/flclash-converter.svg?variant=adaptive)](https://starchart.cc/jinxpil/flclash-converter)
