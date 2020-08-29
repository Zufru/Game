import pygame
from utils import  *
from Classes import *

# Initialize pygame
pygame.init()
#SET TITLE OF WINDOW
pygame.display.set_caption("Sheerwood Forest")

# SETS FPS
clock = pygame.time.Clock()

# RUNNING THE LOOP FOR THE GAME // MAIN LOOP
run = True
while run:
    clock.tick(60)
    player.moving_level()
    
    if hell_beast1.health > 0:
        hell_beast1.draw_breath(window)


    if goblin.visible == True:
        if (player.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3]
        and player.hitbox[1] + player.hitbox[3] > goblin.hitbox[1]):
            if (player.hitbox[0] + player.hitbox[2] > goblin.hitbox[0] 
            and player.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]):
                player.hit()
                score -= 5
                
    if shoot_timing > 0:
        shoot_timing +=1
    if shoot_timing > 3:
        shoot_timing = 0
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # IF BULLET IS OFF THE SCREEN REMOVE THE BULLET
    for bullet in bullets:
        #CHECK IF BULLET IS WITHIN THE ENEMY HITBOX AND REMOVE THE BULLET
        #AND PRINT HIT IF IT IS
        if (bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3]
            and bullet.y + bullet.radius > goblin.hitbox[1]):
            if (bullet.x + bullet.radius > goblin.hitbox[0] 
                and bullet.x - bullet.radius < goblin.hitbox[0]
                + goblin.hitbox[2] and goblin.visible == True):
                #hit_sfx.play()
                goblin.hit()
                score += 100
                bullets.pop(bullets.index(bullet))
                
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))
    # KEYS, PRESSED
    keys = pygame.key.get_pressed()
    #SHOOTS THE BULLET
    if keys[pygame.K_SPACE] and shoot_timing == 0:
        #bullet_sfx.play()
        if player.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Projectile(round(player.x + player.width // 2),
                                      round(player.y + player.height // 2),
                                      6, (0, 0, 0), facing))
        
        shoot_timing = 1
    # MOVING THE PLAYER LEFT AND RIGHT
    if keys[pygame.K_a] and player.x > 1 and player.health >= 1:
        player.x -= player.vel
        player.left = True
        player.right = False
        player.standing = False
    elif keys[pygame.K_d] and player.health >= 1:
        player.x += player.vel
        player.right = True
        player.left = False
        player.standing = False
    else:
        player.standing = True
        player.walkCount = 0

    if not (player.isJump):
        if keys[pygame.K_UP] and player.health >= 1:
            player.isJump = True
            player.right = False
            player.left = False
            player.walkCount = 0
    else:
       if player.jumpCount >= -10:
           neg = 1
           if player.jumpCount < 0:
               neg = -1
           player.y -= (player.jumpCount**2) / 2 * neg
           player.jumpCount -= 1
       else:
           player.isJump = False
           player.jumpCount = 10
           

    if player.level == 0:
        redraw_level1()
    if player.level == 1:
        redraw_level2()

pygame.quit()
