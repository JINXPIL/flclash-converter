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
  <b>Herramienta web avanzada 100% local (HTML de un solo archivo / Vanilla JS) para administrar, probar y convertir servidores proxy.</b><br>
  <i>Proporciona una interfaz conveniente para analizar nodos de cualquier fuente y generar instantáneamente perfiles de enrutamiento optimizados para FlClash, Nekobox (Xray) y Sing-box.</i>
</p>

<p align="center">
  <a href="https://jinxpil.github.io/flclash-converter/">
    <img src="https://img.shields.io/badge/🚀_ABRIR_VERSIÓN_WEB-0052FF?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Open Web Version">
  </a>
</p>

> [!IMPORTANT]
> **Solo para fines educativos.** Este proyecto fue creado exclusivamente para fines de investigación. Por favor, no lo use para fines ilegales. El autor no se hace responsable del mal uso de esta herramienta. Todos los cálculos se realizan estrictamente de forma local en su navegador (Zero-Trust).

---

### 📸 Interfaz (Adaptativa)

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

### 🔌 Protocolos compatibles

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

### 📥 Clientes recomendados

<details>
<summary><b>🤖 Mostrar clientes para Android</b></summary>

- [FlClash](https://github.com/chen08209/FlClash)
- [Karing](https://github.com/KaringX/karing)
- [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
- [FlClashX](https://github.com/pluralplay/FlClashX)
</details>

<details>
<summary><b>🍏 Mostrar clientes para iOS</b></summary>

- [Karing](https://apps.apple.com/us/app/karing/id6472431552)
- [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
- [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)
</details>

<details>
<summary><b>💻 Mostrar clientes para PC (Windows / macOS / Linux)</b></summary>

- [Karing](https://github.com/KaringX/karing)
- [FlClash](https://github.com/chen08209/FlClash)
- [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)
</details>

---

### 🔥 Características principales

- 🛡️ **Seguridad Zero-Trust:** Sin servidores de terceros. Los datos se procesan en la memoria RAM y se destruyen al cerrar la pestaña.
- 🧩 **Omni-Parser:** Decodificación instantánea de suscripciones Base64, ingeniería inversa de configuraciones JSON y soporte de Drag & Drop.
- 🌍 **Editor masivo y Smart GeoIP:** Modificación por lotes de parámetros (SNI, Flow, Fingerprint) y autodetección de la geolocalización de los nodos con banderas (🇫🇮, 🇩🇪).
- 🐛 **Registro de diagnóstico:** Sistema de depuración en segundo plano incorporado que registra interacciones, errores y eventos de red para facilitar la resolución de problemas.
- 🎨 **Motor de temas:** Personalización completa de la interfaz de usuario con la capacidad de importar/exportar diseños a `.json`.
- ⚙️ **Auto-optimización:** Limpieza de duplicados por IP/puerto, eliminación de servidores inactivos después del ping TCP/HTTP y recuperación automática de enlaces rotos.

---

### ⭐ Apoya el proyecto

**Si este proyecto te ha resultado útil, ¡por favor dale una estrella!** :star2:

[![Stargazers over time](https://starchart.cc/jinxpil/flclash-converter.svg?variant=adaptive)](https://starchart.cc/jinxpil/flclash-converter)
