<p align="center">
  <a href="/README.en.md"><b>🇺🇸 English</b></a> •
  <a href="/README.md">🇷🇺 Русский</a> •
  <a href="/README.zh.md">🇨🇳 简体中文</a> •
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
  <b>Extremely powerful and 100% local web tool for managing massive proxy server databases.</b><br>
  <i>Parsing, conversion, and deep optimization of configurations for FlClash, Exclave, Sing-box, and Clash Meta.</i>
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
    <img src="https://img.shields.io/badge/🚀_OPEN_ULTRA_VERSION-0052FF?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Open Web Version">
  </a>
</p>

<p align="center">
  🤖 <b>Also, check out my second project:</b><br>
  👉 <a href="https://github.com/JINXPIL/json-yaml-ai"><b>JSON-YAML-AI</b></a> 👈
</p>

> [!IMPORTANT]
> **Zero-Trust & Privacy First.** All computations are performed strictly locally in your browser. No data ever leaves your device. The tool is created exclusively for educational purposes and deep analysis of network protocols.

> [!WARNING]
> **Warning regarding YAML subscriptions and Timeouts:**
> Many VPN providers intentionally (or due to incompetent API setup) restrict third-party clients when exporting subscriptions. Servers may load successfully into your list, but attempting to connect results in an endless timeout.
> 💡 **How to check who is at fault:** If you take a "raw" link to the same node (e.g., `vless://...` or JSON code), add it manually as a local profile, and **it works** — the issue is 100% on the provider's side. This means their server is blocking your client's requests by `User-Agent` when trying to update the subscription. In other cases, timeouts might be caused by targeted protocol signature blocking by your ISP/DPI.

---

### 📸 Interface (ULTRA Design)

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

### 🔥 What's new in version 17.05 ULTRA? (The HighLoad Perfection)

* 🌐 **Global Protocol Expansion:** Added full parsing support for **VMess, Hysteria2 (hy2), Shadowsocks (SS), and ShadowsocksR (SSR)**.
* 🚀 **Extreme Performance (HighLoad):** Implemented asynchronous chunking and `Set` dictionaries. DOM virtualization allows loading and deduplicating **250,000+ nodes** in milliseconds without freezing the browser!
* 🛡️ **Armor-Piercing YAML Sanitizer:** Industrial-grade Face-Control. The script automatically destroys garbage from public lists (invisible ASCII characters, fake `2022-blake3` ciphers, empty passwords) and guarantees 100% stable import into Mihomo.
* ⚙️ **Victory Over Timeouts:** The YAML generator has been rewritten to meet strict Mihomo standards (added `alpn`, `skip-cert-verify: true`, `servername`, and enhanced Fake-IP DNS).
* 🎨 **New UI/UX:** Separate light/dark themes with independent color saving and a **"Subscription Mode" Toggle** for direct embedding of RAW links (Pastebin/GitHub) into the `proxy-providers` block.

---

### 🔌 Supported Protocols

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

### 🎯 Ready-to-use Presets

To avoid cluttering the page with code, all ready-made presets have been moved to separate folders named after the clients.

<table width="100%">
<thead><tr><th align="left">Platform</th><th align="left">Configuration</th><th align="left">Import Link</th></tr></thead>
<tbody>
<tr>
  <td><b>Happ (Routing)</b></td>
  <td>Optimized for RU regions, embedded AdBlock</td>
  <td>
    <a href="https://jinxpil.github.io/flclash-converter/happ.html">⚡ Fast Install (1-Click)</a><br>
    <a href="https://raw.githubusercontent.com/JINXPIL/flclash-converter/main/HAPP/DEFAULT.json">📄 View Code (JSON)</a>
  </td>
</tr>
<tr>
  <td><b>INCY (Routing)</b></td>
  <td>Optimized for RU regions, embedded AdBlock</td>
  <td>
    <a href="https://jinxpil.github.io/flclash-converter/incy.html">⚡ Fast Install (1-Click)</a><br>
    <a href="https://raw.githubusercontent.com/JINXPIL/flclash-converter/main/INCY/DEFAULT.json">📄 View Code (JSON)</a>
  </td>
</tr>
<tr>
  <td><b>Mihomo / Clash Meta</b></td>
  <td>v79.0 Ultimate (DPI evasion, strict TLS fingerprints)</td>
  <td><a href="https://raw.githubusercontent.com/JINXPIL/flclash-converter/main/MIHOMO/ULTIMATE.yml">🔗 Import YML Config</a></td>
</tr>
</tbody>
</table>

---

### 🚦 What's Inside the Routing (Rules)

Reliable "surgical" split-tunneling so that required resources load without delays, while blocked ones become accessible.

<table width="100%">
<tbody>
<tr>
  <td>🔴 <b>BLOCK</b></td>
  <td>Ads, trackers, telemetry (saves server traffic and device battery).</td>
</tr>
<tr>
  <td>🟢 <b>DIRECT</b></td>
  <td>Local ISPs, Domestic Banks, Government services (ideal low ping, no bans from banks for suspicious IPs).</td>
</tr>
<tr>
  <td>🔵 <b>PROXY</b></td>
  <td>YouTube, Instagram, ChatGPT, foreign CDNs, and all other blocked traffic.</td>
</tr>
</tbody>
</table>

---

### 🛡️ DNS Settings

<table width="100%">
<thead><tr><th align="center">Purpose</th><th align="left">Server</th><th align="left">Why</th></tr></thead>
<tbody>
<tr>
  <td align="center">🏠 <b>DIRECT (Domestic)</b></td>
  <td><a href="https://dns.yandex.ru/">Yandex DNS</a> <code>77.88.8.8</code></td>
  <td>Fast resolving of internal resources, low ping locally, works without an active VPN.</td>
</tr>
<tr>
  <td align="center">🌍 <b>PROXY (Foreign)</b></td>
  <td><a href="https://developers.cloudflare.com/1.1.1.1/">Cloudflare</a> / <a href="https://developers.google.com/speed/public-dns/">Google</a></td>
  <td>Reliable resolving for proxied traffic, protection against DNS spoofing by local ISPs.</td>
</tr>
</tbody>
</table>

---
> [!NOTE]
> Popular clients such as **NekoBox** and **NekoRay** are currently considered deprecated. It is recommended to switch to modern and optimized alternatives based on the latest **sing-box** and **Xray** cores (e.g., **Exclave**, which fully replicates the NekoBox interface, or **Incy**).

<details>
<summary><b>🤖 Android</b></summary>

* [v2RayTun](https://v2raytun.com/) — High-speed and secure client based on Xray Core.
* [FlClash](https://github.com/chen08209/FlClash) — Main cross-platform client.
* [Incy](https://incy.cc/) — Modern, fast client with one-tap import.
* [Happ](https://www.happ.su/main) — Proxy utility for convenient server list management.
* [Exclave](https://github.com/ExclaveNetwork/Exclave) — Modern alternative to NekoBox with a familiar UI.
* [Sing-box](https://github.com/SagerNet/sing-box) — Official clean core for advanced configuration.
* [Hiddify App](https://github.com/hiddify/hiddify-app) — Universal client for any configuration types.
* [v2rayNG](https://github.com/2dust/v2rayNG) — Stable classic solution for the Xray core.
* [Karing](https://github.com/KaringX/karing) — Feature-rich GUI.
* [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
* ~~[NekoBox For Android](https://github.com/MatsuriDayo/NekoBoxForAndroid)~~ *(Deprecated)*
</details>

<details>
<summary><b>🍏 iOS</b></summary>

* [v2RayTun](https://v2raytun.com/) — High-speed and secure client based on Xray Core.
* [Incy](https://incy.cc/) — Excellent modern client in the App Store.
* [Happ](https://www.happ.su/main) — Comfortable proxy utility.
* [Karing](https://apps.apple.com/us/app/karing/id6472431552)
* [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
* [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)
* [Clash Lite](https://apps.apple.com/us/app/clash-lite/id6761357475)
* [V2Lite VPN](https://apps.apple.com/us/app/v2lite-vpn-super-vpn-proxy/id6444585377)
</details>

<details>
<summary><b>💻 Desktop (Win/Mac/Linux)</b></summary>

* [v2RayTun](https://v2raytun.com/) — High-speed and secure client based on Xray Core.
* [Happ](https://www.happ.su/main) — Cross-platform desktop version.
* [v2rayN](https://github.com/2dust/v2rayN) — Powerful customizable client for Windows.
* [FlClash](https://github.com/chen08209/FlClash) — Minimalistic and fast GUI.
* [Karing](https://github.com/KaringX/karing)
* [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)
* ~~[NekoRay](https://github.com/MatsuriDayo/nekoray)~~ *(Deprecated)*
</details>

---

### 🛡️ Alternative Tools (DPI Bypass)

*If standard VPN protocols are completely blocked by your ISP or DPI, use local deep packet inspection bypass tools:*

* [Zapret](https://github.com/bol-van/zapret) — The most powerful and flexible tool for deep DPI bypass at the system level.
* [Zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) — Optimized and configured ready-made scripts for specific popular services.
* [ByeByeDPI](https://github.com/romanvht/ByeByeDPI) — Proven classic solution for local execution on Android.

---

### ⭐ Support the Project

**If Network Builder ULTRA helped you, don't forget to leave a star! This motivates further development of the project.** :star2:

[![Star History Chart](https://api.star-history.com/svg?repos=JINXPIL/flclash-converter&type=Date)](https://star-history.com/#JINXPIL/flclash-converter&Date)