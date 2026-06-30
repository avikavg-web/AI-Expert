import random


def run_chatbot():
    print("Welcome to your Enhanced Chatbot!\n")

    user_name = input("Hello! What is your name? ").strip()
    if not user_name:
        user_name = "Friend"

    print(f"\nNice to meet you, {user_name}!\n")

    while True:
        print("How are you feeling today?")
        print("1. Happy / Great")
        print("2. Sad / Down")
        print("3. Stressed / Busy")
        print("4. Tired / Bored\n")

        mood_choice = (input("Please select a number (1-4) or type your mood: ").strip().lower())

        if mood_choice in ["1", "happy", "great"]:
            print(f"\nThat's good, {user_name}!")
            input("What is one good thing that happened to you today? ")
            print("That sounds nice.\n")

        elif mood_choice in ["2", "sad", "down"]:
            print(f"\nI'm really sorry to hear that, {user_name}.")

        elif mood_choice in ["3", "stressed", "busy"]:
            print("Stress can be overwhelming.")

        elif mood_choice in ["4", "tired", "bored"]:
            print(f"\nLow energy days happen to everyone, {user_name}.")

        else:
            print("I see!")
        play_again = (input("Would you like to talk to the chatbot again? (yes/no): ").strip().lower())
        if play_again not in ["yes", "y"]:
            print("Goodby!")
            break


run_chatbot()