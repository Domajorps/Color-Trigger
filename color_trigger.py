import tkinter as tk
from tkinter import ttk, colorchooser
import threading
import time
import sys
import subprocess
import importlib
import os
import platform

DEFAULT_LANGUAGE = "uk"
CURRENT_LANGUAGE = DEFAULT_LANGUAGE

if "--lang" in sys.argv:
    try:
        _idx = sys.argv.index("--lang")
        if _idx + 1 < len(sys.argv):
            _val = sys.argv[_idx + 1]
            if _val in ["uk", "ru", "en", "zh"]:
                CURRENT_LANGUAGE = _val
    except Exception:
        pass

TRANSLATIONS = {
    "uk": {
        "title": "Color Trigger v2.0 (Простий)",
        "header": "🎯 TriggerBot v1.0",
        "dep_title": "🔧 TriggerBot — Перевірка залежностей",
        "dep_header": "🔧  Перевірка залежностей",
        "dep_subtitle": "TriggerBot v2.0",
        "libraries": "Бібліотеки",
        "install": "Встановити",
        "checking": "Перевірка...",
        "install_all": "📦 Встановити всі відсутні",
        "launch": "🚀 Запустити TriggerBot",
        "recheck": "🔄 Перевірити",
        "log": "Лог",
        "ready": "✅ Ваш пристрій готовий до роботи!",
        "missing": "⚠️ Не встановлено: {missing} з {total}",
        "installing": "⏳ Встановлюю...",
        "installed_ok": "✅ {pkg} встановлено успішно!",
        "error_install": "❌ Помилка: {err}",
        "timeout_install": "⏰ Таймаут: {pkg}",
        "err_general": "❌ {err}",
        "target_color_sec": "1. Колір цілі",
        "pipette": "🖌 Піпетка",
        "palette": "🎨 Палітра",
        "observed": "Помічено: ...",
        "center_sec": "2. Зона (центр екрана)",
        "set_center": "🎯 Встановити центр",
        "size": "Розмір:",
        "tolerance": "Допуск:",
        "show_frame": "Показати рамку",
        "show_zone": "Показати зону реакції",
        "hide_zone": "Сховати зону реакції",
        "status_sec": "3. Статус",
        "status_stopped": "ЗУПИНЕНО",
        "status_waiting": "ОЧІКУВАННЯ SHIFT",
        "status_active": "АКТИВНО!",
        "start": "▶ СТАРТ",
        "stop": "⏹ СТОП",
        "reaction_frame": "Кадр реакції",
        "aim_target_3": "Наведіть на приціл! (3)",
        "aim_target_2": "Наведіть на приціл! (2)",
        "aim_target_1": "Наведіть на приціл! (1)",
        "center_pos": "Центр: {pos}",
        "click_pipette": "Натисніть...",
        "pipette_err": "Помилка піпетки: {err}",
        "pipette_canceled": "Піпетку скасовано",
        "color_chosen": "Колір обрано: {color}",
        "match_click": "ЗБІГ! Клік...",
        "err_msg": "ERR: {err}",
        "quartz_failed": "Quartz click failed, fallback: {err}",
        "live_info": "Центр: {color} | Різниця: {diff} | Відповідність: {match}",
        "yes": "ТАК!",
        "no": "НІ!",
        "dep_pillow": "Робота із зображеннями",
        "dep_pyautogui": "Керування мишею/клавіатурою",
        "dep_pynput": "Слухач клавіш/миші",
        "dep_quartz": "macOS системні події",
        "dep_mss": "Швидкий знімок екрана",
        "dep_numpy": "Математичні обчислення",
    },
    "ru": {
        "title": "Color Trigger v2.0 (Простой)",
        "header": "🎯 TriggerBot v1.0",
        "dep_title": "🔧 TriggerBot — Проверка зависимостей",
        "dep_header": "🔧  Проверка зависимостей",
        "dep_subtitle": "TriggerBot v2.0",
        "libraries": "Библиотеки",
        "install": "Установить",
        "checking": "Проверяю...",
        "install_all": "📦 Установить все недостающие",
        "launch": "🚀 Запустить TriggerBot",
        "recheck": "🔄 Перепроверить",
        "log": "Лог",
        "ready": "✅ Ваше устройство готово к работе!",
        "missing": "⚠️ Не установлено: {missing} из {total}",
        "installing": "⏳ Устанавливаю...",
        "installed_ok": "✅ {pkg} установлен успешно!",
        "error_install": "❌ Ошибка: {err}",
        "timeout_install": "⏰ Таймаут: {pkg}",
        "err_general": "❌ {err}",
        "target_color_sec": "1. Цвет цели",
        "pipette": "🖌 Пипетка",
        "palette": "🎨 Палитра",
        "observed": "Замечено: ...",
        "center_sec": "2. Зона (центр экрана)",
        "set_center": "🎯 Установить центр",
        "size": "Размер:",
        "tolerance": "Допуск:",
        "show_frame": "Показать рамку",
        "show_zone": "Показать зону реакции",
        "hide_zone": "Скрыть зону реакции",
        "status_sec": "3. Статус",
        "status_stopped": "ОСТАНОВЛЕНО",
        "status_waiting": "ОЖИДАНИЕ SHIFT",
        "status_active": "АКТИВНО!",
        "start": "▶ СТАРТ",
        "stop": "⏹ СТОП",
        "reaction_frame": "Кадр реакции",
        "aim_target_3": "Наведите на прицел! (3)",
        "aim_target_2": "Наведите на прицел! (2)",
        "aim_target_1": "Наведите на прицел! (1)",
        "center_pos": "Центр: {pos}",
        "click_pipette": "Нажмите...",
        "pipette_err": "Ошибка пипетки: {err}",
        "pipette_canceled": "Пипетка отменена",
        "color_chosen": "Цвет выбран: {color}",
        "match_click": "СОВПАДЕНИЕ! Клик...",
        "err_msg": "ERR: {err}",
        "quartz_failed": "Quartz click failed, fallback: {err}",
        "live_info": "Центр: {color} | Разница: {diff} | Соответствие: {match}",
        "yes": "ДА!",
        "no": "НЕТ!",
        "dep_pillow": "Работа с изображениями",
        "dep_pyautogui": "Управление мышью/клавиатурой",
        "dep_pynput": "Слушатель клавиш/мыши",
        "dep_quartz": "macOS системные события",
        "dep_mss": "Быстрый скриншот экрана",
        "dep_numpy": "Математические вычисления",
    },
    "en": {
        "title": "Color Trigger v2.0 (Simple)",
        "header": "🎯 TriggerBot v1.0",
        "dep_title": "🔧 TriggerBot — Dependency Checker",
        "dep_header": "🔧  Dependency Checker",
        "dep_subtitle": "TriggerBot v2.0",
        "libraries": "Libraries",
        "install": "Install",
        "checking": "Checking...",
        "install_all": "📦 Install all missing",
        "launch": "🚀 Launch TriggerBot",
        "recheck": "🔄 Recheck",
        "log": "Log",
        "ready": "✅ Your device is ready!",
        "missing": "⚠️ Not installed: {missing} of {total}",
        "installing": "⏳ Installing...",
        "installed_ok": "✅ {pkg} installed successfully!",
        "error_install": "❌ Error: {err}",
        "timeout_install": "⏰ Timeout: {pkg}",
        "err_general": "❌ {err}",
        "target_color_sec": "1. Target Color",
        "pipette": "🖌 Pipette",
        "palette": "🎨 Palette",
        "observed": "Observed: ...",
        "center_sec": "2. Zone (screen center)",
        "set_center": "🎯 Set Center",
        "size": "Size:",
        "tolerance": "Tolerance:",
        "show_frame": "Show Frame",
        "show_zone": "Show Reaction Zone",
        "hide_zone": "Hide Reaction Zone",
        "status_sec": "3. Status",
        "status_stopped": "STOPPED",
        "status_waiting": "WAITING FOR SHIFT",
        "status_active": "ACTIVE!",
        "start": "▶ START",
        "stop": "⏹ STOP",
        "reaction_frame": "Reaction Frame",
        "aim_target_3": "Aim at target! (3)",
        "aim_target_2": "Aim at target! (2)",
        "aim_target_1": "Aim at target! (1)",
        "center_pos": "Center: {pos}",
        "click_pipette": "Click...",
        "pipette_err": "Pipette error: {err}",
        "pipette_canceled": "Pipette canceled",
        "color_chosen": "Color chosen: {color}",
        "match_click": "MATCH! Clicking...",
        "err_msg": "ERR: {err}",
        "quartz_failed": "Quartz click failed, fallback: {err}",
        "live_info": "Center: {color} | Diff: {diff} | Match: {match}",
        "yes": "YES!",
        "no": "NO!",
        "dep_pillow": "Image processing",
        "dep_pyautogui": "Mouse/keyboard control",
        "dep_pynput": "Key/mouse listener",
        "dep_quartz": "macOS system events",
        "dep_mss": "Fast screen capture",
        "dep_numpy": "Mathematical computations",
    },
    "zh": {
        "title": "Color Trigger v2.0 (簡單)",
        "header": "🎯 TriggerBot v1.0",
        "dep_title": "🔧 TriggerBot — 依賴檢查器",
        "dep_header": "🔧  依賴檢查器",
        "dep_subtitle": "TriggerBot v2.0",
        "libraries": "函式庫",
        "install": "安裝",
        "checking": "正在檢查...",
        "install_all": "📦 安裝所有缺失項",
        "launch": "🚀 啟動 TriggerBot",
        "recheck": "🔄 重新檢查",
        "log": "日誌",
        "ready": "✅ 您的裝置已就緒！",
        "missing": "⚠️ 未安裝: {missing} / {total}",
        "installing": "⏳ 正在安裝...",
        "installed_ok": "✅ {pkg} 安裝成功！",
        "error_install": "❌ 錯誤: {err}",
        "timeout_install": "⏰ 超時: {pkg}",
        "err_general": "❌ 錯誤: {err}",
        "target_color_sec": "1. 目標顏色",
        "pipette": "🖌 滴管",
        "palette": "🎨 調色盤",
        "observed": "觀察到: ...",
        "center_sec": "2. 區域 (螢幕中心)",
        "set_center": "🎯 設定中心",
        "size": "大小:",
        "tolerance": "容差:",
        "show_frame": "顯示邊框",
        "show_zone": "顯示反應區域",
        "hide_zone": "隱藏反應區域",
        "status_sec": "3. 狀態",
        "status_stopped": "已停止",
        "status_waiting": "等待 SHIFT",
        "status_active": "啟動中！",
        "start": "▶ 開始",
        "stop": "⏹ 停止",
        "reaction_frame": "反應畫面",
        "aim_target_3": "瞄準目標！(3)",
        "aim_target_2": "瞄準目標！(2)",
        "aim_target_1": "瞄準目標！(1)",
        "center_pos": "中心: {pos}",
        "click_pipette": "點擊...",
        "pipette_err": "滴管錯誤: {err}",
        "pipette_canceled": "滴管已取消",
        "color_chosen": "顏色已選: {color}",
        "match_click": "匹配！點擊中...",
        "err_msg": "錯誤: {err}",
        "quartz_failed": "Quartz點擊失敗，使用備用方案: {err}",
        "live_info": "中心: {color} | 差異: {diff} | 匹配: {match}",
        "yes": "是！",
        "no": "否！",
        "dep_pillow": "圖像處理",
        "dep_pyautogui": "滑鼠/鍵盤控制",
        "dep_pynput": "按鍵/滑鼠監聽器",
        "dep_quartz": "macOS 系統事件",
        "dep_mss": "快速螢幕截圖",
        "dep_numpy": "數學計算",
    }
}

LANG_MAP = {
    "Українська": "uk",
    "Русский": "ru",
    "English": "en",
    "繁體中文": "zh"
}
LANG_MAP_REV = {v: k for k, v in LANG_MAP.items()}

def _t(key, **kwargs):
    lang = CURRENT_LANGUAGE if CURRENT_LANGUAGE in TRANSLATIONS else "en"
    text = TRANSLATIONS[lang].get(key, TRANSLATIONS["en"].get(key, key))
    if kwargs:
        try:
            return text.format(**kwargs)
        except Exception:
            pass
    return text

_DEPENDENCIES = [
    ("Pillow",        "PIL",          "dep_pillow"),
    ("pyautogui",     "pyautogui",    "dep_pyautogui"),
    ("pynput",        "pynput",       "dep_pynput"),
    ("pyobjc-framework-Quartz", "Quartz", "dep_quartz"),
    ("mss",           "mss",          "dep_mss"),
    ("numpy",         "numpy",        "dep_numpy"),
]


def _check_dependencies():
    results = []
    for pip_name, import_name, desc_key in _DEPENDENCIES:
        try:
            importlib.import_module(import_name)
            results.append((pip_name, import_name, desc_key, True))
        except ImportError:
            results.append((pip_name, import_name, desc_key, False))
    return results


def _all_installed():
    return all(ok for _, _, _, ok in _check_dependencies())


def _do_imports():
    global ImageGrab, ImageTk, Image, pyautogui, CGEventCreateMouseEvent, CGEventPost, kCGEventLeftMouseDown, kCGEventLeftMouseUp, kCGMouseButtonLeft, kCGHIDEventTap, CGEventSourceKeyState, kCGEventSourceStateCombinedSessionState
    from PIL import ImageGrab, ImageTk, Image
    import pyautogui as _pyautogui
    pyautogui = _pyautogui
    try:
        from Quartz import (
            CGEventCreateMouseEvent, CGEventPost,
            kCGEventLeftMouseDown, kCGEventLeftMouseUp,
            kCGMouseButtonLeft, kCGHIDEventTap,
            CGEventSourceKeyState, kCGEventSourceStateCombinedSessionState,
        )
    except ImportError:
        pass


def _beep():
    """Cross-platform beep for macOS."""
    try:
        subprocess.Popen(
            ["afplay", "/System/Library/Sounds/Tink.aiff"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
    except Exception:
        print("\a")

class ColorTriggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title(_t("title"))
        self.root.attributes('-topmost', True)
        self.root.geometry("350x600")
        self.root.resizable(False, False)
        
        self.target_color = (255, 0, 0)
        self.is_running = False
        self.shift_pressed = False
        self.monitoring_thread = None
        self.overlay_window = None
        self.picking_mode = False
        self.mouse_listener = None

        self.region_size = 60     
        self.color_tolerance = 30  
        self.scan_step = 2 
        self.create_widgets()
        self._update_ui_texts()
        
        
        self._poll_shift()
        
        self.update_live_info()
        self.update_vision_preview_loop()

    @staticmethod
    def _make_btn(parent, text, command, bg="#555", fg="white",
                  font=("Helvetica Neue", 10, "bold"), padx=10, pady=4,
                  width=None, state="normal"):
        """macOS-safe button: tk.Button ignores fg/bg under Aqua, so we
        build a clickable Label inside a coloured Frame instead."""
        frm = tk.Frame(parent, bg=bg, padx=1, pady=1, cursor="hand2")
        lbl = tk.Label(frm, text=text, font=font, fg=fg, bg=bg,
                       padx=padx, pady=pady, cursor="hand2")
        if width:
            lbl.config(width=width)
        lbl.pack()
        
        frm._lbl = lbl
        frm._cmd = command
        frm._base_bg = bg
        frm._base_fg = fg
        frm._state = state

        def on_click(e):
            if frm._state == "disabled":
                return
            frm._cmd()
        def on_enter(e):
            if frm._state != "disabled":
                lbl.config(bg="#666")
                frm.config(bg="#666")
        def on_leave(e):
            if frm._state != "disabled":
                lbl.config(bg=frm._base_bg)
                frm.config(bg=frm._base_bg)

        lbl.bind("<Button-1>", on_click)
        frm.bind("<Button-1>", on_click)
        lbl.bind("<Enter>", on_enter)
        lbl.bind("<Leave>", on_leave)

        if state == "disabled":
            lbl.config(fg="#999")
        return frm

    @staticmethod
    def _btn_config(btn_frm, **kw):
        """Change text / state / bg / fg of a custom frame-button."""
        lbl = btn_frm._lbl
        if "text" in kw:
            lbl.config(text=kw["text"])
        if "bg" in kw:
            btn_frm._base_bg = kw["bg"]
            btn_frm.config(bg=kw["bg"])
            lbl.config(bg=kw["bg"])
        if "fg" in kw:
            btn_frm._base_fg = kw["fg"]
            lbl.config(fg=kw["fg"])
        if "state" in kw:
            btn_frm._state = kw["state"]
            if kw["state"] == "disabled":
                lbl.config(fg="#999")
            else:
                lbl.config(fg=btn_frm._base_fg)

    def create_widgets(self):
        style = ttk.Style()
        style.configure("Bold.TLabel", font=("Arial", 10, "bold"))
        
        header = tk.Frame(self.root, bg="#222", pady=10)
        header.pack(fill="x")
        
        self.header_title = tk.Label(header, text=_t("header"), font=("Helvetica Neue", 14, "bold"), fg="white", bg="#222")
        self.header_title.pack(side="left", padx=10)
        
        lang_frame = tk.Frame(header, bg="#222")
        lang_frame.pack(side="right", padx=10)
        self.lang_cb = ttk.Combobox(lang_frame, values=["Українська", "Русский", "English", "繁體中文"], width=8, state="readonly")
        self.lang_cb.pack()
        self.lang_cb.bind("<<ComboboxSelected>>", self._on_lang_select)
        self.lang_cb.set(LANG_MAP_REV.get(CURRENT_LANGUAGE, "English"))
        
        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(fill="both", expand=True)

        self.c_frame = tk.LabelFrame(main_frame, text=_t("target_color_sec"), padx=5, pady=5)
        self.c_frame.pack(fill="x", pady=5)
        
        row1 = tk.Frame(self.c_frame)
        row1.pack(fill="x", pady=2)
        
        self.color_display = tk.Label(row1, bg=self.rgb_to_hex(self.target_color), width=6, height=1, relief="solid")
        self.color_display.pack(side="left", padx=5)
        
        self.pick_btn = self._make_btn(row1, text=_t("pipette"), command=self.start_picker,
                                        bg="#eee", fg="#222", font=("Helvetica Neue", 10))
        self.pick_btn.pack(side="left", padx=5)
        
        self.palette_btn = self._make_btn(row1, text=_t("palette"), command=self.choose_color_dialog,
                                           bg="#eee", fg="#222", font=("Helvetica Neue", 10))
        self.palette_btn.pack(side="left", padx=5)
        
        self.live_color_label = tk.Label(self.c_frame, text=_t("observed"), font=("Menlo", 8))
        self.live_color_label.pack(pady=2)

        self.r_frame = tk.LabelFrame(main_frame, text=_t("center_sec"), padx=5, pady=5)
        self.r_frame.pack(fill="x", pady=5)
        
        self.calib_btn = self._make_btn(self.r_frame, text=_t("set_center"),
                                         command=lambda: threading.Thread(target=self.start_calibration).start(),
                                         bg="#ddd", fg="#222", font=("Helvetica Neue", 10))
        self.calib_btn.pack(fill="x", pady=5)
        
        sz_row = tk.Frame(self.r_frame)
        sz_row.pack(fill="x")
        self.size_label = tk.Label(sz_row, text=_t("size"))
        self.size_label.pack(side="left")
        self.region_var = tk.IntVar(value=self.region_size)
        self.region_var.trace_add("write", self.on_settings_change)
        tk.Scale(sz_row, from_=10, to=400, orient="horizontal", variable=self.region_var, showvalue=False).pack(side="left", fill="x", expand=True, padx=5)
        tk.Label(sz_row, textvariable=self.region_var).pack(side="left")

        tol_row = tk.Frame(self.r_frame)
        tol_row.pack(fill="x", pady=5)
        self.tol_label = tk.Label(tol_row, text=_t("tolerance"))
        self.tol_label.pack(side="left")
        self.tol_var = tk.IntVar(value=self.color_tolerance)
        self.tol_var.trace_add("write", self.on_settings_change)
        tk.Scale(tol_row, from_=0, to=150, orient="horizontal", variable=self.tol_var, showvalue=False).pack(side="left", fill="x", expand=True, padx=5)
        tk.Label(tol_row, textvariable=self.tol_var).pack(side="left")

        self.overlay_btn = self._make_btn(self.r_frame, text=_t("show_frame"),
                                           command=self.toggle_overlay,
                                           bg="#FFC107", fg="#222", font=("Helvetica Neue", 10))
        self.overlay_btn.pack(fill="x", pady=5)

        self.ctrl_frame = tk.LabelFrame(main_frame, text=_t("status_sec"), padx=5, pady=5)
        self.ctrl_frame.pack(fill="x", pady=5)
        
        self.status_lbl = tk.Label(self.ctrl_frame, text=_t("status_stopped"), fg="red", font=("Arial", 12, "bold"))
        self.status_lbl.pack(pady=5)
        
        btns = tk.Frame(self.ctrl_frame)
        btns.pack()
        self.btn_start = self._make_btn(btns, text=_t("start"), command=self.start,
                                         bg="#4CAF50", fg="white", width=12)
        self.btn_start.pack(side="left", padx=5)
        self.btn_stop = self._make_btn(btns, text=_t("stop"), command=self.stop,
                                        bg="#f44336", fg="white", width=12, state="disabled")
        self.btn_stop.pack(side="left", padx=5)
        
        self.p_frame = tk.LabelFrame(main_frame, text=_t("reaction_frame"), padx=5, pady=5)
        self.p_frame.pack(fill="x", pady=5)
        self.preview_canvas = tk.Canvas(self.p_frame, height=80, bg="#ccc")
        self.preview_canvas.pack(fill="x")
        
        self.l_frame = tk.LabelFrame(main_frame, text=_t("log"), padx=5, pady=5)
        self.l_frame.pack(fill="both", expand=True)
        self.log_text = tk.Text(self.l_frame, height=5, font=("Menlo", 8))
        self.log_text.pack(fill="both", expand=True)

    def _on_lang_select(self, event):
        global CURRENT_LANGUAGE
        sel = self.lang_cb.get()
        CURRENT_LANGUAGE = LANG_MAP.get(sel, "en")
        self._update_ui_texts()

    def update_status_label(self):
        if not self.is_running:
            self.status_lbl.config(text=_t("status_stopped"), fg="red")
        elif self.shift_pressed:
            self.status_lbl.config(text=_t("status_active"), fg="green")
        else:
            self.status_lbl.config(text=_t("status_waiting"), fg="orange")

    def _update_ui_texts(self):
        self.root.title(_t("title"))
        self.header_title.config(text=_t("header"))
        
        self.c_frame.config(text=_t("target_color_sec"))
        self._btn_config(self.pick_btn, text=_t("pipette") if not self.picking_mode else _t("click_pipette"))
        self._btn_config(self.palette_btn, text=_t("palette"))
        
        self.r_frame.config(text=_t("center_sec"))
        
        if hasattr(self, 'custom_center'):
            self._btn_config(self.calib_btn, text=_t("center_pos", pos=self.custom_center))
        else:
            self._btn_config(self.calib_btn, text=_t("set_center"))
            
        self.size_label.config(text=_t("size"))
        self.tol_label.config(text=_t("tolerance"))
        
        if self.overlay_window:
            self._btn_config(self.overlay_btn, text=_t("hide_zone"))
        else:
            self._btn_config(self.overlay_btn, text=_t("show_frame"))
            
        self.ctrl_frame.config(text=_t("status_sec"))
        self.update_status_label()
        
        self._btn_config(self.btn_start, text=_t("start"))
        self._btn_config(self.btn_stop, text=_t("stop"))
        
        self.p_frame.config(text=_t("reaction_frame"))
        self.l_frame.config(text=_t("log"))


    def on_settings_change(self, *args):
        try:
            self.region_size = self.region_var.get()
            self.color_tolerance = self.tol_var.get()
            if self.overlay_window:
                self.update_overlay()
        except:
            pass

    def get_region(self):
        if hasattr(self, 'custom_center'):
            cx, cy = self.custom_center
        else:
            w, h = pyautogui.size()
            cx, cy = w // 2, h // 2
            
        s = self.region_size
        return (cx - s//2, cy - s//2, cx + s//2, cy + s//2)
        
    def start_calibration(self):
        self._btn_config(self.calib_btn, text=_t("aim_target_3"), bg="orange")
        self.root.update()
        time.sleep(1)
        self._btn_config(self.calib_btn, text=_t("aim_target_2"))
        self.root.update()
        time.sleep(1)
        self._btn_config(self.calib_btn, text=_t("aim_target_1"))
        self.root.update()
        time.sleep(1)

        pos = pyautogui.position()
        self.custom_center = pos
        self._btn_config(self.calib_btn, text=_t("center_pos", pos=pos), bg="#ddd")
        _beep()

        if self.overlay_window:
            self.update_overlay()
        else:
            self.toggle_overlay()

    def toggle_overlay(self):
        if self.overlay_window:
            self.overlay_window.destroy()
            self.overlay_window = None
            self._btn_config(self.overlay_btn, text=_t("show_frame"))
        else:
            self.overlay_window = tk.Toplevel(self.root)
            self.overlay_window.attributes('-topmost', True)
            self.overlay_window.attributes('-alpha', 0.3)
            self.overlay_window.overrideredirect(True)
            
            self.cv = tk.Canvas(self.overlay_window, bg='black', highlightthickness=2, highlightbackground='green')
            self.cv.pack(fill='both', expand=True)
            self.update_overlay()
            self._btn_config(self.overlay_btn, text=_t("hide_zone"))

    def update_overlay(self):
        if self.overlay_window:
            x1, y1, x2, y2 = get_bbox = self.get_region()
            w = x2 - x1
            h = y2 - y1
            self.overlay_window.geometry(f"{w}x{h}+{x1}+{y1}")
            self.cv.delete("all")
            self.cv.create_line(w//2, 0, w//2, h, fill="green")
            self.cv.create_line(0, h//2, w, h//2, fill="green")

    def start_picker(self):
        self.picking_mode = True
        self._btn_config(self.pick_btn, text=_t("click_pipette"), bg="yellow")
        
        import mss
        with mss.mss() as sct:
            self._picker_screenshot = sct.grab(sct.monitors[0])  
        
        self.picker_overlay = tk.Toplevel(self.root)
        self.picker_overlay.attributes('-alpha', 0.01)
        self.picker_overlay.attributes('-topmost', True)
        self.picker_overlay.overrideredirect(True)
        self.picker_overlay.config(cursor="crosshair")
        
        self.picker_overlay.geometry("20000x20000+-10000+-10000")
        
        self.picker_overlay.bind("<Button-1>", self._on_overlay_click)
        self.picker_overlay.bind("<Escape>", lambda e: self.cancel_pick())
        self.picker_overlay.focus_force()

    def _on_overlay_click(self, event):
        x, y = event.x_root, event.y_root
        if self.picker_overlay:
            self.picker_overlay.destroy()
            self.picker_overlay = None
        
        if not self.picking_mode:
            return
        try:
            shot = self._picker_screenshot

            import mss
            with mss.mss() as sct:
                mon = sct.monitors[0]
            px_x = int(x) - mon["left"]
            px_y = int(y) - mon["top"]

            px_x = max(0, min(px_x, shot.width - 1))
            px_y = max(0, min(px_y, shot.height - 1))
            pixel = shot.pixel(px_x, px_y)  
            self.target_color = pixel
            self.finish_pick()
        except Exception as e:
            self.log(_t("pipette_err", err=str(e)))
            self.cancel_pick()
        finally:
            self._picker_screenshot = None

    def cancel_pick(self):
        if hasattr(self, 'picker_overlay') and self.picker_overlay:
            self.picker_overlay.destroy()
            self.picker_overlay = None
        self._picker_screenshot = None
        self.picking_mode = False
        self._btn_config(self.pick_btn, text=_t("pipette"), bg="#eee")
        self.log(_t("pipette_canceled"))

    def finish_pick(self):
        self.picking_mode = False
        self._btn_config(self.pick_btn, text=_t("pipette"), bg="#eee")
        self.color_display.config(bg=self.rgb_to_hex(self.target_color))
        self.log(_t("color_chosen", color=self.target_color))

    def choose_color_dialog(self):
        c = colorchooser.askcolor(color=self.rgb_to_hex(self.target_color))
        if c[0]:
            self.target_color = tuple(map(int, c[0]))
            self.color_display.config(bg=c[1])

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.monitoring_thread = threading.Thread(target=self.loop, daemon=True)
            self.monitoring_thread.start()
            self._btn_config(self.btn_start, state="disabled")
            self._btn_config(self.btn_stop, state="normal")
            self.update_status_label()
            _beep()

    def stop(self):
        self.is_running = False
        self._btn_config(self.btn_start, state="normal")
        self._btn_config(self.btn_stop, state="disabled")
        self.update_status_label()
        _beep()

    def loop(self):
        import mss
        import numpy as np
        
        pyautogui.PAUSE = 0
        
        with mss.mss() as sct:
            while self.is_running:
                if self.shift_pressed:
                    try:
                        x1, y1, x2, y2 = self.get_region()
                        monitor = {
                            "top": int(y1), 
                            "left": int(x1), 
                            "width": int(x2 - x1), 
                            "height": int(y2 - y1)
                        }
                        
                        sct_img = sct.grab(monitor)
                        
                        arr = np.array(sct_img)
                        arr_rgb = arr[:, :, [2, 1, 0]]
                        
                        step = max(1, self.scan_step)
                        scan_slice = arr_rgb[::step, ::step]
                        
                        diff = np.abs(scan_slice.astype(int) - self.target_color)

                        mask = np.all(diff <= self.color_tolerance, axis=2)
                        
                        if np.any(mask):
                            self.shoot()
                            self.log(_t("match_click"))
                            time.sleep(0.1)

                        self.last_img = Image.fromarray(arr_rgb, 'RGB')
                            
                    except Exception as e:
                        self.log(_t("err_msg", err=str(e)))

    def shoot(self):
        try:
            # Use Quartz CGEvents for low-level mouse click on macOS
            from Quartz import (
                CGEventCreateMouseEvent, CGEventPost,
                kCGEventLeftMouseDown, kCGEventLeftMouseUp,
                kCGMouseButtonLeft, kCGHIDEventTap,
            )
            from Quartz import CGEventGetLocation
            import Quartz

            # Get current mouse position
            pos = pyautogui.position()
            point = Quartz.CGPointMake(pos[0], pos[1])

            # Mouse down
            event = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, point, kCGMouseButtonLeft)
            CGEventPost(kCGHIDEventTap, event)

            time.sleep(0.001)

            # Mouse up
            event = CGEventCreateMouseEvent(None, kCGEventLeftMouseUp, point, kCGMouseButtonLeft)
            CGEventPost(kCGHIDEventTap, event)

        except Exception as e:
            self.log(_t("quartz_failed", err=str(e)))
            try:
                pyautogui.click()
            except:
                pass

    def is_match(self, c):
        rd = abs(c[0] - self.target_color[0])
        gd = abs(c[1] - self.target_color[1])
        bd = abs(c[2] - self.target_color[2])
        return max(rd, gd, bd) <= self.color_tolerance

    def update_live_info(self):
        try:
            cx, cy, _, _ = self.get_region() 
            cx += self.region_size // 2
            cy += self.region_size // 2
            
            c = pyautogui.pixel(cx, cy)
            
            rd = abs(c[0] - self.target_color[0])
            gd = abs(c[1] - self.target_color[1])
            bd = abs(c[2] - self.target_color[2])
            diff = max(rd, gd, bd)
            
            match = _t("yes") if diff <= self.color_tolerance else _t("no")
            fg = "green" if diff <= self.color_tolerance else "red"
            
            self.live_color_label.config(text=_t("live_info", color=c, diff=diff, match=match), fg=fg)
            
        except:
            pass
        self.root.after(100, self.update_live_info)

    def update_vision_preview_loop(self):
        if hasattr(self, 'last_img') and self.last_img:
            try:
                i = self.last_img.resize((int(self.last_img.width * (80/self.last_img.height)), 80))
                self.tk_img = ImageTk.PhotoImage(i)
                self.preview_canvas.delete("all")
                self.preview_canvas.create_image(0, 0, anchor="nw", image=self.tk_img)
            except: pass
        self.root.after(100, self.update_vision_preview_loop)

    _VK_SHIFT = 0x38      
    _VK_RIGHT_SHIFT = 0x3C 

    def _poll_shift(self):
        """Poll Shift key state via Quartz — no Accessibility permissions needed."""
        try:
            left = CGEventSourceKeyState(kCGEventSourceStateCombinedSessionState, self._VK_SHIFT)
            right = CGEventSourceKeyState(kCGEventSourceStateCombinedSessionState, self._VK_RIGHT_SHIFT)
            now_pressed = left or right
        except Exception:
            now_pressed = False

        if now_pressed and not self.shift_pressed:
            self.shift_pressed = True
            if self.is_running:
                self.update_status_label()
        elif not now_pressed and self.shift_pressed:
            self.shift_pressed = False
            if self.is_running:
                self.update_status_label()

        self.root.after(30, self._poll_shift)  
                
    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % rgb
    
    def log(self, msg):
        self.log_text.insert("1.0", f"{msg}\n")

_BG         = "#1e1e2e"
_BG_SURFACE = "#282840"
_BG_CARD    = "#313244"
_TEXT       = "#cdd6f4"
_TEXT_DIM   = "#6c7086"
_GREEN      = "#a6e3a1"
_RED        = "#f38ba8"
_YELLOW     = "#f9e2af"
_BLUE       = "#89b4fa"
_MAUVE      = "#cba6f7"
_BTN_BG     = "#45475a"


class _DepCheckerWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(_t("dep_title"))
        self.root.configure(bg=_BG)
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True)

        win_w, win_h = 530, 800
        sx = self.root.winfo_screenwidth() // 2 - win_w // 2
        sy = self.root.winfo_screenheight() // 2 - win_h // 2
        self.root.geometry(f"{win_w}x{win_h}+{sx}+{sy}")

        self.dep_rows = {}
        self.installing = False
        self.should_launch = False

        self._build_ui()
        self._update_ui_texts()

    @staticmethod
    def _make_btn(parent, text, command, bg="#555", fg="white",
                  font=("Helvetica Neue", 10, "bold"), padx=10, pady=4,
                  width=None, state="normal", cursor="hand2"):
        """macOS-safe button using Label-in-Frame."""
        frm = tk.Frame(parent, bg=bg, padx=1, pady=1, cursor=cursor)
        lbl = tk.Label(frm, text=text, font=font, fg=fg, bg=bg,
                       padx=padx, pady=pady, cursor=cursor)
        if width:
            lbl.config(width=width)
        lbl.pack()
        frm._lbl = lbl
        frm._cmd = command
        frm._base_bg = bg
        frm._base_fg = fg
        frm._state = state

        def on_click(e):
            if frm._state == "disabled":
                return
            frm._cmd()
        def on_enter(e):
            if frm._state != "disabled":
                lbl.config(bg="#666")
                frm.config(bg="#666")
        def on_leave(e):
            if frm._state != "disabled":
                lbl.config(bg=frm._base_bg)
                frm.config(bg=frm._base_bg)

        lbl.bind("<Button-1>", on_click)
        frm.bind("<Button-1>", on_click)
        lbl.bind("<Enter>", on_enter)
        lbl.bind("<Leave>", on_leave)

        if state == "disabled":
            lbl.config(fg="#999")
        return frm

    @staticmethod
    def _btn_config(btn_frm, **kw):
        """Change text / state / bg / fg of a custom frame-button."""
        lbl = btn_frm._lbl
        if "text" in kw:
            lbl.config(text=kw["text"])
        if "bg" in kw:
            btn_frm._base_bg = kw["bg"]
            btn_frm.config(bg=kw["bg"])
            lbl.config(bg=kw["bg"])
        if "fg" in kw:
            btn_frm._base_fg = kw["fg"]
            lbl.config(fg=kw["fg"])
        if "state" in kw:
            btn_frm._state = kw["state"]
            if kw["state"] == "disabled":
                lbl.config(fg="#999")
            else:
                lbl.config(fg=btn_frm._base_fg)

    def _build_ui(self):
        header = tk.Frame(self.root, bg=_BG_SURFACE, pady=14)
        header.pack(fill="x")
        
        self.header_title = tk.Label(header, text=_t("dep_header"),
                 font=("Helvetica Neue", 16, "bold"), fg=_MAUVE, bg=_BG_SURFACE)
        self.header_title.pack()
        self.header_subtitle = tk.Label(header, text=_t("dep_subtitle"),
                 font=("Helvetica Neue", 10), fg=_TEXT_DIM, bg=_BG_SURFACE)
        self.header_subtitle.pack()

        lang_frame = tk.Frame(header, bg=_BG_SURFACE)
        lang_frame.pack(anchor="ne", padx=10, pady=(0, 0))
        self.lang_cb = ttk.Combobox(lang_frame, values=["Українська", "Русский", "English", "繁體中文"], width=10, state="readonly")
        self.lang_cb.pack(side="right")
        self.lang_cb.bind("<<ComboboxSelected>>", self._on_lang_select)
        self.lang_cb.set(LANG_MAP_REV.get(CURRENT_LANGUAGE, "English"))

        py_frame = tk.Frame(self.root, bg=_BG, pady=8, padx=20)
        py_frame.pack(fill="x")
        py_ver = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        tk.Label(py_frame, text=f"✅  Python {py_ver}",
                 font=("Helvetica Neue", 11, "bold"), fg=_GREEN, bg=_BG, anchor="w").pack(fill="x")
        tk.Label(py_frame, text=f"    {sys.executable}",
                 font=("Menlo", 8), fg=_TEXT_DIM, bg=_BG, anchor="w").pack(fill="x")

        tk.Frame(self.root, bg=_BTN_BG, height=1).pack(fill="x", padx=20, pady=4)

        self.libs_heading = tk.Label(self.root, text=_t("libraries"), font=("Helvetica Neue", 11, "bold"),
                 fg=_TEXT, bg=_BG, anchor="w", padx=20)
        self.libs_heading.pack(fill="x", pady=(8, 4))

        deps_container = tk.Frame(self.root, bg=_BG, padx=20)
        deps_container.pack(fill="x")

        for pip_name, import_name, desc_key in _DEPENDENCIES:
            row = tk.Frame(deps_container, bg=_BG_CARD, pady=6, padx=10)
            row.pack(fill="x", pady=2)
            row.columnconfigure(1, weight=1)

            status_lbl = tk.Label(row, text="⏳", font=("Helvetica Neue", 12),
                                  fg=_YELLOW, bg=_BG_CARD, width=2)
            status_lbl.grid(row=0, column=0, rowspan=2, padx=(0, 8))

            tk.Label(row, text=pip_name, font=("Helvetica Neue", 10, "bold"),
                     fg=_TEXT, bg=_BG_CARD, anchor="w").grid(row=0, column=1, sticky="w")
            desc_lbl = tk.Label(row, text=_t(desc_key), font=("Helvetica Neue", 8),
                     fg=_TEXT_DIM, bg=_BG_CARD, anchor="w")
            desc_lbl.grid(row=1, column=1, sticky="w")

            install_btn = self._make_btn(
                row, text=_t("install"), command=lambda p=pip_name: self._install_one(p),
                font=("Helvetica Neue", 9), fg=_BG, bg=_BLUE, padx=10
            )

            self.dep_rows[pip_name] = {
                "status_label": status_lbl, "btn": install_btn,
                "desc_label": desc_lbl, "desc_key": desc_key,
                "row": row, "installed": None,
            }

        tk.Frame(self.root, bg=_BTN_BG, height=1).pack(fill="x", padx=20, pady=8)

        self.overall_label = tk.Label(self.root, text=_t("checking"),
                                      font=("Helvetica Neue", 12, "bold"), fg=_YELLOW, bg=_BG)
        self.overall_label.pack(pady=4)

        btn_frame = tk.Frame(self.root, bg=_BG, pady=4)
        btn_frame.pack()

        self.install_all_btn = self._make_btn(
            btn_frame, text=_t("install_all"),
            command=self._install_all,
            font=("Helvetica Neue", 10, "bold"), fg=_BG, bg=_YELLOW,
            padx=16, pady=6
        )
        self.launch_btn = self._make_btn(
            btn_frame, text=_t("launch"),
            command=self._do_launch,
            font=("Helvetica Neue", 11, "bold"), fg=_BG, bg=_GREEN,
            padx=20, pady=8
        )
        self.recheck_btn = self._make_btn(
            btn_frame, text=_t("recheck"),
            command=self._refresh,
            font=("Helvetica Neue", 9), fg=_TEXT, bg=_BTN_BG,
            padx=12, pady=4
        )

        log_frame = tk.Frame(self.root, bg=_BG, padx=20, pady=4)
        log_frame.pack(fill="both", expand=True)
        self.log_heading = tk.Label(log_frame, text=_t("log"), font=("Helvetica Neue", 9),
                 fg=_TEXT_DIM, bg=_BG, anchor="w")
        self.log_heading.pack(fill="x")
        self.log_text = tk.Text(
            log_frame, height=6, font=("Menlo", 8),
            bg=_BG_SURFACE, fg=_TEXT, insertbackground=_TEXT,
            relief="flat", wrap="word"
        )
        self.log_text.pack(fill="both", expand=True)
        self.log_text.config(state="disabled")

    def _on_lang_select(self, event):
        global CURRENT_LANGUAGE
        sel = self.lang_cb.get()
        CURRENT_LANGUAGE = LANG_MAP.get(sel, "en")
        self._update_ui_texts()

    def _update_ui_texts(self):
        self.root.title(_t("dep_title"))
        self.header_title.config(text=_t("dep_header"))
        self.header_subtitle.config(text=_t("dep_subtitle"))
        self.libs_heading.config(text=_t("libraries"))
        self.log_heading.config(text=_t("log"))
        
        for pip_name, data in self.dep_rows.items():
            data["desc_label"].config(text=_t(data["desc_key"]))
            self._btn_config(data["btn"], text=_t("install"))

        self._btn_config(self.install_all_btn, text=_t("installing") if self.installing else _t("install_all"))
        self._btn_config(self.launch_btn, text=_t("launch"))
        self._btn_config(self.recheck_btn, text=_t("recheck"))
        
        self._refresh()

    def _refresh(self):
        results = _check_dependencies()
        missing = 0
        for pip_name, _, _, installed in results:
            rd = self.dep_rows[pip_name]
            rd["installed"] = installed
            if installed:
                rd["status_label"].config(text="✅", fg=_GREEN)
                rd["btn"].grid_forget()
            else:
                missing += 1
                rd["status_label"].config(text="❌", fg=_RED)
                rd["btn"].grid(row=0, column=2, rowspan=2, padx=(8, 0))

        self.install_all_btn.pack_forget()
        self.launch_btn.pack_forget()
        self.recheck_btn.pack_forget()

        if missing == 0:
            self.overall_label.config(text=_t("ready"), fg=_GREEN)
            self.launch_btn.pack(pady=4)
        else:
            self.overall_label.config(
                text=_t("missing", missing=missing, total=len(_DEPENDENCIES)), fg=_RED)
            self.install_all_btn.pack(pady=4)
            self.recheck_btn.pack(pady=4)

    def _install_one(self, pip_name):
        if not self.installing:
            self._run_install([pip_name])

    def _install_all(self):
        if self.installing:
            return
        missing = [n for n, d in self.dep_rows.items() if not d["installed"]]
        if missing:
            self._run_install(missing)

    def _run_install(self, packages):
        self.installing = True
        self._btn_config(self.install_all_btn, state="disabled", text=_t("installing"))
        for n in packages:
            self._btn_config(self.dep_rows[n]["btn"], state="disabled", text="⏳...")

        def worker():
            for pkg in packages:
                self._log(f">>> pip install {pkg}")
                try:
                    r = subprocess.run(
                        [sys.executable, "-m", "pip", "install", pkg],
                        capture_output=True, text=True, timeout=120
                    )
                    if r.returncode == 0:
                        self._log(_t("installed_ok", pkg=pkg))
                    else:
                        self._log(_t("error_install", err=(r.stderr or '')[-300:]))
                except subprocess.TimeoutExpired:
                    self._log(_t("timeout_install", pkg=pkg))
                except Exception as e:
                    self._log(_t("err_general", err=str(e)))
            self.root.after(0, self._after_install)

        threading.Thread(target=worker, daemon=True).start()

    def _after_install(self):
        self.installing = False
        self._btn_config(self.install_all_btn, state="normal", text=_t("install_all"))
        for d in self.dep_rows.values():
            self._btn_config(d["btn"], state="normal", text=_t("install"))
        importlib.invalidate_caches()
        self._refresh()

    def _do_launch(self):
        self.should_launch = True
        self.root.quit() 

    def _log(self, msg):
        def _append():
            self.log_text.config(state="normal")
            self.log_text.insert("end", msg + "\n")
            self.log_text.see("end")
            self.log_text.config(state="disabled")
        if threading.current_thread() is threading.main_thread():
            _append()
        else:
            self.root.after(0, _append)

    def run(self):
        self.root.mainloop()
        return self.should_launch

if __name__ == "__main__":
    if "--skip-check" in sys.argv:
        _do_imports()
        root = tk.Tk()
        app = ColorTriggerApp(root)
        root.mainloop()
    else:
        checker = _DepCheckerWindow()
        should_launch = checker.run()
        checker.root.destroy()

        if should_launch and _all_installed():
            subprocess.Popen([sys.executable, os.path.abspath(__file__), "--skip-check", "--lang", CURRENT_LANGUAGE])
