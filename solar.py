# Example file showing a basic pygame "game loop"
import pygame

class HeavenlyBodies:
    def __init__(self, center_pos: tuple, size: int, color: str):
        self.center_pos = center_pos
        self.size = size
        self.color = color
    def spawn(self):
        #Takes the color, the center position and the size, returns a tuple with the center position
        pygame.draw.circle(screen, self.color, self.center_pos, self.size)



# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True
def spawnPlanet(color: str, center_pos: tuple, size: int) -> tuple:
    #Takes the color, the center position and the size, returns a tuple with the center position
    pygame.draw.circle(screen, "red", center_pos, size)
    return center_pos
    

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # RENDER YOUR GAME HERE
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()