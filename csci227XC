"""
Name: Desiree F Honore
Date: May 19, 2026
Extra Credit Project
"""

import random

# suspects and their clues
suspects = {
    "Alice": "Was seen near the mayor's office late at night.",
    "Bob": "Has been caught stealing small items before.",
    "Carol": "Was heard arguing with the mayor yesterday.",
    "Dave": "Owns a bag that matches one found at the scene.",
    "Eve": "Has no alibi for the time of the crime."
}

# pick who did it
names = list(suspects.keys())
guilty = random.choice(names)

clues_found = []

# intro
print("MURDER MYSTERY: WHO DID IT?")
print("A terrible crime has happened in town!")
print("Someone stole the mayor's golden trophy.")
print("You are the town detective. Find the thief!")

playing = True
while playing:
    print("\nWhat would you like to do?")
    print("1 - Question a suspect")
    print("2 - Review your clues")
    print("3 - Make your accusation")

    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        print("\nSuspects:", ", ".join(names))
        name = input("Who do you want to question? ").strip()
        # fix capitalization so it matches the dictionary
        name = name[0].upper() + name[1:].lower()

        if name in suspects:
            print("Clue: " + suspects[name])
            if name not in clues_found:
                clues_found.append(name)
        else:
            print("That person is not a suspect!")

    elif choice == "2":
        if len(clues_found) == 0:
            print("You haven't found any clues yet!")
        else:
            print("Clues so far:")
            for person in clues_found:
                print("  " + person + ": " + suspects[person])

    elif choice == "3":
        print("\nTime to make your accusation!")
        print("Suspects:", ", ".join(names))
        guess = input("Who do you think is the thief? ").strip()
        guess = guess[0].upper() + guess[1:].lower()

        if guess not in suspects:
            print(guess + " is not a suspect!")
        elif guess == guilty:
            print("You got it! " + guilty + " is the thief!")
            print("Great detective work!")
        else:
            print("Wrong! It was actually " + guilty + "!")
            print("Better luck next time.")

        playing = False

    else:
        print("Please enter 1, 2, or 3.")

print("Thanks for playing!")
