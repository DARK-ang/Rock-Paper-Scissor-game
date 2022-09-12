            #***********first project*****************#
import random           #importing the random module
print("WELCOME TO ROCK PAPER SCISSOR GAME....!!")   #welcome statement

while True: #while loop with true condition which is used to execute all actions
    player=input("Enter Your Choice To Play The Game:")     #input choice
    possible = ["rock","paper","scissor"] #possibilities are stored in a separate list
    score=0
    defeats=0
    #bot choice
    bot = random.choice(possible)
    if player==bot: #this condition is for tie statement
        print("BOTH ARE SAME SO LET'S HAVE TIE")
    elif player=="rock": #this block executes when input is rock
        if bot=="scissor":
            print("ROCK BREAKS SCISSOR..YOU HAD WON")
            score=random.randint(1,10)
            print("you have scored:",score)
        else:
            print("PAPER CATCHES.. ROCK ,SORRY YOU LOSE")
            defeats+=1
            print("LOSES:",defeats)
            
    elif player=="paper":   #this block executes when input is paper
        if bot=="rock":
            print("PAPER CATCHES ROCK.. YOU HAD WIN")
            score=random.randint(1,50)
            print("you have scored:",score)
        else:
            print("SCISSOR CUTS THE PAPER...YOU LOSE")
            defeats+=1
            print("LOSES:",defeats)
                        
    elif player=="scissor":  #this block executes when input is scissor
        if bot=="paper":
            print("SCISSOR CUTS THE PAPER...YOU HAD WON")
            score=random.randint(1,50)
            print("you have scored:",score)
        else:
            print("ROCK BREAKS THE SCISSOR..YOU LOSE")
            defeats+=1
            print("LOSES:",defeats)
            
    else:   #this executes when the input is apart from rock paper and scissor
        print("INVALID INPUT FOR THE GAME")
    continue_game=input("DO YOU WANNA CONTINUE(y/n):") #this is to know whether the player wants to continue the game or not
    if continue_game.lower()!="y": #the loop breaks when it is not equal to "y"
        break

                        #****************END OF THE GAME******************#