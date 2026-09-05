print("==== LIFE SIMULATOR ====")
print("Welcome to your new life😎. ")
print("Create your character🤓: ")

name = input("What is your name?: ")
age = int(input("How old are you?: "))

print(f"Welcome, {name}! Let's begin your new and exciting life😍.")

# Starting stats
health = 70
happiness = 70
money = 80
iq = 90
social = 50

print("\nYour starting stats: ")
print("Health:", health)
print("Happiness:", happiness)
print("Money:", money)
print("Intelligence:", iq)
print("Social:", social)

bad_actions = ["smoke", "scrolling", "video games", "fever", "drink"]
good_actions = ["study", "exercise", "dance", "work", "walk", "meeting friends"]

# Loop until quit or game over
while True:
    print("\nTell me what you did today (or type 'quit' to stop): ")
    action = input("Enter your action: ").lower()

    if action == "quit":
        print("Game Over! Thanks for playing 🎮")
        break

    if action in good_actions:
        print("That's a really good choice😊")
        health += 2
        happiness += 3
    elif action in bad_actions:
        print("That's not good for you, Ohhh Dear!!😓")
        health -= 2
        happiness -= 2
    else:
        print("I am not sure about that.")

    # Show updated stats
    print("\nUpdated stats: ")
    print("Health:", health)
    print("Happiness:", happiness)

    # Check win/lose conditions (inside the loop!)
    if health <= 0:
        print("Oh no!! Your health points hit zero. You are dead 😔")
        break
    if happiness <= 0:
        print("You lost all your happiness. Game Over 😢")
        break
