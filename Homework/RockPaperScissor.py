import random
from colorama import Fore, Style, init

init(autoreset=True)


def get_ai_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(player, ai):
    if player == ai:
        return "tie"

    winning_pairs = { "rock": "scissors", "paper": "rock", "scissors": "paper",}

    if winning_pairs[player] == ai:
        return "player"
    return "ai"


def run_game():
    print(Fore.CYAN + Style.BRIGHT + "Rock Paper Scissors AI initialized.\n")

    player_score = 0
    ai_score = 0

    while True:
        print("Select your move:")
        print("- rock")
        print("- paper")
        print("- scissors")
        print("- Type 'exit' to quit\n")

        player_choice = input("You: ").strip().lower()

        if player_choice in ["exit", "quit", "q"]:
            print(Fore.CYAN + f"\nGame terminated.")
            print(f"Final Score - You: {player_score} | AI: {ai_score}\n")
            break

        if player_choice not in ["rock", "paper", "scissors"]:
            print(Fore.WHITE + "Invalid choice. Try again.\n")
            continue

        ai_choice = get_ai_choice()
        print(Fore.BLUE + f"AI chose: {ai_choice}")

        result = determine_winner(player_choice, ai_choice)

        if result == "tie":
            print(Fore.YELLOW + "Result: Tie.\n")
        elif result == "player":
            player_score += 1
            print(Fore.GREEN + "Result: You win this round.\n")
        else:
            ai_score += 1
            print(Fore.RED + "Result: AI wins this round.\n")

        print(f"Current Score - You: {player_score} | AI: {ai_score}")


if __name__ == "__main__":
    run_game()