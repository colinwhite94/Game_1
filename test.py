import pygame
import random
from pygame import mixer
import time
from time import sleep

#initialze pygame
pygame.init()

# creat screen
screen = pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("night mountain")
icon = pygame.image.load('night mountain.png')
pygame.display.set_icon(icon)

game_state = "start_menu"

#background
background = pygame.image.load('Aurora.png')

#background sound
mixer.music.load('night_sound.wav')
mixer.music.play(-1)

# Init mixer
pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)

# Seperate channels
channel_1 = pygame.mixer.Channel(0)
channel_2 = pygame.mixer.Channel(1)

pygame.key.set_repeat(1000000,1000000)

def draw_start_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 20)
    title0 = font.render('its the dead of winter, you are deep in the woods.', True, (255, 255, 255))
    title1 = font.render('you stayed out too long gathering wild berries, and medicinal plants', True, (255, 255, 255))
    title2 = font.render('for you ailing family.', True, (255, 255, 255))
    title3 = font.render('you must make it back to your cabin, alive.', True, (255, 255, 255))
    title4 = font.render('defend against bears, hunt elk, let the endangered Mt goats roam.', True, (255, 255, 255))
    title5 = font.render('good Luck.', True, (255, 255, 255))
    start_button = font.render('Press [e] for easy, [m] for medium, and [h] for hard', True, (255, 255, 255))
    screen.blit(title0, (100, 25))
    screen.blit(title1, (100, 75))
    screen.blit(title2, (100, 125))
    screen.blit(title3, (100, 175))
    screen.blit(title4, (100, 225))
    screen.blit(title5, (100, 275))
    screen.blit(start_button, (175, 310))
    logo = pygame.image.load('white logo.png')
    screen.blit(logo, (340, 340))
    bear = pygame.image.load('smallbear.png')
    screen.blit(bear, (140, 475))
    elk = pygame.image.load('smallelk.png')
    screen.blit(elk, (340, 475))
    goat = pygame.image.load('smallgoat.png')
    screen.blit(goat, (540, 475))
    pygame.display.update()

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
font1 = pygame.font.Font('freesansbold.ttf', 62)
font2 = pygame.font.Font('freesansbold.ttf', 16)

textX = 10
textY = 570

def show_score(x,y):
    score = font.render("Score: " + str(score_value) + " /10", True, (255,255,255))
    screen.blit(score, (x,y))

def show_instructions():
    instructions0 = font2.render("left arrow shoots left", True, (255,255,255))
    instructions1 = font2.render("right arrow shoots right", True, (255, 255, 255))
    instructions2 = font2.render("elk +1", True, (255,255,255))
    instructions3 = font2.render("goat -1", True, (255, 255, 255))
    instructions4 = font2.render("down is pause", True, (255, 255, 255))
    screen.blit(instructions0, (10, 10))
    screen.blit(instructions1, (10, 35))
    screen.blit(instructions2, (10, 60))
    screen.blit(instructions3, (10, 80))
    screen.blit(instructions4, (680, 580))

def you_win():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 20)
    title0 = font.render('you Win!', True, (255, 255, 255))
    title1 = font.render('your ailing family will survive the winter.', True, (255, 255, 255))
    title2 = font.render('you protected.', True, (255, 255, 255))
    title3 = font.render('you provided.', True, (255, 255, 255))
    title4 = font.render('press [e] for easy, [m] for medium, and [h] for hard', True, (255, 255, 255))
    screen.blit(title0, (175, 100))
    screen.blit(title1, (175, 150))
    screen.blit(title2, (175, 200))
    screen.blit(title3, (175, 250))
    screen.blit(title4, (175, 300))
    logo = pygame.image.load('white logo.png')
    screen.blit(logo, (340, 450))
    pygame.display.update()

def you_died():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 20)
    title0 = font.render('you died, alone in the woods', True, (255, 255, 255))
    title1 = font.render('your family must fend for themselves now', True, (255, 255, 255))
    title2 = font.render('press [e] for easy, [m] for medium, and [h] for hard', True, (255, 255, 255))
    screen.blit(title0, (100, 100))
    screen.blit(title1, (100, 150))
    screen.blit(title2, (100, 200))
    logo = pygame.image.load('white logo.png')
    screen.blit(logo, (340, 435))
    pygame.display.update()

def pause():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 20)
    title0 = font.render('paused', True, (255, 255, 255))
    title1 = font.render('left arrow shoots left, right arrow shoots right', True, (255, 255, 255))
    title2 = font.render('shoot bears before they kill you', True, (255, 255, 255))
    title3 = font.render('leave the endangered mt goats alone, they will charge, but are bluffing', True, (255, 255, 255))
    title4 = font.render('shoot the elk for food', True, (255, 255, 255))
    title5 = font.render('bag 10 elk, to survive the winter', True, (255, 255, 255))
    screen.blit(title0, (100, 100))
    screen.blit(title1, (100, 150))
    screen.blit(title2, (100, 200))
    screen.blit(title3, (100, 250))
    screen.blit(title4, (100, 300))
    screen.blit(title5, (100, 350))
    logo = pygame.image.load('white logo.png')
    screen.blit(logo, (340, 435))
    pygame.display.update()

def aim():
    aim_sound = mixer.Sound('rack.wav')
    aim_sound.play(0)

def aim_on():
    sound0 = pygame.mixer.Sound('rack.wav')
    channel_1.play(sound0, loops=0)
    channel_1.set_volume(.5)

    sound1 = pygame.mixer.Sound('animal.wav')
    channel_2.play(sound1, loops=0)
    channel_2.set_volume(1)

#weapon
weaponImg = pygame.image.load('bigestrifle.png')
h = 1
K=1
xpos1 = 275
def weaponX(h):
    if h < 50:
        xpos = xpos1 + h
    elif h >= 50:
        xpos = xpos1 + 100 - h
    else:
        xpos = xpos1
        h = 0
    return xpos

def weaponY(h):
    ypos = 385
    return ypos

def weapon(x,y):
    screen.blit(weaponImg, (x, y))

#bear
gobearX = random.randint(800, 2000)
sign = random.randint(1, 2)
if sign > 1:
    bearX = gobearX * 1
elif sign < 2:
    bearX = gobearX * -1
gobearY = random.randint(50, 200)
bearY = gobearY

def bear(x,y):
    screen.blit(bearImg, (bearX, bearY))
    bear_sound = mixer.Sound('animal.wav')
    if x > -100 and x < 800:
        bear_sound.play(0)
    return

#elk
elkImg = pygame.image.load('elk.png')
goelkX = random.randint(800, 2000)

def elk(x,y):
    screen.blit(elkImg, (elkX, elkY))
    elk_sound = mixer.Sound('animal.wav')
    if x > -100 and x < 800:
        elk_sound.play(0)
    return

species = 1
bearImg = pygame.image.load('bear.png')



#gameloop
running = True
while running:

    #ability to x-out of game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Start menue interaction
    if game_state == "start_menu":
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            l = 300
            game_state = "game"
        if keys[pygame.K_m]:
            l = 185
            game_state = "game"
        if keys[pygame.K_h]:
            game_state = "game"
            l = 80

    #pausing the game
    if game_state == "pause":
        pause()
        #the unpauses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            game_state = "game"

    #winning the game
    if game_state == "you_win":
        you_win()
        #play again?
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            score_value = 0
            K = 0
            k = 0
            gobearX = random.randint(800, 3000)
            # random left right generator
            sign = random.randint(1, 2)
            if sign > 1:
                bearX = gobearX * 1
            elif sign < 2:
                bearX = gobearX * -1
            gobearY = random.randint(50, 200)
            bearY = gobearY
            species = random.randint(1, 3)
            if species == 1:
                bearImg = pygame.image.load('bear.png')
                species = 1
            elif species == 2:
                bearImg = pygame.image.load('elk.png')
                species = 2
            elif species == 3:
                bearImg = pygame.image.load('goat.png')
                species = 3
            l = 300
            game_state = "game"

        if keys[pygame.K_m]:
            score_value = 0
            K = 0
            k = 0
            gobearX = random.randint(800, 3000)
            # random left right generator
            sign = random.randint(1, 2)
            if sign > 1:
                bearX = gobearX * 1
            elif sign < 2:
                bearX = gobearX * -1
            gobearY = random.randint(50, 200)
            bearY = gobearY
            species = random.randint(1, 3)
            if species == 1:
                bearImg = pygame.image.load('bear.png')
                species = 1
            elif species == 2:
                bearImg = pygame.image.load('elk.png')
                species = 2
            elif species == 3:
                bearImg = pygame.image.load('goat.png')
                species = 3
            l = 185
            game_state = "game"

        if keys[pygame.K_h]:
            score_value = 0
            K = 0
            k = 0
            gobearX = random.randint(800, 3000)
            # random left right generator
            sign = random.randint(1, 2)
            if sign > 1:
                bearX = gobearX * 1
            elif sign < 2:
                bearX = gobearX * -1
            gobearY = random.randint(50, 200)
            bearY = gobearY
            species = random.randint(1, 3)
            if species == 1:
                bearImg = pygame.image.load('bear.png')
                species = 1
            elif species == 2:
                bearImg = pygame.image.load('elk.png')
                species = 2
            elif species == 3:
                bearImg = pygame.image.load('goat.png')
                species = 3
            l = 80
            game_state = "game"

    # winning the game
    if game_state == "you_died":
        you_died()
        # play again?
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            score_value = 0
            K = 0
            k = 0
            gobearX = random.randint(800, 3000)
            # random left right generator
            sign = random.randint(1, 2)
            if sign > 1:
                bearX = gobearX * 1
            elif sign < 2:
                bearX = gobearX * -1
            gobearY = random.randint(50, 200)
            bearY = gobearY
            species = random.randint(1, 3)
            if species == 1:
                bearImg = pygame.image.load('bear.png')
                species = 1
            elif species == 2:
                bearImg = pygame.image.load('elk.png')
                species = 2
            elif species == 3:
                bearImg = pygame.image.load('goat.png')
                species = 3
            l = 300
            game_state = "game"

        if keys[pygame.K_m]:
            score_value = 0
            K = 0
            k = 0
            gobearX = random.randint(800, 3000)
            # random left right generator
            sign = random.randint(1, 2)
            if sign > 1:
                bearX = gobearX * 1
            elif sign < 2:
                bearX = gobearX * -1
            gobearY = random.randint(50, 200)
            bearY = gobearY
            species = random.randint(1, 3)
            if species == 1:
                bearImg = pygame.image.load('bear.png')
                species = 1
            elif species == 2:
                bearImg = pygame.image.load('elk.png')
                species = 2
            elif species == 3:
                bearImg = pygame.image.load('goat.png')
                species = 3
            l = 185
            game_state = "game"

        if keys[pygame.K_h]:
            score_value = 0
            K = 0
            k = 0
            gobearX = random.randint(800, 3000)
            # random left right generator
            sign = random.randint(1, 2)
            if sign > 1:
                bearX = gobearX * 1
            elif sign < 2:
                bearX = gobearX * -1
            gobearY = random.randint(50, 200)
            bearY = gobearY
            species = random.randint(1, 3)
            if species == 1:
                bearImg = pygame.image.load('bear.png')
                species = 1
            elif species == 2:
                bearImg = pygame.image.load('elk.png')
                species = 2
            elif species == 3:
                bearImg = pygame.image.load('goat.png')
                species = 3
            l = 80
            game_state = "game"

    #The game logic
    if game_state == "game":

        keys = pygame.key.get_pressed()

        #pause
        if keys[pygame.K_DOWN]:
            game_state = "pause"

        #for things that will continuosly appear on screen, they go in this loop
        screen.fill((0, 0, 0))

        # background
        screen.blit(background, (0,0))

        #call weapon
        weapon(weaponX(h), weaponY(h))
        #h makes weapon move back and forth
        h += 1
        if h >= 100:
            h = 0
        K += 1

        #call BEAR, pass it coordinate
        bear(bearX, bearY)
        #moves bear to player

        if bearX > -10 and bearX < 600: #only move bear down when on screen
            bearY = bearY + 2 + K/l#185
        if bearX > 275:
            bearX = bearX - 2 - K/l#185
        elif bearX < 275:
            bearX = bearX + 2 + K/l#185
        bearX = bearX + random.randint(-4, 4)
        bearY = bearY + random.randint(-1, 1)

        #If ya die by a freaking bear
        if bearY >= 500:
            if species == 1:
                game_state = "you_died"

            if species != 1:
                gobearX = random.randint(800, 3000)
                # random left right generator
                sign = random.randint(1, 2)
                if sign > 1:
                    bearX = gobearX * 1
                elif sign < 2:
                    bearX = gobearX * -1
                gobearY = random.randint(50, 200)
                bearY = gobearY
                species = random.randint(1, 3)
                if species == 1:
                    bearImg = pygame.image.load('bear.png')
                    species = 1
                elif species == 2:
                    bearImg = pygame.image.load('elk.png')
                    species = 2
                elif species == 3:
                    bearImg = pygame.image.load('goat.png')
                    species = 3

        #rack weapon when pointed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            aim()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            aim()

        if bearX < 250 and bearX > 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and bearY < 600:
            aim_on()
            if species == 1:
                score_value = score_value
            elif species == 2:
                score_value += 1
            elif species == 3:
                score_value -= 1
            gobearX = random.randint(800, 3000)
            #random left right generator
            sign = random.randint(1, 2)
            if sign > 1:
                bearX = gobearX * 1
            elif sign < 2:
                bearX = gobearX * -1
            gobearY = random.randint(50, 200)
            bearY = gobearY
            species = random.randint(1, 3)
            if species == 1:
                bearImg = pygame.image.load('bear.png')
                species = 1
            elif species == 2:
                bearImg = pygame.image.load('elk.png')
                species = 2
            elif species == 3:
                bearImg = pygame.image.load('goat.png')
                species = 3

        if bearX > 250 and bearX < 800 and event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and bearY < 600:
            aim_on()
            if species == 1:
                score_value = score_value
            elif species == 2:
                score_value += 1
            elif species == 3:
                score_value -= 1
            gobearX = random.randint(800, 3000)
            # random left right generator
            sign = random.randint(1, 2)
            if sign > 1:
                bearX = gobearX * 1
            elif sign < 2:
                bearX = gobearX * -1
            gobearY = random.randint(50, 200)
            bearY = gobearY
            species = random.randint(1, 2)
            if species > 1:
                bearImg = pygame.image.load('bear.png')
                species = 1
            elif species < 2:
                bearImg = pygame.image.load('elk.png')
                species = 2
            elif species == 3:
                bearImg = pygame.image.load('goat.png')
                species = 3

        if score_value >=1:
            game_state = "you_win" #you_win()
        show_score(textX, textY)
        show_instructions()
        pygame.display.update() #this line will ALWAY be in a pygame