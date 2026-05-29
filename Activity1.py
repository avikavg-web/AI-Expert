#hi
print("Welcome to AI expert!")

name = input()
print(f"Hi, {name}!")

print("How are you doing today? (good/bad) : ")
mood = input()

if mood == "good":
    print("It's good to hear that")
elif mood == "bad":
    print("I am sorry to hear that")
else:
    print("Sometimes it is hard to put feelings into words :)")

print(f"It was nice chatting with you {name}. Goodbye!")