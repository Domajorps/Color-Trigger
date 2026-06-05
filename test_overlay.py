import tkinter as tk
root = tk.Tk()
root.attributes('-alpha', 0.1) # Must be slightly visible to catch events on mac?
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
def on_click(e):
    print("Clicked at", e.x_root, e.y_root)
    root.destroy()
root.bind("<Button-1>", on_click)
root.mainloop()
