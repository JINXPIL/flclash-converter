<p align="center">
  <a href="/README.en.md">🇺🇸 English</a> •
  <a href="/README.md"><b>🇷🇺 Русский</b></a> •
  <a href="/README.zh.md">🇨🇳 简体中文</a> •
  <a href="/README.zh-TW.md">🇹🇼 繁體中文</a> •
  <a href="/README.fa.md">🇮🇷 فارسی</a> •
  <a href="/README.es.md">🇪🇸 Español</a>
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

<h1 align="center">⚡ Network Builder v17.02 ULTRA</h1>

<p align="center">
  <b>Экстремально мощный и 100% локальный веб-инструмент для управления гигантскими базами прокси-серверов.</b><br>
  <i>Парсинг, конвертация и глубокая оптимизация конфигураций для FlClash, Exclave, Sing-box и Clash Meta.</i>
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
    <img src="https://img.shields.io/badge/🚀_ОТКРЫТЬ_ULTRA--ВЕРСИЮ-0052FF?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Open Web Version">
  </a>
</p>

> [!IMPORTANT]
> **Zero-Trust & Privacy First.** Все вычисления производятся строго локально в вашем браузере. Никакие данные не покидают ваше устройство. Инструмент создан исключительно в образовательных целях для глубокого изучения сетевых протоколов.

> [!WARNING]
> **Внимание: проблема с подписками YAML и тайм-аутами (Timeout):**
> Многие VPN-провайдеры намеренно (или из-за некомпетентной настройки API) ограничивают работу сторонних клиентов при экспорте подписок. Серверы могут успешно загрузиться в ваш список, но при попытке подключения уходят в бесконечный тайм-аут. 
> 💡 **Как проверить, кто виноват:** Если вы берете «сырую» ссылку на этот же узел (например, `vless://...` или JSON-код), добавляете его вручную как локальный профиль, и **он работает** — проблема 100% на стороне провайдера. Это означает, что их сервер блокирует запросы вашего клиента по `User-Agent` при попытке обновить подписку. В остальных случаях причиной тайм-аутов могут быть точечные блокировки сигнатур протоколов со стороны ТСПУ (РКН).

---

### 📸 Интерфейс (ULTRA Design)

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

### 🔥 Что нового в версии 17.02 ULTRA?

* 🚀 **Extreme Parser Engine:** Полная оптимизация кода для работы с **10,000+ узлами** одновременно. Плавный интерфейс даже при гигантских объемах данных.
* 🌍 **ULTRA Localization:** Глубокая поддержка 6 языков (RU, EN, ZH, FA, ES). Интерфейс и системные уведомления теперь полностью адаптированы.
* 🛡️ **Система QuotaGuard:** Интеллектуальная защита от переполнения памяти браузера. Работайте с любыми объемами конфигов без риска вылета вкладки.
* 🧠 **Smart Duplicate Filter:** Автоматическое сравнение серверов по паре `IP:Port`. Программа сама удалит мусор и дубликаты, оставив только уникальные узлы.
* 🛠️ **Refined Diagnostics:** Обновленный логгер событий и исправленные ошибки синтаксиса (SyntaxError fix) для безупречной стабильности.

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
    <td align="center">🔌 <b>TUIC / Socks5 / HTTP</b><br>Full Support</td>
  </tr>
</table>

---

### 🎯 Конфигурации и маршрутизация (Пресеты)

Чтобы не засорять страницу портянками кода, все готовые пресеты вынесены в отдельные файлы репозитория.

* 🌐 **Раздельное туннелирование для Happ** — Оптимизированный пресет правил (Крым, СевГУ, обход ограничений, AdBlock), собранный через конструктор `routing.happ.su`. Предназначен **строго** для клиента Happ.
    * 📄 Ссылка на файл конфигурации: [`./rus_vp_happ.json`](./rus_vp_happ.json)
    * 🔗 Ссылка для импорта в клиент: `https://raw.githubusercontent.com/JINXPIL/flclash-converter/refs/heads/main/rus_vp_happ.json`
* 🛠️ **Оптимизированный YAML-конфиг (Mihomo/Clash)** — v79.0 Ultimate со строгими TLS-отпечатками браузера и защитой от DPI-анализаторов.
    * 📄 Ссылка на файл конфигурации: [`./GL_Crimea_ipv6_yan(9.35).yml`](./GL_Crimea_ipv6_yan(9.35).yml)
    * 🔗 Ссылка для импорта в клиент: `https://raw.githubusercontent.com/JINXPIL/flclash-converter/refs/heads/main/GL_Crimea_ipv6_yan(9.35).yml`

---
> [!NOTE]
> Такие популярные клиенты, как **NekoBox** и **NekoRay**, на текущий момент считаются устаревшими. Рекомендуется переходить на актуальные и оптимизированные аналоги под современные ядра **sing-box** и **Xray** (например, **Exclave**, который полностью повторяет интерфейс NekoBox, или **Incy**).

<details>
<summary><b>🤖 Android</b></summary>

* [v2RayTun](https://v2raytun.com/) — Высокоскоростной и безопасный клиент на базе ядра Xray Core.
* [FlClash](https://github.com/chen08209/FlClash) — Основной кроссплатформенный клиент.
* [Incy](https://incy.cc/) — Современный быстрый клиент с импортом в одно касание.
* [Happ](https://www.happ.su/main) — Прокси-утилита для удобной работы со списками серверов.
* [Exclave](https://github.com/ExclaveNetwork/Exclave) — Современный и актуальный аналог NekoBox со знакомым интерфейсом.
* [Sing-box](https://github.com/SagerNet/sing-box) — Официальное чистое ядро для продвинутой конфигурации.
* [Hiddify App](https://github.com/hiddify/hiddify-app) — Универсальный клиент под любые типы конфигураций.
* [v2rayNG](https://github.com/2dust/v2rayNG) — Стабильное классическое решение для ядра Xray.
* [Karing](https://github.com/KaringX/karing) — Функциональный графический интерфейс.
* [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
* ~~[NekoBox For Android](https://github.com/MatsuriDayo/NekoBoxForAndroid)~~ *(Устарел)*
</details>

<details>
<summary><b>🍏 iOS</b></summary>

* [v2RayTun](https://v2raytun.com/) — Высокоскоростной и безопасный клиент на базе ядра Xray Core.
* [Incy](https://incy.cc/) — Отличный современный клиент в App Store.
* [Happ](https://www.happ.su/main) — Комфортная утилита для прокси.
* [Karing](https://apps.apple.com/us/app/karing/id6472431552)
* [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
* [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)
* [Clash Lite](https://apps.apple.com/us/app/clash-lite/id6761357475)
* [V2Lite VPN](https://apps.apple.com/us/app/v2lite-vpn-super-vpn-proxy/id6444585377)
</details>

<details>
<summary><b>💻 Desktop (Win/Mac/Linux)</b></summary>

* [v2RayTun](https://v2raytun.com/) — Высокоскоростной и безопасный клиент на базе ядра Xray Core.
* [Happ](https://www.happ.su/main) — Кроссплатформенная десктопная версия.
* [v2rayN](https://github.com/2dust/v2rayN) — Мощный настраиваемый клиент для Windows.
* [FlClash](https://github.com/chen08209/FlClash) — Минималистичный и быстрый GUI.
* [Karing](https://github.com/KaringX/karing)
* [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)
* ~~[NekoRay](https://github.com/MatsuriDayo/nekoray)~~ *(Устарел)*
</details>

---

### 🛡️ Альтернативные инструменты (DPI Bypass)

*Если стандартные VPN-протоколы полностью блокируются оператором или ТСПУ, используйте локальный обход глубокого анализа пакетов:*

* [Zapret](https://github.com/bol-van/zapret) — Мощнейший и самый гибкий инструмент для глубокого обхода DPI на уровне системы.
* [Zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube) — Оптимизированные и настроенные готовые скрипты под конкретные популярные сервисы.
* [ByeByeDPI](https://github.com/romanvht/ByeByeDPI) — Проверенное классическое решение для локального запуска на Android.

---

### ⭐ Поддержка проекта

**Если Network Builder ULTRA помог вам, не забудьте поставить звезду! Это мотивирует развивать проект дальше.** :star2:

[![Stargazers over time](https://starchart.cc/jinxpil/flclash-converter.svg?variant=adaptive)](https://starchart.cc/jinxpil/flclash-converter)
