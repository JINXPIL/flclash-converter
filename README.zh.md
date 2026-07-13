<p align="center">
  <a href="/README.en.md">🇺🇸 English</a> •
  <a href="/README.md">🇷🇺 Русский</a> •
  <a href="/README.zh.md"><b>🇨🇳 简体中文</b></a> •
  <a href="/README.zh-TW.md">🇹🇼 繁體中文</a> •
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
  <b>极其强大的 100% 本地 Web 工具，用于管理海量代理服务器数据库。</b><br>
  <i>为 FlClash、Exclave、Sing-box 和 Clash Meta 提供配置解析、转换和深度优化。</i>
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
  🤖 <b>另请关注我的第二个项目：</b><br>
  👉 <a href="https://github.com/JINXPIL/json-yaml-ai"><b>JSON-YAML-AI</b></a> 👈
</p>

> [!IMPORTANT]
> **零信任与隐私至上。** 所有计算严格在您的浏览器本地进行。没有任何数据会离开您的设备。该工具专为教育目的和深度网络协议分析而创建。

> [!WARNING]
> **关于 YAML 订阅和超时 (Timeout) 的警告：**
> 许多 VPN 提供商在导出订阅时故意（或由于 API 设置不当）限制第三方客户端。服务器可能成功加载到您的列表中，但在尝试连接时会导致无限超时。
> 💡 **如何检查问题所在：** 如果您获取同一节点的“原始”链接（例如 `vless://...` 或 JSON 代码），将其作为本地配置文件手动添加，并且 **它可以正常工作** — 那么问题 100% 出在提供商那边。这意味着他们的服务器在尝试更新订阅时通过 `User-Agent` 阻止了您的客户端请求。在其他情况下，超时可能是由于您的 ISP (DPI) 针对协议签名进行了定向封锁。

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

### 🔥 17.05 ULTRA 版本有什么新功能？ (The HighLoad Perfection)

* 🌐 **全球协议扩展：** 增加了对 **VMess, Hysteria2 (hy2), Shadowsocks (SS) 和 ShadowsocksR (SSR)** 的完整解析支持。
* 🚀 **极限性能 (HighLoad)：** 引入了异步分块和 `Set` 字典。DOM 虚拟化允许在几毫秒内加载和去重 **250,000+ 个节点**，而不会使浏览器崩溃！
* 🛡️ **穿甲级 YAML 净化器：** 工业级面部识别控制。脚本自动销毁公共列表中的垃圾（不可见的 ASCII 字符，伪造的 `2022-blake3` 密码，空密码），并保证 100% 稳定导入 Mihomo。
* ⚙️ **战胜超时：** YAML 生成器已被重写以满足严格的 Mihomo 标准（添加了 `alpn`, `skip-cert-verify: true`, `servername` 和增强的 Fake-IP DNS）。
* 🎨 **全新的 UI/UX：** 独立的浅色/深色主题以及独立的颜色保存，以及一个 **“订阅模式”切换开关**，用于将 RAW 链接（Pastebin/GitHub）直接嵌入到 `proxy-providers` 块中。

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

### 🎯 开箱即用的预设

为了避免页面充满代码，所有现成的预设都已移至以客户端命名的单独文件夹中。

<table width="100%">
<thead><tr><th align="left">平台</th><th align="left">配置</th><th align="left">导入链接</th></tr></thead>
<tbody>
<tr>
  <td><b>Happ (Routing)</b></td>
  <td>专为俄罗斯地区优化，内置广告拦截</td>
  <td>
    <a href="https://jinxpil.github.io/flclash-converter/happ.html">⚡ 快速安装 (一键)</a><br>
    <a href="https://raw.githubusercontent.com/JINXPIL/flclash-converter/main/HAPP/DEFAULT.json">📄 查看代码 (JSON)</a>
  </td>
</tr>
<tr>
  <td><b>INCY (Routing)</b></td>
  <td>专为俄罗斯地区优化，内置广告拦截</td>
  <td>
    <a href="https://jinxpil.github.io/flclash-converter/incy.html">⚡ 快速安装 (一键)</a><br>
    <a href="https://raw.githubusercontent.com/JINXPIL/flclash-converter/main/INCY/DEFAULT.json">📄 查看代码 (JSON)</a>
  </td>
</tr>
<tr>
  <td><b>Mihomo / Clash Meta</b></td>
  <td>v79.0 Ultimate (DPI 规避, 严格的 TLS)</td>
  <td><a href="https://raw.githubusercontent.com/JINXPIL/flclash-converter/main/MIHOMO/ULTIMATE.yml">🔗 导入 YML 配置</a></td>
</tr>
</tbody>
</table>

---

### 🚦 路由规则内部逻辑

可靠的“外科手术式”分流，以便所需资源无延迟加载，而受阻的资源变得可访问。

<table width="100%">
<tbody>
<tr>
  <td>🔴 <b>BLOCK (阻止)</b></td>
  <td>广告，追踪器，遥测（节省服务器流量和设备电池）。</td>
</tr>
<tr>
  <td>🟢 <b>DIRECT (直连)</b></td>
  <td>本地 ISP，国内银行，政府服务（理想的低延迟，银行不会因可疑 IP 封禁）。</td>
</tr>
<tr>
  <td>🔵 <b>PROXY (代理)</b></td>
  <td>YouTube, Instagram, ChatGPT, 国外 CDN 和所有其他被封锁的流量。</td>
</tr>
</tbody>
</table>

---

### 🛡️ DNS 设置

<table width="100%">
<thead><tr><th align="center">目的</th><th align="left">服务器</th><th align="left">原因</th></tr></thead>
<tbody>
<tr>
  <td align="center">🏠 <b>DIRECT (国内)</b></td>
  <td><a href="https://dns.yandex.ru/">Yandex DNS</a> <code>77.88.8.8</code></td>
  <td>快速解析内部资源，本地延迟低，无需激活 VPN 即可工作。</td>
</tr>
<tr>
  <td align="center">🌍 <b>PROXY (国外)</b></td>
  <td><a href="https://developers.cloudflare.com/1.1.1.1/">Cloudflare</a> / <a href="https://developers.google.com/speed/public-dns/">Google</a></td>
  <td>代理流量的可靠解析，防止本地 ISP 的 DNS 欺骗。</td>
</tr>
</tbody>
</table>

---
> [!NOTE]
> 诸如 **NekoBox** 和 **NekoRay** 之类的流行客户端目前已被视为过时。建议切换到基于最新 **sing-box** 和 **Xray** 核心的现代和优化替代方案（例如，完全复制 NekoBox 界面的 **Exclave**，或 **Incy**）。

<details>
<summary><b>🤖 Android</b></summary>

* [v2RayTun](https://v2raytun.com/) — 基于 Xray Core 的高速安全客户端。
* [FlClash](https://github.com/chen08209/FlClash) — 主要的跨平台客户端。
* [Incy](https://incy.cc/) — 现代，快速的客户端，支持一键导入。
* [Happ](https://www.happ.su/main) — 用于方便管理服务器列表的代理实用程序。
* [Exclave](https://github.com/ExclaveNetwork/Exclave) — NekoBox 的现代替代品，具有熟悉的 UI。
* [Sing-box](https://github.com/SagerNet/sing-box) — 官方纯净核心，用于高级配置。
* [Hiddify App](https://github.com/hiddify/hiddify-app) — 适用于任何配置类型的通用客户端。
* [v2rayNG](https://github.com/2dust/v2rayNG) — Xray 核心的稳定经典解决方案。
* [Karing](https://github.com/KaringX/karing) — 功能丰富的 GUI。
* [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
* ~~[NekoBox For Android](https://github.com/MatsuriDayo/NekoBoxForAndroid)~~ *(已弃用)*
</details>

<details>
<summary><b>🍏 iOS</b></summary>

* [v2RayTun](https://v2raytun.com/) — 基于 Xray Core 的高速安全客户端。
* [Incy](https://incy.cc/) — App Store 中优秀的现代客户端。
* [Happ](https://www.happ.su/main) — 舒适的代理实用程序。
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
* [FlClash](https://github.com/chen08209/FlClash) — 极简且快速的 GUI。
* [Karing](https://github.com/KaringX/karing)
* [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)
* ~~[NekoRay](https://github.com/MatsuriDayo/nekoray)~~ *(已弃用)*
</details>

---

### 🛡️ 替代工具 (DPI 绕过)

*如果标准 VPN 协议被您的 ISP 或 DPI 完全封锁，请使用本地深度数据包检测绕过工具：*

* [Zapret](https://github.com/bol-van/zapret) — 在系统层面进行深度 DPI 绕过的最强大，最灵活的工具。
* [Zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) — 针对特定热门服务优化和配置的现成脚本。
* [ByeByeDPI](https://github.com/romanvht/ByeByeDPI) — 在 Android 上本地执行的经过验证的经典解决方案。

---

### ⭐ 支持该项目

**如果 Network Builder ULTRA 帮助了您，请不要忘记留下一颗星！这会激发该项目的进一步发展。** :star2:

[![Star History Chart](https://api.star-history.com/svg?repos=JINXPIL/flclash-converter&type=Date)](https://star-history.com/#JINXPIL/flclash-converter&Date)