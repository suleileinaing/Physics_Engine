import pygame
import sys
import constant as c
import balls 

pygame.init()
screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("Physics Engine")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(c.green)
    pygame.display.flip()

    pygame.time.Clock().tick(c.FPS)