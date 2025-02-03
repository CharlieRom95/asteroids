# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    i = 0

    while i < float('inf'):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        i += 1


        Δ = clock.tick(60)
        dt = Δ / 1000
        pygame.display.flip()


    












if __name__ == "__main__":
    main()