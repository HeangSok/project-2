# Pygame template - skeleton for a new pygame project
import pygame
import board
import board_generator
import random
import button
import queue
import os
from collections import deque



# WIDTH = 360
# HEIGHT = 480
FPS = 30
# vec = pygame.math.Vector2
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (222, 161, 133)

# immutable variable
GAME_BOARD = board.Board
SPRITE = 25 # mean 25px per each index of the array
FRAME_PER_SECOND = 60
WIDTH = len(GAME_BOARD[0]) * SPRITE
HEIGHT = len(GAME_BOARD) * SPRITE


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH+250, HEIGHT))
pygame.display.set_caption("PacMan")
clock = pygame.time.Clock()

# read file
with open (os.path.join('asset', 'hight_score.txt')) as file:
    high_score = file.readline()

# upload all graphic
pacman_img = pygame.transform.scale(pygame.image.load(os.path.join('asset/images', 'pacman.png')), (
    23, 23))
pacman_img_close = pygame.transform.scale(pygame.image.load(os.path.join('asset/images', 'mouthclose.png')), (
    23, 23))
wall_img = pygame.transform.scale(pygame.image.load(os.path.join('asset/images', 'wall6.png')), (
    SPRITE, SPRITE)) # last use wall5

red_ghost_img = pygame.transform.scale(pygame.image.load(os.path.join('asset/images', 'redghost.png')), (
    20, 20))

orange_ghost_img = pygame.transform.scale(pygame.image.load(os.path.join('asset/images', 'orangeghost.png')), (
    20, 20))
cyan_ghost_img = pygame.transform.scale(pygame.image.load(os.path.join('asset/images', 'cyanghost.png')), (
    20, 20))
pink_ghost_img = pygame.transform.scale(pygame.image.load(os.path.join('asset/images', 'pinkghost.png')), (
    20, 20))
blue_ghost_img = pygame.transform.scale(pygame.image.load(os.path.join('asset/images', 'blue.png')), (
    20, 20))
pac_dot_img = pygame.transform.scale(pygame.image.load(os.path.join('asset/images', 'pac_dot.png')), (
    15, 10))
power_img = pygame.transform.scale(pygame.image.load(os.path.join('asset/images', 'power.png')), (
    23, 23))
logo_img = pygame.image.load(os.path.join('asset/images', 'Pac-Man.png')).convert()
logo1_img = pygame.transform.scale((pygame.image.load(os.path.join('asset/images', 'logo1.png')).convert()),(197,65))
play_button = pygame.image.load(os.path.join('asset/images', 'play button.png')).convert()
option_button = pygame.image.load(os.path.join('asset/images', 'Option button.png')).convert()
quit_button = pygame.image.load(os.path.join('asset/images', 'Quit button 2.png')).convert()
winner_bg =pygame.image.load(os.path.join('asset/images', 'winner_background.png')).convert()
original_maze_button = pygame.image.load(os.path.join('asset/images', 'original_maze1.png')).convert()
random_maze_button = pygame.image.load(os.path.join('asset/images', 'random_maze1.png')).convert()
original_maze_button.set_colorkey(BLACK)
random_maze_button.set_colorkey(BLACK)
explosion_animation = []
for i in range(1,12):
    file_name = f'tile{i}.png'
    img = pygame.image.load(os.path.join('asset/images', file_name)).convert()
    img.set_colorkey(BLACK)
    img = pygame.transform.scale(img, (25, 25))
    explosion_animation.append(img)

# define function

font_name = pygame.font.match_font("arial") # this command allow you to find generic font that you mentioned; it is useful for cross platforms
def draw_text(screen, text, font_size, x, y):
    font = pygame.font.Font(font_name, font_size) # set a font object
    text_surface = font.render(text, True, WHITE) # True here mean anti-alias
    text_rect = text_surface.get_rect()
    text_rect.x = x
    text_rect.y = y
    screen.blit(text_surface, text_rect)

def live_bar(screen, x, y, live):
    if live < 2:
        live = 0
    BAR_LENGTH = 70
    BAR_HEIGHT = 10
    fill = (live/100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y,fill, BAR_HEIGHT)
    pygame.draw.rect(screen, GREEN, fill_rect)
    pygame.draw.rect(screen, WHITE, outline_rect, 2)  # 2 is the thickness of the outline

def draw_lives(live):
    live_img = pygame.transform.scale(pygame.image.load(os.path.join('asset/images', 'pacman.png')), (
    18, 18))
    if live == 3:
        screen.blit(pacman_img, (WIDTH + 80, 30))
        screen.blit(pacman_img, (WIDTH + 80+25, 30))
        screen.blit(pacman_img,(WIDTH + 80+50, 30))
    elif player.lives == 2:
        screen.blit(pacman_img, (WIDTH + 80, 30))
        screen.blit(pacman_img, (WIDTH + 80+25, 30))
    elif player.lives == 1:
        screen.blit(pacman_img, (WIDTH + 80, 30))



def show_gameover_screen():
    screen.fill(BLACK)
    draw_text(screen,"Game Over!", 64, WIDTH/2-50, HEIGHT/4)
    draw_text(screen,"=> Press space to quit.", 22, WIDTH/2, HEIGHT/2)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    waiting =False
                    quit()

def show_winner_screen():
    screen.fill(BLACK)
    screen.blit(winner_bg,(70,450))
    draw_text(screen,"You Win!", 64, WIDTH/2, HEIGHT/4)
    draw_text(screen,"=> Press space to go back to the menu.", 22, WIDTH/2-60, HEIGHT/2)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    waiting =False
                    start_up()



# define class
class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = wall_img   # first mandatory
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()  # second mandatory
        self.rect.x = 0
        self.rect.x = 0

class PacDot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pac_dot_img  # first mandatory
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()  # second mandatory
        self.rect.x = x * SPRITE + 5
        self.rect.y = y * SPRITE + 10

    def update(self):
        pass

class PowerPellet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = power_img  # first mandatory
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()  # second mandatory
        self.rect.x = x * SPRITE
        self.rect.y = y * SPRITE

    def update(self):
        pass


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = explosion_animation[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 30


    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_animation):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_animation[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_origin = pacman_img  # use this technique when rotate many times
        self.image_origin.set_colorkey(BLACK)
        self.image = self.image_origin.copy()
        self.rect = self.image.get_rect()  # second mandatory
        self.rect.x = 14 * SPRITE
        self.rect.y = 23 * SPRITE
        self.speedx = 0  # pygame variable to move the object on x axis
        self.speedy = 0
        self.last_update = pygame.time.get_ticks()
        self.score = 0
        self.lives = 3
        self.pac_dot_sound = pygame.mixer.Sound(os.path.join('asset/music', 'eat.wav'))
        self.power_pellet_sound = pygame.mixer.Sound(os.path.join('asset/music', 'power_pellet.wav'))
        self.hide_timer = pygame.time.get_ticks()
        self.hidden = False

    def mouth_animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 80:
            self.last_update = now
            self.image_origin = pacman_img_close  # use this technique when rotate many times
            self.image_origin.set_colorkey(BLACK)

        else:
            self.image_origin = pacman_img  # use this technique when rotate many times
            self.image_origin.set_colorkey(BLACK)
    # def mouth_animation(self):
    #     now = pygame.time.get_ticks()
    #     if now - self.last_update > 80:
    #         self.last_update = now
    #         self.image_origin = pacman_img  # use this technique when rotate many times
    #         self.image_origin.set_colorkey(BLACK)
    #     else:
    #         self.image_origin = pacman_img_close  # use this technique when rotate many times
    #         self.image_origin.set_colorkey(BLACK)

    def eat_pac_dots(self):
        hit_pac_dots = pygame.sprite.spritecollide(player, pac_dots, True)
        if hit_pac_dots:
            self.score += 10
            self.pac_dot_sound.play()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH/2, HEIGHT + 300)

    def update(self):   # when u work with sprite and place the all_sprites.update() in while loop this function will update automatically
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 300:
            self.hidden= False
            self.rect.center = player_rect_center
        self.eat_pac_dots()
        self.mouth_animation()
        self.speedx = 0 # turn your speed to 0 here or the player keep running
        self.speedy = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -5
            new_image = pygame.transform.rotate(self.image_origin, 180)
            self.image = new_image

        if keystate[pygame.K_d]:
            self.speedx = +5
            new_image = pygame.transform.rotate(self.image_origin, 0)
            self.image = new_image

        if keystate[pygame.K_w]:
            self.speedy = -5
            new_image = pygame.transform.rotate(self.image_origin, 90)
            self.image = new_image

        if keystate[pygame.K_s]:
            self.speedy = + 5
            new_image = pygame.transform.rotate(self.image_origin, 270)
            self.image = new_image

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        collide_with_wall = pygame.sprite.groupcollide(player_sprite, walls, False, False)
        if collide_with_wall: # this if clause must be used immediately after detect the collision
            self.rect.x += -self.speedx
            self.rect.y += -self.speedy
            self.speedx = 0 # turn your speed to 0 here or the player keep running
            self.speedy = 0

        if self.rect.left > WIDTH: # make the player move back to the edge
            self.rect.right = 0 # make the player go to x = 0
        if self.rect.right < 0: # make the player move back to the edge
            self.rect.left = WIDTH # make the player go to x = WIDTH


class DummyGhost(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = orange_ghost_img  # first mandatory
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()  # second mandatory
        self.rect.x = random.randrange(11, 15) * SPRITE
        self.rect.y = random.randrange(13, 15) * SPRITE
        self.choices = [[-4,4], [-3,3]]
        self.choice = random.choice(self.choices)
        self.speedx = random.choice(self.choice) # pygame variable to move the dummy ghost on x axis
        self.speedy = random.choice(self.choice) # pygame variable to move the dummy ghost on y axis

    def update(self):
        self.rect.y += self.speedy  # move the ghost
        collide_with_wall = pygame.sprite.groupcollide(dummy_ghost,walls,False,False)
        if collide_with_wall:
            self.rect.y += -self.speedy  # stop the ghost
            self.rect.x += self.speedx  # move in new direction
            # self.speedy = random.choice(self.choice) # note: if you put it here, it wont work
            # self.speedx = random.choice(self.choice) # note: if you put it here, it wont work
            collide_with_wall = pygame.sprite.groupcollide(dummy_ghost,walls,False,False)
            if collide_with_wall:
                self.rect.x += -self.speedx
                self.speedy = random.choice(self.choice)
                self.speedx = random.choice(self.choice)


# class SmartGhost(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = orange_ghost_img  # first mandatory
#         self.image.set_colorkey(BLACK)
#         self.rect = self.image.get_rect()  # second mandatory
#         self.rect.x = random.randrange(11, 15) * SPRITE
#         self.rect.y = random.randrange(13, 15) * SPRITE
#         self.choices = [[-4, 4], [-3, 3]]
#         self.choice = random.choice(self.choices)
#         self.speedx = random.choice(self.choice)  # pygame variable to move the object on x axis
#         self.speedy = random.choice(self.choice)
#         self.starting_node = [self.rect.x, self.rect.y]
#         self.visited_nodes = []
#         self.ghosts_queue = queue.Queue()

#     def breath_first_search(self):
#         """Make all the smart ghosts chase after Pacman"""
#         pass


#     def update(self):
#         self.rect.y += self.speedy
#         collide_with_wall = pygame.sprite.groupcollide(smart_ghost, walls, False, False)
#         if collide_with_wall:
#             self.rect.y += -self.speedy
#             self.rect.x += self.speedx

#             collide_with_wall = pygame.sprite.groupcollide(smart_ghost, walls, False, False)
#             if collide_with_wall:
#                 self.rect.x += -self.speedx
#                 self.speedy = random.choice(self.choice)
#                 self.speedx = random.choice(self.choice)

class SmartGhost(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = orange_ghost_img  # first mandatory
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()  # second mandatory
        self.rect.x = random.randrange(11, 15) * SPRITE
        self.rect.y = random.randrange(13, 15) * SPRITE
        self.choices = [[-4, 4], [-3, 3]]
        self.choice = random.choice(self.choices)
        self.speedx = random.choice(self.choice)  # pygame variable to move the object on x axis
        self.speedy = random.choice(self.choice)
        self.starting_node = [self.rect.x, self.rect.y]
        self.visited_nodes = []
        self.ghosts_queue = queue.Queue()

    def bfs(self, start, target):
        queue = deque([start])
        visited = set([start])
        path = {start: None}

        while queue:
            current = queue.popleft()
            if current == target:
                break

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_cell = (current[0] + dx, current[1] + dy)
                if next_cell not in visited and self.is_valid_move(next_cell):
                    queue.append(next_cell)
                    visited.add(next_cell)
                    path[next_cell] = current

        return self.reconstruct_path(path, start, target)

    def is_valid_move(self, position):
        x, y = position
        if 0 <= x < len(GAME_BOARD[0]) and 0 <= y < len(GAME_BOARD):
            return GAME_BOARD[y][x] != 3  # Assuming 3 represents a wall
        return False

    def reconstruct_path(self, path, start, target):
        current = target
        path_to_follow = []

        while current != start:
            path_to_follow.append(current)
            current = path[current]

        path_to_follow.reverse()
        return path_to_follow

    def update(self):
        # Get Pac-Man's position (assuming player is your Pac-Man object)
        pacman_pos = (player.rect.x // SPRITE, player.rect.y // SPRITE)
        # Ghost's current position
        ghost_pos = (self.rect.x // SPRITE, self.rect.y // SPRITE)

        # Find path to Pac-Man
        path_to_pacman = self.bfs(ghost_pos, pacman_pos)

        # Move along the path
        if path_to_pacman and len(path_to_pacman) > 1:
            next_cell = path_to_pacman[1]  # Next cell in the path
            self.rect.x = next_cell[0] * SPRITE
            self.rect.y = next_cell[1] * SPRITE



# ---------------------------------music
pygame.mixer.music.load(os.path.join('asset/music', 'game_start.wav'))

death_sound_effect = pygame.mixer.Sound(os.path.join('asset/music', 'death.wav'))

def character():
    global all_sprites, player_sprite, player, player_rect_center, dummy_ghost, orange_ghost
    global orange_rect_center, cyan_ghost, cyan_rect_center, smart_ghost, red_ghost, red_rect_center
    global pink_ghost, pink_rect_center, walls, pac_dots, power_pellets
    # define sprite
    # ---------------------------------player

    all_sprites = pygame.sprite.Group()
    player_sprite = pygame.sprite.Group()
    player = Player()
    player_sprite.add(player)
    all_sprites.add(player)
    player_rect_center = player.rect.center

    # ---------------------------------dummy_ghost
    dummy_ghost = pygame.sprite.Group()
    orange_ghost = DummyGhost()
    orange_ghost.image = orange_ghost_img
    all_sprites.add(orange_ghost)
    dummy_ghost.add(orange_ghost)
    orange_rect_center = orange_ghost.rect.center

    cyan_ghost = DummyGhost()
    cyan_ghost.image = cyan_ghost_img
    all_sprites.add(cyan_ghost)
    dummy_ghost.add(cyan_ghost)
    cyan_rect_center = cyan_ghost.rect.center


    # ---------------------------------smart_ghost
    smart_ghost = pygame.sprite.Group()
    red_ghost = SmartGhost()
    red_ghost.image = red_ghost_img
    all_sprites.add(red_ghost)
    smart_ghost.add(red_ghost)
    red_rect_center = red_ghost.rect.center

    pink_ghost = SmartGhost()
    pink_ghost.image = pink_ghost_img
    all_sprites.add(pink_ghost)
    smart_ghost.add(pink_ghost)
    pink_rect_center = pink_ghost.rect.center


    # ---------------------------------wall

    walls = pygame.sprite.Group()
    for y, row in enumerate(GAME_BOARD):
        for x, block in enumerate(row):
            if block == 3:
                wall = Wall()
                wall.rect.x = x * SPRITE
                wall.rect.y = y * SPRITE
                walls.add(wall)
                all_sprites.add(wall)



    # ---------------------------------PacDot
    pac_dots = pygame.sprite.Group()
    for y, row in enumerate(GAME_BOARD):
        for x, block in enumerate(row):
            if block == 2:
                pac_dot = PacDot(x, y)
                pac_dots.add(pac_dot)
                all_sprites.add(pac_dot)

    # ---------------------------------PowerPallet
    power_pellets = pygame.sprite.Group()
    for y, row in enumerate(GAME_BOARD):
        for x, block in enumerate(row):
            if block == 6:
                power_pellet = PowerPellet(x, y)
                power_pellets.add(power_pellet)
                all_sprites.add(power_pellet)





# Game loop
# todo:--------------------------------------------------
def game():
    character()
    vulnerable_state = False
    time_check_point = 0
    running = True
    pygame.mixer.music.play()
    while running:

        # keep loop running at the right speed
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        current_time = pygame.time.get_ticks()
        collide_with_power_pellet = pygame.sprite.spritecollide(player,power_pellets,True)
        if collide_with_power_pellet:   # Ghost become vulnerable and turn blue
            time_check_point = pygame.time.get_ticks()
            player.score += 50
            player.power_pellet_sound.play()
            vulnerable_state = True
            red_ghost.image = blue_ghost_img
            pink_ghost.image = blue_ghost_img
            orange_ghost.image = blue_ghost_img
            cyan_ghost.image = blue_ghost_img

        if vulnerable_state and current_time - time_check_point > 2500:  # 2500 = 2.5s
            vulnerable_state = False  # after 2.5 second, the ghost will become normal and turn back to its original color
            red_ghost.image = red_ghost_img
            pink_ghost.image = pink_ghost_img
            orange_ghost.image = orange_ghost_img
            cyan_ghost.image = cyan_ghost_img

        print(f"curr: {current_time},   => checkin time: {time_check_point}" )
        collide_with_dummyghost = pygame.sprite.spritecollide(player, dummy_ghost, False)
        if collide_with_dummyghost and vulnerable_state:
            for hit in collide_with_dummyghost:
                hit.rect.center = orange_rect_center
                player.score += 200
        elif collide_with_dummyghost:
            death_sound_effect.play()
            for hit in collide_with_dummyghost:
                explosion = Explosion(hit.rect.center)
                all_sprites.add(explosion)
                player.hide()
                red_ghost.rect.center = red_rect_center
                pink_ghost.rect.center = pink_rect_center
                orange_ghost.rect.center = orange_rect_center
                cyan_ghost.rect.center = cyan_rect_center
                # player.rect.center = player_rect_center
                player.lives -= 1

        collide_with_smartghost = pygame.sprite.spritecollide(player, smart_ghost, False)
        if collide_with_smartghost and vulnerable_state:
            for hit in collide_with_smartghost:
                hit.rect.center = red_rect_center
                player.score += 200
        elif collide_with_smartghost:
            death_sound_effect.play()
            for hit in collide_with_smartghost:
                explosion = Explosion(hit.rect.center)
                all_sprites.add(explosion)
                player.hide()
                red_ghost.rect.center = red_rect_center
                pink_ghost.rect.center = pink_rect_center
                orange_ghost.rect.center = orange_rect_center
                cyan_ghost.rect.center = cyan_rect_center
                # player.rect.center = player_rect_center
                player.lives -= 1

        if player.lives == 0:
            show_gameover_screen()

        if len(pac_dots) == 0 and len(power_pellets) == 0:
            show_winner_screen()

        # Update
        all_sprites.update()
        # draw/render
        screen.fill(BLACK)
        all_sprites.draw(screen)
        draw_text(screen, f"Level: 01", 18, WIDTH + 25, 5)
        draw_text(screen, f"Lives: ", 18, WIDTH + 25, 30)
        # live_bar(screen, WIDTH + 80, 35, player.lives)
        draw_text(screen, f"Score: {player.score}", 18, WIDTH + 25, 55)
        draw_text(screen, f"High Score: {high_score}", 18, WIDTH + 25, 80)
        draw_lives(player.lives)

        # *after* drawing everything, flip the display
        pygame.display.flip()

    pygame.quit()

# todo:--------------------------------------------------

def maze_configuration():
    global GAME_BOARD
    running = True
    click = False
    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        screen.fill(BLACK)
        pos = pygame.mouse.get_pos()
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True


        origin_button = original_maze_button.get_rect()
        origin_button.x, origin_button.y = (WIDTH + 50) // 2, 300
        random_button = random_maze_button.get_rect()
        random_button.x, random_button.y = (WIDTH + 50) // 2, 400
        if origin_button.collidepoint(pos): #play_button
            if click:
                game()
                click = False
        elif random_button.collidepoint(pos): #option_button
            if click:
                GAME_BOARD = board_generator.random_board
                game()
                click = False

        # render
        screen.blit(original_maze_button, (origin_button.x, origin_button.y))
        screen.blit(random_maze_button, (random_button.x, random_button.y))
        pygame.display.flip()

    pygame.quit()


def start_up():
    running = True
    click = False
    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        screen.fill(BLACK)
        pos = pygame.mouse.get_pos()
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        pb = play_button.get_rect()
        pb.x, pb.y = (WIDTH + 100) // 2, 430+25+35
        ob = option_button.get_rect()
        ob.x, ob.y = (WIDTH + 100) // 2, 520+25+35
        qb = quit_button.get_rect()
        qb.x, qb.y = (WIDTH + 100) // 2, 610+25+35
        if pb.collidepoint(pos): #play_button
            if click:
                game()
                click = False
        elif ob.collidepoint(pos): #option_button
            if click:
                maze_configuration()
                click = False
        elif qb.collidepoint(pos): #quit_button
            if click:
                quit()
                click = False
        # render/draw
        screen.blit(logo1_img, ((WIDTH + 80) // 2, 5+25))
        screen.blit(logo_img,((WIDTH + 80)//2, 75+25))
        screen.blit(play_button, (pb.x, pb.y))
        screen.blit(option_button, (ob.x, ob.y))
        screen.blit(quit_button, (qb.x, qb.y))
        draw_text(screen, f"Title: ", 20, (WIDTH + 80)//2, 285+25)
        draw_text(screen, f"YEAR:", 20, (WIDTH + 80)//2, 285+25+35)
        draw_text(screen, f"COURSE:", 20, (WIDTH + 80) // 2, 320+25+35)
        draw_text(screen, f"NAME:", 20, (WIDTH + 80) // 2, 355+25+35)
        draw_text(screen, f"SNUMBER:", 20, (WIDTH + 80) // 2, 390+25+35)
        draw_text(screen, f"Assignment 1", 20, (WIDTH + 330) // 2, 285 + 25)
        draw_text(screen, f"2021", 20, (WIDTH + 340)//2, 285+25+35)
        draw_text(screen, f"7805ICT", 20, (WIDTH + 340) // 2, 320+25+35)
        draw_text(screen, f"Heang_Sok", 20, (WIDTH + 340) // 2, 355+25+35)
        draw_text(screen, f"s5204340", 20, (WIDTH + 340) // 2, 390+25+35)

        pygame.display.flip()

    pygame.quit()

start_up()
