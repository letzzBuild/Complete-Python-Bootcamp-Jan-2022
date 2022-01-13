#psedu code 
# step 1 : print on the screen fire is in front of you. 
# Do you want to move ahead or get a fire extinguisher ?
# step 2 : take input from user and check what input he has given
# step 3 : based on what input user has given we should next should be printed on the screen.
     # if ans == "moveahed"
        #print on the screen you are burnt . Game Over.
     #else if ans == "fire extinguisher"
     #   print on the screen you are safe and you have come in front of a road which has 2 sides.
        #   Do you want to go left or right ?
        #  take input and check if he wants to go left or right
        #  and soo on it continues.

print("Welcome to Treasure Game !!")
print("you are in front of a Fire.")
ans1 = input("Do you want to move ahead or get a fire extinguisher ?")          
if ans1 == "move ahead":
    print("game Over ! you are burnt")
elif ans1 == "fire extinguisher":
    print("you are safe and you have come in front of a road which has 2 sides.")    
    ans2 = input("Do you want go left or right ?")
    if ans2 == "right":
        print("You are in front of a tiger and Tiger ate you . Game Overs")
    elif ans2=="left":
        print("You have got a partner to help you in finding treasure.")
        ans3 = input("Do you want to take your partner or no ?")
        if ans3 == "yes":
            print("You won!!")
        else:
            print("Game Over")       
else:
    print("Invalid input. Game Over")
