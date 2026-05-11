# ⚡ Network Builder Omni-Core

[🇺🇸 Read in English](#english-version) | [🇷🇺 Читать на Русском](#russian-version) | [🇨🇳 简体中文](#chinese-version)

<a name="russian-version"></a>
## 🇷🇺 Описание проекта

**Network Builder** — это 100% локальный веб-инструмент (Single-File HTML) для управления, тестирования и конвертации прокси-серверов. 

Создан для специалистов по информационной безопасности и сетевых энтузиастов. Позволяет собрать ваши узлы из разрозненных источников и в один клик сгенерировать идеальный профиль маршрутизации для **FlClash**, **Nekobox (Xray)** или **Sing-box**.

![Version](https://img.shields.io/badge/version-15.4_Stable-3fb950?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-58a6ff?style=flat-square)
![Security](https://img.shields.io/badge/security-100%25_Local-ea4aaa?style=flat-square)
![Architecture](https://img.shields.io/badge/architecture-Monolith_(Single_HTML)-8957e5?style=flat-square)

### 🚀 Быстрый старт
👉 **[ОТКРЫТЬ WEB-ВЕРСИЮ](https://jinxpil.github.io/flclash-converter/)** *(работает как PWA, можно добавить на главный экран)*

Или скачайте `index.html` и откройте в любом браузере. Работает в полном офлайне (Zero-Trust Architecture).

### 🔥 Главные фичи (v15.4)
* 🛡️ **Локальная безопасность:** Приватные ключи и серверы не отправляются на чужие API. Все вычисления происходят в вашем браузере. Данные сохраняются в `sessionStorage` и исчезают при закрытии вкладки.
* 📦 **Omni-Парсер:** Расшифровка Base64 подписок и реверс-инжиниринг JSON-конфигов (извлекает серверы, ключи Reality и SNI прямо из `outbounds`).
* 🩺 **Smart Linter & Auto-healing:** Встроенная проверка синтаксиса YAML/JSON перед скачиванием конфига и автоматическое "лечение" битых ссылок при импорте.
* ✏️ **Mass Editor:** Выделяйте узлы и массово меняйте параметры (SNI, Flow, Fingerprint). Незаменимо для VLESS Reality.
* 🌍 **Smart GeoIP:** Автоматическое определение страны сервера и добавление флагов (🇫🇮, 🇩🇪) через API `geojs.io` и регулярные выражения.
* 🧹 **Smart Clean & Deduplication:** Удаление "мертвых" серверов после пингования (HTTP/TCP) и очистка дубликатов по IP/порту с сохранением узла с лучшим пингом.
* 📥 **URL Import:** Загрузка кастомных YAML-шаблонов напрямую по ссылке (GitHub, Pastebin).

### 🔌 Поддерживаемые протоколы
`VLESS` (Reality/Vision) • `VMess` • `Trojan` • `Hysteria2` • `SS/SSR` • `WireGuard` • `TUIC` • `Socks5/HTTP/SSH/Naive`

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
👉 **[OPEN WEB VERSION](https://jinxpil.github.io/flclash-converter/)** *(PWA ready, can be installed to home screen)*

Or download `index.html` and open it in any browser. It works completely offline (Zero-Trust Architecture).

### 🔥 Key Features (v15.4)
* 🛡️ **Local Security:** Private keys and servers are never sent to third-party APIs. All processing happens locally in your browser. Data is secured via `sessionStorage` and cleared upon tab closure.
* 📦 **Omni-Parser:** Supports Base64 subscription decoding and JSON config reverse-engineering (extracts servers, Reality keys, and SNI directly from `outbounds`).
* 🩺 **Smart Linter & Auto-healing:** Built-in YAML/JSON syntax validation before export and automatic healing of broken import links.
* ✏️ **Mass Editor:** Select nodes and batch-edit parameters (SNI, Flow, Fingerprint). Essential for VLESS Reality.
* 🌍 **Smart GeoIP:** Automatically detects server location and appends country flags (🇫🇮, 🇩🇪) via the `geojs.io` API and regex matching.
* 🧹 **Smart Clean & Deduplication:** Removes "dead" servers after a ping test (HTTP/TCP) and clears IP/Port duplicates, keeping the node with the lowest latency.
* 📥 **URL Import:** Load custom YAML templates directly via URL (GitHub, Pastebin).

### 🔌 Supported Protocols
`VLESS` (Reality/Vision) • `VMess` • `Trojan` • `Hysteria2` • `SS/SSR` • `WireGuard` • `TUIC` • `Socks5/HTTP/SSH/Naive`

---

<a name="chinese-version"></a>
## 🇨🇳 项目简介

**Network Builder** 是一个 100% 本地运行的 Web 工具（单文件 HTML），用于管理、测试和转换代理节点。

专为网络安全专家和代理爱好者设计。只需一键，即可将来自不同来源的节点（链接、Base64 订阅、JSON 配置文件）整合并生成适用于 **FlClash**、**Nekobox (Xray)** 或 **Sing-box** 的完美路由配置文件。

### 🚀 快速开始
👉 **[打开网页版](https://jinxpil.github.io/flclash-converter/)** *(支持 PWA，可添加到主屏幕)*

或者下载 `index.html` 并在任何浏览器中打开。完全离线运行（零信任架构）。

### 🔥 核心功能 (v15.4)
* 🛡️ **本地安全:** 私钥和服务器节点永远不会发送到第三方 API。所有计算和解析均在您的浏览器中完成。数据保存在 `sessionStorage` 中，关闭标签页后自动清除。
* 📦 **全能解析器 (Omni-Parser):** 支持 Base64 订阅解码和 JSON 配置逆向工程（直接从 `outbounds` 提取节点、Reality 密钥和 SNI）。
* 🩺 **智能语法检查 & 自动修复:** 导出前自动验证 YAML/JSON 语法，并在导入时自动修复损坏的节点链接。
* ✏️ **批量修改 (Mass Editor):** 选中节点并批量修改参数（SNI、Flow、Fingerprint）。非常适合 VLESS Reality 的快速配置。
* 🌍 **智能 GeoIP:** 通过 `geojs.io` API 和正则表达式自动识别节点国家并添加国旗 emoji (🇫🇮, 🇩🇪)。
* 🧹 **智能清理与去重:** 延迟测试 (HTTP/TCP) 后一键删除失效节点，并按 IP/端口清理重复项（自动保留延迟最低的节点）。
* 📥 **URL 导入:** 直接通过链接导入自定义 YAML 模板（支持 GitHub、Pastebin）。

### 🔌 协议支持
`VLESS` (Reality/Vision) • `VMess` • `Trojan` • `Hysteria2` • `SS/SSR` • `WireGuard` • `TUIC` • `Socks5/HTTP/SSH/Naive`
