import pygame
import time
import random

screenWidth = 600
screenHeight = 600

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Blackjack")
running = True

while(running):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

    pygame.display.flip()

pygame.quit()