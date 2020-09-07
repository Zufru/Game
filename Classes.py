# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 15:26:01 2020

@author: Tenkkeys
"""

import pygame
from utils import *
clockfps = 60
current_iomage = 0
time = 0
playerstart_x = 25
playerstart_y = 380
screen_width = 1000
screen_height = 600
window = pygame.display.set_mode((screen_width, screen_height))

# ------------------------------------------------------------------------------------------ DIALOGUE VARIABLES
chat_dialogue_size = (150, 400, 700, 150)
WHITE = (255, 255, 255)
GREY = (105, 105, 105)
BLACK = (0, 0, 0)
SILVER = (192, 192, 192)
convo_1S_xy = (295, 420) 
convo_2S_xy = (295, 445)
convo_3S_xy = (295, 470)
convo_4S_xy = (295, 495)
convo_5S_xy = (295, 520)
exit_PS_xy = (798, 535)
f_npc_icon_xy = (169, 422)

class Item():
    def __init__(self, name, x, y, width, height):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.collisionbox = (self.x, self.y, self.width, self.height)
        self.visible = True
        
    def draw(self, window):
        if self.visible:
            pygame.draw.rect(window, (255, 0, 0), self.collisionbox, 2)
        else:
            pass
        
    def __str__(self):
        return f'{name}'
# -------------------------------------------------------------------------------------------------- OBJECTS
class Object():
    def __init__(self, x, y, width, height, visible):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.visible = visible
        
    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
    
    def collide(self):
        player.y = self.hitbox[1] - player.height

# --------------------------------------------------------------------------------------------------------- NPC CLASS
class Npc_Female():
    def __init__(self, x, y, width, height, inConversation):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inConversation = False
        self.hitbox = (self.x + 45, self.y + 50, self.width - 15, self.height - 25)
        self.idle_movement = 0
        self.conversation_index = 0
        
    def draw(self, window):
        self.idle_movement += 1
        if self.idle_movement + 1 > 56:
            self.idle_movement = 0
        window.blit(female_npc_level1_left[self.idle_movement//9], (self.x, self.y))
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    
    def conversation(self, window):
        if self.inConversation:
            font1 = pygame.font.Font('misc/Fonts/SuperLegendBoy-4w8Y.ttf', 14)
            exit_font = pygame.font.Font('misc/Fonts/SuperLegendBoy-4w8Y.ttf', 10)
            exit_prompt = exit_font.render('Enter...', True, WHITE)
            if player.quest_index == 0:
                conversation1 = font1.render("Hello adventurer, havent seen anyone here in a while.", True, WHITE)
                conversation2 = font1.render("Hey while youre here do you mind getting back my ring?", True, WHITE)
                conversation3 = font1.render("It should be behind the demon guy over there.", True, WHITE)
                conversation4 = font1.render("Ill give you a nice helmet if you can bring it to me", True, WHITE)
                conversation5 = font1.render('next time we meet!', True, WHITE)
                pygame.draw.rect(window, BLACK, (chat_dialogue_size), 0)
                pygame.draw.rect(window, SILVER, (chat_dialogue_size), 5)
                window.blit(conversation1, (convo_1S_xy))
                window.blit(conversation2, (convo_2S_xy))
                window.blit(conversation3, (convo_3S_xy))
                window.blit(conversation4, (convo_4S_xy))
                window.blit(conversation5, (convo_5S_xy))
                window.blit(exit_prompt, (exit_PS_xy))
                window.blit(female_npc_chaticon, f_npc_icon_xy)
            if player.quest_index == 1 and 'Hannah\s Ring' not in player.inventory:
                return_without_ring = font1.render('You dont have my ring yet, return when you do.', True, WHITE)
                pygame.draw.rect(window, BLACK, (chat_dialogue_size), 0)
                pygame.draw.rect(window, SILVER, (chat_dialogue_size), 5)
                window.blit(exit_prompt, (exit_PS_xy))
                window.blit(female_npc_chaticon, (f_npc_icon_xy))
                window.blit(return_without_ring, (convo_1S_xy))
            if player.quest_index == 1 and 'Hannah\s Ring' in player.inventory:
                return_with_ring = font1.render('Hey you found my ring! Thanks!', True, WHITE)
                return_with_ring2 = font1.render('Heres something for your trouble', True, WHITE)
                reward = font1.render('+ WORKING', True, WHITE)
                pygame.draw.rect(window, BLACK, (chat_dialogue_size), 0)
                pygame.draw.rect(window, SILVER, (chat_dialogue_size), 5)
                window.blit(return_with_ring, (convo_1S_xy))
                window.blit(return_with_ring2, (convo_2S_xy))
                window.blit(exit_prompt, (exit_PS_xy))
                window.blit(female_npc_chaticon, (f_npc_icon_xy))
                window.blit(reward, (player.hitbox[0], player.hitbox[1] - 10))
                player.quest1_completed = 1
            if player.quest_index == 2:
                returning_after_quest = font1.render('Thanks for finding my ring!', True, WHITE)
                pygame.draw.rect(window, BLACK, (chat_dialogue_size), 0)
                pygame.draw.rect(window, SILVER, (chat_dialogue_size), 5)
                window.blit(female_npc_chaticon, (f_npc_icon_xy))
                window.blit(exit_prompt, (exit_PS_xy))
                window.blit(returning_after_quest, (convo_1S_xy))
                
# ------------------------------------------------------------------------------------------------------Door class 
class Door():
    def __init__(self, x, y, width, height, visible):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.visible = visible
        
    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
# ---------------------------------------------------------------------------------------------------- Player Class 
class Player():
    """
    PLAYER CLASS TO DEFINE POSITION AND MOVEMENT
    """
    def __init__(self, x, y , width, height):
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.vel = 5
        self.left = False
        self.right = False
        self.isJump = False
        self.damage = 1
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x, self.y, 38, 64)
        self.level = 1
        self.visible = True
        self.health = 5
        self.idle_counter = 0
        self.colliding = False
        self.blocking = False
        self.death_count = 0
        self.quest_index = 0
        self.inventory = []
        self.quest1_completed = 0
    
    def death(self, window):
        if self.health == 0:
            self.hitbox = (0, 0, 0, 0)
            self.death_count += 1
            if self.death_count +  1 > 40:
                window.blit(player_death[3], (self.x, self.y))
            elif self.death_count > 0:
                window.blit(player_death[self.death_count//10], (self.x, self.y))
            if self.death_count > 130:
                window.blit(g_over, (0,0))
            
    
    def draw(self, window):
        """
        DRAW FUNCTION TO CLEAN UP CODE
        """
        #DRAW THE OBJECT TO THE SCREEN
        if self.walkCount + 1 >= 40 and self.health > 0:
            self.walkCount = 0
        if not self.standing and self.health > 0:
            if self.left:
                window.blit(walkLeft[self.walkCount//10], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                window.blit(walkRight[self.walkCount//10], (self.x, self.y))
                self.walkCount += 1
        if self.standing and self.health > 0:
            if self.idle_counter + 1 > 32:
                self.idle_counter = 0
            if self.idle_counter >= 0 and self.right:
                window.blit(char[self.idle_counter//8], (self.x, self.y))
                self.idle_counter += 1
            if self.idle_counter >= 0 and self.left:
                window.blit(charL[self.idle_counter//8], (self.x, self.y))
                self.idle_counter += 1
        self.hitbox = (self.x + 5, self.y + 1, 47, 64)
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
    
    def hit(self):
        self.health -= 1
        if self.health >= 1:
            self.x = self.x - 30
            self.y = self.y
            self.walkCount = 0
        else:
            pass

    def healthgfx(self, healthnum):
        if self.health == 5:
            window.blit(health_gfx[5] ,(0, 5))
        elif self.health == 4:
            window.blit(health_gfx[4] ,(0, 5))
        elif self.health == 3:
             window.blit(health_gfx[3] ,(0, 5))
        elif self.health == 2:
            window.blit(health_gfx[2] ,(0, 5))
        elif self.health == 1:
            window.blit(health_gfx[1] ,(0, 5))
    
    def moving_level(self):
        if  self.x > 940 and player.level == 1:
            self.level = 2
            self.x = playerstart_x
            self.y = playerstart_y
        if self.x < 5 and player.level == 2:
            self.level = 1
            self.x = 870
            self.y = 480
# -------------------------------------------------------------------------------------------- Projectile Class
class Projectile():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 12 * facing
        self.travel_speed = 0
        self.shot_speed = 0
    
    def draw(self, window):
        if self.travel_speed + 1 > 54:
            self.travel_speed = 0
        if self.travel_speed > 0:
            window.blit(energy_ball_player[self.travel_speed//6], (self.x, self.y))
        #pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
        self.travel_speed +=1
        
# ---------------------------------------------------------------------------------------------- Goblin Class
class Goblin():
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
            self.hitbox[1] - 20, 50, 5))
            pygame.draw.rect(window, (0,255,0), (self.hitbox[0],
            self.hitbox[1]- 20, 50 - (5 * (10 - self.health)), 5))
            
    def hit(self):
        if self.health > 0:
            self.health -= player.damage
        elif self.health == 0:
            self.visible = False

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
                
# ------------------------------------------------------------------------------------------------- MASKED ENEMY
class Masked_Enemy(Goblin):
    def __init__(self, x, y, width, height, end):
        super().__init__(x, y, width, height, end)
        self.health = 23
        self.visible = True
        self.hitCounter = 0
        
    def draw(self, window):
        self.move()
        if self.visible:
            if self.walkCount + 1 > 42:
                self.walkCount = 0
            if self.vel > 0:
                window.blit(masked_enemy_walkRight[self.walkCount//7], (self.x, self.y))
                self.walkCount +=1
            else:
                window.blit(masked_enemy_walkLeft[self.walkCount//7], (self.x, self.y))
                self.walkCount += 1
            self.hitbox = (self.x, self.y, self.width, self.height)
            pygame.draw.rect(window, (255,0,0), (self.hitbox[0],
            self.hitbox[1] - 20, 50, 5))
            pygame.draw.rect(window, (0,255,0), (self.hitbox[0],
            self.hitbox[1]- 20, 50 - (5 * (10 - self.health)), 5))
    def hit(self):
        if self.health > 0:
            self.health -= player.damage
        elif self.health == 0:
            self.visible = False
# ------------------------------------------------------------------------------------------------ HELL BEAST CLASS
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
        self.breath_start = 20
        self.breath_finish = 80
        self.display_fps = 20
        self.reset_rotation_breath = 300
        self.idle_movement_displayfps = 10
        self.idle_movement_start = 0
        self.reset_idle_rotation = 60
        self.breathing = False
        
    def draw(self, window):
        if self.health > 0:
            if self.idle_movement + 1 >= self.reset_idle_rotation:
                self.idle_movement = 0
            self.idle_movement +=1
            if self.idle_movement > self.idle_movement_start:
                window.blit(hell_beast[self.idle_movement//
                                       self.idle_movement_displayfps],
                            (self.x, self.y))

    
    def draw_breath(self, window):
        if self.health > 0:
            if self.breath_timer + 1 > self.reset_rotation_breath:
                self.breath_timer = 0
            if (self.breath_timer > self.breath_start
                and self.breath_timer < self.breath_finish):
                self.breathing = True
                window.blit(hell_beast_breath
                            [self.breath_timer//self.display_fps],
                            (self.x, self.y))
                self.breath_timer += 1
            else:
                self.draw(window)
                self.breath_timer += 1


class Torch_ani():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.movement = 0
    
    def draw(self, window):
        self.movement += 1
        if self.movement + 1 > 42:
            self.movement = 0
        if self.movement >= 0:
            window.blit(torchesfire1[self.movement//6], (self.x, self.y))
            
# ------------------------------------------------------------------------------------------- MONSTER//NPC//PLAYER
player = Player(playerstart_x, playerstart_y, 64, 64)
player_level2 = Player(5, 515 - 64, 64, 64)
goblin = Goblin(400, 405, 64, 64, 780)
hell_beast1 = Hell_beast(850, 400, 80, 90)
f_npc_level1 = Npc_Female(205, 143, 64, 64, False)
masked_enemy1 = Masked_Enemy(175, 480, 60, 60, 780)
masked_enemy2 = Masked_Enemy(480, 220, 60, 60, 900)
# ------------------------------------------------------------------------------------------------- ITEMS
hannahs_ring = Item('Hannah\s Ring', 930, 230, 32, 32)
# ------------------------------------------------------------------------------------------------- LEVEL ONE
concrete_woodbridge_level1 = Object(2, 512, 230, 60, True)
stairsup1_level1 = Object(243, 506, 40, 30, True)
stairsup2_level1 = Object(293, 475, 40, 23, True)
stairsup3_level1 = Object(343, 462, 40, 30, True)
pillar1_level1 = Object(387, 440, 35, 30, True)
pillar2_level1 = Object(431, 440, 38, 30, True)
pillar3_level1 = Object(580, 443, 35, 30, True)
pillar4_level1 = Object(630, 443, 35, 30, True)
pillar5_level1 = Object(780, 443, 35, 30, True)
platform1_level1 = Object(482, 443, 35, 30, True)
platform2_level1 = Object(530, 443, 35, 30, True)
platform3_level1 = Object(680, 443, 35, 30, True)
platform4_level1 = Object(730, 443, 35, 30, True)
floor1_level1 = Object(850, 560, 150, 50, True)
floor2_level1 = Object(2, 230, 150, 50, True)
floor3_level1 = Object(152, 230, 150, 50, True)
torchani_level1 = Torch_ani(883, 515, 10, 20)
entrydoor_level1 = Door(860, 452, 70, 105, True)
# # ------------------------------------------------------------------------------------------------ LEVEL TWO  
floor1_level2 = Object(2, 560, 150, 50, True)
floor2_level2 = Object(152, 550, 150, 50, True)
floor3_level2 = Object(304, 550, 150, 50, True)
floor4_level2 = Object(456, 550, 150, 50, True)
floor5_level2 = Object(606, 550, 150, 50, True)
floor6_level2 = Object(758, 550, 150, 50, True)
floor7_level2 = Object(910, 550, 150, 50, True)
floor8_level2 = Object(910, 300, 150, 50, True)
floor9_level2 = Object(758, 300, 150, 50, True)
floor10_level2 = Object(606, 300, 150, 50, True)
floor11_level2 = Object(456, 300, 150, 50, True)
door_up_a_level = Object(5, 452, 70, 105, True)
door_down_a_level = Object(478, 190, 70, 105, True)
def clear_enemys():
    # Clear all enemys on screen
    goblin.visible = False

# ------------------------------------------------------------------------------------------------- DRAW LEVEL 1
def redraw_level1_clean():
    pygame.display.update()
    
def redraw_level1():
    # (image, (width, height))
    masked_enemy1.visible = False
    window.blit(bg, (0, 0))
    window.blit(props[2], (concrete_woodbridge_level1.x, concrete_woodbridge_level1.y))
    window.blit(props[3], (stairsup1_level1.x, stairsup1_level1.y))
    window.blit(props[4], (stairsup2_level1.x, stairsup2_level1.y))
    window.blit(props[5], (stairsup3_level1.x, stairsup3_level1.y))
    window.blit(props[6], (pillar1_level1.x, pillar1_level1.y))
    window.blit(props[7], (pillar2_level1.x, pillar2_level1.y))
    window.blit(props[9], (platform1_level1.x, platform1_level1.y))
    window.blit(props[9], (platform2_level1.x, platform2_level1.y))
    window.blit(props[10], (pillar3_level1.x, pillar3_level1.y))
    window.blit(props[11], (pillar4_level1.x, pillar4_level1.y))
    window.blit(props[12], (platform3_level1.x, platform3_level1.y))
    window.blit(props[13], (platform4_level1.x, platform4_level1.y))
    window.blit(props[14], (pillar5_level1.x, pillar5_level1.y))
    window.blit(props[15], (floor1_level1.x, floor1_level1.y))
    window.blit(props[15], (floor2_level1.x, floor2_level1.y))
    window.blit(props[15], (floor3_level1.x, floor3_level1.y))
    window.blit(doors[0], (entrydoor_level1.x, entrydoor_level1.y))
    window.blit(doors[0], (30, 120))
    if f_npc_level1.inConversation == True:
        f_npc_level1.conversation(window)
    torchani_level1.draw(window)
    window.blit(torches[0], (879, 530))
    if player.visible == True:
        player.draw(window)
    goblin.draw(window)
    f_npc_level1.draw(window)
    #DRAW BULLET TO WINDOW
    for bullet in bullets:
        bullet.draw(window)
    if player.health == 0:
        player.death(window)
    # UPDATE THE SCREEN FOR THE MOVEMENT
    player.healthgfx(player.health)
    pygame.display.update()

# ----------------------------------------------------------------------------------------------- DRAW LEVEL 2
def redraw_level2():
        # (image, (width, height))
        if player.level == 2:
            clear_enemys()
            window.blit(bg, (0, 0))
            # hell_beast1.draw(window)
            # if (hell_beast1.health > 0 and hell_beast1.breath_timer > 20 
            #     and hell_beast1.breath_timer < 80):
            #     window.blit(bg, (0, 0))
            #     hell_beast1.draw_breath(window)
            window.blit(props[15], (floor1_level2.x, floor1_level2.y))
            window.blit(props[15], (floor2_level2.x, floor2_level2.y))
            window.blit(props[15], (floor3_level2.x, floor3_level2.y))
            window.blit(props[15], (floor4_level2.x, floor4_level2.y))
            window.blit(props[15], (floor5_level2.x, floor5_level2.y))
            window.blit(props[15], (floor6_level2.x, floor6_level2.y))
            window.blit(props[15], (floor7_level2.x, floor7_level2.y))
            window.blit(doors[0], (door_up_a_level.x, door_up_a_level.y))
            window.blit(props[15], (floor8_level2.x, floor8_level2.y))
            window.blit(props[15], (floor9_level2.x, floor9_level2.y))
            window.blit(props[15], (floor10_level2.x, floor10_level2.y))
            window.blit(props[15], (floor11_level2.x, floor11_level2.y))
            window.blit(doors[0], (door_down_a_level.x, door_down_a_level.y))
            if hannahs_ring.visible:
                window.blit(game_items[0], (hannahs_ring.x, hannahs_ring.y))
            if player.visible == True:
                player.draw(window)
            for bullet in bullets:
                bullet.draw(window)
            if masked_enemy1.health > 0:
                masked_enemy1.visible = True
                masked_enemy1.draw(window)
            if masked_enemy2.health > 0:
                masked_enemy2.visible = True
                masked_enemy2.draw(window)
            # hell_beast1.breath_timer += 1
            player.healthgfx(player.health)
            if player.health == 0:
                player.death(window)
            pygame.display.update()

# ---------------------------------------------------------------------------------------------------- COLLISION
def object_collision(object_var):
    if (player.hitbox[1] < object_var.hitbox[1] + object_var.hitbox[3]
    and player.hitbox[1] + player.hitbox[3] > object_var.hitbox[1]):
        if(player.hitbox[0] + player.hitbox[2] > object_var.hitbox[0]
        and player.hitbox[0] < object_var.hitbox[0] + object_var.hitbox[2]):
            Object.collide(object_var)
            player.colliding = True
    if not (player.hitbox[1] < object_var.hitbox[1] + object_var.hitbox[3]
    and player.hitbox[1] + player.hitbox[3] > object_var.hitbox[1]):
        if(player.hitbox[0] + player.hitbox[2] > object_var.hitbox[0]
        and player.hitbox[0] < object_var.hitbox[0] + object_var.hitbox[2]):
            player.colliding = False

def door_collision_check(door_class):
    if (player.hitbox[1] < door_class.hitbox[1] + door_class.hitbox[3]
    and player.hitbox[1] + player.hitbox[3] > door_class.hitbox[1]):
        if(player.hitbox[0] + player.hitbox[2] > door_class.hitbox[0]
        and player.hitbox[0] < door_class.hitbox[0] + door_class.hitbox[2]):
            return True
# ------------------------------------------------------------------------------------------------ NPC DIALOGUE HITBOX
def female_NPC_collision_check(NPC):
    if (player.hitbox[1] < NPC.hitbox[1] + NPC.hitbox[3]
    and player.hitbox[1] + player.hitbox[3] > NPC.hitbox[1]):
        if(player.hitbox[0] + player.hitbox[2] > NPC.hitbox[0]
        and player.hitbox[0] < NPC.hitbox[0] + NPC.hitbox[2]):
            return True
        
# ----------------------------------------------------------------------------------------------- ITEM COLLISION
def item_collision_check(item):
    if (player.hitbox[1] < item.collisionbox[1] + item.collisionbox[3]
    and player.hitbox[1] + player.hitbox[3] > item.collisionbox[1]):
        if(player.hitbox[0] + player.hitbox[2] > item.collisionbox[0]
        and player.hitbox[0] < item.collisionbox[0] + item.collisionbox[2]):
            return True
        
# ----------------------------------------------------------------------------------------------- ENEMY HITBOX FOR PLAYER
def enemy_hitbox_for_player(enemy):
    if enemy.visible == True:
        if (player.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3]
        and player.hitbox[1] + player.hitbox[3] > enemy.hitbox[1]):
            if (player.hitbox[0] + player.hitbox[2] > enemy.hitbox[0] 
            and player.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]):
                player.hit()
