import pygame

# Initialize pygame
pygame.init()
#SET SIZE OF WINDOW
window = pygame.display.set_mode((800, 500))
#SET TITLE OF WINDOW
pygame.display.set_caption("Sheerwood Forest")
# BULLET SOUND EFFECT WHEN SHOT
#bullet_sfx = [
#    pygame.mixer.sound('Sound/bullet.wav'),
#    ]
# BULLET SOUND EFECT WHEN HITS TARGET
#hit_sfx = [
#    pygame.mixer.sound('Sound/hit.wav')
#    ]
# BACKGROUND MUSIC
#music = pygame.mixer.music.load('Sound/music.mp3')
#pygame.mixer.music.play(-1)
#LIST OF IMAGES TO LOAD WHILE WALKING RIGHT
walkRight = [
    pygame.image.load('Sprites/player/knight iso char_run right_0.png'), 
    pygame.image.load('Sprites/player/knight iso char_run right_1.png'), 
    pygame.image.load('Sprites/player/knight iso char_run right_2.png'),
    pygame.image.load('Sprites/player/knight iso char_run right_3.png'),
    pygame.image.load('Sprites/player/knight iso char_run right_4.png'),
    pygame.image.load('Sprites/player/knight iso char_run right_5.png')
    ]
health_gfx = [
    #pygame.image.load('Sprites/healthbars/health_bg.png'),
    #pygame.image.load('Sprites/healthbars/health_border.png'),
    pygame.image.load('Sprites/healthbars/full_health.png'),
    pygame.image.load('Sprites/healthbars/health -1.png'),
    pygame.image.load('Sprites/healthbars/health -2.png'),
    pygame.image.load('Sprites/healthbars/health -3.png'),
    pygame.image.load('Sprites/healthbars/health -4.png'),
    pygame.image.load('Sprites/healthbars/health -5.png'),
    pygame.image.load('Sprites/healthbars/health -6.png'),
    pygame.image.load('Sprites/healthbars/health -7.png'),
    pygame.image.load('Sprites/healthbars/health -8.png'),
    pygame.image.load('Sprites/healthbars/health -9.png')
    ]

enviroment = [
    pygame.image.load('Sprites/box.png'),
    pygame.image.load('Sprites/backgrounds/tree01 (2).png')
    ]
#LLIST OF IMAGES TO LOAD WHILE WALKING LEFT
walkLeft = [
    pygame.image.load('Sprites/player/knight iso char_run left_0.png'),
    pygame.image.load('Sprites/player/knight iso char_run left_1.png'),
    pygame.image.load('Sprites/player/knight iso char_run left_2.png'),
    pygame.image.load('Sprites/player/knight iso char_run left_3.png'),
    pygame.image.load('Sprites/player/knight iso char_run left_4.png'),
    pygame.image.load('Sprites/player/knight iso char_run left_5.png')
    ]
# BACKGROUND IMAGE
bg = pygame.image.load('Sprites/backgrounds/sky_fc.png')
clouds = [
    pygame.image.load('Sprites/backgrounds/clouds_front_fc.png'),
    pygame.image.load('Sprites/backgrounds/clouds_mid_fc.png')
]
trees = [
    pygame.image.load('Sprites/backgrounds/tree01.png')
    ]
# CHARACTER IDLE IMAGE
char = [
        pygame.image.load('Sprites/player/knight iso char_idle_0.png'),
        pygame.image.load('Sprites/player/knight iso char_idle_1.png'),
        pygame.image.load('Sprites/player/knight iso char_idle_2.png'),
        pygame.image.load('Sprites/player/knight iso char_idle_3.png')
        ]
hell_beast = [
    pygame.image.load('Sprites/Hell_beast/hellb1.png'),
    pygame.image.load('Sprites/Hell_beast/hellb2.png'),
    pygame.image.load('Sprites/Hell_beast/hellb3.png'),
    pygame.image.load('Sprites/Hell_beast/hellb4.png'),
    pygame.image.load('Sprites/Hell_beast/hellb5.png'),
    pygame.image.load('Sprites/Hell_beast/hellb6.png'),
    pygame.image.load('Sprites/Hell_beast/hellb1.png'),
    pygame.image.load('Sprites/Hell_beast/hellb2.png'),
    pygame.image.load('Sprites/Hell_beast/hellb3.png'),
    pygame.image.load('Sprites/Hell_beast/hellb4.png')
    ]
hell_beast_breath = [
    pygame.image.load('Sprites/Hell_beast/hellb_breath1.png'),
    pygame.image.load('Sprites/Hell_beast/hell-beast-breath2.png'),
    pygame.image.load('Sprites/Hell_beast/hell-beast-breath3.png'),
    pygame.image.load('Sprites/Hell_beast/hell-beast-breath4.png')
    ]
# SETS FPS
clock = pygame.time.Clock()

class Box_Object():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.collisionbox = (self.x, self.y, 64, 68)
        
    def draw(self, window):
        self.collisionbox = (self.x, self.y, 64, 68)
        #pygame.draw.rect(window, (255, 0, 0), self.collisionbox, 2)

class Player():
    """
    PLAYER CLASS TO DEFINE POSITION AND MOVEMENT
    """
    def __init__(self, x, y , width, height):
        self.x = x
        self.y = y
        self. width = width
        self. height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.isJump = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.level = 0
        self.visible = True
        self.health = 10
        
    def draw(self, window):
        """
        DRAW FUNCTION TO CLEAN UP CODE
        """
        #DRAW THE OBJECT TO THE SCREEN
        if self.walkCount + 1 >= 36:
            self.walkCount = 0
        if not (self.standing):
            if self.left:
                window.blit(walkLeft[self.walkCount//6], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                window.blit(walkRight[self.walkCount//6], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                window.blit(walkRight[0], (self.x, self.y))
            else:
                window.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 25, self.y + 10, 28, 84)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
    
    def hit(self):
        self.x = 60
        self.y = self.y
        self.walkCount = 0
        self.health -= 1
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        window.blit(text, (800/2 - text.get_width()/2, 250))
        i = 0
        while i < 1000:
            i += 1
            

        
            
    def healthgfx(self, healthnum):
        if self.health == 10:
            return window.blit(health_gfx[0] ,(0, 0))
        elif self.health == 9:
            return window.blit(health_gfx[1] ,(0, 0))
        elif self.health == 8:
            return window.blit(health_gfx[2] ,(0, 0))
        elif self.health == 7:
            return window.blit(health_gfx[3] ,(0, 0))
        elif self.health == 6:
            return window.blit(health_gfx[4] ,(0, 0))
        elif self.health == 5:
            return window.blit(health_gfx[5] ,(0, 0))
        elif self.health == 4:
            return window.blit(health_gfx[6] ,(0, 0))
        elif self.health == 3:
            return window.blit(health_gfx[7] ,(0, 0))
        elif self.health == 2:
            return window.blit(health_gfx[8] ,(0, 0))
        elif self.health == 1:
            return window.blit(health_gfx[9] ,(0, 0))
    
    def moving_level(self):
        if player.x > 800:
            self.x = 60
            self.y = self.y
            self.level += 1

class Projectile():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 12 * facing
    
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


class Enemy():
    walkLeft = [
        pygame.image.load('Sprites/e_goblin/L1E.png'),
        pygame.image.load('Sprites/e_goblin/L2E.png'),
        pygame.image.load('Sprites/e_goblin/L3E.png'),
        pygame.image.load('Sprites/e_goblin/L4E.png'),
        pygame.image.load('Sprites/e_goblin/L5E.png'),
        pygame.image.load('Sprites/e_goblin/L6E.png'),
        pygame.image.load('Sprites/e_goblin/L7E.png'),
        pygame.image.load('Sprites/e_goblin/L8E.png'),
        pygame.image.load('Sprites/e_goblin/L9E.png'),
        pygame.image.load('Sprites/e_goblin/L10E.png'),
        pygame.image.load('Sprites/e_goblin/L11E.png')
        ]
    
    walkRight = [
        pygame.image.load('Sprites/e_goblin/R1E.png'),
        pygame.image.load('Sprites/e_goblin/R2E.png'),
        pygame.image.load('Sprites/e_goblin/R3E.png'),
        pygame.image.load('Sprites/e_goblin/R4E.png'),
        pygame.image.load('Sprites/e_goblin/R5E.png'),
        pygame.image.load('Sprites/e_goblin/R6E.png'),
        pygame.image.load('Sprites/e_goblin/R7E.png'),
        pygame.image.load('Sprites/e_goblin/R8E.png'),
        pygame.image.load('Sprites/e_goblin/R9E.png'),
        pygame.image.load('Sprites/e_goblin/R10E.png'),
        pygame.image.load('Sprites/e_goblin/R11E.png')
        ]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.health = 10
        self.visible = True

    def draw(self, window):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            
            if self.vel > 0:
                window.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            else:
                window.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            self.hitbox = (self.x + 20, self.y, 28, 60)
            #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
            # MAKING HEALTHBAR FIRST IS RED SECONDS GREEN
            pygame.draw.rect(window, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(window, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False 
        print('HIT!')

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

class Hell_beast():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = True
        self.health = 340
        self.hitbox = (self.x, self.y, 28, 60)
        self.idle_movement = 0
        self.breath_timer = 0
            
    def draw(self, window):
        if self.health > 0:
            if self.idle_movement + 1 >= 36:
                self.idle_movement = 0
                self.breath_timer += 1
            self.idle_movement +=1
            if self.idle_movement > 0:
                window.blit(hell_beast[self.idle_movement//6], (self.x, self.y))

    
    def draw_breath(self, window):
        if self.health > 0:
            self.breath_timer += 1
            if self.breath_timer > 80:
                self.breath_timer = 0
            if self.breath_timer >= 10 and self.breath_timer < 40:
                window.blit(hell_beast_breath[self.breath_timer//10], (hell_beast1.x, hell_beast1.y))
            

        #     if self.idle_movement == 0:
        #         self.idle_movement += 1
        #         window.blit(hell_beast[0], (self.x, self.y))
        #     elif self.idle_movement == 1:
        #         window.blit(hell_beast[1], (self.x, self.y))
        #         self.idle_movement += 1
        #     elif self.idle_movement == 2:
        #         window.blit(hell_beast[2], (self.x, self.y))
        #         self.idle_movement += 1
        #     elif self.idle_movement == 3:
        #         window.blit(hell_beast[3], (self.x, self.y))
        #         self.idle_movement += 1
        #     elif self.idle_movement == 4:   
        #         window.blit(hell_beast[4], (self.x, self.y))
        #         self.idle_movement += 1
        #     elif self.idle_movement == 5:    
        #         window.blit(hell_beast[5], (self.x, self.y))
        #         self.idle_movement = 0
        # else:
        #    pass
            
# CREATE A PLAYER INSTANCE
player = Player(100, 415, 64, 64)
goblin = Enemy(250, 445, 64, 64, 700)
box = Box_Object(738, 432, 64, 68)
hell_beast1 = Hell_beast(500, 345, 80, 90)
shoot_timing = 0

def clear_enemys():
    goblin.visible = False

def redraw_level1():
    # FILL THE SCREEN SO THE IT DOSENT MAKE THOUSANDS OF IMAGES
    window.blit(bg, (0, 0))
    window.blit(clouds[1], (0, 0))
    window.blit(clouds[0], (0, 0))
    window.blit(enviroment[1] , (50, 0))
    window.blit(enviroment[0] , (500, 200))
    window.blit(enviroment[0] , (738 - 32, 432 - 68))
    window.blit(enviroment[0] , (738 -64, 432))
    box.draw(window)
    text = font.render(f'Score: {score}', 1, (0,0,0))
    window.blit(text, (650, 10))
    if player.visible == True:
        player.draw(window)
    goblin.draw(window)
    #DRAW BULLET TO WINDOW
    for bullet in bullets:
        bullet.draw(window)
    # UPDATE THE SCREEN FOR THE MOVEMENT
    player.healthgfx(player.health)
    pygame.display.update()

def redraw_level2():
        clear_enemys()
        window.blit(bg, (0, 0))
        window.blit(clouds[1], (0, 0))
        window.blit(clouds[0], (0, 0))
        text = font.render(f'Score: {score}', 1, (0,0,0))
        window.blit(text, (650, 10))
        hell_beast1.draw(window)
        if hell_beast1.health > 0 and hell_beast1.breath_timer > 10 and hell_beast1.breath_timer < 40:
            window.blit(clouds[1], (0, 0))
            window.blit(clouds[0], (0, 0))
            hell_beast1.draw_breath(window)
        player.draw(window)
        box.draw(window)
        for bullet in bullets:
            bullet.draw(window)
        pygame.display.update()

shootloop = 0
font = pygame.font.SysFont('comicsans', 30, True)
score = 0
# RUNNING THE LOOP FOR THE GAME // MAIN LOOP
run = True
# LIST FOR BULLETS
bullets = []
while run:
    clock.tick(60)
    player.moving_level()
    
    #if (player.hitbox[1] < box.collisionbox[1] + box.collisionbox[3]
   #     and player.hitbox[1] + player.hitbox[3] > box.collisionbox[1]):
  #      if (player.hitbox[0] + player.hitbox[2] > box.collisionbox [0]
 #           and player.hitbox[0] < box.collisionbox[0] + box.collisionbox[2]):
#            box.collide()

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
    if keys[pygame.K_a] and player.x > 1:
        player.x -= player.vel
        player.left = True
        player.right = False
        player.standing = False
    elif keys[pygame.K_d]:
        player.x += player.vel
        player.right = True
        player.left = False
        player.standing = False
    else:
        player.standing = True
        player.walkCount = 0

    if not (player.isJump):
        #if keys[pygame.K_UP] and y > vel:
        #    y -= vel
        #if keys[pygame.K_DOWN] and y < 1000 - height - vel:
        #    y += vel
        if keys[pygame.K_UP]:
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
        hell_beast1.breath_timer += 1
        
pygame.quit()