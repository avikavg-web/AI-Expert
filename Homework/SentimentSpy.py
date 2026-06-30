import random
from textblob import TextBlob


def run_chatbot():
    print("Welcome to your Enhanced Chatbot: Sentiment Spy Edition!\n")

    user_name = input("Hello! What is your name? ").strip()
    if not user_name:
        user_name = "Agent"

    print(f"\nWelcome to the mission, {user_name}!\n")

    conversation_history = []
    sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}

    while True:
        print("--- Main Menu ---")
        print("Type a message to analyze its sentiment, or use a command:")
        print("'history' - View conversation logs")
        print("'stats'   - View real-time sentiment stats")
        print("'exit'    - Close chatbot and print Mission Report\n")

        user_input = input("You: ").strip()

        if user_input.lower() == "!exit":
            break

        elif user_input.lower() == "!history":
            print("\n--- Conversation History ---")
            if not conversation_history:
                print("No history recorded yet.\n")
            else:
                for idx, log in enumerate(conversation_history, 1):
                    print(f"{idx}. {log['user']}: \"{log['text']}\" | Sentiment: {log['sentiment'].upper()}")
                print()  
            continue

        elif user_input.lower() == "!stats":
            print("\n--- Sentiment Statistics ---")
            print(f"Positive Statements: {sentiment_counts['positive']}")
            print(f"Negative Statements: {sentiment_counts['negative']}")
            print(f"Neutral Statements:  {sentiment_counts['neutral']}\n")
            continue

        elif not user_input:
            print("Please type something so I can analyze it!\n")
            continue

        analysis = TextBlob(user_input)
        polarity = analysis.sentiment.polarity
        if polarity > 0.1:
            sentiment = "positive"
            reply = random.choice(["That sounds incredibly positive! Keep that vibe alive.","Excellent energy! Thanks for sharing a bright perspective.",])
        elif polarity < -0.1:
            sentiment = "negative"
            reply = random.choice(["I detect some down files there. Remember to take things step-by-step.","Sounds heavy. Don't be too hard on yourself today.",])
        else:
            sentiment = "neutral"
            reply = random.choice(
                ["Got it. Fascinating perspective.","A balanced and clear observation.",])

        sentiment_counts[sentiment] += 1
        conversation_history.append({"user": user_name, "text": user_input, "sentiment": sentiment})

        print(f"Chatbot: {reply}\n")


    print(f"Name: {user_name}")
    print(f"Total Lines Analyzed: {len(conversation_history)}")
    print("\n[Sentiment Breakdowns]")
    print(f"🟢 Positive Vibes: {sentiment_counts['positive']}")
    print(f"🔴 Negative Vibes: {sentiment_counts['negative']}")
    print(f"🟡 Neutral Observations: {sentiment_counts['neutral']}")
    print(f"\nGoodbye, {user_name}! Mission accomplished.")


if __name__ == "__main__":
    run_chatbot()