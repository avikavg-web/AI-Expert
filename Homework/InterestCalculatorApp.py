import tkinter as tk
from tkinter import messagebox


def calculate_interest():
    try:
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())

        simple_interest = (principal * rate * time) / 100

        total_amount = principal * ((1 + rate / 100) ** time)
        compound_interest = total_amount - principal

        lbl_si_result.config(text=f"${simple_interest:,.2f}")
        lbl_ci_result.config(text=f"${compound_interest:,.2f}")

    except ValueError:
        messagebox.showerror(
            "Input Error", "Please enter valid numeric values for all fields."
        )


root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.configure(bg="#f4f6f9")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

lbl_header = tk.Label(
    root,
    text="Interest Calculator",
    font=("Arial", 16, "bold"),
    bg="#f4f6f9",
    fg="#333333",
)
lbl_header.grid(row=0, column=0, columnspan=2, pady=20)

lbl_principal = tk.Label(
    root, text="Principal ($):", font=("Arial", 11), bg="#f4f6f9", anchor="e"
)
lbl_principal.grid(row=1, column=0, sticky="ew", padx=20, pady=10)
entry_principal = tk.Entry(root, font=("Arial", 11), bd=2, relief="groove")
entry_principal.grid(row=1, column=1, sticky="w", padx=20, pady=10)

lbl_time = tk.Label(
    root, text="Time (Years):", font=("Arial", 11), bg="#f4f6f9", anchor="e"
)
lbl_time.grid(row=2, column=0, sticky="ew", padx=20, pady=10)
entry_time = tk.Entry(root, font=("Arial", 11), bd=2, relief="groove")
entry_time.grid(row=2, column=1, sticky="w", padx=20, pady=10)

lbl_rate = tk.Label(
    root, text="Rate of Interest (%):", font=("Arial", 11), bg="#f4f6f9", anchor="e"
)
lbl_rate.grid(row=3, column=0, sticky="ew", padx=20, pady=10)
entry_rate = tk.Entry(root, font=("Arial", 11), bd=2, relief="groove")
entry_rate.grid(row=3, column=1, sticky="w", padx=20, pady=10)

btn_calculate = tk.Button(
    root,
    text="Calculate",
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    activeforeground="white",
    padx=10,
    pady=5,
    command=calculate_interest,
)
btn_calculate.grid(row=4, column=0, columnspan=2, pady=20)

lbl_si_text = tk.Label(
    root,
    text="Simple Interest:",
    font=("Arial", 11, "bold"),
    bg="#f4f6f9",
    anchor="e",
)
lbl_si_text.grid(row=5, column=0, sticky="ew", padx=20, pady=8)
lbl_si_result = tk.Label(
    root, text="$0.00", font=("Arial", 11, "bold"), bg="#f4f6f9", fg="#2e7d32"
)
lbl_si_result.grid(row=5, column=1, sticky="w", padx=20, pady=8)

lbl_ci_text = tk.Label(
    root,
    text="Compound Interest:",
    font=("Arial", 11, "bold"),
    bg="#f4f6f9",
    anchor="e",
)
lbl_ci_text.grid(row=6, column=0, sticky="ew", padx=20, pady=8)
lbl_ci_result = tk.Label(
    root, text="$0.00", font=("Arial", 11, "bold"), bg="#f4f6f9", fg="#1565c0"
)
lbl_ci_result.grid(row=6, column=1, sticky="w", padx=20, pady=8)

root.mainloop()