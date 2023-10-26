import random
import os
os.system("clear")
failureDetected = False
ties = 0
wins = 0
losses = 0
userChoiceNum = 0
       
def getmode():
    print("Hello")
    print("Choose a mode")
    print("(1)Normal")
    print("(2)AI Powered (unavaliable)")
    return int(input("Choice: "))

def startGame():
    global failureDetected, wins, losses, ties, userChoiceNum
    computerChoice = random.randint(1,3)
    #1 is rock
    #2 is paper
    #3 is scissors
    #4 is used by user to exit
    print()
    print("-----------------------------------------")
    print()

    userChoice = input("(R)ock, (P)aper, (S)cissors, or E(x)it? ").capitalize()
    
    if userChoice == "R" :
        userChoiceNum = 1

    elif userChoice == "P":
        userChoiceNum = 2

    elif userChoice == "S":
        userChoiceNum = 3
        
    elif userChoice == "X":
        userChoiceNum = 4

    else:
        failureDetected = True
        print("Error")
        startGame()


    if(failureDetected == False):
        if(userChoiceNum == 4):
            gamesPlayed = wins+ties+losses
            if gamesPlayed > 0:
                winRate = wins/gamesPlayed
                print("Exited with "+str(gamesPlayed)+" games played.")
                print("Win rate: "+str(winRate))
                print("Bye!!!")
            else:
                print("Not enough games played for statistics.")
                print("Bye!!!")
        elif(computerChoice == userChoiceNum):
            ties = ties+1
            print("Tie!")
            print("Ties: "+str(ties)+", Wins: "+str(wins)+", Losses: "+str(losses))
            startGame()
        elif(computerChoice == 1 and userChoiceNum == 2):
            wins= wins+1
            print("Paper beats rocks, you win!")
            print("Ties: "+str(ties)+", Wins: "+str(wins)+", Losses: "+str(losses))
            startGame()
        elif(computerChoice == 1 and userChoiceNum == 3):
            losses = losses+1
            print("Rock beats scissors, you lose!")
            print("Ties: "+str(ties)+", Wins: "+str(wins)+", Losses: "+str(losses))
            startGame()
        elif(computerChoice == 2 and userChoiceNum == 1):
            losses= losses + 1
            print("Paper beats rock, you lose!")
            print("Ties: "+str(ties)+", Wins: "+str(wins)+", Losses: "+str(losses))
            startGame()
        elif(computerChoice == 2 and userChoiceNum == 3):
            wins= wins+1
            print("Scissors beats paper, you win!")
            print("Ties: "+str(ties)+", Wins: "+str(wins)+", Losses: "+str(losses))
            startGame()
        elif(computerChoice == 3 and userChoiceNum == 1):
            wins = wins+1
            print("Rock beats scissors, you win!")
            print("Ties: "+str(ties)+", Wins: "+str(wins)+", Losses: "+str(losses))
            startGame()
        elif(computerChoice == 3 and userChoiceNum == 2):
            losses = losses+1
            print("Scissors beats rock, you lose!")
            print("Ties: "+str(ties)+", Wins: "+str(wins)+", Losses: "+str(losses))
            startGame()

        else:
            print("Variable unaccounted for, computer choice: "+str(computerChoice)+", userChoice: "+str(userChoiceNum))
    

choice = getmode()

if choice == 1:
    startGame()
elif choice == 2:
    print("Coming soon!")
else:
    print("Incorrect input.")