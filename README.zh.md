[English](/README.en.md) | [Русский](/README.md) | [简体中文](/README.zh.md)

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

**Network Builder** 是一款高级的 100% 本地 Web 工具（单文件 HTML / Vanilla JS），用于管理、测试和转换代理服务器。它提供了便捷的界面，可解析来自任何来源的节点，并为 FlClash、Nekobox (Xray) 和 Sing-box 即时生成优化的路由配置文件。

> [!IMPORTANT]
> **仅供学习交流。** 本项目仅为研究目的而创建。请勿将其用于非法用途。作者对本工具的滥用不承担任何责任。所有计算均在您的浏览器中严格本地进行（零信任）。

作为一款强大的网络工具，Network Builder 无需后端服务器即可提供最高性能，支持 10 多种协议，并提供深度的 UI 自定义。

### 📸 界面

<p align="center">
  <img src="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/JSON%20to%20YAML%20Converter.jpg" alt="JSON to YAML" width="48%">
  <img src="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/Yaml%20Code%20Formatter.jpg" alt="YAML Formatter" width="48%">
</p>

## 🚀 快速开始

👉 **[打开网页版](https://jinxpil.github.io/flclash-converter/)** *（支持 PWA，可添加到智能手机主屏幕）*

或者从 [Releases](https://github.com/jinxpil/flclash-converter/releases) 部分下载最新的 `index.html` 并在浏览器中打开。完全离线工作。

## 📥 推荐客户端

为了使用生成的配置文件和路由，我们建议使用以下应用程序：

### 🤖 Android
- [FlClash](https://github.com/chen08209/FlClash)
- [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
- [FlClashX](https://github.com/pluralplay/FlClashX)

### 🍏 iOS
- [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
- [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)

### 💻 PC (Windows / macOS / Linux)
- [FlClash](https://github.com/chen08209/FlClash)
- [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)

## 🔥 核心功能

- **零信任安全 (Zero-Trust Security):** 无第三方服务器。数据在内存中处理，关闭标签页后即销毁。
- **全能解析器 (Omni-Parser):** 即时解码 Base64 订阅，逆向工程 JSON 配置，并支持拖拽 (Drag & Drop)。
- **批量编辑器 & 智能 GeoIP:** 批量修改参数（SNI、Flow、Fingerprint），并自动识别节点地理位置添加国旗（🇫🇮, 🇩🇪）。
- **诊断日志 (Diagnostic Logger):** 内置后台调试系统，记录交互、错误和网络事件，便于排查问题。
- **主题引擎 (Theme Engine):** 全面的界面自定义，支持导入/导出 `.json` 设计。
- **自动优化:** 按 IP/端口清理重复项，TCP/HTTP 延迟测试后移除失效节点，并自动修复损坏的链接。

## 🔌 支持的协议

`VLESS` (Reality/Vision) • `VMess` • `Trojan` • `Hysteria2` • `SS/SSR` • `WireGuard` • `TUIC` • `Socks5` • `HTTP`

## ⭐ 支持项目

**如果这个项目对您有帮助，请给它点个 Star！** :star2:

## 📈 Star 历史

[![Stargazers over time](https://starchart.cc/jinxpil/flclash-converter.svg?variant=adaptive)](https://starchart.cc/jinxpil/flclash-converter)
