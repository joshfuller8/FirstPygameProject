import pygame
import os

pygame.init()

# tuple representing the display dimensions as constants
(WIDTH, HEIGHT) = (1920, 1080)

# WIN represents the display window as a constant
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# change displayed name of program
pygame.display.set_caption('my first game')

# creating colors in RGB format as constants to be easily reused
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
TEALY_DAN = (0, 200, 200)
SKY = (0, 255, 255)

GRASS = (0, 185, 0)
background = SKY


# create a player class
class PlayerCharacter:

    def __init__(self, sprite):
        # positional and data
        self.x = 500
        self.y = 500
        self.width = 200
        self.height = 200
        self.sprite = pygame.transform.scale(sprite, (self.width, self.height))
        # character stats
        self.vel_x = 10
        self.vel_y = 20
        self.jump_height = 25
        self.can_jump = True

        self.max_jump_height = 150
        self.remaining_jump_height = self.max_jump_height


# set a frame rate constant
FPS = 60

# sprite constants
# mage_image_file = pygame.image.load(os.path.join('Assets', 'amg1_fr1.gif'))
# mage = pygame.transform.scale(mage_image_file, (200, 200))


player = PlayerCharacter(pygame.image.load(os.path.join('Assets', 'Lucas.jpg')))
# size and position of ground as a constant
GROUND = pygame.Rect(0, player.height + 500, WIDTH, HEIGHT)


# function will display each frame as the game is played
def draw_window():
    SCREEN.fill(background)
    pygame.draw.rect(SCREEN, GRASS, GROUND)
    SCREEN.blit(player.sprite, (player.x, player.y))
    pygame.display.update()


def main():
    # global user_input
    # player = PlayerCharacter(pygame.image.load(os.path.join('Assets', 'amg1_fr1.gif')))
    # player = pygame.Rect(200, GROUND.y - mage.get_height(), 250, 10)
    # user_input = pygame.key.get_pressed()
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # define key presses / controls
        user_input = pygame.key.get_pressed()

        # needs work    ############################################
        # jump
        if user_input[pygame.K_SPACE] and player.can_jump:
            player.y -= player.vel_y / 2
            player.vel_y -= 1
        if player.vel_y == 0 or not user_input[pygame.K_SPACE]:
            player.can_jump = False
        if not player.can_jump:
            player.y += player.vel_y / 2
            player.vel_y += 1
            if player.y > 500:
                player.y = 500
                if player.y == 500 and not user_input[pygame.K_SPACE]:
                    player.can_jump = True
                    player.vel_y = player.jump_height
        # #######################


        # move character to the left equal to character velocity
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            player.x -= player.vel_x

        # move character to the right equal to character velocity
        if user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            player.x += player.vel_x

        # update the window
        draw_window()
    pygame.quit()


main()
