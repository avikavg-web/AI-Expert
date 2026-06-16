import time, pandas as pd
from textblob import TextBlob

# Init colors


# Load CSV (same error output)
try: df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print( "Error: The file 'imdb_top_1000.csv' was not found."); raise SystemExit

# Unique genres
genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})

def dots():
    """Prints ... with delay (AI thinking effect)."""
    for _ in range(3): print(".", end="", flush=True); time.sleep(0.5)

def senti(p):
    """Polarity -> label."""
    return "Positive 😊" if p > 0 else "Negative 😞" if p < 0 else "Neutral 😐"

def recommend(genre=None, mood=None, rating=None, n=5):
    """Filter by genre/rating, shuffle, analyze Overview polarity, return n (title, polarity) or message."""
    d = df
    if genre:
        d = d[d["Genre"].str.contains(genre, case = False, na = False)]
    # 3) If rating not None: filter IMDB_Rating >= rating
    if rating:
        d = d[d["IMDB_Rating"] >= rating]
    # 4) If empty: return "No suitable movie recommendations found."
    d = d.sample(frac = 1).reset_index(drop = True)

    recommendations = []
    for idx, row in d.iterrows():
        overview = row["Overview"]
        if pd.isna(overview):
            continue
        polarity = TextBlob(overview).sentiment.polarity
        if mood and ((TextBlob(mood).sentiment.polarity < 0 and polarity > 0) or polarity >= 0):
            recommendations.append((row["Series_Title"], polarity))
        elif not mood:
            recommendations.append((row["Series_Title"], polarity))
        if len(recommendations) == n:
            break
    return recommendations if recommendations else "No suitable movie recommendations found"
    # 5) Shuffle: sample(frac=1).reset_index(drop=True)
    # 6) need_nonneg = bool(mood)
    # 7) Loop rows:
    #    - skip missing Overview
    #    - pol = TextBlob(overview).sentiment.polarity
    #    - if not need_nonneg or pol >= 0: append (Series_Title, pol)
    #    - stop at n
    # 8) Return list else same message
    

def show(recs, name):
    """Print in same format: header + numbered 🎥 lines with polarity + senti()."""
    print(f"\nAI-Analyzed Movie Recommendations for {name}:")
    for idx, (title, polarity) in enumerate(recs, 1):
        sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
        print(f"{idx}. {title} (Polarity: {polarity:.2f}, {sentiment})")
    # Print: "\n🍿 AI-Analyzed Movie Recommendations for {name}:"
    # Loop enumerate(recs, 1) and print:
    # "{i}. 🎥 {title} (Polarity: {p:.2f}, {senti(p)})"

def processing_animation():
    for _ in range (3):
        print(".", end = "", flush = True)
        time.sleep(0.5)
    print()

def get_genre(name):
    """Print genres, then ask: Enter genre number or name: (repeat until valid)."""
    print(f"\nLet's find the perfect movie for you, {name}!\n")

    print("Available genres:")
    for idx, genre in enumerate(genres, 1):
        print(f"{idx}. {genre}")
    print()

    while True:
        genre_input = input("Enter genre number or name: ").strip()
        if genre_input.isdigit() and 1 <= int(genre_input) <= len(genres):
            genre = genres[int(genre_input) - 1]
            break
        elif genre_input.title() in genres:
            genre = genre_input.title()
            break
        print("\nInvalid input. Try again. \n")

    mood = input("How do you feel today (Descirbe your mood): ").strip()
    print("\nAnalyzing your mood and finding movies . . . ")
    processing_animation()

    recs = recommend( genre = genre, mood = mood)
    if isinstance(recs, str):
        print(recs)
    else:
        show(recs, name)
                                               
                                               
    # Print "Available Genres: " then each: "{i}. {genre}"
    # Input prompt must match exactly
    # Accept valid number OR exact title-cased genre name
    # On invalid: print "Invalid input. Try again.\n"
if __name__ == "__main__":
    print("Welcome to Movie AI recommender")
    user_name = input("Enter your name: ").strip()
    get_genre(user_name)




    

# MAIN (students write)
# 1) Print welcome + ask name + greet
# 2) Print 🔍 line
# 3) genre = get_genre(); mood input
# 4) Print "Analyzing mood" + dots(); compute mood polarity + print mood line
# 5) rating = get_rating()
# 6) Print "Finding movies for {name}" + dots()
# 7) recs = recommend(...); if str print red else show()
# 8) Loop ask "Would you like more recommendations? (yes/no):"
#    - no -> print enjoy line + break
#    - yes -> recommend again + show
#    - else -> invalid choice line
