import random

def player():
    pinput=int(input("Enter your choice\n1.Rock\n2.Paper\n3.Scissor\nPress 4 To exit the game\n"))
    if(pinput==1):
        return 1
    elif(pinput==2):
        return 2
    elif(pinput==3):
        return 3
    elif(pinput==4):
        return 4
    else:
        return 5
   

def game(player,bot):
    if(player==1 and bot==2):
        print("Bot Won!!")
        return 2
    elif(player==2 and bot==1):
        print("Player Won!!")
        return 1
    elif(player==2 and bot==3):
        print("Bot Won!!")
        return 2
    elif(player==3 and bot==2):
        print("Player Won!!")
        return 1
    elif(player==1 and bot==3):
        print("Player Won!!")
        return 1
    elif(player==3 and bot==1):
        print("Bot Won!!")
        return 2
    else:
        print("The game is draw!!")


playerscore=0
botscore=0
playing=0


while playing==0:
    botinput=random.randint(1,3)

    playerinput=player()

   
    if(playerinput==4):
        print("You quit the game!!")
        print(f"Final Score is\nPlayer={playerscore}\nBot={botscore}")
        break
    elif(playerinput==5):
        print("Invalid choice")
    
    if(playerinput>0 and playerinput<4):
        if(botinput==1):
            print("Bot selected ROCK")
        elif(botinput==2):
            print("Bot selected PAPER")
        elif(botinput==3):
            print("BOT selected SCISSOR")

    if(playerinput>0 and playerinput<4):
        score=game(playerinput,botinput)
    else:
        continue

    if(score==1):
        playerscore+=1
    elif(score==2):
        botscore+=1

    print("The score of Player is:-",playerscore) 
    print("The score of Bot is:-",botscore) 





    
    