[🇺🇸 English](/README.en.md) | [🇷🇺 Русский](/README.md) | [🇨🇳 简体中文](/README.zh.md) | [🇹🇼 繁體中文](/README.zh-TW.md) | [🇮🇷 فارسی](/README.fa.md) | [🇪🇸 Español](/README.es.md)

<p align="center">
  <a href="https://github.com/jinxpil/flclash-converter/releases">
    <img src="https://img.shields.io/github/v/release/jinxpil/flclash-converter.svg?style=flat-square" alt="Release">
  </a>
  <a href="https://github.com/jinxpil/flclash-converter/releases/latest">
    <img src="https://img.shields.io/github/downloads/jinxpil/flclash-converter/total.svg?style=flat-square" alt="Downloads">
  </a>
  <a href="#">
    <img src="https://img.shields.io/github/languages/top/jinxpil/flclash-converter.svg?style=flat-square" alt="Language">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License">
  </a>
  <a href="https://github.com/jinxpil/flclash-converter/stargazers">
    <img src="https://img.shields.io/github/stars/jinxpil/flclash-converter.svg?style=flat-square" alt="Stars">
  </a>
</p>

**Network Builder** یک ابزار وب ۱۰۰٪ محلی و پیشرفته (تک‌فایل HTML / Vanilla JS) برای مدیریت، آزمایش و تبدیل سرورهای پروکسی است. این ابزار یک رابط کاربری مناسب برای استخراج گره‌ها (nodes) از هر منبعی و تولید فوری پروفایل‌های مسیریابی بهینه‌شده برای FlClash، Nekobox (Xray) و Sing-box ارائه می‌دهد.

> [!IMPORTANT]
> **فقط برای اهداف آموزشی.** این پروژه منحصراً برای اهداف تحقیقاتی ایجاد شده است. لطفاً از آن برای مقاصد غیرقانونی استفاده نکنید. نویسنده هیچ مسئولیتی در قبال استفاده نادرست از این ابزار ندارد. تمام محاسبات کاملاً به صورت محلی در مرورگر شما انجام می‌شود (Zero-Trust).

به عنوان یک ابزار قدرتمند شبکه، Network Builder بدون نیاز به سرورهای بک‌اند بالاترین عملکرد را ارائه می‌دهد، از بیش از ۱۰ پروتکل پشتیبانی می‌کند و امکان شخصی‌سازی عمیق رابط کاربری را فراهم می‌سازد.

### 📸 رابط کاربری

<p align="center">
  <img src="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/JSON%20to%20YAML%20Converter.jpg" alt="JSON to YAML" width="48%">
  <img src="https://raw.githubusercontent.com/jinxpil/flclash-converter/main/media/Yaml%20Code%20Formatter.jpg" alt="YAML Formatter" width="48%">
</p>

## 🚀 شروع سریع

👉 **[باز کردن نسخه وب](https://jinxpil.github.io/flclash-converter/)** *(به عنوان PWA کار می‌کند، می‌توانید آن را به صفحه اصلی گوشی هوشمند خود اضافه کنید)*

یا آخرین فایل `index.html` را از بخش [Releases](https://github.com/jinxpil/flclash-converter/releases) دانلود کرده و در مرورگر خود باز کنید. کاملاً به صورت آفلاین کار می‌کند.

## 📥 کلاینت‌های پیشنهادی

برای استفاده از پروفایل‌ها و مسیریابی تولید شده، برنامه‌های زیر را توصیه می‌کنیم:

### 🤖 Android
- [FlClash](https://github.com/chen08209/FlClash)
- [Karing](https://github.com/KaringX/karing)
- [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)
- [FlClashX](https://github.com/pluralplay/FlClashX)

### 🍏 iOS
- [Karing](https://apps.apple.com/us/app/karing/id6472431552)
- [Clash.MI](https://apps.apple.com/us/app/clash-mi/id6744321968)
- [Stash](https://apps.apple.com/us/app/stash-rule-based-proxy/id1596063349)

### 💻 PC (Windows / macOS / Linux)
- [Karing](https://github.com/KaringX/karing)
- [FlClash](https://github.com/chen08209/FlClash)
- [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)

## 🔥 ویژگی‌های اصلی

- **امنیت Zero-Trust:** هیچ سرور شخص ثالثی درگیر نیست. داده‌ها در حافظه رم پردازش شده و با بستن تب از بین می‌روند.
- **تجزیه‌کننده Omni:** رمزگشایی فوری اشتراک‌های Base64، مهندسی معکوس پیکربندی‌های JSON و پشتیبانی از Drag & Drop.
- **ویرایشگر گروهی و GeoIP هوشمند:** تغییر دسته‌ای پارامترها (SNI، Flow، Fingerprint) و تشخیص خودکار موقعیت مکانی گره‌ها با پرچم‌ها (🇫🇮، 🇩🇪).
- **ثبت‌کننده خطایاب (Diagnostic Logger):** سیستم اشکال‌زدایی پس‌زمینه داخلی که تعاملات، خطاها و رویدادهای شبکه را برای عیب‌یابی آسان ثبت می‌کند.
- **موتور پوسته (Theme Engine):** شخصی‌سازی کامل رابط کاربری با قابلیت وارد/صادر کردن طراحی‌ها به `.json`.
- **بهینه‌سازی خودکار:** پاک‌سازی موارد تکراری بر اساس IP/پورت، حذف سرورهای از کار افتاده پس از پینگ TCP/HTTP، و بازیابی خودکار لینک‌های خراب.

## 🔌 پروتکل‌های پشتیبانی‌شده

`VLESS` (Reality/Vision) • `VMess` • `Trojan` • `Hysteria2` • `SS/SSR` • `WireGuard` • `TUIC` • `Socks5` • `HTTP`

## ⭐ حمایت از پروژه

**اگر این پروژه برای شما مفید بود، لطفاً به آن ستاره بدهید!** :star2:

## 📈 ستاره‌ها در طول زمان

[![Stargazers over time](https://starchart.cc/jinxpil/flclash-converter.svg?variant=adaptive)](https://starchart.cc/jinxpil/flclash-converter)
