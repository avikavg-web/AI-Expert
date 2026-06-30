import random



MOVIES = [
    {
        "title": "Inception",
        "genre": "sci-fi",
        "mood": "thoughtful",
        "rating": 8.8,
        "overview": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
        "sentiment": "Positive / Intricate",
    },
    {
        "title": "The Hangover",
        "genre": "comedy",
        "mood": "happy",
        "rating": 7.7,
        "overview": "Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing.",
        "sentiment": "Neutral / Energetic",
    },
    {
        "title": "The Conjuring",
        "genre": "horror",
        "mood": "scared",
        "rating": 7.5,
        "overview": "Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse.",
        "sentiment": "Negative / Ominous",
    },
    {
        "title": "Interstellar",
        "genre": "sci-fi",
        "mood": "thoughtful",
        "rating": 8.7,
        "overview": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        "sentiment": "Positive / Inspiring",
    },
    {
        "title": "Superbad",
        "genre": "comedy",
        "mood": "happy",
        "rating": 7.6,
        "overview": "Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-fueled party goes awry.",
        "sentiment": "Positive / Humorous",
    },
]


def display_movie(movie):
    print(f"\nTitle: {movie['title']}")
    print(f"Genre: {movie['genre'].capitalize()}")
    print(f"Mood Profile: {movie['mood'].capitalize()}")
    print(f"IMDb Rating: {movie['rating']}/10")
    print(f"Overview: {movie['overview']}")
    print( f"Sentiment Analysis: {movie['sentiment']}\n")


def get_random_movie():
    return random.choice(MOVIES)


def filter_movies(criterion, value):
    filtered = []
    for movie in MOVIES:
        if criterion == "rating" and movie["rating"] >= float(value):
            filtered.append(movie)
        elif criterion != "rating" and movie[criterion] == str(value).lower():
            filtered.append(movie)
    return filtered


def run_recommendation_system():
    print( "AI Movie Recommendation System Online.\n")

    while True:
        print("Select recommendation type:")
        print("1. Random suggestion")
        print("2. Filter by Genre")
        print("3. Filter by Mood")
        print("4. Filter by Minimum IMDb Rating")
        print("5. Exit\n")

        choice = input("Selection: ").strip()

        if choice in ["5", "exit", "quit", "q"]:
            print("\nSystem shut down.")
            break

        if choice == "1":
            movie = get_random_movie()
            display_movie(movie)

        elif choice == "2":
            genre_input = (input("Enter genre (Sci-Fi, Comedy, Horror): ").strip().lower())
            results = filter_movies("genre", genre_input)
            if results:
                display_movie(random.choice(results))
            else:
                print("No matching genres found.\n")

        elif choice == "3":
            mood_input = ( input("Enter mood (Thoughtful, Happy, Scared): ").strip().lower())
            results = filter_movies("mood", mood_input)
            if list(results):
                display_movie(random.choice(results))
            else:
                print("No matching moods found.\n")

        elif choice == "4":
            rating_input = input("Enter minimum IMDb score (e.g. 7.5): ").strip()
            try:
                results = filter_movies("rating", rating_input)
                if results:
                    display_movie(random.choice(results))
                else:
                    print("No movies found matching or exceeding that rating.\n")
            except ValueError:
                print("Invalid numeric threshold.\n")

        else:
            print("Invalid selection choice.\n")

if __name__ == "__main__":
    run_recommendation_system()