import random
def diceroll():
    x=random.randint(1,6)
    return x
print("Welcome to the dice simulator :)")
def wanna_roll():
    roll=input("Press y to roll or any key to exit ")
    while(roll.lower()== "y"):
        print("You rolled a ", diceroll())
        wanna_roll()
        break
        
wanna_roll()

