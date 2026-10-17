# SNAKE, WATER, GUN GAME
# We all have played snake, water gun game in our chidhood. If you 
# haven't, google the rules of this game and write a python program 
# capable of playing this game with the user.
'''
1 for snake
-1 for water
0 for gun
'''
import random
computer = random.choice([-1, 0, 1])

# computer = -1
'''
n = int(input("Enter number of rounds you want to play: "))
for i in range(n):
    while True:
        youstr = input("Enter your choice(s,w,g): ")
        if(youstr in ["s", "w", "g"]):
            break
        else:
            print("Invalid input! Please enter again.")
'''
youstr = input("Enter your choice(s,w,g): ")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

you = youDict[youstr]

# by now we have 2 numbers(variables), you and computer
print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")
if(computer == you):
    print("It's a draw")
else:
    if(computer == -1 and you == 1):            # -1-1 = -2
        print("You win!")
    elif(computer == -1 and you == 0):          # -1-0 = -1
        print("You lose!")
    elif(computer == 1 and you == -1):          # 1-(-1) = 2
        print("You lose!")
    elif(computer == 1 and you == 0):           # 1-0 = 1
        print("You win!")
    elif(computer == 0 and you == -1):          # 0-(-1) = 1
        print("You win!")
    elif(computer == 0 and you == 1):           # 0-1 = -1
        print("You lose!")
    else:
        print("Something wrong!")

# also it can be in else part
'''
THE BELOW LOGIC IS WRITTEN ON THE BASIS OF (computer - you)
else:
    if((computer - you) == -1 or (computer - you) == 2):
        print("You lose!")
    else:
        print("You win!")
'''

