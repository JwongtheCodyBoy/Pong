import pygame, sys, random

pygame.init()

WIDTH, HEIGHT = 1280, 720
 
FONT = pygame.font.Font("Satoshi-Variable.ttf", int(WIDTH/20))

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
CLOCK = pygame.time.Clock()

def drawDotLine():
    for i in range(-16, HEIGHT, HEIGHT//14):
        pygame.draw.rect(SCREEN, (255,255,255), (WIDTH//2+10, i, 10, HEIGHT//20))

def PlayGame():
    # Paddles
    player = pygame.Rect(WIDTH-110, HEIGHT/2 -50, 10,100)
    opponent = pygame.Rect(110, HEIGHT/2 -50, 10, 100)
    opponent_score, player_score = 0, 0

    # Ball
    ball_radius = 20
    ball = pygame.Rect(WIDTH/2 -10, HEIGHT/2 -10, ball_radius,ball_radius)
    x_speed, y_speed = 1,1

    while True:
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP]:
            if player.top > 0:
                player.top -= 2
        if keys_pressed[pygame.K_DOWN]:
            if player.bottom < HEIGHT:
                player.top += 2

        if lonely:
            if opponent.y < ball.y:
                opponent.top += 2
            if opponent.bottom > ball.y:
                opponent.bottom -=2
        else:
            if keys_pressed[pygame.K_w]:
                if opponent.top > 0:
                    opponent.top -= 2
            if keys_pressed[pygame.K_s]:
                if opponent.bottom < HEIGHT:
                    opponent.top += 2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if ball.y + ball_radius >= HEIGHT:
            y_speed *= -1
        elif ball.y - ball_radius <= 0:
            y_speed *= -1

        if player.x - ball.width <= ball.x <= player.x and ball.y in range(player.top-ball.width, player.bottom+ball.width):    #basic: if ball is touching player in both X and Y then redirect        #complex If ball x is in the surface of the paddle and half of the paddle then While also ball.y is inside the Y Positions then redirect
            x_speed = -1

            middleplayer = player.y + player.height/2
            differenceY =  ball.y - middleplayer
            y_speed = differenceY / (player.height/2)
            
        if opponent.x - ball.width <= ball.x <= opponent.x and ball.y in range(opponent.top-ball.width, opponent.bottom+ball.width):    #basic: if ball is touching player in both X and Y then redirect        #complex If ball x is in the surface of the paddle and half of the paddle then While also ball.y is inside the Y Positions then redirect
            x_speed = 1

            middleopponent = opponent.y + opponent.height/2
            differenceY =  ball.y - middleopponent
            y_speed = differenceY / (opponent.height/4)

        if ball.x <= 0:
            player_score += 1
            ball.center = (WIDTH/2, HEIGHT/2)
            x_speed, y_speed = random.choice([-1, 1]), random.choice([-1, 1])   # no randint because if randint 0 is < 1 and > -1, and 0 speed = shit
        elif ball.x >= WIDTH:
            opponent_score += 1
            ball.center = (WIDTH/2, HEIGHT/2)
            x_speed, y_speed = random.choice([-1, 1]), random.choice([-1, 1])

        ball.x += x_speed * 2
        ball.y += y_speed * 2

        player_score_text = FONT.render(str(player_score), True, "white")
        opponent_score_text = FONT.render(str(opponent_score), True, "white")

        SCREEN.fill("black")

        pygame.draw.rect(SCREEN, "white", player)
        pygame.draw.rect(SCREEN, "white", opponent)
        pygame.draw.circle(SCREEN, 'white', ball.center,10)
        drawDotLine()

        SCREEN.blit(player_score_text, (WIDTH/2+100, 50))
        SCREEN.blit(opponent_score_text, (WIDTH/2-120, 50))

        pygame.display.update()
        CLOCK.tick(300)

# ChatGPT menu
button_width, button_height = int(WIDTH *0.3), int(HEIGHT *0.18)
play_button_rect = pygame.Rect(WIDTH // 4 - button_width // 2, HEIGHT // 2 - button_height // 2, button_width, button_height)
exit_button_rect = pygame.Rect(3 * WIDTH // 4 - button_width // 2, HEIGHT // 2 - button_height // 2, button_width, button_height)

lonely = False
checkbox_rect = pygame.Rect(exit_button_rect.x * 1.08, HEIGHT // 2 + 150, 20, 20)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

CHECKBOX_ON_COLOR = (250, 250, 250)
CHECKBOX_OFF_COLOR = (0, 0, 0)

def draw_buttons():
    pygame.draw.rect(SCREEN, GRAY, play_button_rect)
    pygame.draw.rect(SCREEN, GRAY, exit_button_rect)
    play_text = FONT.render("Play", True, WHITE)
    exit_text = FONT.render("Exit", True, WHITE)
    SCREEN.blit(play_text, (play_button_rect.x + (button_width - play_text.get_width()) // 2, play_button_rect.y + (button_height - play_text.get_height()) // 2))
    SCREEN.blit(exit_text, (exit_button_rect.x + (button_width - exit_text.get_width()) // 2, exit_button_rect.y + (button_height - exit_text.get_height()) // 2))

def draw_checkbox():
    pygame.draw.rect(SCREEN, WHITE, checkbox_rect, 2)  # Draw the border of the checkbox
    if lonely:
        pygame.draw.rect(SCREEN, CHECKBOX_ON_COLOR, checkbox_rect)
    else:
        pygame.draw.rect(SCREEN, CHECKBOX_OFF_COLOR, checkbox_rect)
        pygame.draw.rect(SCREEN, WHITE, checkbox_rect, 2)

    label_font = pygame.font.Font("Satoshi-Variable.ttf", int(HEIGHT/20))
    checkbox_label = label_font.render("Lonely Mode", True, WHITE)
    SCREEN.blit(checkbox_label, (checkbox_rect.x + checkbox_rect.width + 10, checkbox_rect.y - (checkbox_rect.height * 3)/4))

def menu():
    global lonely
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    print("Play button clicked!")
                    PlayGame()
                elif exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif checkbox_rect.collidepoint(event.pos):
                    lonely = not lonely

        # screen.fill(BLACK)
        draw_buttons()
        draw_checkbox()
        pygame.display.flip()

menu()
