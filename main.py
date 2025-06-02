import pygame
import constants

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 #milliseconds

    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="gray")
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
        main()