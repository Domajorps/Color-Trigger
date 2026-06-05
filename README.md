# 🎯 Color Trigger (macOS)

Automatic color-based click tool with multilingual interface.

> 🌐 **Languages below**: English → Українська → Русский → 繁體中文

---

# 🇬🇧 English

## 📋 Description

The program creates a window on top of all applications that monitors a central screen area. When the target color is detected in this area and the **Shift** key is held down, a left mouse click is automatically performed.

## 🌐 Language Support

The interface is available in four languages:
- 🇺🇦 Українська (Ukrainian)
- 🇷🇺 Русский (Russian)
- 🇬🇧 English
- 🇹🇼 繁體中文 (Traditional Chinese)

You can change the language in the dropdown menu in the window header, or set it at launch:

```bash
python3 color_trigger.py --lang en
```

## ✨ Features

- ✅ Window always on top of all applications
- ⚡ Fast screen capture via `mss` and `numpy`
- 📊 Real-time color match indication
- 🖱️ Click via Quartz CGEvents (low-level)
- 🎨 Pipette tool for picking color directly from screen
- 🔧 Built-in dependency checker and installer
- 🌐 Multilingual interface with instant switching

## 🚀 Getting Started

### Via Launcher (recommended)

```bash
python3 launcher.py
```

### Direct Launch

```bash
python3 color_trigger.py
```

## 📖 How to Use

1. **Set the size** — use the slider to choose the search area size (screen center).
2. **Enable frame** — click "Show Frame" to see where the bot is scanning.
3. **Choose a color** — click **"🖌 Pipette"**, then click anywhere on the screen.
4. **Click "▶ START"**
5. **Hold Shift** — when the color matches, an automatic click will occur.

## ⚙️ Parameters

| Parameter | Range | Default | Description |
|-----------|-------|---------|-------------|
| Area size | 10–400 px | 60 px | Size of the square monitoring zone |
| Color tolerance | 0–150 | 30 | Allowable RGB deviation from the target color |

## ⚠️ Requirements

- macOS 10.15+
- Python 3.7+
- Dependencies: Pillow, pyautogui, pynput, pyobjc-framework-Quartz, mss, numpy

## 💡 Tips

- Start with a large tolerance (50–70) and gradually decrease for precision
- Use the frame to make sure the correct part of the screen is being monitored
- For better accuracy, choose unique colors that rarely appear on screen

---

# 🇺🇦 Українська

## 📋 Опис

Програма створює вікно поверх усіх додатків, яке моніторить центральну область екрана. Коли у цій області знайдено заданий колір і затиснуто клавішу **Shift**, автоматично виконується клік лівою кнопкою миші.

## 🌐 Підтримка мов

Інтерфейс програми доступний чотирма мовами:
- 🇺🇦 Українська
- 🇷🇺 Русский
- 🇬🇧 English
- 🇹🇼 繁體中文 (Традиційна китайська)

Мову можна змінити у випадаючому списку в шапці вікна програми, або задати при запуску:

```bash
python3 color_trigger.py --lang uk
```

## ✨ Можливості

- ✅ Вікно завжди поверх усіх додатків
- ⚡ Швидкий захват екрана через `mss` та `numpy`
- 📊 Індикація збігів кольору у реальному часі
- 🖱️ Клік через Quartz CGEvents (низькорівневий)
- 🎨 Піпетка для вибору кольору прямо з екрана
- 🔧 Вбудована перевірка та встановлення залежностей
- 🌐 Мультимовний інтерфейс з миттєвим перемиканням

## 🚀 Запуск

### Через лаунчер (рекомендовано)

```bash
python3 launcher.py
```

### Напряму

```bash
python3 color_trigger.py
```

## 📖 Інструкція

1. **Налаштуйте розмір** — повзунком оберіть розмір області пошуку (центр екрана).
2. **Увімкніть рамку** — натисніть «Показати рамку», щоб бачити, де шукає бот.
3. **Оберіть колір** — натисніть **«🖌 Піпетка»**, потім клікніть у будь-якому місці екрана.
4. **Натисніть «▶ СТАРТ»**
5. **Затисніть Shift** — коли колір збігається, відбудеться автоматичний клік.

## ⚙️ Параметри

| Параметр | Діапазон | За замовчуванням | Опис |
|----------|----------|-----------------|------|
| Розмір області | 10–400 px | 60 px | Розмір квадратної зони моніторингу |
| Допуск кольору | 0–150 | 30 | Допустиме відхилення RGB від цільового кольору |

## ⚠️ Вимоги

- macOS 10.15+
- Python 3.7+
- Залежності: Pillow, pyautogui, pynput, pyobjc-framework-Quartz, mss, numpy

## 💡 Поради

- Починайте з великого допуску (50–70) і поступово зменшуйте для точності
- Використовуйте рамку, щоб переконатися, що відстежується потрібна частина екрана
- Для кращої точності обирайте унікальні кольори, які рідко зустрічаються на екрані

---

# 🇷🇺 Русский

## 📋 Описание

Программа создает окно поверх всех приложений, которое мониторит центральную область экрана. Когда в этой области обнаруживается заданный цвет и зажата клавиша **Shift**, автоматически выполняется клик левой кнопкой мыши.

## 🌐 Поддержка языков

Интерфейс программы доступен на четырех языках:
- 🇺🇦 Українська
- 🇷🇺 Русский
- 🇬🇧 English
- 🇹🇼 繁體中文 (Традиционный китайский)

Язык можно сменить в выпадающем списке в шапке окна программы, или задать при запуске:

```bash
python3 color_trigger.py --lang ru
```

## ✨ Возможности

- ✅ Окно всегда поверх всех приложений
- ⚡ Быстрый захват экрана через `mss` и `numpy`
- 📊 Индикация совпадений цвета в реальном времени
- 🖱️ Клик через Quartz CGEvents (низкоуровневый)
- 🎨 Пипетка для выбора цвета прямо с экрана
- 🔧 Встроенная проверка и установка зависимостей
- 🌐 Мультиязычный интерфейс с мгновенным переключением

## 🚀 Запуск

### Через лаунчер (рекомендуется)

```bash
python3 launcher.py
```

### Напрямую

```bash
python3 color_trigger.py
```

## 📖 Инструкция

1. **Настройте размер** — ползунком выберите размер области поиска (центр экрана).
2. **Включите рамку** — нажмите «Показать рамку», чтобы видеть, где ищет бот.
3. **Выберите цвет** — нажмите **«🖌 Пипетка»**, затем кликните в любом месте экрана.
4. **Нажмите «▶ СТАРТ»**
5. **Зажмите Shift** — когда цвет совпадет, произойдет автоматический клик.

## ⚙️ Параметры

| Параметр | Диапазон | По умолчанию | Описание |
|----------|----------|-------------|----------|
| Размер области | 10–400 px | 60 px | Размер квадратной зоны мониторинга |
| Допуск цвета | 0–150 | 30 | Допустимое отклонение RGB от целевого цвета |

## ⚠️ Требования

- macOS 10.15+
- Python 3.7+
- Зависимости: Pillow, pyautogui, pynput, pyobjc-framework-Quartz, mss, numpy

## 💡 Советы

- Начните с большого допуска (50–70) и постепенно уменьшайте для точности
- Используйте рамку, чтобы убедиться, что отслеживается нужная часть экрана
- Для лучшей точности выбирайте уникальные цвета, которые редко встречаются на экране

---

# 🇹🇼 繁體中文

## 📋 說明

程式會建立一個置頂視窗，監控螢幕的中央區域。當在該區域偵測到指定顏色且按住 **Shift** 鍵時，將自動執行滑鼠左鍵點擊。

## 🌐 語言支援

介面支援四種語言：
- 🇺🇦 Українська（烏克蘭語）
- 🇷🇺 Русский（俄語）
- 🇬🇧 English（英語）
- 🇹🇼 繁體中文

您可以在視窗標題列的下拉選單中切換語言，或在啟動時指定：

```bash
python3 color_trigger.py --lang zh
```

## ✨ 功能特色

- ✅ 視窗始終置頂於所有應用程式之上
- ⚡ 透過 `mss` 和 `numpy` 進行快速螢幕擷取
- 📊 即時顏色匹配指示
- 🖱️ 透過 Quartz CGEvents 進行低階滑鼠點擊
- 🎨 滴管工具可直接從螢幕上選取顏色
- 🔧 內建依賴項檢查與安裝功能
- 🌐 多語言介面，支援即時切換

## 🚀 開始使用

### 透過啟動器（推薦）

```bash
python3 launcher.py
```

### 直接啟動

```bash
python3 color_trigger.py
```

## 📖 使用說明

1. **設定大小** — 使用滑桿選擇搜尋區域的大小（螢幕中心）。
2. **啟用邊框** — 點擊「顯示邊框」以查看偵測範圍。
3. **選擇顏色** — 點擊 **「🖌 滴管」**，然後在螢幕任意位置點擊所需顏色。
4. **點擊「▶ 開始」**
5. **按住 Shift** — 當顏色匹配時，將自動執行點擊。

## ⚙️ 參數設定

| 參數 | 範圍 | 預設值 | 說明 |
|------|------|--------|------|
| 區域大小 | 10–400 像素 | 60 像素 | 正方形監控區域的大小 |
| 顏色容差 | 0–150 | 30 | 與目標顏色的可接受 RGB 偏差值 |

## ⚠️ 系統需求

- macOS 10.15+
- Python 3.7+
- 依賴項：Pillow、pyautogui、pynput、pyobjc-framework-Quartz、mss、numpy

## 💡 使用技巧

- 從較大的容差值（50–70）開始，逐步縮小以提高精確度
- 使用邊框確認監控的是正確的螢幕區域
- 為獲得更好的準確性，選擇螢幕上罕見的獨特顏色

---

## 📄 License / Ліцензія / Лицензия / 授權條款

Free for personal use. / Безкоштовно для особистого використання. / Бесплатно для личного использования. / 免費供個人使用。
