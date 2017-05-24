import random
import time
Userdice = random.randint(1, 6)
Compdice = random.randint(1, 6)
winlose = ""
def dice():
        

    if Userdice > Compdice:
            winlose = "win"
    if Userdice == Compdice: 
            winlose = "tie"
    if Compdice > Userdice: 
            winlose = "lose"
    print("The computer got:")
    print(Compdice)
    print("You got:")
    print(Userdice)
    if winlose == "win":
        print("Congratulations! You have won!")
    if winlose == "tie":
        print("Close game, you tied!")
    if winlose == "lose":
        print("Aw, you lost! Try again and maybe you'll win!")
            
while True:
    print("Try again (y/n)")
    replay = input()
    if replay == "y":
        dice()
    else:
        print("Thanks for playing!")
