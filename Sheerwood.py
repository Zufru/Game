# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 15:26:01 2020

@author: Tenkkeys
"""

import pygame
from utils import  *
from Classes import *

# Initialize pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Sheerwood Forest")
clock = pygame.time.Clock()
cursor_select = 0
shoot_speed = 0
attack_speed = 1
shootloop = 0

def enemy_hitbox_collision(enemy):
        if (bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3]
        and bullet.y + bullet.radius > enemy.hitbox[1]):
            if (bullet.x + bullet.radius > enemy.hitbox[0] 
            and bullet.x - bullet.radius < enemy.hitbox[0]
            + enemy.hitbox[2] and enemy.visible == True):
            #hit_sfx.play()
                enemy.hit()
                bullets.pop(bullets.index(bullet))
                
# RUNNING THE LOOP FOR THE GAME // MAIN LOOP
run = False
# RUNNING THE TITLE SCREEN
title_screen_display = True
# ----------------------------------------------------------------------------------------------TITLE SCREEN 
starting = True
while starting:
    while title_screen_display:
        clock.tick(60)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                title_screen_display = False
        window.blit(title_screen_img, (0, 0))
        if keys[pygame.K_w]:
            cursor_select = 0
        if keys[pygame.K_s]:
            cursor_select = 1
        inInstructions = False
        select_cursor_font = pygame.font.Font('misc/Fonts/AncientModernTales-a7Po.ttf', 45)
        select_cursor_render = select_cursor_font.render('>', True, WHITE)
        title_font = pygame.font.Font('misc/Fonts/AncientModernTales-a7Po.ttf', 68)
        title = title_font.render('SHEERWOOD', True, WHITE)
        play_game_font = pygame.font.Font('misc/Fonts/AncientModernTales-a7Po.ttf', 34)
        pg_font_render = play_game_font.render('NEW GAME', True, WHITE)
        pg_font_renderGREY = play_game_font.render('NEW GAME', True, GREY)
        instructions_font = pygame.font.Font('misc/Fonts/AncientModernTales-a7Po.ttf', 34)
        instructions_font_render = instructions_font.render('INSTRUCTIONS', True, WHITE)
        instructions_font_renderGREY = instructions_font.render('INSTRUCTIONS', True, GREY)
        w_key_instructions = pygame.font.Font('misc/Fonts/AncientModernTales-a7Po.ttf', 23)
        w_ki = w_key_instructions.render('Press the W key to walk through doorways. (if elligible)', True, BLACK)
        a_key_instructions = pygame.font.Font('misc/Fonts/AncientModernTales-a7Po.ttf', 23)
        a_ki = a_key_instructions.render('Press the A key to walk to the left.', True, BLACK)
        d_key_instructions = pygame.font.Font('misc/Fonts/AncientModernTales-a7Po.ttf', 23)
        d_ki = d_key_instructions.render('Press the D key to walk to the right.', True, BLACK)
        e_key_instructions = pygame.font.Font('misc/Fonts/AncientModernTales-a7Po.ttf', 23)
        e_ki = e_key_instructions.render('Press the E key to interact with npcs and items.', True, BLACK)
        space_key_instructions = pygame.font.Font('misc/Fonts/AncientModernTales-a7Po.ttf', 23)
        space_ki = space_key_instructions.render('Press the SPACE key to attack.', True, BLACK)
        escape_key_instructions = pygame.font.Font('misc/Fonts/AncientModernTales-a7Po.ttf', 23)
        esc_ki = escape_key_instructions.render('Press ESC to return to Main Menu', True, BLACK)
        if cursor_select == 0:
            window.blit(title, (320, 100))
            window.blit(select_cursor_render, (380, 272))
            window.blit(pg_font_render, (410, 280))
            window.blit(instructions_font_renderGREY, (410, 340))
        if cursor_select == 1:
            window.blit(title, (320, 100))
            window.blit(select_cursor_render, (380, 332))
            window.blit(pg_font_renderGREY, (410, 280))
            window.blit(instructions_font_render, (410, 340))
        pygame.display.update()
        
        if cursor_select == 0 and keys[pygame.K_RETURN]:
            title_screen_display = False
            starting = False
            # player.level = 1
            run = True
        if cursor_select == 1 and keys[pygame.K_RETURN]:
                inInstructions = True
                title_screen_display = False
            
    while inInstructions:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inInstructions = False
                title_screen_display = False
        window.blit(title_screen_img, (0, 0))
        window.blit(instruction_scroll, (150, 20))
        window.blit(key_img_instructions[0], (210, 140))
        window.blit(w_ki, (265, 155))
        window.blit(key_img_instructions[1], (210, 200))
        window.blit(a_ki, (265, 215))
        window.blit(key_img_instructions[2], (210, 260))
        window.blit(d_ki, (265, 275))
        window.blit(key_img_instructions[4], (210, 320))
        window.blit(e_ki, (265, 335))
        window.blit(key_img_instructions[3], (210, 380))
        window.blit(space_ki, (365, 395))
        window.blit(esc_ki, (350, 450))
        pygame.display.update()
        if keys[pygame.K_ESCAPE]:
            inInstructions = False
            title_screen_display = True

# ------------------------------------------------------------------------------------ MAIN GAME // MAIN LOOP
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    player.moving_level()
    keys = pygame.key.get_pressed()
    if player.level == 1:
        object_collision(concrete_woodbridge_level1)
        object_collision(stairsup1_level1)
        object_collision(stairsup2_level1)
        object_collision(stairsup3_level1)
        object_collision(pillar1_level1)
        object_collision(pillar2_level1)
        object_collision(platform1_level1)
        object_collision(platform2_level1)
        object_collision(pillar3_level1)
        object_collision(pillar4_level1)
        object_collision(platform3_level1)
        object_collision(platform4_level1)
        object_collision(pillar5_level1)
        object_collision(floor1_level1)
        object_collision(floor2_level1)
        object_collision(floor3_level1)
    if player.level == 2:
        object_collision(floor1_level2)
        object_collision(floor2_level2)
        object_collision(floor3_level2)
        object_collision(floor4_level2)
        object_collision(floor5_level2)
        object_collision(floor6_level2)
        object_collision(floor7_level2)
        object_collision(floor8_level2)
        object_collision(floor9_level2)
        object_collision(floor10_level2)
        object_collision(floor11_level2)
    
    if not player.colliding:
        player.y += 20
# ----------------------------------------------------------------------------------------  fALLING OFF SCREEN
    if player.y > screen_height:
        player.x = playerstart_x
        player.y = playerstart_y
        player.health -= 1
# ---------------------------------------------------------------------------------------- DOOR COLLISION
    if (door_collision_check(entrydoor_level1) and keys[pygame.K_w]
        and player.level == 1):
        player.x = 10
        player.y = 160
        door_sfx.play()
    
    if (door_collision_check(door_up_a_level) and keys[pygame.K_w]
    and player.level == 2):
        player.x = 476
        player.y = 200
        door_sfx.play()
        
# ----------------------------------------------------------------------------------- NPC DIALOGUE/CHAT COLLISION CHECK 
    if female_NPC_collision_check(f_npc_level1) and keys[pygame.K_e]:
        ping_sound.play()
        f_npc_level1.inConversation = True
        pygame.display.update()
        
    if keys[pygame.K_RETURN] and female_NPC_collision_check(f_npc_level1):
        f_npc_level1.inConversation = False
        if player.quest_index == 0:
            player.quest_index = 1
        elif player.quest1_completed == 1:
            player.quest_index = 2
            
        
    # if hell_beast1.health > 0:
    #     hell_beast1.draw_breath(window)
        
# --------------------------------------------------------------------------------------ITEM COLLISION
    if item_collision_check(hannahs_ring) and keys[pygame.K_e]:
        hannahs_ring.visible = False
        player.inventory.append(hannahs_ring.name)
            
# ---------------------------------------------------------------------------------- CHECKING IS PLAYER IS HIT
    enemy_hitbox_for_player(goblin)
    enemy_hitbox_for_player(masked_enemy1)
    enemy_hitbox_for_player(masked_enemy2)
    
# ---------------------------------------------------------------------------------------- SPELLS/BULLETS 
    if shoot_speed > 0:
        shoot_speed +=1
    if shoot_speed > 25:
        shoot_speed = 0

    for bullet in bullets:
        #CHECK IF BULLET IS WITHIN THE ENEMY HITBOX AND REMOVE THE BULLET
        #AND PRINT HIT IF IT IS
        enemy_hitbox_collision(goblin)
        enemy_hitbox_collision(masked_enemy1)
        enemy_hitbox_collision(masked_enemy2)
                
        if bullet.x < screen_width and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))
    #SHOOTS THE BULLET
    if keys[pygame.K_SPACE] and not f_npc_level1.inConversation:
        #bullet_sfx.play()
        if player.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 3:
            bullets.append(Projectile(round(player.x + player.width // 2),
                                      round(player.y + player.height // 2),
                                      6, (0, 0, 0), facing))

# ------------------------------------------------------------------------------------------PLAYER MOVEMENT
    if keys[pygame.K_a] and player.health >= 1 and not f_npc_level1.inConversation:
        player.x -= player.vel
        player.left = True
        player.right = False
        player.standing = False
    elif keys[pygame.K_d] and player.health >= 1 and not f_npc_level1.inConversation:
        player.x += player.vel
        player.right = True
        player.left = False
        player.standing = False
    else:
        player.standing = True
        player.walkCount = 0

    # if not (player.isJump):
    #     if keys[pygame.K_UP] and player.health >= 1:
    #         player.isJump = True
    #         player.right = False
    #         player.left = False
    #         player.walkCount = 0
    # else:
    #     if player.jumpCount >= -10:
    #         neg = 1
    #         if player.jumpCount < 0:
    #             neg = -1
    #         player.y -= (player.jumpCount**2) / 2 * neg
    #         player.jumpCount -= 1

    #     else:
    #         player.isJump = False
    #         player.jumpCount = 10
    
# ------------------------------------------------------------------------------------- REDRAWING PLAYER CURRENT LEVEL
    if player.level == 1:
        redraw_level1()
    if player.level == 2:
        redraw_level2()

pygame.quit()
        #if keys[pygame.K_UP] and y > vel:
        #    y -= vel
        #if keys[pygame.K_DOWN] and y < 1000 - height - vel:
        #    y += vel
