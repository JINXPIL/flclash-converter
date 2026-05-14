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
  <b>高级的 100% 本地 Web 工具（单文件 HTML / Vanilla JS），用于管理、测试和转换代理服务器。</b><br>
  <i>提供便捷的界面，可解析来自任何来源的节点，并为 FlClash、Nekobox (Xray) 和 Sing-box 即时生成优化的路由配置文件。</i>
</p>

<p align="center">
  <a href="https://jinxpil.github.io/flclash-converter/">
    <img src="https://img.shields.io/badge/🚀_打开网页版-0052FF?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Open Web Version">
  </a>
</p>

> [!IMPORTANT]
> **仅供学习交流。** 本项目仅为研究目的而创建。请勿将其用于非法用途。作者对本工具的滥用不承担任何责任。所有计算均在您的浏览器中严格本地进行（零信任）。

---

### 📸 界面 (自适应)

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
    <td align="center">🔌 <b>TUIC / Socks5 / HTTP</b><br>Other Protocols</td>
  </tr>
</table>

---

### 📥 推荐客户端

<details>
<summary><b>🤖 显示 Android 客户端</b></summary>

- [FlClash](https://github.com/chen08209/FlClash)
- [Karing](https://github.com/KaringX/karing)
- [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
- [FlClashX](https://github.com/pluralplay/FlClashX)
</details>

<details>
<summary><b>🍏 显示 iOS 客户端</b></summary>

- [Karing](https://apps.apple.com/us/app/karing/id6472431552)
- [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
- [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)
</details>

<details>
<summary><b>💻 显示 PC (Windows / macOS / Linux) 客户端</b></summary>

- [Karing](https://github.com/KaringX/karing)
- [FlClash](https://github.com/chen08209/FlClash)
- [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)
</details>

---

### 🔥 核心功能

- 🛡️ **零信任安全 (Zero-Trust Security):** 无第三方服务器。数据在内存中处理，关闭标签页后即销毁。
- 🧩 **全能解析器 (Omni-Parser):** 即时解码 Base64 订阅，逆向工程 JSON 配置，并支持拖拽 (Drag & Drop)。
- 🌍 **批量编辑器 & 智能 GeoIP:** 批量修改参数（SNI、Flow、Fingerprint），并自动识别节点地理位置添加国旗（🇫🇮, 🇩🇪）。
- 🐛 **诊断日志 (Diagnostic Logger):** 内置后台调试系统，记录交互、错误和网络事件，便于排查问题。
- 🎨 **主题引擎 (Theme Engine):** 全面的界面自定义，支持导入/导出 `.json` 设计。
- ⚙️ **自动优化:** 按 IP/端口清理重复项，TCP/HTTP 延迟测试后移除失效节点，并自动修复损坏的链接。

---

### ⭐ 支持项目

**如果这个项目对您有帮助，请给它点个 Star！** :star2:

[![Stargazers over time](https://starchart.cc/jinxpil/flclash-converter.svg?variant=adaptive)](https://starchart.cc/jinxpil/flclash-converter)
