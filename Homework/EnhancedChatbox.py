import random


def run_chatbot():
    print("Welcome to your Enhanced Chatbot!")

    user_name = input("Hello! What is your name? ").strip()
    if not user_name:
        user_name = "Friend"

    print(f"\nNice to meet you, {user_name}!")

    while True:
        print("\nHow are you feeling today?")
        print("1. Happy / Great")
        print("2. Sad / Down")
        print("3. Stressed / Busy")
        print("4. Tired / Bored")

        mood_choice = (
            input("Please select a number (1-4) or type your mood: ")
            .strip()
            .lower()
        )

        if mood_choice in ["1", "happy", "great"]:
            print(
                f"\nThat's fantastic to hear, {user_name}! Happiness is contagious."
            )
            follow_up = input(
                "What is one good thing that happened to you today? "
            )
            print("That sounds wonderful! I hope your day keeps getting better.")

        elif mood_choice in ["2", "sad", "down"]:
            print(f"\nI'm really sorry to hear that you're feeling down, {user_name}.")
            follow_up = input(
                "Would you like to talk about it? Or do you prefer a distraction? (talk/distraction): "
            ).lower()
            if "talk" in follow_up:
                input("Go ahead, I'm listening: ")
                print(
                    "Thank you for sharing that with me. Remember to take things one step at a time."
                )
            else:
                jokes = [
                    "Why don't scientists trust atoms? Because they make up everything!",
                    "What do you call a fake noodle? An impasta!",
                    "Why did the scarecrow win an award? Because he was outstanding in his field!",
                ]
                print(f"Here is a quick joke for you: {random.choice(jokes)}")

        elif mood_choice in ["3", "stressed", "busy"]:
            print(
                f"\nTake a deep breath, {user_name}. Stress can be overwhelming."
            )
            follow_up = input(
                "Can you take a 5-minute break right now to stretch or drink water? (yes/no): "
            ).lower()
            if "y" in follow_up:
                print("Excellent choice. Go do that now! Your work can wait.")
            else:
                print(
                    "I understand. Just remember to be kind to yourself today."
                )

        elif mood_choice in ["4", "tired", "bored"]:
            print(f"\nLow energy days happen to everyone, {user_name}.")
            follow_up = input(
                "Would you rather listen to some music or get up and walk around? (music/walk): "
            ).lower()
            if "music" in follow_up:
                print("Put on your favorite track! Music is great for the soul.")
            else:
                print(
                    "A quick walk or change of scenery is perfect for resetting your focus."
                )

        else:
            print(
                f"\nI see! Emotions are complex, and it's perfectly fine to feel that way."
            )
            input("What has been occupying your mind the most today? ")
            print("Interesting. Thanks for sharing that perspective with me.")

        print("\n------------------------------------")
        play_again = (
            input("Would you like to talk to the chatbot again? (yes/no): ")
            .strip()
            .lower()
        )
        if play_again not in ["yes", "y"]:
            print(f"\nGoodbye, {user_name}! Have a wonderful rest of your day.")
            break


run_chatbot()