import pygame
import constants
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    dt = 0 #milliseconds
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatables.update(dt)

        for asteroid in asteroids:
            if player.if_collision(asteroid):
                print("Game over!")
                sys.exit(0)
            for bullet in shots:
                if bullet.if_collision(asteroid):
                    asteroid.kill()
                    bullet.kill()

        screen.fill(color="black")
        
        for drawable in drawables:
            drawable.draw(screen) 

        pygame.display.flip()
        dt = clock.tick(60) / 1000 #limits framerate to 60 fps


if __name__ == "__main__":
        main()