import pygame
import random
import math
import sys
from pygame import mixer

# Initialize the pygame
pygame.init()

# Create the screen (X and Y Coordinates)
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('assets/ufo.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('assets/background.png')

# Font
font = pygame.font.Font('assets/retro.ttf', 60)
resume_instruction_font = pygame.font.Font('assets/retro.ttf', 45)

# # Function to stop music
# def music_control():
#     return True


# Function to display pause screen
def resume_screen():
    screen.blit(background, (0, 0))
    resume_text = font.render("Game Paused", True, (255, 255, 255))
    resume_instruction = resume_instruction_font.render("Press P to Resume", True, (255, 255, 255))
    screen.blit(resume_text, (280, 260))
    screen.blit(resume_instruction, (265, 320))
    pygame.display.update()

# Function to display main menu
def main_menu():
    
    def draw_menu():
        screen.blit(background, (0, 0))
        menu_text = font.render("SPACE INVADERS", True, (255, 255, 255))
        start_text = font.render("Press Enter to Start", True, (255, 255, 255))
        screen.blit(menu_text, (260, 200))
        screen.blit(start_text, (190, 300))
        pygame.display.update()

    menu_running = True
    paused = False
    while menu_running:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if paused:
                        menu_running = False
                        main(username)
                    else:
                        if len(sys.argv) > 1:
                            username = sys.argv[1]
                        else:
                            username = 'Guest'
                        menu_running = False
                        main(username)
                # elif event.key == pygame.K_p:
                #     paused = True
                #     resume_screen()

def main(username):
    # Initialize the pygame
    pygame.init()

    # Create the screen (X and Y Coordinates)
    screen = pygame.display.set_mode((800, 600))

    # Background
    background = pygame.image.load('assets/background.png')

    # Background sound
    # if music:
    mixer.music.load('assets/background.wav')
    mixer.music.play(-1)

    # Title and icon
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load('assets/ufo.png')
    pygame.display.set_icon(icon)

    # Player
    playerImg = pygame.image.load('assets/player.png')
    playerX = 370
    playerY = 480
    playerX_change = 0
    player_lives = 3

    # Enemy
    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemy = 6

    for i in range(num_of_enemy):
        enemyImg.append(pygame.image.load('assets/enemy.png'))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(4)
        enemyY_change.append(40)

    # Bullet
    bulletImg = pygame.image.load('assets/bullet.png')
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state = "ready"

    # UFO
    ufoImg = pygame.image.load('assets/ufo.png')
    ufoX = random.randint(0, 736)
    ufoY = 50
    ufoX_change = 4
    ufo_health = 100

    # UFO Bullet
    ufoBulletImg = pygame.image.load('assets/bullet.png')
    ufoBulletX = 0
    ufoBulletY = 0
    ufoBulletY_change = 10
    ufoBullet_state = "ready"
    ufo_fire_interval = 1000  # Fire every 1000 milliseconds
    last_ufo_fire_time = pygame.time.get_ticks()

    # Score
    score_value = 0

    font = pygame.font.Font('assets/retro.ttf', 50)
    over_font = pygame.font.Font('assets/retro.ttf', 100)
    username_font = pygame.font.Font('assets/retro.ttf', 50)


    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(over_text, (250, 250))

    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))
    
    def show_username(x, y):
        user_text = username_font.render(username, True, (255, 255, 255))
        screen.blit(user_text, (x, y))

    def show_lives(x, y):
        lives = font.render("Lives : " + str(player_lives), True, (255, 255, 255))
        screen.blit(lives, (x, y))

    def enemy(x, y, i):
        screen.blit(enemyImg[i], (x, y))

    def player(x, y):
        screen.blit(playerImg, (x, y))

    def fire_bullet(x, y):
        nonlocal bullet_state
        bullet_state = "fire"
        screen.blit(bulletImg, (x + 16, y + 10))

    def fire_ufo_bullet(x, y):
        nonlocal ufoBullet_state
        ufoBullet_state = "fire"
        screen.blit(ufoBulletImg, (x + 16, y + 10))

    def isCollision(obj1X, obj1Y, obj2X, obj2Y, threshold=25):
        distance = math.sqrt((obj1X - obj2X) ** 2 + (obj1Y - obj2Y) ** 2)
        return distance < threshold
    
    def restart_game():
        nonlocal playerX, playerY, playerX_change, player_lives, enemyX, enemyY, \
            bulletX, bulletY, bulletX_change, bulletY_change, bullet_state, \
            ufoX, ufoY, ufoX_change, ufo_health, ufoBulletX, ufoBulletY, \
            ufoBulletY_change, ufoBullet_state, last_ufo_fire_time, score_value

        # Player
        playerX = 370
        playerY = 480
        playerX_change = 0
        player_lives = 3

        # Enemy
        for i in range(num_of_enemy):
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        # Bullet
        bulletX = 0
        bulletY = 480
        bulletX_change = 0
        bulletY_change = 10
        bullet_state = "ready"

        # UFO
        ufoX = random.randint(0, 736)
        ufoY = 50
        ufoX_change = 4
        ufo_health = 100

        # UFO Bullet
        ufoBulletX = 0
        ufoBulletY = 0
        ufoBulletY_change = 10
        ufoBullet_state = "ready"
        last_ufo_fire_time = pygame.time.get_ticks()

        # Score
        score_value = 0

    # Game loop
    running = True
    paused = False
    while running:
        # RGB
        screen.fill('black')
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mixer.music.stop()
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    playerX_change = -5
                if event.key == pygame.K_d:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound('assets/laser.wav')
                        bullet_sound.play()
                        bulletX = playerX
                        fire_bullet(playerX, bulletY)
                if event.key == pygame.K_r:
                    restart_game()
                if event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        print(paused)
                        resume_screen()
                # if event.key == pygame.K_m:
                #     mixer.music.stop()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    playerX_change = 0

        if not paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mixer.music.stop()
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        playerX_change = -5
                    elif event.key == pygame.K_d:
                        playerX_change = 5
                    elif event.key == pygame.K_SPACE:
                        if bullet_state == "ready":
                            bullet_sound = mixer.Sound('assets/laser.wav')
                            bullet_sound.play()
                            bulletX = playerX
                            fire_bullet(playerX, bulletY)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        playerX_change = 0

            # Player movement
            playerX += playerX_change
            if playerX <= 0:
                playerX = 0
            elif playerX >= 736:
                playerX = 736

            # Enemy movement
            for i in range(num_of_enemy):
                if enemyY[i] > 440:
                    if player_lives == 0:
                        for j in range(num_of_enemy):
                            enemyY[j] = 2000
                        ufoX = 2000
                        game_over_text()
                        break
                    else:
                        enemyX[i] = random.randint(0, 736)
                        enemyY[i] = random.randint(50, 150)
                        
                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 3
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -3
                    enemyY[i] += enemyY_change[i]
                collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
                if collision:
                    explosion_sound = mixer.Sound('assets/explosion.wav')
                    explosion_sound.play()
                    bulletY = 480
                    bullet_state = "ready"
                    score_value += 1
                    enemyX[i] = random.randint(0, 736)
                    enemyY[i] = random.randint(50, 150)
                enemy(enemyX[i], enemyY[i], i)

            # Bullet movement
            if bulletY <= 0:
                bulletY = 480
                bullet_state = "ready"
            if bullet_state == "fire":
                fire_bullet(bulletX, bulletY)
                bulletY -= bulletY_change

            # UFO movement
            ufoX += ufoX_change
            if ufoX <= 0:
                ufoX_change = 3
            elif ufoX >= 736:
                ufoX_change = -3

            # UFO bullet movement and firing logic
            current_time = pygame.time.get_ticks()
            if ufoBullet_state == "ready" and current_time - last_ufo_fire_time > ufo_fire_interval:
                ufoBulletX = ufoX
                ufoBulletY = ufoY
                ufoBullet_state = "fire"
                last_ufo_fire_time = current_time
            if ufoBullet_state == "fire":
                fire_ufo_bullet(ufoBulletX, ufoBulletY)
                ufoBulletY += ufoBulletY_change
                if ufoBulletY >= 600:
                    ufoBullet_state = "ready"

            # Check collision between UFO bullet and player
            if ufoBullet_state == "fire" and isCollision(playerX, playerY, ufoBulletX, ufoBulletY, threshold=27):
                player_lives -= 1
                ufoBullet_state = "ready"
                if player_lives <= 0:
                    for j in range(num_of_enemy):
                        enemyY[j] = 2000
                        ufoX = 2000
                    game_over_text()

            # Check collision between player bullet and UFO
            if isCollision(ufoX, ufoY, bulletX, bulletY, threshold=25):
                explosion_sound = mixer.Sound('assets/explosion.wav')
                explosion_sound.play()
                ufo_health -= 25
                bulletY = 480
                bullet_state = "ready"
                if ufo_health <= 0:
                    ufoX = random.randint(0, 736)  # Move UFO off screen
                    ufo_health = 200
                    score_value += 50

            # Draw UFO
            screen.blit(ufoImg, (ufoX, ufoY))

            player(playerX, playerY)
            show_score(10, 10)
            show_lives(300, 10)  # Show lives on the top right corner
            show_username(550, 10)

            pygame.display.update()


if __name__ == "__main__":
    main_menu()