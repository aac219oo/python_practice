import pygame as pg
import math

pg.init()
screen = pg.display.set_mode((640, 480))
pg.display.set_caption("平滑半圓")

bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255, 255, 255))

center = (320, 270)
radius = 60
points = []

# 生成從 0 到 π 的點（180 度）
for angle in range(0, 181, 5):  # 每 5 度取一點
    rad = math.radians(angle)
    x = center[0] + radius * math.cos(rad)
    y = center[1] - radius * math.sin(rad)  # 注意 y 軸方向要相反
    points.append((x, y))

# 畫半圓邊框（可以加厚度）
pg.draw.lines(bg, (0, 0, 0), False, points, 2)

# 如果想要實心半圓，補上底邊畫 polygon：
# pg.draw.polygon(bg, (0, 0, 0), [center] + points)

screen.blit(bg, (0, 0))
pg.display.flip()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit()
