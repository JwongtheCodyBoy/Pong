import pygame, sys, random
 
pygame.init()
 
WIDTH, HEIGHT = 1280, 720       
 
FONT = pygame.font.SysFont("Satoshi-Variable.ttf", int(WIDTH/20))
 
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))   # Make Screen this size
pygame.display.set_caption("Pong")
CLOCK = pygame.time.Clock()

# Paddle Variables
player = pygame.Rect(WIDTH-110, HEIGHT/2 -50, 10,100)
opponent = pygame.Rect(110, HEIGHT/2 -50, 10, 100)
opponent_score, player_score = 0, 0

# Ball variables
ball_radius = 20
ball = pygame.Rect(WIDTH/2 -10, HEIGHT/2 -10, ball_radius,ball_radius)
x_speed, y_speed = 1,1
 
def drawDotLine():
    for i in range(-16, HEIGHT, HEIGHT//14):
        pygame.draw.rect(SCREEN, (255,255,255), (WIDTH//2+10, i, 10, HEIGHT//20))
 
while True:                     # Keep Pygames active until closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # PLAYER INPUTS SECTION
    keys_pressed = pygame.key.get_pressed()
    # Arrow player
    if keys_pressed[pygame.K_UP]:
        if player.top > 0:
            player.top -= 2
    if keys_pressed[pygame.K_DOWN]:
        if player.bottom < HEIGHT:
            player.top += 2
    # WS player
    if keys_pressed[pygame.K_w]:
            if opponent.top > 0:
                opponent.top -= 2
    if keys_pressed[pygame.K_s]:
        if opponent.bottom < HEIGHT:
            opponent.top += 2
    # OPTIONAL ENEMY "AI" SCRIPTS
    # opponent_mid = opponent.y + opponent.height/2
    # margin = int(opponent.height*0.65)
    # if opponent_mid - margin < ball.y:      #for hard mode use opponent.y instead of opponent_mid + margin  Increase dificluty by lowering margin
    #     opponent.top += 2
    # if opponent_mid + margin > ball.y:      #for hard mode use opponent.bottom instead of opponent_mid - margin
    #     opponent.bottom -=2
    
    # BALL SECTION
    # If ball touches top or bottom, throw it in opposite direction
    if ball.y + ball_radius >= HEIGHT or ball.y - ball_radius <= 0:
        y_speed *= -1
    
    # If ball reaches WS player side, arrow player get score and reset ball
    if ball.x <= 0:
        player_score += 1
        ball.center = (WIDTH/2, HEIGHT/2)
        x_speed, y_speed = random.choice([-1, 1]), random.choice([-1, 1])

    # If ball reaches arrow player side, WS player get score and reset ball
    if ball.x >= WIDTH:
        opponent_score += 1
        ball.center = (WIDTH/2, HEIGHT/2)
        x_speed, y_speed = random.choice([-1, 1]), random.choice([-1, 1])
        
    # If ball touches Arrow player paddle, reverse x-direction, calculate bounce of ball on Y
        # Calculates by finding paddle's middle, then find the difference of between the Y, 
        # that will be our direction vector, divide it by player.height so we can 
        # adjust the speed magintude to the correct speed,reason why because we added middle player is very large number
    if player.x - ball.width <= ball.x <= player.x and ball.y in range(player.top-ball.width, player.bottom+ball.width):    
        x_speed = -1
        middleplayer = player.y + player.height/2
        differenceY =  ball.y - middleplayer
        y_speed = differenceY / (player.height/2)
    # If ball touches WS player paddle, reverse x-direction, calculate bounce of ball on Y
    if opponent.x - ball.width <= ball.x <= opponent.x and ball.y in range(opponent.top-ball.width, opponent.bottom+ball.width):
            x_speed = 1
            middleopponent = opponent.y + opponent.height/2
            differenceY =  ball.y - middleopponent
            y_speed = differenceY / (opponent.height/2)
    
    # Move the ball according to x,y dir with multiplyer of 2 (coz feel good)
    ball.x += x_speed * 2
    ball.y += y_speed * 2
    
    # Reseting screen
    SCREEN.fill("black")

    # Drawing stuff on screen
    # Paddles and ball
    pygame.draw.rect(SCREEN, "white", player)
    pygame.draw.rect(SCREEN, "white", opponent)
    pygame.draw.circle(SCREEN, 'white', ball.center,10)
    
    drawDotLine()
    
    # Score stuff
    player_score_text = FONT.render(str(player_score), True, "white")
    opponent_score_text = FONT.render(str(opponent_score), True, "white")
    SCREEN.blit(player_score_text, (WIDTH/2+50, 50))
    SCREEN.blit(opponent_score_text, (WIDTH/2-50, 50))
 
    pygame.display.update()     # Update game frame 
    CLOCK.tick(300)             # Advance game tick (0.3 s)