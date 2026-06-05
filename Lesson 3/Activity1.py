import re, random



destination = {
    "beaches": ["Bali", "Hawaii", "Florida"],
    "mountains": ["Swiss Alps", "Rocky Mountain", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why did the Java developer go camping? To finally catch some bugs in their natural habitat.",
    "I tried to teach a squirrel Python. It ran away halfway through the loops… guess it preferred recursion in the trees."
    "Why do travelers always feel hot? Because of their hotspot!"
]

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    print("TravelBot: Do you prefer beaches, mountains, or cities?")
    preference = input("You: ")
    preference = normalize_input(preference)

    if preference in destination:
        suggestion = random.choice(destination[preference])
        print(f"TravelBot: How abput {suggestion}?")
        print("TravelBot: Do you like it? (yes / no)")
        answer = input("You:").lower()

        if answer == "yes":
            print(f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print("TravelBot: Let's try another.")
            recommend()
        else:
            print("TravelBot: I'll suggest again.")
            recommend()

    else:
        print("TravelBot: Sorry, I don't have that type of destination")

    show_help()

def packing_tips():
    print("TravelBot: Where to?")
    location = normalize_input(input("You:"))
    print("TravelBot: How many days?")
    days = input("You:")

    print(f"TravelBot: Packing tips for {days} days in {location}:")
    print("- Pack versatile clothes")
    print("- Bring chargers/adapters")
    print("- Check the weather forecast")

def tell_joke():
    print(f"TravelBoy: {random.choice(jokes)}")

def show_help():
    print("I can:")
    print("- Suggest travel spots (say 'recommendation')")
    print("- Offer packing tips (say 'packing)")
    print("- Tell a joke (say 'joke')")
    print("Type 'exit' or 'bye' to end. \n")

def chat():
    print("Hello! I'm TravelBot")
    name = input("What is your name?")
    print(f"Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = input(f"{name}:")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print("TravelBot: Safe travels! Goodbye!")
            break
        else:
            print("TravelBot: Could you rephrase?")

if __name__ == "__main__":
    chat()