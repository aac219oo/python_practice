import pygame as pg
import random
import sys

pg.init()

# 遊戲設定
width, height = 600, 400
block_size = 20
screen = pg.display.set_mode((width, height))
pg.display.set_caption("貪吃蛇")

clock = pg.time.Clock()
font = pg.font.SysFont(None, 35)

# 顏色
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

def draw_snake(snake_blocks):
    for block in snake_blocks:
        pg.draw.rect(screen, GREEN, pg.Rect(block[0], block[1], block_size, block_size))

def draw_food(pos):
    pg.draw.rect(screen, RED, pg.Rect(pos[0], pos[1], block_size, block_size))

def draw_message(text, color, y_offset=0):
    font = pg.font.Font("fonts/GenSenRounded2-B.ttc", 24)
    msg = font.render(text, True, color)
    text_rect = msg.get_rect(center=(width // 2, height // 2 + y_offset))
    screen.blit(msg, text_rect)

def show_start_screen():
    screen.fill(BLACK)
    draw_message("貪吃蛇", WHITE, -40)
    draw_message("按任意鍵開始遊戲", WHITE, 10)
    pg.display.update()

    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                waiting = False

def game_loop():
    x = width // 2
    y = height // 2
    dx, dy = 0, 0

    snake = [[x, y]]
    snake_length = 1

    food = [random.randrange(0, width, block_size), random.randrange(0, height, block_size)]

    running = True
    game_over = False

    while running:
        while game_over:
            screen.fill(BLACK)
            draw_message("你輸了！按 R 重玩 或 Q 離開", RED)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    game_over = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        running = False
                        game_over = False
                    if event.key == pg.K_r:
                        game_loop()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and dx == 0:
                    dx = -block_size
                    dy = 0
                elif event.key == pg.K_RIGHT and dx == 0:
                    dx = block_size
                    dy = 0
                elif event.key == pg.K_UP and dy == 0:
                    dy = -block_size
                    dx = 0
                elif event.key == pg.K_DOWN and dy == 0:
                    dy = block_size
                    dx = 0

        # 移動蛇頭
        x += dx
        y += dy
        new_head = [x, y]

        # 撞牆或撞自己
        if (
            x < 0 or x >= width or y < 0 or y >= height or
            new_head in snake
        ):
            game_over = True

        snake.insert(0, new_head)

        # 吃到食物
        if x == food[0] and y == food[1]:
            food = [random.randrange(0, width, block_size), random.randrange(0, height, block_size)]
            snake_length += 1
        else:
            snake.pop()

        screen.fill(BLACK)
        draw_snake(snake)
        draw_food(food)
        pg.display.update()

        clock.tick(10)

    pg.quit()
    sys.exit()

# 遊戲執行
show_start_screen()
game_loop()
