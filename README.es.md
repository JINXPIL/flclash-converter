<p align="center">
  <a href="/README.en.md">🇺🇸 English</a> •
  <a href="/README.md">🇷🇺 Русский</a> •
  <a href="/README.zh.md">🇨🇳 简体中文</a> •
  <a href="/README.zh-TW.md">🇹🇼 繁體中文</a> •
  <a href="/README.fa.md">🇮🇷 فارسی</a> •
  <a href="/README.es.md"><b>🇪🇸 Español</b></a>
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
  <b>Una herramienta web extremadamente potente y 100% local para gestionar bases de datos gigantes de servidores proxy.</b><br>
  <i>Análisis, conversión y profunda optimización de configuraciones para FlClash, Exclave, Sing-box y Clash Meta.</i>
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
    <img src="https://img.shields.io/badge/🚀_ABRIR_VERSIÓN_ULTRA-0052FF?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Open Web Version">
  </a>
</p>

<p align="center">
  🤖 <b>También echa un vistazo a mi segundo proyecto:</b><br>
  👉 <a href="https://github.com/JINXPIL/json-yaml-ai"><b>JSON-YAML-AI</b></a> 👈
</p>

> [!IMPORTANT]
> **Zero-Trust y Privacidad Primero.** Todos los cálculos se realizan estrictamente de forma local en tu navegador. Ningún dato sale de tu dispositivo. Esta herramienta fue creada exclusivamente con fines educativos para el estudio profundo de los protocolos de red.

> [!WARNING]
> **Atención: problema con las suscripciones YAML y tiempos de espera (Timeout):**
> Muchos proveedores de VPN restringen intencionalmente (o debido a una configuración de API deficiente) la exportación de suscripciones por parte de clientes de terceros. Los servidores pueden cargarse correctamente en tu lista, pero al intentar conectarse, entran en un tiempo de espera infinito.
> 💡 **Cómo comprobar quién es el culpable:** Si tomas un enlace "sin procesar" al mismo nodo exacto (por ejemplo, `vless://...` o código JSON), lo agregas manualmente como perfil local y **funciona** — el problema es 100% del proveedor. Esto significa que su servidor bloquea las solicitudes de tu cliente según el `User-Agent` al intentar actualizar la suscripción. En otros casos, los tiempos de espera pueden deberse a un bloqueo preciso de las firmas de los protocolos por parte de tu cortafuegos.

---

### 📸 Interfaz (Diseño ULTRA)

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

### 🔥 ¿Qué hay de nuevo en la versión 17.05 ULTRA? (La Perfección HighLoad)

* 🌐 **Expansión Masiva de Protocolos:** Se añadió soporte completo para el análisis de **VMess, Hysteria2 (hy2), Shadowsocks (SS) y ShadowsocksR (SSR)**.
* 🚀 **Rendimiento Extremo (HighLoad):** Implementación de procesamiento asíncrono (Chunking) y diccionarios `Set`. ¡La virtualización del DOM permite cargar y eliminar duplicados de **más de 250,000 nodos** en milisegundos sin congelar tu navegador!
* 🛡️ **Sanitizador YAML a Prueba de Balas:** Control de calidad industrial. El script destruye automáticamente la basura de las listas públicas (caracteres ASCII invisibles, cifrados `2022-blake3` falsos, contraseñas vacías) y garantiza una importación 100% estable en Mihomo.
* ⚙️ **Derrotando los Timeouts:** El generador YAML ha sido reescrito bajo los estrictos estándares de Mihomo (se añadió `alpn`, `skip-cert-verify: true`, `servername` y un enrutador Fake-IP DNS mejorado).
* 🎨 **Nueva UI/UX:** Temas Claro/Oscuro separados con guardado independiente de colores personalizados, y un **Interruptor de "Modo Suscripción"** para incrustar enlaces RAW (Pastebin/GitHub) directamente en el bloque `proxy-providers`.

---

### 🔌 Protocolos Soportados

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

### 🎯 Configuraciones y Enrutamiento (Preajustes)

Para no saturar la página con bloques de código, todos los preajustes listos para usar se han trasladado a archivos separados del repositorio.

* 🌐 **Túnel Dividido para Happ** — Preajuste de reglas optimizado, construido a través de `routing.happ.su`. Diseñado **estrictamente** para el cliente Happ.
    * 📄 Enlace del archivo de configuración: [`./rus_vp_happ.json`](./rus_vp_happ.json)
    * 🔗 Enlace de importación para el cliente: `https://raw.githubusercontent.com/JINXPIL/flclash-converter/refs/heads/main/rus_vp_happ.json`
* 🛠️ **Configuración YAML Optimizada (Mihomo/Clash)** — v79.0 Ultimate con huellas dactilares estrictas de navegadores TLS y protección contra analizadores DPI.
    * 📄 Enlace del archivo de configuración: [`./GL_Crimea_ipv6_yan(9.35).yml`](./GL_Crimea_ipv6_yan(9.35).yml)
    * 🔗 Enlace de importación para el cliente: `https://raw.githubusercontent.com/JINXPIL/flclash-converter/refs/heads/main/GL_Crimea_ipv6_yan(9.35).yml`

---
> [!NOTE]
> Clientes populares como **NekoBox** y **NekoRay** se consideran obsoletos en la actualidad. Se recomienda migrar a alternativas modernas y optimizadas basadas en los núcleos más recientes de **sing-box** y **Xray** (por ejemplo, **Exclave**, que replica completamente la interfaz de NekoBox, o **Incy**).

<details>
<summary><b>🤖 Android</b></summary>

* [v2RayTun](https://v2raytun.com/) — Cliente de alta velocidad y seguro basado en Xray Core.
* [FlClash](https://github.com/chen08209/FlClash) — El principal cliente multiplataforma.
* [Incy](https://incy.cc/) — Cliente moderno y rápido con importación con un solo toque.
* [Happ](https://www.happ.su/main) — Utilidad proxy para la gestión conveniente de listas de servidores.
* [Exclave](https://github.com/ExclaveNetwork/Exclave) — Reemplazo moderno para NekoBox con una interfaz familiar.
* [Sing-box](https://github.com/SagerNet/sing-box) — Núcleo limpio oficial para configuración avanzada.
* [Hiddify App](https://github.com/hiddify/hiddify-app) — Cliente universal para cualquier tipo de configuración.
* [v2rayNG](https://github.com/2dust/v2rayNG) — Solución clásica y estable para el núcleo Xray.
* [Karing](https://github.com/KaringX/karing) — Interfaz gráfica rica en funciones.
* [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
* ~~[NekoBox For Android](https://github.com/MatsuriDayo/NekoBoxForAndroid)~~ *(Obsoleto)*
</details>

<details>
<summary><b>🍏 iOS</b></summary>

* [v2RayTun](https://v2raytun.com/) — Cliente de alta velocidad y seguro basado en Xray Core.
* [Incy](https://incy.cc/) — Gran cliente moderno en la App Store.
* [Happ](https://www.happ.su/main) — Utilidad proxy cómoda.
* [Karing](https://apps.apple.com/us/app/karing/id6472431552)
* [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
* [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)
* [Clash Lite](https://apps.apple.com/us/app/clash-lite/id6761357475)
* [V2Lite VPN](https://apps.apple.com/us/app/v2lite-vpn-super-vpn-proxy/id6444585377)
</details>

<details>
<summary><b>💻 Desktop (Win/Mac/Linux)</b></summary>

* [v2RayTun](https://v2raytun.com/) — Cliente de alta velocidad y seguro basado en Xray Core.
* [Happ](https://www.happ.su/main) — Versión de escritorio multiplataforma.
* [v2rayN](https://github.com/2dust/v2rayN) — Potente cliente personalizable para Windows.
* [FlClash](https://github.com/chen08209/FlClash) — Interfaz gráfica minimalista y rápida.
* [Karing](https://github.com/KaringX/karing)
* [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)
* ~~[NekoRay](https://github.com/MatsuriDayo/nekoray)~~ *(Obsoleto)*
</details>

---

### 🛡️ Herramientas Alternativas (DPI Bypass)

*Si los protocolos VPN estándar están completamente bloqueados por tu ISP o firewall, usa herramientas locales para eludir la Inspección Profunda de Paquetes:*

* [Zapret](https://github.com/bol-van/zapret) — La herramienta más potente y flexible para evitar el DPI a nivel del sistema.
* [Zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) — Scripts optimizados y listos para usar para servicios populares específicos.
* [ByeByeDPI](https://github.com/romanvht/ByeByeDPI) — Una solución clásica y comprobada para ejecución local en Android.

---

### ⭐ Apoya el Proyecto

**Si Network Builder ULTRA te ha ayudado, ¡por favor no olvides dejar una estrella! Esto motiva el desarrollo continuo del proyecto.** :star2:

[![Star History Chart](https://api.star-history.com/svg?repos=jinxpil/flclash-converter&type=Date)](https://star-history.com/#jinxpil/flclash-converter&Date)
