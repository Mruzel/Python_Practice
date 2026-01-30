import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# ---------------- Functions ---------------- #

def calculate_profit():
    try:
        income = float(income_entry.get())
        expenses = float(expenses_entry.get())

        profit = income - expenses

        result_label.config(
            text=f"Net Profit: ${profit:,.2f}",
            fg="green" if profit >= 0 else "red"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


def show_chart():
    try:
        income = float(income_entry.get())
        expenses = float(expenses_entry.get())
        profit = income - expenses

        labels = ["Income", "Expenses", "Profit"]
        values = [income, expenses, profit]

        plt.figure()
        plt.bar(labels, values)
        plt.title("Monthly Business Summary")
        plt.ylabel("Amount ($)")
        plt.show()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


# ---------------- Main Window ---------------- #

root = tk.Tk()
root.title("Business Profit Tracker")
root.geometry("400x350")
root.resizable(False, False)

# ---------------- UI ---------------- #

title_label = tk.Label(
    root,
    text="Business Profit Tracker",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)

# Income
income_label = tk.Label(root, text="Monthly Income ($)")
income_label.pack()
income_entry = tk.Entry(root, width=25)
income_entry.pack(pady=5)

# Expenses
expenses_label = tk.Label(root, text="Monthly Expenses ($)")
expenses_label.pack()
expenses_entry = tk.Entry(root, width=25)
expenses_entry.pack(pady=5)

# Buttons
calculate_btn = tk.Button(
    root,
    text="Calculate Profit",
    width=20,
    command=calculate_profit
)
calculate_btn.pack(pady=10)

chart_btn = tk.Button(
    root,
    text="Show Chart",
    width=20,
    command=show_chart
)
chart_btn.pack(pady=5)

# Result
result_label = tk.Label(
    root,
    text="Net Profit: $0.00",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=15)

# ---------------- Run App ---------------- #

root.mainloop()