import pygame
from utils import *

width0 = 0
current_level = 0
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


# ------------------------------------------------------- Player Class -----------------------------------
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
        self.level = current_level
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
        if  self.x > 800:
            self.x = 60
            self.y = self.y
            self.level += 1


# ------------------------------------------------- Projectile Class ----------------------------------------
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


# ------------------------------------------------- Goblin Class --------------------------------------------
class Enemy():
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
                window.blit(walkRightgoblin[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            else:
                window.blit(walkLeftgoblin[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            self.hitbox = (self.x + 20, self.y, 28, 60)
            #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
            # MAKING HEALTHBAR FIRST IS RED SECONDS GREEN
            pygame.draw.rect(window, (255,0,0), (self.hitbox[0],
            self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(window, (0,255,0), (self.hitbox[0],
            self.hitbox[1]- 20, 50 - (5 * (10 - self.health)), 10))
            
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

# ----------------------------------------------- Hell beast class -----------------------------------------
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
            self.idle_movement +=1
            if self.idle_movement > 0:
                window.blit(hell_beast[self.idle_movement//6], (self.x, self.y))

    
    def draw_breath(self, window):
        if self.health > 0:
            if self.breath_timer + 1 > 1000:
                self.breath_timer = 0
            if self.breath_timer > 10 and self.breath_timer < 40:
                window.blit(hell_beast_breath[self.breath_timer//10],
                            (self.x, self.y))
                self.breath_timer += 1
            else:
                self.draw(window)
                self.breath_timer += 1
        print(self.breath_timer)
        
player = Player(100, 415, 64, 64)
goblin = Enemy(250, 445, 64, 64, 700)
box = Box_Object(738, 432, 64, 68)
hell_beast1 = Hell_beast(500, 345, 80, 90)

def clear_enemys():
    # Clear all enemys on screen
    goblin.visible = False

# ----------------------------------------------------- Draw Level 1 ------------------------------------------
def redraw_level1():
    # (image, (width, height))
    window.blit(bg, (0, 0))
    window.blit(clouds[1], (0, 0))
    window.blit(clouds[0], (0, 0))
    window.blit(enviroment[1] , (50, 0))
    window.blit(enviroment[0] , (500, 200))
    window.blit(enviroment[0] , (738 - 32, 432 - 68))
    window.blit(enviroment[0] , (738 -64, 432))
    box.draw(window)
    if player.visible == True:
        player.draw(window)
    goblin.draw(window)
    #DRAW BULLET TO WINDOW
    for bullet in bullets:
        bullet.draw(window)
    # UPDATE THE SCREEN FOR THE MOVEMENT
    player.healthgfx(player.health)
    if player.health <= 0:
        window.blit(g_over, (0,0))
    pygame.display.update()

# ---------------------------------------------------- Draw level 2 ---------------------------------------------
def redraw_level2():
        # (image, (width, height))
        clear_enemys()
        window.blit(bg, (0, 0))
        window.blit(clouds[1], (0, 0))
        window.blit(clouds[0], (0, 0))
        hell_beast1.draw(window)
        if hell_beast1.health > 0 and hell_beast1.breath_timer > 20 and hell_beast1.breath_timer < 80:
            window.blit(clouds[1], (0, 0))
            window.blit(clouds[0], (0, 0))
            hell_beast1.draw_breath(window)
        player.draw(window)
        box.draw(window)
        for bullet in bullets:
            bullet.draw(window)
        if player.health <= 0:
            window.blit(g_over, (0,0))
        hell_beast1.breath_timer += 1
        pygame.display.update()