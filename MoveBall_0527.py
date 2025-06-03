import pygame as pg
import random
import time
import ctypes
import json
import os
# 初始化
pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("PyGame 小遊戲")
clock = pg.time.Clock()
font = pg.font.Font("C:/Windows/Fonts/msjh.ttc", 24)
large_font = pg.font.Font("C:/Windows/Fonts/msjh.ttc", 56)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,80,80,255)
BLUE = (90,90,255,255)

# 遊戲邊界範圍
boundary_rect = pg.Rect(10, 100, 780, 490)
boundary_rect_border = 5

# 載入背景
background_img = pg.image.load("images/moveball/background.jpg").convert()
bg_resized  = pg.transform.scale(background_img, (boundary_rect.width - boundary_rect_border*2, boundary_rect.height - boundary_rect_border*2))

# 紀錄最高分排名
HIGHSCORE_FILE = "json/highscores.json"

def load_highscores():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_highscores(highscores):
    with open(HIGHSCORE_FILE, "w", encoding="utf-8") as f:
        json.dump(highscores, f, ensure_ascii=False, indent=2)

# 輸入法強制切換成英文模式
imm32 = ctypes.WinDLL("imm32", use_last_error=True)
IME_CMODE_ALPHANUMERIC = 0x0000
IME_SMODE_NONE = 0x0000

def get_hwnd():
    return pg.display.get_wm_info()["window"]

def force_ime_english(hwnd):
    hIMC = imm32.ImmGetContext(hwnd)
    if hIMC:
        imm32.ImmSetConversionStatus(hIMC, IME_CMODE_ALPHANUMERIC, IME_SMODE_NONE)
        imm32.ImmAssociateContext(hwnd, None)

force_ime_english(get_hwnd())

# 小精靈動畫載入幀
frames = []
for i in range(2):
    new_size = (40, 40)
    pacman_image = pg.image.load(f"images/moveball/pacman_{i}.png").convert_alpha()
    resized_image = pg.transform.scale(pacman_image, new_size)
    frames.append(resized_image)

# 控制動畫
frame_index = 0
frame_timer = 0
frame_delay = 150  # 每幀持續時間（毫秒）

# 處理圖片顏色重新渲染
def tint_image(image, tint_color):
    tinted = image.copy()
    tint_surface = pg.Surface(image.get_size(), pg.SRCALPHA)
    tint_surface.fill(tint_color)
    tinted.blit(tint_surface, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
    return tinted

# 劃出小精靈(player) 
def draw_pacman(surface, x, y, frame_image, color, direction):
    angle = {
        "right": 0,
        "down": 270,
        "left": 180,
        "up": 90,
    }[direction]
    rotated_img = pg.transform.rotate(frame_image, angle)
    rect = rotated_img.get_rect(center=(x, y))
    rotated_img = tint_image(rotated_img, color)
    surface.blit(rotated_img, rect)

# 玩家設定
# 新增玩家起始方向設定值
players = [
    {"name": "藍色玩家", "color": BLUE, "x": 200, "y": 300, "keys": [pg.K_a, pg.K_d, pg.K_w, pg.K_s], "score": 0, "direction": "right"},
    {"name": "紅色玩家", "color": RED, "x": 600, "y": 300, "keys": [pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN], "score": 0, "direction": "left"},
]
player_radius = 20
speed = 5

# 載入得分點圖片
def load_star_image(path, size):
    image = pg.image.load(path).convert_alpha()
    return pg.transform.scale(image, size)

star_size = (25, 25)

# 星星設定：每顆星星有不同分數與深淺色(原)
# 得分點設定：每個分數有不同的圖片，如每行後的註釋
star_types = [
    {"img": load_star_image('images/moveball/pacman_1.png', star_size).convert_alpha(), "score": 1}, #白球 1 分
    {"img": load_star_image('images/moveball/star.png', star_size), "score": 3}, #星星 3 分
    {"img": load_star_image('images/moveball/cherry.png', star_size), "score": 5} #櫻桃 5 分
]

stars = []
score_popups = []
star_lifetime = 3  # 星星停留的秒數
star_size = 30
star_count = 6

# 建立星星
def create_star():
    star_type = random.choice(star_types)
    return {
        "x": random.randint(boundary_rect.left + star_size, boundary_rect.right - star_size),
        "y": random.randint(boundary_rect.top + star_size, boundary_rect.bottom - star_size),
        "img": star_type["img"],
        "score": star_type["score"],
        "born_time": time.time()
    }

# 初始化多顆星星
for _ in range(star_count):
    stars.append(create_star())

# 遊戲時間限制
game_duration = 31
start_time = time.time()

def show_start_screen():
    screen.fill(WHITE)
    pg.draw.rect(screen, (0, 0, 0), boundary_rect, boundary_rect_border)
    screen.blit(bg_resized, (boundary_rect.left + boundary_rect_border, boundary_rect.top + boundary_rect_border))
    overlay = pg.Surface(screen.get_size(), pg.SRCALPHA)
    overlay.fill((255, 255, 255, 128))
    screen.blit(overlay, (0, 0))
    title_text = large_font.render("歡迎來到BM小遊戲~", True, BLACK)
    info_text = font.render("按下空白鍵開始遊戲", True, BLACK)
    # 載入排行榜
    highscores = load_highscores()
    top_text = font.render("歷史最高分排行榜", True, BLACK)
    screen.blit(top_text, (30, 350))

    for i, record in enumerate(highscores[:5]):  # 取前五名
        rank_text = font.render(f"{i+1}. {record['name']}：{record['score']} 分", True, BLACK)
        screen.blit(rank_text, (30, 390 + i * 30))

    screen.blit(title_text, title_text.get_rect(center=(400, 50)))
    screen.blit(info_text, info_text.get_rect(center=(400, 300)))

    pg.display.update()

    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    waiting = False
        clock.tick(30)
    
        # 倒數 3 秒
    for i in range(3, 0, -1):
        screen.fill(WHITE)
        pg.draw.rect(screen, (0, 0, 0), boundary_rect, boundary_rect_border)
        screen.blit(bg_resized, (boundary_rect.left + boundary_rect_border, boundary_rect.top + boundary_rect_border))
        for ii, player in enumerate(players):
            text = font.render(f"{player['name']} 分數：{player['score']}", True, (0, 0, 0))
            screen.blit(text, (20, 20 + ii * 40))
        time_text = font.render(f"剩餘時間：   秒", True, (0, 0, 0))
        screen.blit(time_text, (550, 20))
        for player in players:
            draw_pacman(screen, player["x"], player["y"], frames[frame_index], player["color"], player["direction"])

        count_text = large_font.render(str(i), True, (255, 0, 0))
        screen.blit(count_text, count_text.get_rect(center=(400, 300)))
        pg.display.update()
        pg.time.wait(1000)

    return time.time()

def main_game():
    global stars, score_popups, start_time, frame_index, frame_timer, players
    # 重設遊戲狀態
    stars = [create_star() for _ in range(star_count)]
    score_popups = []
    frame_index = 0
    frame_timer = 0
    for player in players:
        player["score"] = 0
        player["x"], player["y"] = (200, 300) if player["name"] == "藍色玩家" else (600, 300)
        player["direction"] = "right" if player["name"] == "藍色玩家" else "left"

    start_time = show_start_screen()

    # 主迴圈
    running = True
    while running:
        dt = clock.tick(60)
        # clock.tick(60)
        screen.fill(WHITE)

        pg.draw.rect(screen, (0, 0, 0), boundary_rect, boundary_rect_border)
        screen.blit(bg_resized, (boundary_rect.left + boundary_rect_border, boundary_rect.top + boundary_rect_border))
        start_text = large_font.render("開始！", True, (255, 0, 0))
        if time.time() - start_time < 1.5:
            screen.blit(start_text, start_text.get_rect(center=(400, 300)))

        # 小精靈動畫
        frame_timer += dt

        if frame_timer >= frame_delay:
            frame_timer = 0
            frame_index = (frame_index + 1) % len(frames)


        elapsed_time = time.time() - start_time
        remain_time = max(0, int(game_duration - elapsed_time))
        if remain_time == 0:
            running = False
        # 處理事件
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        # 玩家控制
        keys = pg.key.get_pressed()
        for player in players:
            left, right, up, down = player["keys"]
            if keys[left] and player["x"] - player_radius > boundary_rect.left + boundary_rect_border:
                player["x"] -= speed
                player["direction"] = "left"
            if keys[right] and player["x"] + player_radius < boundary_rect.right - boundary_rect_border:
                player["x"] += speed
                player["direction"] = "right"
            if keys[up] and player["y"] - player_radius > boundary_rect.top + boundary_rect_border:
                player["y"] -= speed
                player["direction"] = "up"
            if keys[down] and player["y"] + player_radius < boundary_rect.bottom - boundary_rect_border:
                player["y"] += speed
                player["direction"] = "down"

        # 星星更新與碰撞判斷
        new_stars = []
        for star in stars:
            # 星星超時自動換位置
            if time.time() - star["born_time"] > star_lifetime:
                new_stars.append(create_star())
                continue

            star_rect = pg.Rect(star["x"], star["y"], star_size, star_size)
            eaten = False

            for player in players:
                dx = player["x"] - (star["x"] + star_size // 2)
                dy = player["y"] - (star["y"] + star_size // 2)
                dist = (dx ** 2 + dy ** 2) ** 0.5
                if dist < player_radius + star_size // 2:
                    player["score"] += star["score"]
                    eaten = True
                    # 新增分數浮動提示
                    score_popups.append({
                        "text": f"+{star['score']}",
                        "pos": (star["x"] + star_size // 2, star["y"]),  # 顯示在星星位置上方
                        "start_time": time.time(),
                        "color": player["color"]
                    })
                    break

            if not eaten:
                new_stars.append(star)

        # 在主迴圈畫玩家和星星之後，新增顯示浮動分數提示：
        current_time = time.time()
        for popup in score_popups[:]:  # 複製列表遍歷，方便刪除元素
            elapsed = current_time - popup["start_time"]
            if elapsed > 1.0:  # 顯示超過1秒就移除
                score_popups.remove(popup)
            else:
                # 漂浮效果（向上移動 30 像素/秒）
                float_y = popup["pos"][1] - elapsed * 30
                text_surface = font.render(popup["text"], True, popup["color"])
                text_rect = text_surface.get_rect(center=(popup["pos"][0], float_y))
                screen.blit(text_surface, text_rect)

        while len(new_stars) < star_count:
                new_stars.append(create_star())
        stars = new_stars

        # 畫出玩家
        for player in players:
            draw_pacman(screen, player["x"], player["y"], frames[frame_index], player["color"], player["direction"])

        # 畫出星星
        for star in stars:
            screen.blit(star["img"], (star["x"], star["y"]))

        # 顯示分數時間
        for i, player in enumerate(players):
            text = font.render(f"{player['name']} 分數：{player['score']}", True, (0, 0, 0))
            screen.blit(text, (20, 20 + i * 40))
        time_text = font.render(f"剩餘時間：{remain_time} 秒", True, (0, 0, 0))
        screen.blit(time_text, (550, 20))

        pg.display.update()

    # 遊戲結束畫面
    #screen.fill(WHITE) #清空畫面
    max_score = max(p["score"] for p in players)
    winner = [p for p in players if p["score"] == max_score]
    winner_text = font.render(f"遊戲結束！{winner[0]['name']}獲勝！", True, winner[0]['color'])
    draw_text = font.render(f"平手！", True, BLACK)
    restart_text = font.render(f"按下空白鍵重新開始遊戲", True, winner[0]['color'])
    overlay = pg.Surface(screen.get_size(), pg.SRCALPHA)
    overlay.fill((255, 255, 255, 128))
    screen.blit(overlay, (0, 0))
    if len(winner) > 1:
        screen.blit(draw_text, (380, 250))
    else:
        screen.blit(winner_text, (250, 250))
    screen.blit(restart_text, (260, 280))

    # --- 遊戲結束後更新排行榜 ---
    winner = max(players, key=lambda x: x["score"])
    highscores = load_highscores()
    highscores.append({
        "name": winner["name"],
        "score": winner["score"]
    })

    # 按照分數排序，只保留前五名
    highscores.sort(key=lambda x: x["score"], reverse=True)
    highscores = highscores[:5]

    save_highscores(highscores)

    pg.display.update()

    # 等待任意鍵
    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    waiting = False

while True:
    main_game()