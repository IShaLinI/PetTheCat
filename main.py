# imports
import pygame as pg
import pygame.image
import constants

from gif import Gif
from animator import Animator

# Game Data
catImages = []

gameClock = pg.time.Clock()
frameTracker = 1

# Player Variables
clicks = 0
lastMilestone = -1
catType = 0

menuVisible = False

# initialize pygame
pg.init()

# Fill the array with cat images
for i in range(46):
    filePath = "assets/sprites/cats/sprites/tile0" + "{:02d}".format(i) + ".png"
    catImages.append(pygame.image.load(filePath))

# Window Setup
pg.display.set_caption("PET THE CAT!")
SCREEN_SIZE = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
gameWindow = pg.display.set_mode(SCREEN_SIZE)
pg.mouse.set_visible(False)

# Gifs
iconGif = Gif("icon.gif", 15, (0, 0), (32, 32))
cursorGif = Gif("cursor.gif", 20, (0, 0), (64, 64))

# Cat
cat = pygame.Rect((0, 0), (constants.CAT_SIZE, constants.CAT_SIZE))
cat.center = (int(constants.SCREEN_WIDTH / 2), int(constants.SCREEN_HEIGHT / 2))

# Menu Images
backButtonImage = pygame.image.load("assets/images/btnBack.png")
exitButtonImage = pygame.image.load("assets/images/btnExit.png")
menuButtonImage = pygame.image.load("assets/images/btnMenu.png")

# Image Scaling
backButtonImage = pygame.transform.scale(backButtonImage, (
    int(backButtonImage.get_width() * constants.MENU_BUTTON_SCALE), constants.MENU_BUTTON_HEIGHT)).convert()
exitButtonImage = pygame.transform.scale(exitButtonImage, (
    int(exitButtonImage.get_width() * constants.MENU_BUTTON_SCALE), constants.MENU_BUTTON_HEIGHT)).convert()
menuButtonImage = pygame.transform.scale(menuButtonImage, (
    int(menuButtonImage.get_width() * constants.MENU_BUTTON_SCALE), constants.MENU_BUTTON_HEIGHT)).convert()

# Menu Rectangles
backButtonRect = backButtonImage.get_rect()
exitButtonRect = exitButtonImage.get_rect()
menuButtonRect = menuButtonImage.get_rect()

menuAnimation = Animator([backButtonRect, exitButtonRect, menuButtonRect], constants.MENU_ANIMATION, 2)

while True:

    menuAnimation.update()

    # Set the background color
    gameWindow.fill(constants.BACKGROUND_COLOR)

    # Set the icon
    pg.display.set_icon(iconGif.current_frame)

    # move cursor
    cursorGif.rect.center = pygame.mouse.get_pos()

    # search for mouse collision with exit button
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cat.collidepoint(pygame.mouse.get_pos()):
                clicks += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pass

    # Progress Cat
    if clicks % 30 == 0 and clicks != lastMilestone:
        lastMilestone = clicks
        catType += 1
    if catType == 46:
        catType = 0

    # update Gifs
    iconGif.update()
    cursorGif.update()

    # draw cat
    gameWindow.blit(pygame.transform.scale(catImages[catType], cat.size), cat.topleft)

    # draw cursor
    gameWindow.blit(cursorGif.current_frame, cursorGif.rect.topleft)

    # Keep the frame rate
    gameClock.tick(constants.FRAME_RATE)

    # Update the display
    pg.display.update()
