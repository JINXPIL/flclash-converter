[English](/README.en.md) | [Русский](/README.md) | [简体中文](/README.zh.md)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/logo-dark.png">
    <img alt="Network Builder" src="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/logo-light.png" width="300">
  </picture>
</p>

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

**Network Builder** 是一个高级的 100% 本地运行的 Web 工具（单文件 HTML / 原生 JS），专门用于管理、测试和转换代理节点。它提供了一个用户友好的界面，可以解析来自任何来源的节点，并瞬间生成适用于 FlClash、Nekobox (Xray) 和 Sing-box 的深度优化路由配置文件。

> [!IMPORTANT]
> **仅供学习交流使用。** 本项目仅为研究和教育目的而创建。请勿将其用于任何非法用途。作者对本工具的任何滥用不承担任何责任。所有数据计算均严格在您的浏览器中本地完成（零信任安全）。

作为一个强大的网络工具，Network Builder 无需依赖后端服务器即可提供极高的性能，支持 10 多种协议，并提供深度的界面自定义功能。

### 📸 界面截图

<p align="center">
  <img src="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/JSON%20to%20YAML%20Converter.jpg" alt="JSON to YAML" width="48%">
  <img src="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/Yaml%20Code%20Formatter.jpg" alt="YAML Formatter" width="48%">
</p>

## 🚀 快速开始

👉 **[打开网页版](https://jinxpil.github.io/flclash-converter/)** *(支持 PWA，可直接添加到手机主屏幕)*

或者从 [Releases](https://github.com/jinxpil/flclash-converter/releases) 下载最新的 `index.html` 并在浏览器中打开。完全支持离线运行。

## 🔥 核心功能

- **零信任安全 (Zero-Trust Security):** 无第三方服务器参与。数据在内存中处理，关闭标签页即焚。
- **全能解析器 (Omni-Parser):** 瞬间解码 Base64 订阅、JSON 配置逆向工程，并支持拖拽 (Drag & Drop) 导入文件。
- **批量编辑 & 智能 GeoIP:** 批量修改节点参数（SNI、Flow、Fingerprint），自动解析节点地理位置并添加国旗 emoji (🇫🇮, 🇩🇪)。
- **诊断日志 (Diagnostic Logger):** 内置后台调试系统，记录交互、错误和网络事件，方便排查故障。
- **主题引擎 (Theme Engine):** 全面的界面定制功能，支持导入和导出 `.json` 设计配置。
- **自动优化:** 清理 IP/端口重复项，通过 TCP/HTTP 延迟测试自动删除失效服务器，并自动修复损坏的链接。

## 🔌 协议支持

`VLESS` (Reality/Vision) • `VMess` • `Trojan` • `Hysteria2` • `SS/SSR` • `WireGuard` • `TUIC` • `Socks5` • `HTTP`

## ⭐ 支持项目

**如果这个项目对您有帮助，请给它一个星星！** :star2:

## 📈 星星历史趋势

[![Stargazers over time](https://starchart.cc/jinxpil/flclash-converter.svg?variant=adaptive)](https://starchart.cc/jinxpil/flclash-converter)
