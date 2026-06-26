import random
import tkinter as tk


def play(user_choice):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    result_text = f"You chose: {user_choice.capitalize()}\nComputer chose: {computer_choice.capitalize()}\n\n"

    if user_choice == computer_choice:
        result_text += "It's a Tie!"
        color = "orange"
    elif ((user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper")):
        result_text += "You Win!"
        color = "green"
    else:
        result_text += "Computer Wins!"
        color = "red"

    lbl_result.config(text=result_text, fg=color)


root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")
root.configure(bg="white")

lbl_header = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"), bg="white")
lbl_header.pack(pady=20)

btn_frame = tk.Frame(root, bg="white")
btn_frame.pack(pady=20)

btn_rock = tk.Button(btn_frame, text="Rock",font=("Arial", 11), width=10, command=lambda: play("rock"))
btn_rock.grid(row=0, column=0, padx=5)

btn_paper = tk.Button(btn_frame, text="Paper", font=("Arial", 11), width=10, command=lambda: play("paper"))
btn_paper.grid(row=0, column=1, padx=5)

btn_scissors = tk.Button( btn_frame, text="Scissors", font=("Arial", 11), width=10, command=lambda: play("scissors"))
btn_scissors.grid(row=0, column=2, padx=5)

lbl_result = tk.Label(root, text="Click a button to play!", font=("Arial", 12, "bold"), bg="white")
lbl_result.pack(pady=30)

root.mainloop()