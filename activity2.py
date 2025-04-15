import pygame
import sys
pygame.init()
white = (255,255,255)
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pygame")
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background,(500,500))
bird= pygame.image.load("bird2.png")
bird = pygame.transform.scale(bird,(150,150))
font = pygame.font.Font(None,40)
text = font.render("hi it is maneet singh",True,white)
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background,(0,0))
    screen.blit(bird,(0,100))
    screen.blit(text,(200,100))
    pygame.display.flip()
pygame.quit()
