import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
# print("s :Snake   w  : Water   g  : Gun ")
youstr = input("Enter your choice (s/w/g): ").lower()  # Convert input to lowercase
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

if youstr not in youDict:
    print("Invalid input. Please enter 's', 'w', or 'g'.")
    exit() #Exit the program if input is invalid
    
you = youDict[youstr]

print(f"Your choice: {reverseDict[you]}\nComputer choice: {reverseDict[computer]}")
if computer == you:
    print("It's a draw")

else:
    if (computer == -1 and you == 1) or \
            (computer == 1 and you == 0) or \
            (computer == 0 and you == -1):
        print("You win")

    else:
        print("You lose")