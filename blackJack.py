from random import choice
from random import choices
from replit import clear
def dealCard(a):
    return choice(a)

def calculateScore(cards):
    if(sum(cards)==21 and len(cards)==2):
        return 0
    
    if(11 in cards and sum(cards)>21):
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def dealCard(cards):
    return choice(cards)

def compare(a,b):
    if userScore==compScore:
        return "Draw"
    elif compScore ==0:
        return "You lose"
    elif userScore==0:
        return("You win with a blackjack")
    elif userScore>21:
        return("You went over!")
    elif compScore>21:
        return("Opponent went over!")
    elif userScore > compScore:
        return "You win"
    else:
        return "You lose!"
    
affirmative=["y","yes"]
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def playGame():
    userCards=choices(cards,k=2)
    compCards=choices(cards,k=2)
    gameOver=False

    while not gameOver:
        userScore=calculateScore(userCards)
        compScore=calculateScore(compCards)

        print(f"Your cards: {userCards}, current score: {userScore}")
        print(f"Computer's first card: {compCards[0]}")

        if userScore==0 or compScore==0 or userScore>21:
            gameOver=True
        else:
            userDeal=input("Do you want to draw another card? ")
            if(userDeal in affirmative):
                userCards.append(dealCard(cards))
            else:
                gameOver=True

    while compScore != 0 and compScore<17:
        compCards.append(dealCard(cards))
        compScore=calculateScore(compCards)

    print(f"Your final hand:{userCards}, final score:{userScore}")
    print(f"Computer's final hand:{compCards}, final score:{compScore}")
    print(compare(userCards,compCards))

while input("Do you want to play a game of blackjack? Type 'y' or 'n' ")=="y":
    clear()
    playGame()
    