#Dragon Game in Python
import random

#intro to game
print(
    "Hello I am Computo, and welcome to Brents fabulous, wonderful, amazing Dragon Game!!"
)
print("")
#asking user if ready
userEntry = input("Ready to begin? (yes or no) ").lower()
print("")

#running game if user is ready
while userEntry == ("yes"):
    print(
        "You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight."
    )
    
    #generating a random number
    randomNumber = random.randint(1,2)
    print("")
    print(randomNumber)
    print("")
   
    #checking if users number is valid
    while userEntry != "1" and userEntry != "2":
        userEntry = input("Which cave will you enter? 1 or 2? ")
    print("")
    print("You approach the cave...")
    print("")
    print("It is dark and spooky...")
    print("")
    
    #checking users number entry to print ending
    if int(userEntry) == randomNumber:
        print(
            "A large dragon jumps out in front of you! He opens his jaws and... Gives you a treasure"
        )
    else:
        print(
            "A large dragon jumps out in front of you! He opens his jaws and... Gobbles you down in one bite!"
        )
    print("")
    print("")

    #asking user if they wanna play again
    userEntry = input("Would you like to play again? (yes or no) ")
    print("")

#thanking user for playing
if userEntry == "no":
    print("Thank you for playing.")
