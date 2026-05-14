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

<h1 align="center">⚡ Network Builder v17.00 ULTRA</h1>

<p align="center">
  <b>一款专业、100% 本地运行的 Web 工具，用于管理、深度清理和转换海量代理服务器数据库。</b><br>
  <i>适用于 FlClash、Nekobox (Xray)、Sing-box 和 Clash Meta 配置的统一生态系统。</i>
</p>

<p align="center">
  <a href="https://jinxpil.github.io/flclash-converter/">
    <img src="https://img.shields.io/badge/🚀_开启_ULTRA_版本-0052FF?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Open Web Version">
  </a>
</p>

> [!IMPORTANT]
> **零信任安全 (Zero-Trust Security)。** 本项目没有后端服务。从解析到生成二维码的所有操作均在您的浏览器内存中完成。任何 UUID、密钥或 IP 地址均不会上传至第三方服务器。

---

### 📸 界面展示 (ULTRA 设计)

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

### 🔥 v17.00 ULTRA 有什么新功能？

- 🚀 **极限解析引擎 (Extreme Parser Engine)：** 解析引擎经过全面优化，可同时处理 **10,000+ 个节点**。即使面对超大型数据库，界面依然流畅，搜索瞬时响应。
- 🌍 **ULTRA 本地化：** 全面支持 6 种语言 (RU, EN, ZH, ZH-TW, FA, ES)。针对各个地区优化了用户界面和系统通知。
- 🛡️ **QuotaGuard 内存防护：** 智能浏览器内存控制系统。防止在导入体积巨大的订阅文件时发生应用崩溃 (QuotaExceededError)。
- 🧠 **智能去重过滤：** 基于 IP:Port 对的自动节点比对。程序可瞬时识别并删除冗余节点，确保节点列表精简唯一。
- 🛠️ **极致稳定性：** 修复了弹窗界面的关键语法错误 (SyntaxError)，并优化了移动设备的剪贴板性能。

---

### 🔌 支持协议

<table align="center" width="100%">
  <tr>
    <td align="center">🛡️ <b>VLESS / VMess</b><br>Reality, Vision, gRPC</td>
    <td align="center">⚡ <b>Hysteria 1/2</b><br>极速传输与跳港</td>
    <td align="center">🐎 <b>Trojan</b><br>隐身 TLS 与密码验证</td>
  </tr>
  <tr>
    <td align="center">🔒 <b>WireGuard</b><br>原生 VPN 与 AmneziaWG</td>
    <td align="center">🌐 <b>Shadowsocks / RR</b><br>经典与 AEAD 加密</td>
    <td align="center">🔌 <b>TUIC / Socks5 / HTTP</b><br>完整协议兼容性</td>
  </tr>
</table>

---

### 🔥 核心功能

- 🧩 **全能解析器 (Omni-Parser)：** 瞬时 Base64 订阅解码，从文本中提取原始链接，以及对复杂 JSON/YAML 配置的深度逆向工程。
- 🌍 **批量编辑器 (Mass Editor)：** 一键为数千个选定节点批量修改参数（如 SNI, Fingerprint, Flow, Public Key）。
- 🌍 **智能 GeoIP：** 自动检测服务器所在的国家与城市，并自动为名称添加对应的国旗标志 (🇫🇮, 🇩🇪, 🇺🇸)。
- ⚙️ **自动优化：** 测试后自动删除“失效”节点，支持列表随机打乱 (Shuffle)，并自动修复损坏的 URI 链接。
- 🐛 **诊断日志系统 (Diagnostic Logger)：** 内置实时事件监控系统，用于追踪配置问题与网络连接状态。

---

### 📥 推荐客户端 (ULTRA 兼容)

<details>
<summary><b>🤖 Android 平台</b></summary>

- [FlClash](https://github.com/chen08209/FlClash) — 推荐客户端
- [Karing](https://github.com/KaringX/karing) — 进阶用户界面
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

### ⭐ 支持项目

**如果 Network Builder ULTRA 对您有所帮助，请不要忘记给予一个 Star！这是我持续开发与改进的最大动力。** :star2:

[![Stargazers over time](https://starchart.cc/jinxpil/flclash-converter.svg?variant=adaptive)](https://starchart.cc/jinxpil/flclash-converter)
