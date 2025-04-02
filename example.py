print("hello there! I am AI BOT, what's your name? : ")
name = input()
print(f"nice to meet you, {name}.")
print("How are you doing today? (good/bad) : ")
mood = input().lower()
if mood == "good":
    print("That's good!")
elif mood == "bad":
    print("that not nice hope your day get's better")
else:
    print("I know sometimes it is hard to put feelings in words.")
