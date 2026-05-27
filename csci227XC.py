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


#Python Game Extra Credit Essay
#I decided to make a murder mystery game because I've always been into detective movies and characters like Sherlock Holmes and Knives Out. 
#The idea of narrowing down suspects based on clues seemed like something that would go well with a text-based Python game, and it gave me a 
#good excuse to practice using dictionaries and loops in a way that actually felt useful instead of just doing assignments. I wanted it to feel 
#like you're actually investigating something, not just picking from a menu, even though technically that's what you're doing.
#The main data structure I used was a dictionary that maps each suspect's name to their clue, which made it easy to look up information when the 
#player chooses someone to question. I used a while loop for the core game loop so the player can keep investigating until they're ready to make a 
#guess, and I stored the clues the player has already seen in a list so they can review them before accusing anyone. I also used the random module 
#to randomly assign the guilty suspect each time the game runs, which makes the game replayable since you can't just memorize the answer. Handling 
#user input was important too. I had to normalize capitalizing letters so that typing "alice" or "ALICE" would still match "Alice" in the dictionary, 
#which I did using string slicing and the upper() and lower() functions.
#The trickiest part of the project was honestly just getting the game flow to feel right. My first version was kind of all over the place so I ended 
#up restructuring it so the reveal only happens when the player picks option 3, and then the game ends smoothly after that. I also had a small bug at 
#first where the game would crash if you typed in a name that wasn't in the suspect list during the killer reveal, so I had to add a check for that. 
#Overall, I'm pretty happy with how it turned out, and if I had more time I'd probably add multiple rounds, more suspects, and maybe even a voting 
#system like in the town judge leetcode problem.
