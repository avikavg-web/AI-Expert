import tkinter as tk


def check_strength(*args):
    password = entry_password.get()
    length = len(password)

    if length == 0:
        lbl_result.config(text="", fg="black")
    elif length <= 5:
        lbl_result.config(text="Weak", fg="red")
    elif 6 <= length <= 8:
        lbl_result.config(text="Medium", fg="orange")
    elif 9 <= length <= 12:
        lbl_result.config(text="Strong", fg="light green")
    else:
        lbl_result.config(text="Very Strong", fg="dark green")


root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")
root.configure(bg="Blue")

root.columnconfigure(0, weight=1)

lbl_header = tk.Label(root, text="Password Strength Checker", font=("Arial", 16, "bold"), bg="Red", fg="Blue")
lbl_header.pack(pady=30)

lbl_prompt = tk.Label(
    root, text="Enter your password:", font=("Arial", 11), bg="Green")
lbl_prompt.pack(pady=5)

password_var = tk.StringVar()
password_var.trace_add("write", check_strength)

entry_password = tk.Entry(
    root, textvariable=password_var, font=("Arial", 12), show="*", width=25)
entry_password.pack(pady=10)

lbl_status = tk.Label(
    root, text="Password Strength:", font=("Arial", 11), bg="Yellow")
lbl_status.pack(pady=(20, 5))

lbl_result = tk.Label(
    root, text="", font=("Arial", 14, "bold"), bg="Purple", width=15)
lbl_result.pack(pady=5)

root.mainloop()