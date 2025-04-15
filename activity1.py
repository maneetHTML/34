import pygame 
pygame.init()
screen = pygame.display.set_mode((640,600))
pygame.display.set_caption("My first pygame")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()