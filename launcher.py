import tkinter as tk
from tkinter import font as tkfont, ttk
import subprocess
import sys
import threading
import importlib
import os

# --- LOCALIZATION CONFIGURATION ---
# Supported codes: "uk" (Ukrainian), "ru" (Russian), "en" (English), "zh" (Traditional Chinese)
DEFAULT_LANGUAGE = "ru"
CURRENT_LANGUAGE = DEFAULT_LANGUAGE

# Read command line override if present
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
        "error_install": "❌ Помилка при встановленні {pkg}: {err}",
        "timeout_install": "⏰ Таймаут при встановленні {pkg}",
        "err_general": "❌ {err}",
        "launching": "🚀 Запускаю: {path}",
        "dep_pillow": "Робота із зображеннями",
        "dep_pyautogui": "Керування мишею/клавіатурою",
        "dep_pynput": "Слухач клавіш/миші",
        "dep_quartz": "macOS системні події",
        "dep_mss": "Швидкий знімок екрана",
        "dep_numpy": "Математичні обчислення",
    },
    "ru": {
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
        "error_install": "❌ Ошибка при установке {pkg}: {err}",
        "timeout_install": "⏰ Таймаут при установке {pkg}",
        "err_general": "❌ {err}",
        "launching": "🚀 Запускаю: {path}",
        "dep_pillow": "Работа с изображениями",
        "dep_pyautogui": "Управление мышью/клавиатурой",
        "dep_pynput": "Слушатель клавиш/мыши",
        "dep_quartz": "macOS системные события",
        "dep_mss": "Быстрый скриншот экрана",
        "dep_numpy": "Математические вычисления",
    },
    "en": {
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
        "error_install": "❌ Error installing {pkg}: {err}",
        "timeout_install": "⏰ Timeout installing {pkg}",
        "err_general": "❌ {err}",
        "launching": "🚀 Launching: {path}",
        "dep_pillow": "Image processing",
        "dep_pyautogui": "Mouse/keyboard control",
        "dep_pynput": "Key/mouse listener",
        "dep_quartz": "macOS system events",
        "dep_mss": "Fast screen capture",
        "dep_numpy": "Mathematical computations",
    },
    "zh": {
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
        "error_install": "❌ 安裝 {pkg} 發生錯誤: {err}",
        "timeout_install": "⏰ 安裝 {pkg} 超時",
        "err_general": "❌ 錯誤: {err}",
        "launching": "🚀 正在啟動: {path}",
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

DEPENDENCIES = [
    ("Pillow",        "PIL",          "dep_pillow"),
    ("pyautogui",     "pyautogui",    "dep_pyautogui"),
    ("pynput",        "pynput",       "dep_pynput"),
    ("pyobjc-framework-Quartz", "Quartz", "dep_quartz"),
    ("mss",           "mss",          "dep_mss"),
    ("numpy",         "numpy",        "dep_numpy"),
]

BG           = "#1e1e2e"
BG_SURFACE   = "#282840"
BG_CARD      = "#313244"
TEXT         = "#cdd6f4"
TEXT_DIM     = "#6c7086"
GREEN        = "#a6e3a1"
RED          = "#f38ba8"
YELLOW       = "#f9e2af"
BLUE         = "#89b4fa"
MAUVE        = "#cba6f7"
BTN_BG       = "#45475a"
BTN_HOVER    = "#585b70"


class DependencyChecker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(_t("dep_title"))
        self.root.configure(bg=BG)
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True)

        win_w, win_h = 520, 620
        sx = self.root.winfo_screenwidth() // 2 - win_w // 2
        sy = self.root.winfo_screenheight() // 2 - win_h // 2
        self.root.geometry(f"{win_w}x{win_h}+{sx}+{sy}")

        self.dep_rows = {}      # pip_name -> dict(status_label, btn, ...)
        self.installing = False

        self._build_ui()
        self._update_ui_texts()

    def _build_ui(self):
        header = tk.Frame(self.root, bg=BG_SURFACE, pady=14)
        header.pack(fill="x")
        
        self.header_title = tk.Label(
            header, text=_t("dep_header"),
            font=("Helvetica Neue", 16, "bold"), fg=MAUVE, bg=BG_SURFACE
        )
        self.header_title.pack()
        self.header_subtitle = tk.Label(
            header, text=_t("dep_subtitle"),
            font=("Helvetica Neue", 10), fg=TEXT_DIM, bg=BG_SURFACE
        )
        self.header_subtitle.pack()

        # Language Selector
        lang_frame = tk.Frame(header, bg=BG_SURFACE)
        lang_frame.pack(anchor="ne", padx=10, pady=(0, 0))
        self.lang_cb = ttk.Combobox(lang_frame, values=["Українська", "Русский", "English", "繁體中文"], width=10, state="readonly")
        self.lang_cb.pack(side="right")
        self.lang_cb.bind("<<ComboboxSelected>>", self._on_lang_select)
        self.lang_cb.set(LANG_MAP_REV.get(CURRENT_LANGUAGE, "English"))

        py_frame = tk.Frame(self.root, bg=BG, pady=8, padx=20)
        py_frame.pack(fill="x")

        py_ver = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        py_path = sys.executable
        tk.Label(
            py_frame,
            text=f"✅  Python {py_ver}",
            font=("Helvetica Neue", 11, "bold"), fg=GREEN, bg=BG, anchor="w"
        ).pack(fill="x")
        tk.Label(
            py_frame,
            text=f"    {py_path}",
            font=("Menlo", 8), fg=TEXT_DIM, bg=BG, anchor="w"
        ).pack(fill="x")

        tk.Frame(self.root, bg=BTN_BG, height=1).pack(fill="x", padx=20, pady=4)

        self.libs_heading = tk.Label(
            self.root, text=_t("libraries"), font=("Helvetica Neue", 11, "bold"),
            fg=TEXT, bg=BG, anchor="w", padx=20
        )
        self.libs_heading.pack(fill="x", pady=(8, 4))

        deps_container = tk.Frame(self.root, bg=BG, padx=20)
        deps_container.pack(fill="x")

        for pip_name, import_name, desc_key in DEPENDENCIES:
            row = tk.Frame(deps_container, bg=BG_CARD, pady=6, padx=10)
            row.pack(fill="x", pady=2)
            row.columnconfigure(1, weight=1)

            status_lbl = tk.Label(
                row, text="⏳", font=("Helvetica Neue", 12),
                fg=YELLOW, bg=BG_CARD, width=2
            )
            status_lbl.grid(row=0, column=0, rowspan=2, padx=(0, 8))

            tk.Label(
                row, text=pip_name, font=("Helvetica Neue", 10, "bold"),
                fg=TEXT, bg=BG_CARD, anchor="w"
            ).grid(row=0, column=1, sticky="w")
            desc_lbl = tk.Label(
                row, text=_t(desc_key), font=("Helvetica Neue", 8),
                fg=TEXT_DIM, bg=BG_CARD, anchor="w"
            )
            desc_lbl.grid(row=1, column=1, sticky="w")

            install_btn = tk.Button(
                row, text=_t("install"), font=("Helvetica Neue", 9),
                fg=BG, bg=BLUE, activebackground=MAUVE,
                relief="flat", padx=10, cursor="hand2",
                command=lambda p=pip_name: self._install_one(p)
            )

            self.dep_rows[pip_name] = {
                "status_label": status_lbl,
                "btn": install_btn,
                "desc_label": desc_lbl,
                "desc_key": desc_key,
                "row": row,
                "installed": None,
            }

        tk.Frame(self.root, bg=BTN_BG, height=1).pack(fill="x", padx=20, pady=8)

        self.overall_label = tk.Label(
            self.root, text=_t("checking"),
            font=("Helvetica Neue", 12, "bold"), fg=YELLOW, bg=BG
        )
        self.overall_label.pack(pady=4)

        btn_frame = tk.Frame(self.root, bg=BG, pady=4)
        btn_frame.pack()

        self.install_all_btn = tk.Button(
            btn_frame, text=_t("install_all"),
            font=("Helvetica Neue", 10, "bold"), fg=BG, bg=YELLOW,
            activebackground="#e0c878", relief="flat", padx=16, pady=6,
            cursor="hand2", command=self._install_all
        )

        self.launch_btn = tk.Button(
            btn_frame, text=_t("launch"),
            font=("Helvetica Neue", 11, "bold"), fg=BG, bg=GREEN,
            activebackground="#8cd490", relief="flat", padx=20, pady=8,
            cursor="hand2", command=self._launch_app
        )

        self.recheck_btn = tk.Button(
            btn_frame, text=_t("recheck"),
            font=("Helvetica Neue", 9), fg=TEXT, bg=BTN_BG,
            activebackground=BTN_HOVER, relief="flat", padx=12, pady=4,
            cursor="hand2", command=self._check_all
        )

        log_frame = tk.Frame(self.root, bg=BG, padx=20, pady=4)
        log_frame.pack(fill="both", expand=True)
        self.log_heading = tk.Label(
            log_frame, text=_t("log"), font=("Helvetica Neue", 9),
            fg=TEXT_DIM, bg=BG, anchor="w"
        )
        self.log_heading.pack(fill="x")
        self.log_text = tk.Text(
            log_frame, height=6, font=("Menlo", 8),
            bg=BG_SURFACE, fg=TEXT, insertbackground=TEXT,
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
            data["btn"].config(text=_t("install"))

        self.install_all_btn.config(text=_t("installing") if self.installing else _t("install_all"))
        self.launch_btn.config(text=_t("launch"))
        self.recheck_btn.config(text=_t("recheck"))

        self._check_all()

    def _check_all(self):
        missing = 0
        for pip_name, import_name, desc_key in DEPENDENCIES:
            installed = self._check_module(import_name)
            row_data = self.dep_rows[pip_name]
            row_data["installed"] = installed

            if installed:
                row_data["status_label"].config(text="✅", fg=GREEN)
                # Скрыть кнопку
                row_data["btn"].grid_forget()
            else:
                missing += 1
                row_data["status_label"].config(text="❌", fg=RED)
                # Показать кнопку
                row_data["btn"].grid(row=0, column=2, rowspan=2, padx=(8, 0))

        self.install_all_btn.pack_forget()
        self.launch_btn.pack_forget()
        self.recheck_btn.pack_forget()

        if missing == 0:
            self.overall_label.config(
                text=_t("ready"),
                fg=GREEN
            )
            self.launch_btn.pack(pady=4)
        else:
            self.overall_label.config(
                text=_t("missing", missing=missing, total=len(DEPENDENCIES)),
                fg=RED
            )
            self.install_all_btn.pack(pady=4)
            self.recheck_btn.pack(pady=4)

    def _check_module(self, import_name):
        try:
            importlib.import_module(import_name)
            return True
        except ImportError:
            return False

    def _install_one(self, pip_name):
        if self.installing:
            return
        self._run_install([pip_name])

    def _install_all(self):
        if self.installing:
            return
        missing = [
            name for name, data in self.dep_rows.items()
            if not data["installed"]
        ]
        if missing:
            self._run_install(missing)

    def _run_install(self, packages):
        self.installing = True
        self.install_all_btn.config(state="disabled", text=_t("installing"))
        for name in packages:
            self.dep_rows[name]["btn"].config(state="disabled", text="⏳...")

        def worker():
            for pkg in packages:
                self._log(f">>> pip install {pkg}")
                try:
                    result = subprocess.run(
                        [sys.executable, "-m", "pip", "install", pkg],
                        capture_output=True, text=True, timeout=120
                    )
                    if result.returncode == 0:
                        self._log(_t("installed_ok", pkg=pkg))
                    else:
                        self._log(_t("error_install", pkg=pkg, err=(result.stderr[-300:] if result.stderr else "Unknown error")))
                except subprocess.TimeoutExpired:
                    self._log(_t("timeout_install", pkg=pkg))
                except Exception as e:
                    self._log(_t("err_general", err=str(e)))

            self.root.after(0, self._after_install)

        threading.Thread(target=worker, daemon=True).start()

    def _after_install(self):
        self.installing = False
        self.install_all_btn.config(state="normal", text=_t("install_all"))
        for name, data in self.dep_rows.items():
            data["btn"].config(state="normal", text=_t("install"))
        importlib.invalidate_caches()
        self._check_all()

    def _launch_app(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(script_dir, "color_trigger.py")
        self._log(_t("launching", path=script_path))
        subprocess.Popen([sys.executable, script_path, "--lang", CURRENT_LANGUAGE], cwd=script_dir)
        self.root.after(500, self.root.destroy)

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


if __name__ == "__main__":
    app = DependencyChecker()
    app.run()
