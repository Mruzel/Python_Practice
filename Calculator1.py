import tkinter as tk

# ---------------- Functions ---------------- #

def press(key):
    if key == "C":
        display_var.set("")
    elif key == "=":
        try:
            result = eval(display_var.get())
            display_var.set(result)
        except:
            display_var.set("Error")
    else:
        display_var.set(display_var.get() + key)


def key_input(event):
    key = event.keysym

    if key in ("Return", "KP_Enter"):
        press("=")
    elif key == "BackSpace":
        display_var.set(display_var.get()[:-1])
    elif key == "Escape":
        press("C")
    elif key.startswith("KP_"):
        kp = key.replace("KP_", "")
        if kp in "0123456789":
            press(kp)
        elif kp == "Add":
            press("+")
        elif kp == "Subtract":
            press("-")
        elif kp == "Multiply":
            press("*")
        elif kp == "Divide":
            press("/")
        elif kp == "Decimal":
            press(".")
    elif event.char in "0123456789+-*/.":
        press(event.char)

    return "break"


# ---------------- Main Window ---------------- #

root = tk.Tk()
root.title("Black & Gold Calculator")
root.geometry("320x480")  # Slightly taller for watermark
root.configure(bg="black")
root.resizable(False, False)

root.bind_all("<Key>", key_input)

# ---------------- Display ---------------- #

display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 22, "bold"),
    bg="white",
    fg="black",
    bd=10,
    relief="ridge",
    justify="right"
)
display.pack(fill="x", padx=10, pady=15)

root.focus_force()

# ---------------- Button Style ---------------- #

btn_bg = "#D4AF37"
btn_fg = "black"
btn_font = ("Arial", 16, "bold")

# ---------------- Buttons Layout ---------------- #

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
    ("C",)
]

btn_frame = tk.Frame(root, bg="black")
btn_frame.pack()

for row in buttons:
    row_frame = tk.Frame(btn_frame, bg="black")
    row_frame.pack(pady=5)

    for btn in row:
        tk.Button(
            row_frame,
            text=btn,
            width=5,
            height=2,
            font=btn_font,
            bg=btn_bg,
            fg=btn_fg,
            command=lambda b=btn: press(b)
        ).pack(side="left", padx=5)

# ---------------- Watermark ---------------- #

watermark = tk.Label(
    root,
    text="mRuZel",
    font=("Arial", 10, "italic"),
    fg="#666666",   # subtle gray
    bg="black"
)
watermark.pack(side="bottom", pady=8)

# ---------------- Run App ---------------- #

root.mainloop()
