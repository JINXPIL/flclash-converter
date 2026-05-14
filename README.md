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
  <b>Продвинутый 100% локальный веб-инструмент (Single-File HTML / Vanilla JS) для управления, тестирования и конвертации прокси-серверов.</b><br>
  <i>Предоставляет удобный интерфейс для парсинга узлов из любых источников и мгновенной генерации оптимизированных профилей маршрутизации для FlClash, Nekobox (Xray) и Sing-box.</i>
</p>

<p align="center">
  <a href="https://jinxpil.github.io/flclash-converter/">
    <img src="https://img.shields.io/badge/🚀_ОТКРЫТЬ_WEB--ВЕРСИЮ-0052FF?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Open Web Version">
  </a>
</p>

> [!IMPORTANT]
> **Только для образовательных целей.** Данный проект создан исключительно в исследовательских целях. Пожалуйста, не используйте его в незаконных целях. Автор не несет ответственности за неправомерное использование данного инструмента. Все вычисления производятся строго локально в вашем браузере (Zero-Trust).

---

### 📸 Интерфейс (Адаптивный)

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

### 🔌 Поддерживаемые протоколы

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

### 📥 Рекомендуемые клиенты

<details>
<summary><b>🤖 Показать клиенты для Android</b></summary>

- [FlClash](https://github.com/chen08209/FlClash)
- [Karing](https://github.com/KaringX/karing)
- [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
- [FlClashX](https://github.com/pluralplay/FlClashX)
</details>

<details>
<summary><b>🍏 Показать клиенты для iOS</b></summary>

- [Karing](https://apps.apple.com/us/app/karing/id6472431552)
- [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
- [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)
</details>

<details>
<summary><b>💻 Показать клиенты для ПК (Windows / macOS / Linux)</b></summary>

- [Karing](https://github.com/KaringX/karing)
- [FlClash](https://github.com/chen08209/FlClash)
- [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)
</details>

---

### 🔥 Главные возможности

- 🛡️ **Zero-Trust Security:** Никаких сторонних серверов. Данные обрабатываются в оперативной памяти и уничтожаются при закрытии вкладки.
- 🧩 **Omni-Парсер:** Мгновенное декодирование Base64-подписок, реверс-инжиниринг JSON-конфигов и поддержка Drag & Drop.
- 🌍 **Mass Editor & Smart GeoIP:** Пакетное изменение параметров (SNI, Flow, Fingerprint) и авто-определение геолокации узлов с добавлением флагов (🇫🇮, 🇩🇪).
- 🐛 **Diagnostic Logger:** Встроенная система фоновой отладки, записывающая взаимодействия, ошибки и сетевые события для удобного поиска неполадок.
- 🎨 **Theme Engine:** Полная кастомизация интерфейса с возможностью импорта/экспорта дизайна в `.json`.
- ⚙️ **Авто-оптимизация:** Очистка дубликатов по IP/порту, удаление мертвых серверов после TCP/HTTP пинга и автоматическое восстановление битых ссылок.

---

### ⭐ Поддержка проекта

**Если этот проект оказался полезен для вас, пожалуйста, поставьте ему звезду!** :star2:

[![Stargazers over time](https://starchart.cc/jinxpil/flclash-converter.svg?variant=adaptive)](https://starchart.cc/jinxpil/flclash-converter)
