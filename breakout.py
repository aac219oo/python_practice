import pygame as pg
import random
import math
import time

# 初始化
pg.init()
screen_width, screen_height = 800, 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("小球彈跳進階版")
font = pg.font.Font("C:/Windows/Fonts/msjh.ttc", 22)  # Windows 微軟正黑體
clock = pg.time.Clock()

# 顏色設定
WHITE = (255, 255, 255)


# 倒數計時設定
start_time = time.time()
total_time = 30  # 秒
base_speed = 3

# Ball 類別
class Ball:
    def __init__(self):
        self.surface = pg.Surface((40, 40), pg.SRCALPHA)
        pg.draw.circle(self.surface,(random.randint(0,255),random.randint(0,255),random.randint(0,255)), (20, 20), 20)
        self.rect = self.surface.get_rect()
        self.rect.center = (random.randint(100, 700), random.randint(100, 500))
        angle = random.uniform(20, 70)
        rad = math.radians(angle)
        self.dx = base_speed * math.cos(rad)
        self.dy = -base_speed * math.sin(rad)

    def update(self, speed_factor):
        self.rect.x += self.dx * speed_factor
        self.rect.y += self.dy * speed_factor

        # 邊界反彈
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.dx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.dy *= -1

    def draw(self):
        screen.blit(self.surface, self.rect.topleft)

# 初始化球列表
balls = [Ball() for _ in range(5)]  # 初始 5 顆球

# 主迴圈
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    # 計算剩餘時間與加速倍率
    elapsed = time.time() - start_time
    remain_time = max(0, int(total_time - elapsed))
    speed_factor = 1 + (1 - remain_time / total_time) * 2  # 最後速度最多變為 3 倍

    # 處理事件
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if len(balls) <= 10:
                balls.append(Ball())  # 點擊滑鼠左鍵新增一顆球

    # 更新並繪製每顆球
    for ball in balls:
        ball.update(speed_factor)
        ball.draw()

    # 顯示倒數時間與球數
    timer_text = font.render(f"剩餘時間：{remain_time} 秒", True, (0, 0, 0))
    count_text = font.render(f"球數：{len(balls)}", True, (0, 0, 0))
    screen.blit(timer_text, (20, 20))
    screen.blit(count_text, (20, 60))

    pg.display.update()

    if remain_time <= 0:
        running = False

# 遊戲結束畫面
screen.fill(WHITE)
end_text = font.render("遊戲結束！", True, (255, 0, 0))
screen.blit(end_text, (screen_width // 2 - 80, screen_height // 2))
pg.display.update()
pg.time.wait(1000)

pg.quit()