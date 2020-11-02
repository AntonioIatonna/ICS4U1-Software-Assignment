import pygame
import time
import random

# Create card images
ASpades = pygame.image.load('Final Project/assets/cards/as.png')
AClubs = pygame.image.load('Final Project/assets/cards/ac.png')
AHearts = pygame.image.load('Final Project/assets/cards/ah.png')
ADiamonds = pygame.image.load('Final Project/assets/cards/ad.png')
Spades2 = pygame.image.load('Final Project/assets/cards/2s.png')
Clubs2 = pygame.image.load('Final Project/assets/cards/2c.png')
Hearts2 = pygame.image.load('Final Project/assets/cards/2h.png')
Diamonds2 = pygame.image.load('Final Project/assets/cards/2d.png')
Spades3 = pygame.image.load('Final Project/assets/cards/3s.png')
Clubs3 = pygame.image.load('Final Project/assets/cards/3c.png')
Hearts3 = pygame.image.load('Final Project/assets/cards/3h.png')
Diamonds3 = pygame.image.load('Final Project/assets/cards/3d.png')
Spades4 = pygame.image.load('Final Project/assets/cards/4s.png')
Clubs4 = pygame.image.load('Final Project/assets/cards/4c.png')
Hearts4 = pygame.image.load('Final Project/assets/cards/4h.png')
Diamonds4 = pygame.image.load('Final Project/assets/cards/4d.png')
Spades5 = pygame.image.load('Final Project/assets/cards/5s.png')
Clubs5 = pygame.image.load('Final Project/assets/cards/5c.png')
Hearts5 = pygame.image.load('Final Project/assets/cards/5h.png')
Diamonds5 = pygame.image.load('Final Project/assets/cards/5d.png')
Spades6 = pygame.image.load('Final Project/assets/cards/6s.png')
Clubs6 = pygame.image.load('Final Project/assets/cards/6c.png')
Hearts6 = pygame.image.load('Final Project/assets/cards/6h.png')
Diamonds6 = pygame.image.load('Final Project/assets/cards/6d.png')
Spades7 = pygame.image.load('Final Project/assets/cards/7s.png')
Clubs7 = pygame.image.load('Final Project/assets/cards/7c.png')
Hearts7 = pygame.image.load('Final Project/assets/cards/7h.png')
Diamonds7 = pygame.image.load('Final Project/assets/cards/7d.png')
Spades8 = pygame.image.load('Final Project/assets/cards/8s.png')
Clubs8 = pygame.image.load('Final Project/assets/cards/8c.png')
Hearts8 = pygame.image.load('Final Project/assets/cards/8h.png')
Diamonds8 = pygame.image.load('Final Project/assets/cards/8d.png')
Spades9 = pygame.image.load('Final Project/assets/cards/9s.png')
Clubs9 = pygame.image.load('Final Project/assets/cards/9c.png')
Hearts9 = pygame.image.load('Final Project/assets/cards/9h.png')
Diamonds9 = pygame.image.load('Final Project/assets/cards/9d.png')
Spades10 = pygame.image.load('Final Project/assets/cards/10s.png')
Clubs10 = pygame.image.load('Final Project/assets/cards/10c.png')
Hearts10 = pygame.image.load('Final Project/assets/cards/10h.png')
Diamonds10 = pygame.image.load('Final Project/assets/cards/10d.png')
JSpades = pygame.image.load('Final Project/assets/cards/js.png')
JClubs = pygame.image.load('Final Project/assets/cards/jc.png')
JHearts = pygame.image.load('Final Project/assets/cards/jh.png')
JDiamonds = pygame.image.load('Final Project/assets/cards/jd.png')
QSpades = pygame.image.load('Final Project/assets/cards/qs.png')
QClubs = pygame.image.load('Final Project/assets/cards/qc.png')
QHearts = pygame.image.load('Final Project/assets/cards/qh.png')
QDiamonds = pygame.image.load('Final Project/assets/cards/qd.png')
KSpades = pygame.image.load('Final Project/assets/cards/ks.png')
KClubs = pygame.image.load('Final Project/assets/cards/kc.png')
KHearts = pygame.image.load('Final Project/assets/cards/kh.png')
KDiamonds = pygame.image.load('Final Project/assets/cards/kd.png')

# Creating card arrays
cards = [ASpades, AClubs, AHearts, ADiamonds, Spades2, Clubs2, Hearts2, Diamonds2, Spades3, Clubs3, Diamonds3, Spades4, Clubs4, Hearts4, Diamonds4, Spades5, Clubs5, Hearts5, Diamonds5, Spades6, Clubs6, Hearts6, Diamonds6, Spades7, Clubs7, Hearts7, Diamonds7, Spades8, Clubs8, Hearts8, Diamonds8, Spades9, Clubs9, Hearts9, Diamonds9, Spades10, Clubs10, Hearts10, Diamonds10, JSpades, JClubs, JHearts, JDiamonds, QSpades, QClubs, QHearts, QDiamonds, KSpades, KClubs, KHearts, KDiamonds]
card2 = [Spades2, Clubs2, Hearts2, Diamonds2]
card3 = [Spades3, Clubs3, Hearts3, Diamonds3]
card4 = [Spades4, Clubs4, Hearts4, Diamonds4]
card5 = [Spades5, Clubs5, Hearts5, Diamonds5]
card6 = [Spades6, Clubs6, Hearts6, Diamonds6]
card7 = [Spades7, Clubs7, Hearts7, Diamonds7]
card8 = [Spades8, Clubs8, Hearts8, Diamonds8]
card9 = [Spades9, Clubs9, Hearts9, Diamonds9]
card10 = [Spades10, Clubs10, Hearts10, Diamonds10, JSpades, JClubs, JHearts, JDiamonds, QSpades, QClubs, QHearts, QDiamonds, KSpades, KClubs, KHearts, KDiamonds]
cardA = [ASpades, AClubs, AHearts, ADiamonds]

# Colours
grey = (192, 192, 192)
black = (0, 0, 0)
white = (255, 255, 255)
greenTable = (80, 150, 15)
redTable = (128, 10, 10)
blueTable = (54, 95, 156)
goldTable = (184, 132, 48)

def getCard(activeList):
    card = random.choice(cards)
    cards.remove(card)
    activeList.append(card)
    return card

def getValue(card):
    if(card in card2):
        return 2
    elif(card in card3):
        return 3
    elif(card in card4):
        return 4
    elif(card in card5):
        return 5
    elif(card in card6):
        return 6
    elif(card in card7):
        return 7
    elif(card in card8):
        return 8
    elif(card in card9):
        return 9
    elif(card in card10):
        return 10
    elif(card in cardA):
        return 11
    else:
        print("Error")

def updateScore(score):
    screen.fill(greenTable, (0, 0, 125, 100))
    userScore = font.render("Player: " + str(userTotal), True, white)
    dealerScore = font.render("Dealer: " + str(dealerTotal), True, white)
    screen.blit(dealerScore, (10, 25))
    screen.blit(userScore, (10, 50))

# Begin main code
# Init game
pygame.init()
screen = pygame.display.set_mode((650, 500))
pygame.display.set_caption("Blackjack")
font = pygame.font.SysFont('eras bold itc', 30)
running = True
stand = False
gameover = False
gameResult = ""
userCards = []
userTotal = 0
dealerCards = []
dealerTotal = 0

# Create background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(greenTable)
hitButton = pygame.draw.rect(background, grey, (10, 445, 90, 40))
standButton = pygame.draw.rect(background, grey, (10, 390, 90, 40))
hitText = font.render("Hit", True, black)
standText = font.render("Stand", True, black)

# Show objects on screen
screen.blit(background, (0, 0))
screen.blit(hitText, (40, 458))
screen.blit(standText, (25, 402))
updateScore(userTotal)
updateScore(dealerTotal)

while(running):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT): # if user closes window end all operations
            running = False
        elif(event.type == pygame.MOUSEBUTTONDOWN and hitButton.collidepoint(event.pos) and not (gameover or stand)): # if user hits
            card = getCard(userCards)
            userTotal += getValue(card)
            for i in range(len(userCards)): # displays user cards on screen
                x = 125 + i * 50
                screen.blit(userCards[i], (x, 350))
            updateScore(userTotal)
        elif(event.type == pygame.MOUSEBUTTONDOWN and standButton.collidepoint(event.pos) and not (gameover or stand)): # if user stands
            stand = True
            while(dealerTotal < 17 and dealerTotal <= userTotal and userTotal != dealerTotal):
                card = getCard(dealerCards)
                dealerTotal += getValue(card)
                for j in range(len(dealerCards)): # displays dealer cards on screen
                    x = 125 + j * 50
                    screen.blit(dealerCards[j], (x, 10))
                updateScore(dealerTotal)
                pygame.display.flip() # re-init display to prevent getting stuck in loop
                time.sleep(1.5)
        elif(dealerTotal == 21 or userTotal > 21 or dealerTotal >= 17 or dealerTotal > userTotal or (userTotal == dealerTotal and userTotal > 0)): # if win conditions are met
            gameover = True
            if(userTotal == dealerTotal):
                gameResult = "Tie"
                pos = 305
            elif(userTotal == 21 or dealerTotal > 21 or (userTotal > dealerTotal and userTotal <= 21)):
                gameResult = "User Wins"
                pos = 275
            elif(dealerTotal == 21 or userTotal > 21 or (dealerTotal > userTotal and dealerTotal <= 21)):
                gameResult = "Dealer Wins"
                pos = 255
            resultText = font.render(gameResult, True, white)
            screen.blit(resultText, (pos, 250))

    pygame.display.flip()

pygame.quit()