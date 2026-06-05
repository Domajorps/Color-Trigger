import tkinter as tk
import pyautogui
root = tk.Tk()
root.attributes('-alpha', 0.01) # Nearly invisible
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.config(cursor="crosshair")

def on_click(e):
    x, y = e.x_root, e.y_root
    print(f"Clicked at {x}, {y}")
    root.destroy()
    # Read color after window is destroyed
    def read_color():
        try:
            r, g, b = pyautogui.pixel(x, y)
            print(f"Color: {r}, {g}, {b}")
        except Exception as ex:
            print("Error", ex)
    import time
    time.sleep(0.1) # Wait for destroy to propagate visually
    read_color()

root.bind("<Button-1>", on_click)
root.mainloop()
