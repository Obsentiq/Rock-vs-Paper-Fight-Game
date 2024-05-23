import pygame
import math
import random
from pygame import mixer

program_run = True
while program_run:
    # Initiization Stage
    # Initializing the game
    pygame.init()
    game_over_status = False

    # Setting up the screen
    screen = pygame.display.set_mode((800, 600))

    # Title and Icon
    pygame.display.set_caption('Rock Paper Scissors (Rock vs Paper!)')
    icon = pygame.image.load('Rock - Neutral Stance 1.png')
    pygame.display.set_icon(icon)

    # Background
    background = pygame.image.load('background-2.png')

    #Main_Menu_Background
    Logo_list = ['RockvsPaper0.jpg', 'RockvsPaper1.jpg', 'RockvsPaper2.jpg', 'RockvsPaper3.jpg', 'RockvsPaper4.jpg', 'RockvsPaper5.jpg', 'RockvsPaper6.jpg', 'RockvsPaper7.jpg', 'RockvsPaper8.jpg', 'RockvsPaper9.jpg', 'RockvsPaper10.jpg', 'RockvsPaper11.jpg', 'RockvsPaper12.jpg', 'RockvsPaper13.jpg', 'RockvsPaper14.jpg', 'RockvsPaper15.jpg', 'RockvsPaper16.jpg']
    Logo = pygame.image.load('RockPaperScissorsLogo.jpg')
    Logo_Final = pygame.image.load('RockvsPaperlogo.jpg')

    # Rock
    rock_neutral_1 = pygame.image.load('Rock - Neutral Stance 1.png')
    rock_neutral_1_x = 50
    rock_neutral_1_x_change = 0
    rock_neutral_1_y = 100

    rock_neutral_2 = pygame.image.load('Rock - Neutral Stance 2.png')

    rock_punch = pygame.image.load('Rock - Punch Stance.png')

    rock_attack = pygame.image.load('Rock - Rock Attack Stance.png')

    rock_1 = pygame.image.load('Rock 1.png')
    rock_1_x = 50
    rock_1_y = 600
    rock_1_x_change = 5
    rock_1_y_change = -20

    rock_2 = pygame.image.load('Rock 2.png')
    rock_2_x = 50
    rock_2_x_change = 3
    rock_2_y = 600
    rock_2_y_change = -10

    neutral_mode = 1
    rock_health_value = 120
    paper_health_value = 120

    Rock1 = False
    Rock2 = False
    # Font for Score
    font = pygame.font.Font('freesansbold.ttf', 50)
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    text_font = pygame.font.Font('LUMINA.ttf', 15)
    new_font = pygame.font.Font('LUMINA.ttf', 50)
    rock_health_x = 5
    rock_health_y = 1
    paper_health_x = 450
    paper_health_y = 1

    # Paper
    paper_neutral_stance_1 = pygame.image.load('Paper - Neutral Stance 1.png')
    paper_neutral_stance_1_x = 600
    paper_neutral_stance_1_y = 100
    paper_neutral_stance_2 = pygame.image.load('Paper - Neutral Stance 2.png')
    paper_punch_stance = pygame.image.load('Paper - Punch Stance.png')

    # Background Sound
    mixer.music.load('cyborg-in-me-background-music-for-video-blog-promo-stories-188531.mp3')
    mixer.music.play(-1)

    # game over
    over_x = 200
    over_y = 268

    def start(x, y):
        start_text = text_font.render('DEFEAT PAPER WITH ROCK! To Start, press Space.', True, (0, 0, 0))
        screen.blit(start_text, (x, y))

    def restart(x, y):
        restart_text = text_font.render('To play again, press Space.', True, (0, 0, 0))
        screen.blit(restart_text, (x, y))

    def name(x, y):
        name_text = new_font.render('Rimon Kayastha presents', True, (0, 0, 0))
        screen.blit(name_text, (x, y))

    def rock_score(x, y, z):
        rock_health = font.render('Rock: ' + str(x) + ' HP', True, (0, 0, 0))
        screen.blit(rock_health, (y, z))


    def game_over(x, y):
        game_over_text = over_font.render('GAME OVER', True, (255, 0, 0))
        screen.blit(game_over_text, (x, y))


    def you_win(x, y):
        game_over_text = over_font.render('YOU WIN!!', True, (0, 255, 0))
        screen.blit(game_over_text, (x, y))


    def paper_score(x, y, z):
        paper_health = font.render('Paper: ' + str(x) + ' HP', True, (0, 0, 0))
        screen.blit(paper_health, (y, z))


    def rock_neutral1(x, y):
        screen.blit(rock_neutral_1, (x, y))


    def rock_neutral2(x, y):
        screen.blit(rock_neutral_2, (x, y + 20))


    def rock_punch_stance(x, y):
        screen.blit(rock_punch, (x, y))


    def rock_attack_stance(x, y):
        screen.blit(rock_attack, (x, y))


    def rock_1_position(x, y):
        screen.blit(rock_1, (x, y))


    def rock_2_position(x, y):
        screen.blit(rock_2, (x, y))


    def paper_neutral_1(x, y):
        screen.blit(paper_neutral_stance_1, (x, y))


    def paper_neutral_2(x, y):
        screen.blit(paper_neutral_stance_2, (x, y))


    def paper_punch(x, y):
        screen.blit(paper_punch_stance, (x, y))


    def isCollision(w, y, x, z):
        distance = math.sqrt((math.pow(w - x, 2)) + (math.pow(y - z, 2)))
        if distance <= 300:
            return True

    #Setting defaults
    clock = pygame.time.Clock()

    rock_up = False
    main_menu_state = True
    movement = 0
    running = False
    a = 0
    b = 0
    c = 0
    e = 0
    Count = 0
    nopunch = True
    gameover = False
    LogoCount = 0
    Logostate = True
    FinalLogoCount = 0
    Finallogostate = False
    Eachlogostate = False
    EachCount = 0
    i = 0
    j = 0


    while main_menu_state:
        screen.fill((255, 255, 255))

        if Logostate:
            screen.blit(Logo, (0, 0))
            LogoCount += 1
        if LogoCount > 100:
            Logostate = False
            Eachlogostate = True
        if Eachlogostate:
            if 0 <= i < len(Logo_list):
                imgtemp = pygame.image.load(Logo_list[i])
                screen.blit(imgtemp, (0, 0))
                EachCount += 1
        if EachCount > 100:
            if i >= len(Logo_list):
                Eachlogostate = False
                Finallogostate = True
            i += 1
        if Finallogostate:
            screen.blit(Logo_Final, (0, 0))
            j += 1
        if j > 100:
            start(225, 500)
        name(125, 50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu_state = False
                program_run = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    running = True
                    main_menu_state = False
                    Logostate = True
                    Finallogostate = False
        pygame.display.update()
        clock.tick(120)


    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, -100))
        if neutral_mode == 2 and a == 30:
            neutral_mode = 1
            a = 0
        elif neutral_mode == 1 and a == 30:
            neutral_mode = 2
            a = 0
        elif neutral_mode == 3 and a == 50:
            if isCollision(rock_neutral_1_x, rock_neutral_1_y, paper_neutral_stance_1_x, paper_neutral_stance_1_y):
                if game_over_status is False:
                    paper_health_value -= 10
                    Count += 1
            neutral_mode = 1
            a = 0

        # screen.blit(rock_neutral_stance, (50, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                program_run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rock_neutral_1_x_change = 3
                elif event.key == pygame.K_LEFT:
                    rock_neutral_1_x_change = -3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    rock_neutral_1_x_change = 0
                if event.key == pygame.K_s:
                    neutral_mode = 3
                elif event.key == pygame.K_d:
                    neutral_mode = 4
                if game_over_status and event.key == pygame.K_SPACE:
                    running = False
                    main_menu_state = True
        rock_neutral_1_x += rock_neutral_1_x_change
        if rock_neutral_1_x <= 0:
            rock_neutral_1_x = 1
        elif rock_neutral_1_x >= 480:
            rock_neutral_1_x = 480
        if neutral_mode == 1:
            rock_neutral1(rock_neutral_1_x, rock_neutral_1_y)
            paper_neutral_2(paper_neutral_stance_1_x, paper_neutral_stance_1_y)
            a += 1
        elif neutral_mode == 2:
            rock_neutral2(rock_neutral_1_x, rock_neutral_1_y)
            paper_neutral_1(paper_neutral_stance_1_x, paper_neutral_stance_1_y)
            a += 1
        elif neutral_mode == 3:
            rock_punch_stance(rock_neutral_1_x, rock_neutral_1_y)
            paper_neutral_1(paper_neutral_stance_1_x, paper_neutral_stance_1_y)
            a += 1
        elif neutral_mode == 4:
            rock_attack_stance(rock_neutral_1_x, rock_neutral_1_y)
            paper_neutral_1(paper_neutral_stance_1_x, paper_neutral_stance_1_y)
        if neutral_mode == 4 and rock_up == False and Count >= 3:
            rock_1_position(rock_1_x, rock_1_y)
            rock_2_position(rock_2_x, rock_2_y)
            rock_1_y += rock_1_y_change
            rock_2_y += rock_2_y_change
            if rock_1_y <= 50:
                rock_1_y = 50
            if rock_2_y <= 400:
                rock_2_y = 400
            if rock_1_y <= 50 and rock_2_y <= 400:
                rock_up = True
        if rock_up == True:
            rock_1_x += rock_1_x_change
            rock_2_x += rock_2_x_change
            if abs(rock_1_x - paper_neutral_stance_1_x) <= 30:
                rock_1_x = 50
                rock_1_y = 600
                if game_over_status is False:
                    paper_health_value -= 10
                Rock1 = True
            if abs(rock_2_x - paper_neutral_stance_1_x) <= 30:
                rock_2_x = 50
                rock_2_y = 600
                if game_over_status is False:
                    paper_health_value -= 10
                Rock2 = True
            if Rock1 and Rock2:
                rock_up = False
                neutral_mode = 1
                Rock1 = False
                Rock2 = False
            Count = 0
        rock_1_position(rock_1_x, rock_1_y)
        rock_2_position(rock_2_x, rock_2_y)

        # if nopunch:
        #     if movement == 0:
        #         paper_neutral_stance_1_x -= 5
        #         b = b+1
        #         if b == 50:
        #             movement = 1
        #     if movement == 1:
        #         paper_neutral_stance_1_x += 5
        #         b = b-1
        #         if b == 0:
        #             movement = 0
        #     if random.randint(2, 101) % 101 == 0:
        #         nopunch = False
        #
        #     if not nopunch and c < 50:
        #         paper_punch(paper_neutral_stance_1_x, paper_neutral_stance_1_y)
        #         c = c+1
        #         if c == 50:
        #             nopunch = True
        #             c = 0
        #             if (paper_neutral_stance_1_x - rock_neutral_1_x) <= 177:
        #                 rock_health_value -= 20

        if nopunch:
            if movement == 0:
                paper_neutral_stance_1_x -= 5
                b += 1
                if b == 50:
                    nopunch = False
                    movement = 1
            elif movement == 1:
                paper_neutral_stance_1_x += 5
                b -= 1
                if b == 0:
                    nopunch = False
                    movement = 0

            if random.randint(2, 101) % 101 == 0:
                movement = 1 - movement
            if paper_neutral_stance_1_x >= 600:
                paper_neutral_stance_1_x = 599
            if paper_neutral_stance_1_x <= 300:
                paper_neutral_stance_1_x = 300

        if not nopunch and e == 0:
            paper_neutral_stance_1_y = 5000
            paper_punch(paper_neutral_stance_1_x - 20, 100)
            c += 1
            if c == 50:
                if (paper_neutral_stance_1_x - rock_neutral_1_x) <= 177:
                    rock_health_value -= 20
                c = 0
                nopunch = True
                paper_neutral_stance_1_y = 100

        if rock_health_value <= 0:
            game_over(over_x, over_y)
            restart(300, 560)
            nopunch = False
            game_over_status = True
            e = 1
        if paper_health_value <= 0:
            you_win(over_x + 2, over_y)
            restart(300, 560)
            nopunch = False
            game_over_status = True
            e = 1

        rock_score(rock_health_value, rock_health_x, rock_health_y)
        paper_score(paper_health_value, paper_health_x, paper_health_y)

        pygame.display.update()
        clock.tick(120)
