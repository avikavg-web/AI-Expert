import datetime
import random
from colorama import Fore, Style, init

init(autoreset=True)


def get_weather():
    weathers = [ "It is 22°C and sunny.","It is currently raining.","It is overcast and cold.",]
    return random.choice(weathers)


def get_news():
    headlines = ["Scientists discovered a new species of deep-sea jellyfish.", "The city park's new botanical garden is now open.", "A new open-source programming language was released today.",]
    return random.choice(headlines)


def get_local_time(city):
    city = city.lower()
    now = datetime.datetime.now()

    if "london" in city:
        london_time = now + datetime.timedelta(hours=8)
        return f"London time is approximately {london_time.strftime('%I:%M %p')}."
    elif "tokyo" in city:
        tokyo_time = now + datetime.timedelta(hours=16)
        return f"Tokyo time is approximately {tokyo_time.strftime('%I:%M %p')}."
    elif "new york" in city or "ny" in city:
        ny_time = now + datetime.timedelta(hours=3)
        return (f"New York time is approximately {ny_time.strftime('%I:%M %p')}.")
    else:
        return f"Local system time is {now.strftime('%I:%M %p')}. Specify London, Tokyo, or New York if needed."


def run_chatbot():
    print(Fore.CYAN + Style.BRIGHT + "Chatbot initialized.\n")

    user_name = input("Enter your name: ").strip()
    if not user_name:
        user_name = "User"

    print(Fore.GREEN + f"\nHello, {user_name}.\n")

    while True:
        print("Select an option:")
        print("- State a mood (Happy, Sad, Stressed, Tired)")
        print("- Ask for 'weather'")
        print("- Ask for 'news'")
        print("- Ask for 'time'")
        print("- Type 'exit' to log out\n")

        user_input = input("You: ").strip().lower()

        if user_input in ["exit", "quit", "q"]:
            print(Fore.CYAN + f"\nProgram terminated. Goodbye, {user_name}.")
            break

        if "weather" in user_input or "rain" in user_input or "sun" in user_input:
            print(Fore.YELLOW + f"Chatbot: {get_weather()}\n")

        elif "news" in user_input or "headline" in user_input:
            print(Fore.MAGENTA + f"Chatbot: Current headline: {get_news()}\n")

        elif "time" in user_input or "clock" in user_input:
            print(Fore.BLUE + f"Chatbot: {get_local_time(user_input)}\n")

        elif any(word in user_input for word in ["1", "happy", "great", "good"]):
            print(Fore.GREEN + f"\nChatbot: Noted.")
            input("What happened? ")
            print("Chatbot: Okay.\n")

        elif any(word in user_input for word in ["2", "sad", "down", "unhappy"]):
            print(Fore.RED + f"\nChatbot: Acknowledged.")
            follow_up = input( "Do you want to explain, or do you want a joke? (explain/joke): ").lower()

            if "explain" in follow_up or "talk" in follow_up:
                input("Go ahead: ")
                print(Fore.RED + "Chatbot: Thanks for the context. Take it standard.\n")
            else:
                jokes = [ "Why don't scientists trust atoms? Because they make up everything.","What do you call a fake noodle? An impasta."]
                print(Fore.YELLOW + f"Chatbot: {random.choice(jokes)}\n")

        elif any(word in user_input for word in ["3", "stressed", "busy"]):
            print(Fore.RED + f"\nChatbot: Understood. Stress levels are high.")
            follow_up = input("Can you take a 5-minute break? (yes/no): ").lower()
            if "y" in follow_up:
                print( Fore.GREEN + "Chatbot: Go do that. The work will still be here.\n" )
            else:
                print(Fore.RED + "Chatbot: Understood. Carry on.\n")

        elif any(word in user_input for word in ["4", "tired", "bored"]):
            print(Fore.BLUE + f"\nChatbot: Fatigue is common.")
            follow_up = input(
                "Would you prefer music or a walk? (music/walk): " ).lower()
            if "music" in follow_up:
                print(Fore.GREEN + "Chatbot: Play a track.\n")
            else:
                print(Fore.BLUE + "Chatbot: A walk might reset focus.\n")

        else:
            print(Fore.WHITE + f"\nChatbot: Input unclear.")
            input("What is on your mind? ")
            print("Chatbot: Understood.\n")


run_chatbot()