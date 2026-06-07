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
  <b>极其强大且 100% 本地化的网络工具，用于管理庞大的代理服务器数据库。</b><br>
  <i>解析、转换并深度优化 FlClash、Exclave、Sing-box 和 Clash Meta 的配置。</i>
</p>

<p align="center">
  <a href="https://jinxpil.github.io/flclash-converter/">
    <img src="https://img.shields.io/badge/🚀_打开_ULTRA--版本-0052FF?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Open Web Version">
  </a>
</p>

> [!IMPORTANT]
> **零信任与隐私至上。** 所有计算均在您的浏览器中严格本地执行。任何数据都不会离开您的设备。该工具仅用于教育目的，旨在深度研究网络协议。

> [!WARNING]
> **注意：YAML 订阅与连接超时 (Timeout) 问题：**
> 许多 VPN 提供商在导出订阅时，会故意（或由于 API 配置不当）限制第三方客户端的使用。服务器可以成功加载到您的列表中，但在尝试连接时会进入无限超时状态。
> 💡 **如何排查原因：** 如果您获取该节点的“原生”链接（例如 `vless://...` 或 JSON 代码）并将其作为本地配置文件手动添加，且**可以正常工作** —— 那么问题 100% 出在提供商端。这意味着他们的服务器在尝试更新订阅时，通过 `User-Agent` 拦截了您客户端的请求。在其他情况下，超时可能是由于审查防火墙（DPI）对协议特征实施的精准拦截造成的。

---

### 📸 界面 (ULTRA Design)

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

### 🔥 17.01 ULTRA 版本有什么新功能？

- 🚀 **Extreme Parser Engine:** 极速解析引擎，代码全面优化，支持同时处理 **10,000+ 节点**。即使数据量巨大，界面依然流畅。
- 🌍 **ULTRA Localization:** 深度支持 6 种语言 (RU, EN, ZH, FA, ES)。界面和系统通知现已完全适配。
- 🛡️ **QuotaGuard 系统:** 智能防止浏览器内存溢出。处理任何大小的配置都不会导致标签页崩溃。
- 🧠 **Smart Duplicate Filter:** 智能去重，通过 IP:端口 自动比对服务器。程序自动清理垃圾和重复项，仅保留唯一的节点。
- 🛠️ **Refined Diagnostics:** 更新了事件日志并修复了语法错误 (SyntaxError fix)，确保完美稳定性。

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

### 📥 推荐客户端 (ULTRA 兼容)

> [!NOTE]
> 流行的客户端如 **NekoBox** 和 **NekoRay** 目前已被视为过时。强烈建议切换到基于 **sing-box** 和 **Xray** 内核的现代优化替代品（例如，完全还原 NekoBox 界面的 **Exclave**，或者 **Incy**）。

<details>
<summary><b>🤖 Android (安卓)</b></summary>

- [v2RayTun](https://v2raytun.com/) — 基于 Xray Core 的高速安全客户端。
- [FlClash](https://github.com/chen08209/FlClash) — 主要的跨平台客户端。
- [Incy](https://incy.cc/) — 支持一键导入的现代快速客户端。
- [Happ](https://www.happ.su/main) — 便捷管理服务器列表的代理工具。
- [Exclave](https://github.com/ExclaveNetwork/Exclave) — 现代化且保持更新的 NekoBox 替代品，界面熟悉。
- [Sing-box](https://github.com/SagerNet/sing-box) — 官方纯净内核，适合高级配置。
- [Hiddify App](https://github.com/hiddify/hiddify-app) — 支持所有配置类型的通用客户端。
- [v2rayNG](https://github.com/2dust/v2rayNG) — 基于 Xray 内核的稳定经典解决方案。
- [Karing](https://github.com/KaringX/karing) — 功能丰富的图形界面。
- [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
- ~~[NekoBox For Android](https://github.com/MatsuriDayo/NekoBoxForAndroid)~~ *(已过时)*
</details>

<details>
<summary><b>🍏 iOS (苹果)</b></summary>

- [v2RayTun](https://v2raytun.com/) — 基于 Xray Core 的高速安全客户端。
- [Incy](https://incy.cc/) — App Store 中优秀的现代客户端。
- [Happ](https://www.happ.su/main) — 舒适的代理工具。
- [Karing](https://apps.apple.com/us/app/karing/id6472431552)
- [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
- [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)
- [Clash Lite](https://apps.apple.com/us/app/clash-lite/id6761357475)
- [V2Lite VPN](https://apps.apple.com/us/app/v2lite-vpn-super-vpn-proxy/id6444585377)
</details>

<details>
<summary><b>💻 Desktop (电脑端 Win/Mac/Linux)</b></summary>

- [v2RayTun](https://v2raytun.com/) — 基于 Xray Core 的高速安全客户端。
- [Happ](https://www.happ.su/main) — 跨平台桌面版本。
- [v2rayN](https://github.com/2dust/v2rayN) — 强大的 Windows 可自定义客户端。
- [FlClash](https://github.com/chen08209/FlClash) — 极简快速的 GUI。
- [Karing](https://github.com/KaringX/karing)
- [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)
- ~~[NekoRay](https://github.com/MatsuriDayo/nekoray)~~ *(已过时)*
</details>

---

### 🛡️ 替代工具 (DPI 绕过 / 防火墙穿透)

*如果标准 VPN 协议被您的运营商或审查防火墙完全封锁，请使用本地的深度包检测 (DPI) 绕过工具：*

* [Zapret](https://github.com/bol-van/zapret) — 系统级深度绕过 DPI 最强大、最灵活的工具。
* [Zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) — 针对特定热门服务预先配置好的优化脚本。
* [ByeByeDPI](https://github.com/romanvht/ByeByeDPI) — 在 Windows 上本地运行的成熟经典解决方案。

---

### ⭐ 支持项目

**如果 Network Builder ULTRA 帮助了您，请不要忘记点个 Star ⭐️！这能激励项目进一步发展。**

[![Stargazers over time](https://starchart.cc/jinxpil/flclash-converter.svg?variant=adaptive)](https://starchart.cc/jinxpil/flclash-converter)
