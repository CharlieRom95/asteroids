# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    
    # Create groups first
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set up containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)  # Note the comma
    Shot.containers = (updatable, drawable, shots)

    # Then create instances
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    campo = AsteroidField()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        
        Δ = clock.tick(60)
        dt = Δ / 1000
        updatable.update(dt)

        for thing in asteroids:
            if thing.collisions(player):
                sys.exit("Game over!")

            for bullet in shots:
                if bullet.collisions(thing):
                    thing.kill()
                    bullet.kill()
                    

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()


    

if __name__ == "__main__":
    main()