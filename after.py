import pygame
import sys
pygame.init()
white = (58,58,58)
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("My first game screen")
background = pygame.image.load("OIP.jpg")
background = pygame.transform.scale(background,(500,500))
bird= pygame.image.load("goblin.jpg")
bird = pygame.transform.scale(bird,(150,150))
font = pygame.font.Font("freesansbold.ttf",30)
text = font.render("My pygame",True,white)
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background,(0,0))
    screen.blit(bird,(150,200))
    screen.blit(text,(100,300))
    pygame.display.flip()
pygame.quit()
