import tkinter as tk
from datetime import datetime

open("keystrokes.txt", "w").close()


def log_key(event):
    key = event.keysym

    if key == "space":
        key = "[space]"
    elif key == "Return":
        key = "[next line] \n"
    elif key == "BackSpace":
        key = "[BACKSPACE]"
    elif len(key) > 1:
        key = f"[{key}]"

    with open("keystrokes.txt", "a") as file:
        time=datetime.now().strftime("%H:%M:%S")
        file.write(f"{time}: {key}\n")

root = tk.Tk()
root.title("Simple Keylogger Simulator")
root.geometry("500x300")

label = tk.Label(
    root,
    text="Type inside the box below.\nYour keystrokes will be saved.",
    font=("Arial", 12)
)
label.pack(pady=10)

text_box = tk.Text(
    root,
    height=10,
    width=50,
    font=("Arial", 12),
    wrap="word"
)
text_box.pack(pady=10)

text_box.bind("<Key>", log_key)

def clear_log():
    open("keystrokes.txt", "w").close()
clear_button = tk.Button(
    root,
    text="Clear Log File",
    command=clear_log,
    font=("Arial", 12)
)
clear_button.pack(pady=15)

root.mainloop()