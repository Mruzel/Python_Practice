import tkinter as tk
from tkinter import messagebox

# ---------------- CONSTANTS ---------------- #
STANDARD_DEDUCTION = {
    "Single": 15750,
    "Married Filing Jointly": 31500,
    "Head of Household": 23625
}


TAX_RATE = 0.10  # simple estimate for demo
EITC_TABLE = {0: 600, 1: 3995, 2: 6604, 3: 7430}  # simplified max credits

# ---------------- FUNCTIONS ---------------- #
def calculate_eitc(income, dependents):
    dependents = min(dependents, 3)
    max_credit = EITC_TABLE[dependents]
    if income <= 10000:
        return max_credit
    elif income <= 25000:
        return max_credit * 0.5
    else:
        return 0

def calculate_tax():
    try:
        income = float(entry_income.get())
        expenses = float(entry_expenses.get())
        dependents = int(entry_dependents.get())
        status = filing_status.get()

        taxable_income = max(0, income - expenses - STANDARD_DEDUCTION[status])
        estimated_tax = taxable_income * TAX_RATE
        eitc = calculate_eitc(income, dependents)

        final_tax = max(0, estimated_tax - eitc)
        refund_or_due = -final_tax if final_tax > 0 else 0  # negative means due

        result_text = (
            f"Estimated Tax Summary (TY 2025)\n\n"
            f"Filing Status: {status}\n"
            f"Total Household Income: ${income:,.2f}\n"
            f"Total Expenses (W-2 withheld + business): ${expenses:,.2f}\n"
            f"Taxable Income: ${taxable_income:,.2f}\n"
            f"Estimated Tax: ${estimated_tax:,.2f}\n"
            f"EITC: -${eitc:,.2f}\n"
            f"--------------------------------\n"
        )

        if refund_or_due >= 0:
            result_text += f"Estimated Refund: ${refund_or_due:,.2f}"
        else:
            result_text += f"Estimated Tax Due: ${abs(final_tax):,.2f}"

        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("Household Tax Estimator – TY 2025 (Estimate Only)")
root.geometry("500x600")
root.configure(bg="white")
root.resizable(False, False)

# Title
tk.Label(root, text="Household Tax Estimator (Estimate Only)", font=("Arial", 16, "bold"),
         bg="white").pack(pady=10)

tk.Label(root, text="⚠ This calculator is for estimation only.\nConsult a tax professional for exact results.",
         fg="red", bg="white").pack(pady=5)

# Instructions
tk.Label(root, text="💡 Enter total household income (W-2 + 1099 etc.) and expenses (tax withheld + business).",
         fg="blue", bg="white", wraplength=450, justify="left").pack(pady=5)

# Filing Status
tk.Label(root, text="Filing Status:", bg="white").pack(pady=5)
filing_status = tk.StringVar(value="Single")
tk.OptionMenu(root, filing_status, "Single", "Married Filing Jointly", "Head of Household").pack()

# Total Income
tk.Label(root, text="Total Household Income ($):", bg="white").pack(pady=5)
entry_income = tk.Entry(root)
entry_income.pack()

# Total Expenses
tk.Label(root, text="Total Expenses ($) – W-2 withheld + business expenses", bg="white", wraplength=450, justify="left").pack(pady=5)
entry_expenses = tk.Entry(root)
entry_expenses.pack()

# Dependents
tk.Label(root, text="Number of Dependents:", bg="white").pack(pady=5)
entry_dependents = tk.Entry(root)
entry_dependents.insert(0, "0")
entry_dependents.pack()

# Calculate Button at the bottom
tk.Button(root, text="Calculate Estimate", bg="black", fg="white",
          font=("Arial", 14, "bold"), command=calculate_tax).pack(side="bottom", pady=20)

# Result Label
result_label = tk.Label(root, text="", bg="white", font=("Arial", 11), justify="left")
result_label.pack(pady=10)

# Talk to Tax Pro CTA
tk.Label(root, text="💬 Want a full professional review? Contact Strits Tax today!",
         fg="green", bg="white", font=("Arial", 12, "bold"), wraplength=450, justify="center").pack(side="bottom", pady=10)

# Watermark
tk.Label(root, text="mRuZel | Estimate Only", fg="gray", bg="white", font=("Arial", 9)).pack(side="bottom", pady=5)

root.mainloop()
