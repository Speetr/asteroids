import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    pygame.init()

    # set game resolution
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create player object
    protag = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # used to set fps to 60
    gameclock = pygame.time.Clock()
    dt = 0

    #  main game loop
    while True:
        # write to our log
        log_state()

        #get user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #black background
        screen.fill("black")

        # render player
        protag.draw(screen)

        # refresh the screen
        pygame.display.flip()

        # pause the game until 1/60th of a second has passed
        dt = gameclock.tick(60) / 1000
        # print(dt)

    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
