import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def calculate_tax():
    try:
        income = float(entry_income.get())
        dependents = int(entry_dependents.get())
        status = filing_status.get()

        deductions = {
            "Single": 14600,
            "Married Filing Jointly": 29200,
            "Head of Household": 21900
        }

        taxable_income = max(0, income - deductions[status])

        tax = 0
        if status == "Single":
            tax = taxable_income * 0.10 if taxable_income <= 11600 else (11600 * 0.10) + ((taxable_income - 11600) * 0.12)
        elif status == "Married Filing Jointly":
            tax = taxable_income * 0.10 if taxable_income <= 23200 else (23200 * 0.10) + ((taxable_income - 23200) * 0.12)
        else:
            tax = taxable_income * 0.10 if taxable_income <= 16550 else (16550 * 0.10) + ((taxable_income - 16550) * 0.12)

        credit = dependents * 2000
        final_tax = max(0, tax - credit)

        result_label.config(text=f"Taxable Income: ${taxable_income:,.2f}\nEstimated Tax: ${final_tax:,.2f}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input")

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Federal Tax Calculator 2025")
root.geometry("440x520")
root.configure(bg="black")

# 🔥 FORCE WINDOW TO FRONT (macOS FIX)
root.lift()
root.attributes("-topmost", True)
root.after(100, lambda: root.attributes("-topmost", False))

# ---------------- LOGO ---------------- #

try:
    img = Image.open("strits_tax_logo.png")
    img = img.resize((260, 70))
    logo_img = ImageTk.PhotoImage(img)
    logo_label = tk.Label(root, image=logo_img, bg="black")
    logo_label.image = logo_img  # 🔥 PREVENT GC
    logo_label.pack(pady=10)
except Exception as e:
    print("Logo load failed:", e)
    tk.Label(root, text="STRITS TAX", fg="gold", bg="black",
             font=("Arial", 18, "bold")).pack(pady=10)

# ---------------- UI ---------------- #

tk.Label(root, text="Annual Income ($):", fg="white", bg="black").pack()
entry_income = tk.Entry(root)
entry_income.pack()

tk.Label(root, text="Filing Status:", fg="white", bg="black").pack(pady=5)
filing_status = tk.StringVar(value="Single")
tk.OptionMenu(root, filing_status, "Single", "Married Filing Jointly", "Head of Household").pack()

tk.Label(root, text="Dependents:", fg="white", bg="black").pack(pady=5)
entry_dependents = tk.Entry(root)
entry_dependents.insert(0, "0")
entry_dependents.pack()

tk.Button(root, text="Calculate", bg="gold", fg="black",
          font=("Arial", 14, "bold"), command=calculate_tax).pack(pady=15)

result_label = tk.Label(root, text="", fg="white", bg="black", font=("Arial", 12))
result_label.pack()

tk.Label(root, text="mRuZel", fg="gray", bg="black",
         font=("Arial", 10, "italic")).pack(side="bottom", pady=5)

print("GUI started successfully")  # 🔍 DEBUG CONFIRMATION
root.mainloop()
