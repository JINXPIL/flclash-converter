<p align="center">
  <a href="/README.en.md">🇺🇸 English</a> •
  <a href="/README.md">🇷🇺 Русский</a> •
  <a href="/README.zh.md">🇨🇳 简体中文</a> •
  <a href="/README.zh-TW.md">🇹🇼 繁體中文</a> •
  <a href="/README.fa.md">🇮🇷 فارسی</a> •
  <a href="/README.es.md"><b>🇪🇸 Español</b></a>
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
  <b>Herramienta web extremadamente potente y 100% local para gestionar bases de datos masivas de servidores proxy.</b><br>
  <i>Análisis, conversión y optimización profunda de configuraciones para FlClash, Exclave, Sing-box y Clash Meta.</i>
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
    <img src="https://img.shields.io/badge/🚀_ABRIR_LA_VERSIÓN_ULTRA-0052FF?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Open Web Version">
  </a>
</p>

<p align="center">
  🤖 <b>También echa un vistazo a mi segundo proyecto:</b><br>
  👉 <a href="https://github.com/JINXPIL/json-yaml-ai"><b>JSON-YAML-AI</b></a> 👈
</p>

> [!IMPORTANT]
> **Zero-Trust y privacidad primero.** Todos los cálculos se realizan estrictamente de forma local en tu navegador. Ningún dato sale de tu dispositivo. La herramienta fue creada exclusivamente con fines educativos y para el análisis profundo de protocolos de red.

> [!WARNING]
> **Advertencia: problema con las suscripciones YAML y los tiempos de espera (Timeout):**
> Muchos proveedores de VPN restringen intencionalmente (o debido a una configuración de API incompetente) el uso de clientes de terceros al exportar suscripciones. Los servidores pueden cargarse correctamente en tu lista, pero al intentar conectarse, entran en un tiempo de espera infinito. 
> 💡 **Cómo comprobar quién tiene la culpa:** Si tomas un enlace "crudo" al mismo nodo (por ejemplo, `vless://...` o código JSON), lo agregas manualmente como un perfil local, y **funciona** — el problema es 100% del lado del proveedor. Esto significa que su servidor está bloqueando las solicitudes de tu cliente a través del `User-Agent` al intentar actualizar la suscripción. En otros casos, los tiempos de espera pueden deberse a bloqueos específicos de firmas de protocolos por parte de tu proveedor de Internet (DPI).

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

### 🔥 ¿Qué hay de nuevo en la versión 17.05 ULTRA? (The HighLoad Perfection)

* 🌐 **Expansión global de protocolos:** Se agregó soporte completo para el análisis de **VMess, Hysteria2 (hy2), Shadowsocks (SS) y ShadowsocksR (SSR)**.
* 🚀 **Rendimiento extremo (HighLoad):** Se implementó la fragmentación asíncrona (chunking) y diccionarios de tipo `Set`. ¡La virtualización del DOM permite cargar y deduplicar **más de 250.000 nodos** en milisegundos sin congelar el navegador!
* 🛡️ **Sanitizador YAML antibalas:** Control de seguridad a nivel industrial. El script destruye automáticamente la basura de las listas públicas (caracteres ASCII invisibles, cifrados falsos `2022-blake3`, contraseñas vacías) y garantiza una importación 100% estable en Mihomo.
* ⚙️ **Victoria sobre los tiempos de espera:** El generador de YAML fue reescrito bajo los estrictos estándares de Mihomo (se agregaron `alpn`, `skip-cert-verify: true`, `servername` y DNS Fake-IP mejorado).
* 🎨 **Nuevo UI/UX:** Tema claro/oscuro separado con guardado independiente de colores y un **interruptor de "Modo de suscripción"** para incrustar directamente enlaces RAW (Pastebin/GitHub) en el bloque `proxy-providers`.

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
    <td align="center">🔌 <b>TUIC / Socks5 / HTTP</b><br>Full Support</td>
  </tr>
</table>

---

### 🎯 Ajustes preestablecidos listos para usar

Para no saturar la página con código, todos los ajustes preestablecidos se han movido a carpetas separadas según el nombre del cliente.

<table width="100%">
<thead><tr><th align="left">Plataforma</th><th align="left">Configuración</th><th align="left">Enlace de importación</th></tr></thead>
<tbody>
<tr>
  <td><b>Happ (Routing)</b></td>
  <td>Optimizado para la región, AdBlock integrado</td>
  <td>
    <a href="https://jinxpil.github.io/flclash-converter/happ.html">⚡ Instalación rápida (1 clic)</a><br>
    <a href="https://raw.githubusercontent.com/JINXPIL/flclash-converter/main/HAPP/DEFAULT.json">📄 Ver código (JSON)</a>
  </td>
</tr>
<tr>
  <td><b>INCY (Routing)</b></td>
  <td>Optimizado para la región, AdBlock integrado</td>
  <td>
    <a href="https://jinxpil.github.io/flclash-converter/incy.html">⚡ Instalación rápida (1 clic)</a><br>
    <a href="https://raw.githubusercontent.com/JINXPIL/flclash-converter/main/INCY/DEFAULT.json">📄 Ver código (JSON)</a>
  </td>
</tr>
<tr>
  <td><b>Mihomo / Clash Meta</b></td>
  <td>v79.0 Ultimate (Evasión de DPI, huellas TLS estrictas)</td>
  <td><a href="https://raw.githubusercontent.com/JINXPIL/flclash-converter/main/MIHOMO/ULTIMATE.yml">🔗 Importar configuración YML</a></td>
</tr>
</tbody>
</table>

---

### 🚦 ¿Qué incluye el enrutamiento? (Reglas)

Túnel dividido (split-tunneling) "quirúrgico" y confiable para que los recursos necesarios carguen sin demoras y los bloqueados se vuelvan accesibles.

<table width="100%">
<tbody>
<tr>
  <td>🔴 <b>BLOCK (Bloquear)</b></td>
  <td>Anuncios, rastreadores, telemetría (ahorra tráfico del servidor y batería del dispositivo).</td>
</tr>
<tr>
  <td>🟢 <b>DIRECT (Directo)</b></td>
  <td>Proveedores locales, Bancos nacionales, Servicios gubernamentales (ping bajo ideal, sin bloqueos de los bancos por IP sospechosas).</td>
</tr>
<tr>
  <td>🔵 <b>PROXY (Por VPN)</b></td>
  <td>YouTube, Instagram, ChatGPT, CDN extranjeros y todo el resto del tráfico bloqueado.</td>
</tr>
</tbody>
</table>

---

### 🛡️ Configuración de DNS

<table width="100%">
<thead><tr><th align="center">Propósito</th><th align="left">Servidor</th><th align="left">Por qué</th></tr></thead>
<tbody>
<tr>
  <td align="center">🏠 <b>DIRECT (Nacional)</b></td>
  <td><a href="https://dns.yandex.ru/">Yandex DNS</a> <code>77.88.8.8</code></td>
  <td>Resolución rápida de recursos internos, ping bajo local, funciona sin un VPN activo.</td>
</tr>
<tr>
  <td align="center">🌍 <b>PROXY (Extranjero)</b></td>
  <td><a href="https://developers.cloudflare.com/1.1.1.1/">Cloudflare</a> / <a href="https://developers.google.com/speed/public-dns/">Google</a></td>
  <td>Resolución confiable para el tráfico del proxy, protección contra la suplantación de DNS por parte de los proveedores locales.</td>
</tr>
</tbody>
</table>

---
> [!NOTE]
> Clientes populares como **NekoBox** y **NekoRay** se consideran obsoletos en la actualidad. Se recomienda cambiar a alternativas modernas y optimizadas basadas en los núcleos actuales **sing-box** y **Xray** (por ejemplo, **Exclave**, que replica completamente la interfaz de NekoBox, o **Incy**).

<details>
<summary><b>🤖 Android</b></summary>

* [v2RayTun](https://v2raytun.com/) — Cliente seguro y de alta velocidad basado en Xray Core.
* [FlClash](https://github.com/chen08209/FlClash) — Principal cliente multiplataforma.
* [Incy](https://incy.cc/) — Cliente moderno y rápido con importación de un solo toque.
* [Happ](https://www.happ.su/main) — Utilidad proxy para la gestión cómoda de servidores.
* [Exclave](https://github.com/ExclaveNetwork/Exclave) — Alternativa moderna a NekoBox con una interfaz familiar.
* [Sing-box](https://github.com/SagerNet/sing-box) — Núcleo oficial limpio para configuraciones avanzadas.
* [Hiddify App](https://github.com/hiddify/hiddify-app) — Cliente universal para cualquier tipo de configuración.
* [v2rayNG](https://github.com/2dust/v2rayNG) — Solución clásica y estable para el núcleo Xray.
* [Karing](https://github.com/KaringX/karing) — Interfaz gráfica rica en funciones.
* [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
* ~~[NekoBox For Android](https://github.com/MatsuriDayo/NekoBoxForAndroid)~~ *(Obsoleto)*
</details>

<details>
<summary><b>🍏 iOS</b></summary>

* [v2RayTun](https://v2raytun.com/) — Cliente seguro y de alta velocidad basado en Xray Core.
* [Incy](https://incy.cc/) — Excelente cliente moderno en la App Store.
* [Happ](https://www.happ.su/main) — Cómoda utilidad proxy.
* [Karing](https://apps.apple.com/us/app/karing/id6472431552)
* [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
* [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)
* [Clash Lite](https://apps.apple.com/us/app/clash-lite/id6761357475)
* [V2Lite VPN](https://apps.apple.com/us/app/v2lite-vpn-super-vpn-proxy/id6444585377)
</details>

<details>
<summary><b>💻 Desktop (Win/Mac/Linux)</b></summary>

* [v2RayTun](https://v2raytun.com/) — Cliente seguro y de alta velocidad basado en Xray Core.
* [Happ](https://www.happ.su/main) — Versión de escritorio multiplataforma.
* [v2rayN](https://github.com/2dust/v2rayN) — Potente cliente personalizable para Windows.
* [FlClash](https://github.com/chen08209/FlClash) — Interfaz gráfica minimalista y rápida.
* [Karing](https://github.com/KaringX/karing)
* [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)
* ~~[NekoRay](https://github.com/MatsuriDayo/nekoray)~~ *(Obsoleto)*
</details>

---

### 🛡️ Herramientas alternativas (Evasión de DPI)

*Si los protocolos VPN estándar están completamente bloqueados por su proveedor o DPI, utilice herramientas locales para evadir la inspección profunda de paquetes:*

* [Zapret](https://github.com/bol-van/zapret) — La herramienta más potente y flexible para evadir DPI a nivel del sistema.
* [Zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) — Scripts listos para usar, optimizados y configurados para servicios populares específicos.
* [ByeByeDPI](https://github.com/romanvht/ByeByeDPI) — Solución clásica comprobada para ejecución local en Android.

---

### ⭐ Apoya el proyecto

**Si Network Builder ULTRA te ha ayudado, ¡no olvides dejar una estrella! Esto motiva a seguir desarrollando el proyecto.** :star2:

[![Star History Chart](https://api.star-history.com/svg?repos=JINXPIL/flclash-converter&type=Date)](https://star-history.com/#JINXPIL/flclash-converter&Date)