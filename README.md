# ⚡ Network Builder Omni-Core (v15.1 Community Edition)

[🇺🇸 Read in English](#english-version) | [🇷🇺 Читать на Русском](#russian-version)

<a name="russian-version"></a>
## 🇷🇺 Описание проекта

**Network Builder** — это 100% локальный веб-инструмент (Single-File HTML) для управления, тестирования и конвертации прокси-серверов. 

Создан для специалистов по информационной безопасности. Позволяет собрать ваши узлы из разрозненных источников и в один клик сгенерировать идеальный профиль маршрутизации для **FlClash**, **Nekobox (Xray)** или **Sing-box**.

![Version](https://img.shields.io/badge/version-15.1_Community-3fb950?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-58a6ff?style=flat-square)
![Security](https://img.shields.io/badge/security-100%25_Local-ea4aaa?style=flat-square)
![Architecture](https://img.shields.io/badge/architecture-Monolith_(Single_HTML)-8957e5?style=flat-square)

### 🚀 Быстрый старт
👉 **[ОТКРЫТЬ WEB-ВЕРСИЮ](https://jinxpil.github.io/flclash-converter/)**

Или скачайте `index.html` и откройте в любом браузере. Работает в полном офлайне (Zero-Trust Architecture).

### 🔥 Главные фичи
* 🛡️ **Локальная безопасность:** Приватные ключи и серверы не отправляются на чужие API. Все вычисления происходят в браузере (движок V8).
* 📦 **Omni-Парсер:** Поддержка расшифровки Base64 подписок и реверс-инжиниринг JSON-конфигов (вытаскивает серверы, ключи Reality и SNI прямо из `outbounds`).
* ✏️ **Mass Editor:** Выделяйте узлы и массово меняйте параметры (SNI, Flow, Fingerprint). Незаменимо для VLESS Reality.
* 🌍 **Smart GeoIP:** Автоматическое определение страны сервера и добавление флагов (🇫🇮, 🇩🇪) через API `geojs.io`.
* 🧹 **Smart Clean & Deduplication:** Удаление "мертвых" серверов после пинга и очистка дубликатов по IP.

### 🔌 Протоколы
`VLESS` (Reality/Vision) • `VMess` • `Trojan` • `Hysteria2` • `SS/SSR` • `WireGuard` • `TUIC` • `Socks5/HTTP/SSH`

### 💎 Вшитый профиль (Ultimate v77.0)
При экспорте в FlClash используется глубоко оптимизированный профиль:
* Блокировка рекламы, фишинга и трекеров (Hagezi, Adblock).
* Прямая маршрутизация (`DIRECT`) для RU-сегмента (Госуслуги, банки, маркетплейсы).
* Глобальное проксирование для AI-сервисов (ChatGPT, Claude, Gemini) и IT-инфраструктуры (GitHub, Docker).

---

<a name="english-version"></a>
## 🇺🇸 Project Overview

**Network Builder** is a 100% local web tool (Single-File HTML) for managing, testing, and converting proxy servers. 

Designed for cybersecurity specialists and proxy enthusiasts. It allows you to gather your nodes from various sources and generate an ideal routing profile for **FlClash**, **Nekobox (Xray)**, or **Sing-box** in one click.

### 🚀 Quick Start
👉 **[OPEN WEB VERSION](https://jinxpil.github.io/flclash-converter/)**

Or download `index.html` and open it in any browser. It works completely offline (Zero-Trust Architecture).

### 🔥 Key Features
* 🛡️ **Local Security:** Private keys and servers are never sent to third-party APIs. All processing happens locally in your browser.
* 📦 **Omni-Parser:** Supports Base64 subscription decoding and JSON config reverse-engineering (extracts servers, Reality keys, and SNI directly from `outbounds`).
* ✏️ **Mass Editor:** Select nodes and batch-edit parameters (SNI, Flow, Fingerprint). Essential for VLESS Reality.
* 🌍 **Smart GeoIP:** Automatically detects server location and appends country flags (🇫🇮, 🇩🇪) via the `geojs.io` API.
* 🧹 **Smart Clean & Deduplication:** Removes "dead" servers after a ping test and clears IP/Port duplicates.

### 🔌 Supported Protocols
`VLESS` (Reality/Vision) • `VMess` • `Trojan` • `Hysteria2` • `SS/SSR` • `WireGuard` • `TUIC` • `Socks5/HTTP/SSH`
