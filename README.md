# ⚡ Network Builder Omni-Core

[🇺🇸 Read in English](#-project-overview) | [🇷🇺 Читать на Русском](#-описание-проекта) | [🇨🇳 简体中文](#-项目简介)

<p align="center">
  [![Release](https://img.shields.io/github/v/release/jinxpil/flclash-converter.svg)](https://github.com/jinxpil/flclash-converter/releases)
  [![Downloads](https://img.shields.io/github/downloads/jinxpil/flclash-converter/total.svg)](https://github.com/jinxpil/flclash-converter/releases)
  [![Stars](https://img.shields.io/github/stars/jinxpil/flclash-converter.svg)](https://github.com/jinxpil/flclash-converter/stargazers)
  [![Forks](https://img.shields.io/github/forks/jinxpil/flclash-converter.svg)](https://github.com/jinxpil/flclash-converter/network)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
</p>

---

## 🇷🇺 Описание проекта

**Network Builder** — это 100% локальный веб-инструмент (Single-File HTML / Vanilla JS) для управления, тестирования и конвертации прокси-серверов.

Спроектирован для специалистов по информационной безопасности и сетевых энтузиастов. Инструмент парсит узлы из любых разрозненных источников и мгновенно генерирует оптимизированные профили маршрутизации для **FlClash**, **Nekobox (Xray)** или **Sing-box**.

### 🚀 Быстрый старт

👉 **[ОТКРЫТЬ WEB-ВЕРСИЮ](https://jinxpil.github.io/flclash-converter/)** *(работает как PWA, можно добавить на главный экран)*

Или скачайте `index.html` и откройте в браузере. Работает в полном офлайне (Zero-Trust Architecture).

### 🔥 Главные фичи (v16.15)

* 🛡️ **Zero-Trust Security:** Никаких сторонних серверов. Вычисления происходят в вашем браузере. Данные защищены в `sessionStorage` и уничтожаются при закрытии вкладки.
* ⚡ **Core Optimization:** Использование паттерна Proxy для кэширования DOM, умный `debounce` при вводе и централизованный State Management — инструмент работает мгновенно даже с тысячами строк.
* 📱 **Fluid UI & i18n:** Mobile-first дизайн. Текстовые блоки с умным авто-ресайзом (растягиваются под контент) и встроенная локализация интерфейса "на лету" (RU, EN, CN) через `data-атрибуты`.
* 🎨 **Theme Engine:** Полная кастомизация интерфейса с сохранением в браузере и возможностью импорта/экспорта дизайна в `.json`.
* 📦 **Omni-Парсер:** Декодирование Base64-подписок, умный реверс-инжиниринг JSON-конфигов и поддержка Drag & Drop (файлы `.txt`, `.json`, `.yaml`).
* 🩺 **Smart Linter & Auto-healing:** Встроенная проверка синтаксиса YAML/JSON и автоматическое восстановление битых ссылок при импорте.
* 🛠️ **Diagnostic Logger:** Встроенная система фоновой отладки, записывающая взаимодействия, ошибки и сетевые события с возможностью выгрузки лога.
* ✏️ **Mass Editor:** Пакетное изменение параметров (SNI, Flow, Fingerprint) для выделенных узлов. Идеально для тонкой настройки VLESS Reality.
* 🌍 **Smart GeoIP:** Автоматическое определение страны сервера и интеграция флагов (🇫🇮, 🇩🇪) через API `geojs.io` и Regex-фильтры.
* 🧹 **Smart Clean:** Очистка дубликатов по IP/порту (с сохранением узла с лучшим пингом) и удаление мертвых серверов после HTTP/TCP пинга.
* 📥 **URL Import:** Инъекция кастомных YAML-шаблонов напрямую по ссылке (GitHub Raw, Pastebin).

### 🔌 Поддерживаемые протоколы

`VLESS` (Reality/Vision) • `VMess` • `Trojan` • `Hysteria2` • `SS/SSR` • `WireGuard` • `TUIC` • `Socks5/HTTP/SSH/Naive`

### 💎 Вшитый профиль (Ultimate v77.0)

При экспорте в FlClash используется аппаратно-оптимизированный YAML-профиль:
* Блокировка рекламы, фишинга и трекеров (Hagezi, Adblock, Sukka).
* Прямая маршрутизация (`DIRECT`) для RU-сегмента (Госуслуги, банки, маркетплейсы).
* Глобальное проксирование с балансировкой для AI-сервисов (ChatGPT, Claude, Gemini) и IT-инфраструктуры (GitHub, Docker).

---

## 🇺🇸 Project Overview

**Network Builder** is a 100% local web tool (Single-File HTML / Vanilla JS) for managing, testing, and converting proxy servers.

Engineered for cybersecurity specialists and proxy enthusiasts. It parses nodes from fragmented sources and instantly generates highly optimized routing profiles for **FlClash**, **Nekobox (Xray)**, or **Sing-box**.

### 🚀 Quick Start

👉 **[OPEN WEB VERSION](https://jinxpil.github.io/flclash-converter/)** *(PWA ready, can be installed to home screen)*

Or download `index.html` and open it locally. Fully operational completely offline (Zero-Trust Architecture).

### 🔥 Key Features (v16.15)

* 🛡️ **Zero-Trust Security:** No backend servers. All processing happens locally in your browser. Data is secured via `sessionStorage` and wiped upon tab closure.
* ⚡ **Core Optimization:** Framework-less State Management, DOM caching via JS Proxy pattern, and smart `debounce` rendering for extreme performance.
* 📱 **Fluid UI & i18n:** Mobile-first adaptive UI with auto-resizing text areas and built-in on-the-fly localization (RU, EN, CN) via `data-attributes`.
* 🎨 **Theme Engine:** Full UI customization with local storage saving and `.json` design import/export capabilities.
* 📦 **Omni-Parser:** Base64 subscription decoding, JSON config reverse-engineering, and Drag & Drop file support.
* 🩺 **Smart Linter & Auto-healing:** Built-in YAML/JSON syntax validation and automatic healing of corrupted import links.
* 🛠️ **Diagnostic Logger:** Built-in background debugging system that records UI interactions, errors, and network events with export functionality.
* ✏️ **Mass Editor:** Batch-edit parameters (SNI, Flow, Fingerprint) for selected nodes. Essential for VLESS Reality tuning.
* 🌍 **Smart GeoIP:** Automatically resolves server locations and appends country flags (🇫🇮, 🇩🇪) via the `geojs.io` API and Regex matching.
* 🧹 **Smart Clean & Deduplication:** Clears IP/Port duplicates (retaining the node with the lowest latency) and purges dead servers via HTTP/TCP ping tests.
* 📥 **URL Import:** Inject custom YAML templates directly via URL (GitHub Raw, Pastebin).

### 🔌 Supported Protocols

`VLESS` (Reality/Vision) • `VMess` • `Trojan` • `Hysteria2` • `SS/SSR` • `WireGuard` • `TUIC` • `Socks5/HTTP/SSH/Naive`

---

## 🇨🇳 项目简介

**Network Builder** 是一个 100% 本地运行的 Web 工具（单文件 HTML / 原生 JS），用于管理、测试和转换代理节点。

专为网络安全专家和代理爱好者打造。它可以解析来自任何零散来源的节点，并瞬间生成适用于 **FlClash**、**Nekobox (Xray)** 或 **Sing-box** 的深度优化路由配置文件。

### 🚀 快速开始

👉 **[打开网页版](https://jinxpil.github.io/flclash-converter/)** *(支持 PWA，可添加到主屏幕)*

或者下载 `index.html` 在本地打开。完全支持离线运行（零信任架构）。

### 🔥 核心功能 (v16.15)

* 🛡️ **零信任安全:** 无后端服务器参与。所有解析与计算均在浏览器本地完成。数据存储于 `sessionStorage`，关闭标签页即焚。
* ⚡ **底层优化:** 无框架的状态管理 (State Management)，基于 JS Proxy 模式的 DOM 缓存，以及智能防抖 (Debounce) 技术，处理海量节点依然丝滑。
* 📱 **流畅的 UI & 多语言 (i18n):** 移动端优先的自适应界面，内置基于数据属性的实时本地化切换（中/英/俄）。
* 🎨 **主题引擎 (Theme Engine):** 全面的界面定制功能，支持本地保存以及 `.json` 设计配置的导入/导出。
* 📦 **全能解析器 (Omni-Parser):** 支持 Base64 订阅解码、JSON 配置逆向工程以及拖拽文件导入。
* 🩺 **智能语法检查 & 自动修复:** 导出前自动验证 YAML/JSON 语法，并在导入时自动修复损坏的节点链接。
* 🛠️ **诊断日志 (Diagnostic Logger):** 内置后台调试系统，记录 UI 交互、错误和网络事件，并支持导出日志文件。
* ✏️ **批量编辑器 (Mass Editor):** 批量修改所选节点的参数（SNI、Flow、Fingerprint），VLESS Reality 调优利器。
* 🌍 **智能 GeoIP:** 通过 `geojs.io` API 和正则表达式自动解析节点国家并添加国旗 emoji (🇫🇮, 🇩🇪)。
* 🧹 **智能清理与去重:** 根据 IP/端口清理重复项（自动保留延迟最低的节点），并通过 HTTP/TCP 延迟测试一键删除失效节点。
* 📥 **URL 导入:** 直接通过链接注入自定义 YAML 模板（支持 GitHub Raw、Pastebin）。

### 🔌 协议支持

`VLESS` (Reality/Vision) • `VMess` • `Trojan` • `Hysteria2` • `SS/SSR` • `WireGuard` • `TUIC` • `Socks5/HTTP/SSH/Naive`

---

## ⭐ Support project

**Если этот проект вам помог, пожалуйста, поставьте звезду!** 🌟
**If this project is helpful to you, you may wish to give it a star!** 🌟
**如果这个项目对您有帮助，请给它一个星星！** 🌟

## 📈 Stargazers over Time

[![Stargazers over time](https://starchart.cc/jinxpil/flclash-converter.svg?variant=adaptive)](https://starchart.cc/jinxpil/flclash-converter)
