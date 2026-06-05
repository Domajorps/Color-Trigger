import tkinter as tk
import pyautogui
root = tk.Tk()
root.attributes('-alpha', 0.01)
root.overrideredirect(True)
root.attributes('-topmost', True)
root.geometry("20000x20000+-10000+-10000")
root.config(cursor="crosshair")

def on_click(e):
    x, y = e.x_root, e.y_root
    print(f"Clicked at {x}, {y}")
    root.destroy()

root.bind("<Button-1>", on_click)
root.mainloop()
