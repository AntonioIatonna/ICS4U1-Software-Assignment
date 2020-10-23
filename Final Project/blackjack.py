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
cardA = [ASpades, AClubs, AHearts, ADiamonds]
card2 = [Spades2, Clubs2, Hearts2, Diamonds2]
card3 = [Spades3, Clubs3, Hearts3, Diamonds3]
card4 = [Spades4, Clubs4, Hearts4, Diamonds4]
card5 = [Spades5, Clubs5, Hearts5, Diamonds5]
card6 = [Spades6, Clubs6, Hearts6, Diamonds6]
card7 = [Spades7, Clubs7, Hearts7, Diamonds7]
card8 = [Spades8, Clubs8, Hearts8, Diamonds8]
card9 = [Spades9, Clubs9, Hearts9, Diamonds9]
card10 = [Spades10, Clubs10, Hearts10, Diamonds10, JSpades, JClubs, JHearts, JDiamonds, QSpades, QClubs, QHearts, QDiamonds, KSpades, KClubs, KHearts, KDiamonds]

# Colours
grey = (192, 192, 192)
black = (0, 0, 0)

# Begin main code
# Init game
pygame.init()
screen = pygame.display.set_mode((650, 500))
pygame.display.set_caption("Blackjack")
font= pygame.font.SysFont('eras bold itc', 30)
running = True
stand = False
gameover = False

# Create background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((80, 150, 15))
hitButton = pygame.draw.rect(background, grey, (10, 445, 90, 40))
standButton = pygame.draw.rect(background, grey, (10, 390, 90, 40))
hitText = font.render("Hit", True, black)
standText = font.render("Stand", True, black)

# Show objects on screen
screen.blit(background, (0, 0))
screen.blit(hitText, (40, 458))
screen.blit(standText, (25, 402))

userCards = []
dealerCards = []

while(running):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

    pygame.display.flip()

pygame.quit()