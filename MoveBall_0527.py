import pygame as pg
import random
import time
import json
import os
import math
# 初始化
pg.init()
#
pg.mixer.init()
pg.mixer.music.load("music/bg_music.mp3")
pg.mixer.music.play(-1)
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("BM王")
clock = pg.time.Clock()
font = pg.font.Font("C:/Windows/Fonts/msjh.ttc", 24)
large_font = pg.font.Font("C:/Windows/Fonts/msjh.ttc", 72)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 80, 80, 255)
BLUE = (90, 90, 255, 255)
# 玩家方向
DIRECTION_ANGLES = {
    "right": 0,
    "up-right": 45,
    "up": 90,
    "up-left": 135,
    "left": 180,
    "down-left": 225,
    "down": 270,
    "down-right": 315,
}
# 文字輸入禁止，避免中文輸入的wasd無法支援玩家移動
pg.key.stop_text_input()

# 載入音效
walk_sound = pg.mixer.Sound("music/small_footsteps.mp3")
walk_sound.set_volume(0.3)
score_sound = pg.mixer.Sound("music/coin03.mp3")
hit_sound = pg.mixer.Sound("music/knocking_a_wall.mp3")
stun_sound = pg.mixer.Sound("music/powerdown04.mp3")
start_sound = pg.mixer.Sound("music/button01b.mp3")
restart_sound = pg.mixer.Sound("music/button02b.mp3")
count_sound = pg.mixer.Sound("music/select01.mp3")
gameStart_sound = pg.mixer.Sound("music/select09.mp3")
# 包裝內建載入圖片函式
def load_image(path, size):
    image = pg.image.load(path).convert_alpha()
    return pg.transform.scale(image, size)


# 載入 icon
icon_size = [64, 64]
icon_surface = load_image("images/bmKing/icon.png", icon_size)
pg.display.set_icon(icon_surface)

back_size = [800, 600]
back_img = load_image("images/bmKing/icon.png", back_size)
start_size = [250, 30.6]
start_img = load_image("images/bmKing/start.png", start_size)

# 遊戲邊界範圍
boundary_rect = pg.Rect(10, 100, 780, 490)
boundary_rect_border = 5

# 載入背景
bg_size = [
    boundary_rect.width - boundary_rect_border * 2,
    boundary_rect.height - boundary_rect_border * 2
]
bg_img = load_image("images/bmKing/background.jpg", bg_size)

# 紀錄最高分排名
HIGHSCORE_FILE = "json/highscores.json"


# 讀取歷史紀錄
def load_highscores():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


# 儲存歷史紀錄
def save_highscores(highscores):
    with open(HIGHSCORE_FILE, "w", encoding="utf-8") as f:
        json.dump(highscores, f, ensure_ascii=False, indent=2)


# 建立單位碰撞面積
def create_hitmask(image):
    width, height = image.get_size()
    hitmask = []
    for x in range(width):
        col = []
        for y in range(height):
            alpha = image.get_at((x, y))[3]  # alpha channel
            col.append(alpha > 0)
        hitmask.append(col)
    return hitmask


# 小精靈動畫載入幀
frames = []
for i in range(2):
    new_size = (40, 40)
    pacman_image = load_image(f"images/bmKing/pacman_{i}.png", new_size)
    frames.append(pacman_image)

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
    angle = DIRECTION_ANGLES.get(direction, 0)
    rotated_img = pg.transform.rotate(frame_image, angle)
    rect = rotated_img.get_rect(center=(x, y))
    rotated_img = tint_image(rotated_img, color)
    surface.blit(rotated_img, rect)


# 玩家設定
# 新增玩家起始方向設定值
player_size = [40, 40]
player_radius = 20
speed = 5
players = [
    {
        "name": "藍色玩家",
        "img": load_image('images/bmKing/rock.png', player_size),
        "color": BLUE,
        "x": 200,
        "y": 300,
        "keys": [pg.K_a, pg.K_d, pg.K_w, pg.K_s],
        "score": 0,
        "direction": "right",
        "last_hit_rock": 0,
        "hitmask": create_hitmask(pacman_image),
        "stun_cooldown": 0,
        "last_collided_with": None,
        "has_separated": True
    },
    {
        "name": "紅色玩家",
        "img": load_image('images/bmKing/rock.png', player_size),
        "color": RED,
        "x": 600,
        "y": 300,
        "keys": [pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN],
        "score": 0,
        "direction": "left",
        "last_hit_rock": 0,
        "hitmask": create_hitmask(pacman_image),
        "stun_cooldown": 0,
        "last_collided_with": None,
        "has_separated": True
    },
]

# 建立石頭單位，玩家碰撞到石頭會扣3分
rock_size = [50, 33.6]
rock_types = [
    {
        "img": load_image('images/bmKing/rock.png', rock_size),
        "score": -3
    },
]
rocks = []
rock_size = 50
rock_count = 12


# 建立石頭
def create_rock():
    rock_type = random.choice(rock_types)
    rock_width = rock_type["img"].get_width()
    rock_height = rock_type["img"].get_height()

    # 檢查是否與玩家重疊
    while True:
        x = random.randint(
            boundary_rect.left + boundary_rect_border,
            boundary_rect.right - rock_width - boundary_rect_border)
        y = random.randint(
            boundary_rect.top + boundary_rect_border,
            boundary_rect.bottom - rock_height - boundary_rect_border)
        new_rect = pg.Rect(x - rock_width // 2, y - rock_height // 2,
                           rock_width, rock_height)

        overlap = False
        for player in players:
            player_rect = pg.Rect(player["x"] - player_radius * 3,
                                  player["y"] - player_radius * 3,
                                  player_radius * 6, player_radius * 6)
            if new_rect.colliderect(player_rect):
                overlap = True
                break
        if not overlap:
            break
    return {
        "x": x,
        "y": y,
        "img": rock_type["img"],
        "score": rock_type["score"],
        "hitmask": create_hitmask(rock_type["img"])
    }


# 初始化多顆石頭
for _ in range(rock_count):
    rocks.append(create_rock())

# 星星設定：每顆星星有不同分數與深淺色(原)
# 得分點設定：每個分數有不同的圖片，如每行後的註釋
star_size = (25, 25)
star_types = [
    {
        "img": load_image('images/bmKing/pacman_1.png', star_size),
        "score": 1
    },  #白球 1 分
    {
        "img": load_image('images/bmKing/star.png', star_size),
        "score": 3
    },  #星星 3 分
    {
        "img": load_image('images/bmKing/cherry.png', star_size),
        "score": 5
    }  #櫻桃 5 分
]

stars = []
score_popups = []
star_lifetime = 4  # 星星停留的秒數
star_size = 30
star_count = 16


# 建立星星
def create_star():
    star_type = random.choice(star_types)
    while True:
        x = random.randint(boundary_rect.left + boundary_rect_border,
                           boundary_rect.right - star_size)
        y = random.randint(boundary_rect.top + boundary_rect_border,
                           boundary_rect.bottom - star_size)
        new_rect = pg.Rect(x, y, star_size, star_size)

        # 檢查是否與任一石頭重疊
        overlap = False
        for rock in rocks:
            rock_rect = pg.Rect(rock["x"], rock["y"], rock_size, rock_size)
            if new_rect.colliderect(rock_rect):
                overlap = True
                break

        if not overlap:
            break

    return {
        "x": x,
        "y": y,
        "img": star_type["img"],
        "score": star_type["score"],
        "born_time": time.time()
    }


# 初始化多顆星星
for _ in range(star_count):
    stars.append(create_star())

# 暈眩圖
stun_size = [40, 18.4]
stun_image = load_image("images/bmKing/stun.png", stun_size)


# 通用的像素級碰撞判斷
def pixel_perfect_collision(obj_x, obj_y, obj_radius, target):
    obj_rect = pg.Rect(obj_x - obj_radius, obj_y - obj_radius, obj_radius * 2,
                       obj_radius * 2)
    target_rect = pg.Rect(target["x"], target["y"], target["img"].get_width(),
                          target["img"].get_height())

    if not obj_rect.colliderect(target_rect):
        return False

    intersection = obj_rect.clip(target_rect)
    if intersection.width == 0 or intersection.height == 0:
        return False

    for x in range(intersection.width):
        for y in range(intersection.height):
            obj_px = intersection.x - obj_rect.x + x
            obj_py = intersection.y - obj_rect.y + y
            target_px = intersection.x - target_rect.x + x
            target_py = intersection.y - target_rect.y + y

            dist_x = obj_px - obj_radius
            dist_y = obj_py - obj_radius
            if dist_x**2 + dist_y**2 > obj_radius**2:
                continue

            if (0 <= target_px < len(target["hitmask"])
                    and 0 <= target_py < len(target["hitmask"][0])
                    and target["hitmask"][target_px][target_py]):
                return True
    return False


# 檢查是否與多個障礙物碰撞（適用任意角色）
def check_collision_with_targets(x, y, radius, targets):
    for target in targets:
        if pixel_perfect_collision(x, y, radius, target):
            return target  # 回傳第一個碰到的物件
    return None


# 檢查是否玩家互相碰撞
def check_player_collisions():
    current_time = time.time()
    for i, player1 in enumerate(players):
        for j, player2 in enumerate(players):
            if i >= j:
                continue  # 避免重複檢查

            # 計算兩玩家的距離
            dx = player1["x"] - player2["x"]
            dy = player1["y"] - player2["y"]
            distance_squared = dx**2 + dy**2
            min_distance = player_radius * 2

            if distance_squared < min_distance**2:
                # 玩家還在接觸中，但若他們沒分開過，就不能再次觸發
                if (player1["last_collided_with"] == player2
                        and not player1["has_separated"]
                        or player2["last_collided_with"] == player1
                        and not player2["has_separated"]):
                    continue

                # 若任一方處於冷卻中，也不觸發
                if player1["stun_cooldown"] > current_time or player2[
                        "stun_cooldown"] > current_time:
                    continue

                # 撞到了，觸發暈眩與聲音
                stun_sound.play()
                cooldown_time = 1.2
                player1["stun_cooldown"] = current_time + cooldown_time
                player2["stun_cooldown"] = current_time + cooldown_time

                # 更新狀態
                player1["last_collided_with"] = player2
                player2["last_collided_with"] = player1
                player1["has_separated"] = False
                player2["has_separated"] = False
            else:
                # 他們已分開
                if player1["last_collided_with"] == player2:
                    player1["has_separated"] = True
                if player2["last_collided_with"] == player1:
                    player2["has_separated"] = True


# 渲染遊戲開始畫面
def show_start_screen():
    screen.fill(WHITE)
    screen.blit(back_img, (0, 0))
    pg.draw.rect(screen, (0, 0, 0), boundary_rect, boundary_rect_border)
    screen.blit(bg_img, (boundary_rect.left + boundary_rect_border,
                         boundary_rect.top + boundary_rect_border))
    overlay = pg.Surface(screen.get_size(), pg.SRCALPHA)
    overlay.fill((255, 255, 255, 128))
    screen.blit(overlay, (0, 0))
    logo_size = [540, 356]
    logo_img = load_image("images/bmKing/logo.png", logo_size)

    # 載入排行榜
    highscores = load_highscores()
    top_text = font.render("歷史最高分排行榜", True, BLACK)
    screen.blit(top_text, (30, 350))

    for i, record in enumerate(highscores[:5]):  # 取前五名
        rank_text = font.render(f"{i+1}. {record['name']}：{record['score']} 分",
                                True, BLACK)
        screen.blit(rank_text, (30, 390 + i * 30))

    screen.blit(logo_img, logo_img.get_rect(center=(400, 150)))

    pg.display.update()

    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    start_sound.play()
                    waiting = False

        # ✅ 使用 sin 波產生閃爍值（0 到 1）
        t = pg.time.get_ticks() / 1000  # 時間（秒）
        brightness = (math.sin(t * 2 * math.pi / 2) + 1) / 2  # 每 2 秒循環，範圍 0~1

        # ✅ 混合白色與紅色
        base_color = (255, 100, 100)
        max_color = (255, 255, 255)
        tint_color = tuple(
            int(base_color[i] + (max_color[i] - base_color[i]) * brightness)
            for i in range(3)
        )

        tinted_img = tint_image(start_img, tint_color)
        screen.blit(tinted_img, tinted_img.get_rect(center=(400, 500)))

        pg.display.flip()
        clock.tick(60)

    # 開始遊戲後倒數 3 秒
    for i in range(3, 0, -1):
        screen.fill(WHITE)
        screen.blit(back_img, (0, 0))
        pg.draw.rect(screen, (0, 0, 0), boundary_rect, boundary_rect_border)
        screen.blit(bg_img, (boundary_rect.left + boundary_rect_border,
                             boundary_rect.top + boundary_rect_border))
        for ii, player in enumerate(players):
            text = font.render(f"{player['name']} 分數：{player['score']}", True,
                               WHITE)
            screen.blit(text, (20, 20 + ii * 40))
        time_text = font.render(f"剩餘時間：   秒", True, WHITE)
        screen.blit(time_text, (550, 20))
        for player in players:
            draw_pacman(screen, player["x"], player["y"], frames[frame_index],
                        player["color"], player["direction"])
        count_sound.play()
        count_text = large_font.render(str(i), True, (255, 0, 0))
        screen.blit(count_text, count_text.get_rect(center=(400, 300)))
        pg.display.update()
        pg.time.wait(1000)
    gameStart_sound.play()
    return time.time()


# 遊戲時間限制
game_duration = 31
start_time = time.time()


# 遊戲主要邏輯
def main_game():
    global rocks, stars, score_popups, start_time, frame_index, frame_timer, players
    # 重設遊戲狀態
    stars = [create_star() for _ in range(star_count)]
    rocks = [create_rock() for _ in range(rock_count)]
    score_popups = []
    frame_index = 0
    frame_timer = 0
    for player in players:
        player["score"] = 0
        player["x"], player["y"] = (200,
                                    300) if player["name"] == "藍色玩家" else (600,
                                                                           300)
        player["direction"] = "right" if player["name"] == "藍色玩家" else "left"

    start_time = show_start_screen()

    # 主迴圈
    running = True
    while running:
        dt = clock.tick(60)
        # clock.tick(60)
        screen.fill(WHITE)
        screen.blit(back_img, (0, 0))
        pg.draw.rect(screen, (0, 0, 0), boundary_rect, boundary_rect_border)
        screen.blit(bg_img, (boundary_rect.left + boundary_rect_border,
                             boundary_rect.top + boundary_rect_border))
        # 畫出石頭
        for rock in rocks:
            screen.blit(rock["img"], (rock["x"], rock["y"]))

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

        current_time = time.time()

        check_player_collisions()
        # 玩家控制
        keys = pg.key.get_pressed()
        for player in players:
            left, right, up, down = player["keys"]
            new_x = player["x"]
            new_y = player["y"]
            moving = False

            # 暈眩時不讓玩家移動
            if current_time < player["stun_cooldown"]:
                continue

            if keys[left] and player[
                    "x"] - player_radius > boundary_rect.left + boundary_rect_border:
                new_x -= speed
                player["direction"] = "left"
                moving = True
            if keys[right] and player[
                    "x"] + player_radius < boundary_rect.right - boundary_rect_border:
                new_x += speed
                player["direction"] = "right"
                moving = True
            if keys[up] and player[
                    "y"] - player_radius > boundary_rect.top + boundary_rect_border:
                new_y -= speed
                player["direction"] = "up"
                moving = True
            if keys[down] and player[
                    "y"] + player_radius < boundary_rect.bottom - boundary_rect_border:
                new_y += speed
                player["direction"] = "down"
                moving = True

            dx, dy = 0, 0
            if keys[left]:
                dx -= 1
            if keys[right]:
                dx += 1
            if keys[up]:
                dy -= 1
            if keys[down]:
                dy += 1
            # 設定方向
            if dx == 1 and dy == 0:
                player["direction"] = "right"
            elif dx == 1 and dy == -1:
                player["direction"] = "up-right"
            elif dx == 0 and dy == -1:
                player["direction"] = "up"
            elif dx == -1 and dy == -1:
                player["direction"] = "up-left"
            elif dx == -1 and dy == 0:
                player["direction"] = "left"
            elif dx == -1 and dy == 1:
                player["direction"] = "down-left"
            elif dx == 0 and dy == 1:
                player["direction"] = "down"
            elif dx == 1 and dy == 1:
                player["direction"] = "down-right"
            # 移動時的音效
            if moving:
                if not pg.mixer.Channel(1).get_busy():  # 使用特定的頻道播放走路音效避免重疊
                    pg.mixer.Channel(1).play(walk_sound)
            # 玩家撞到石頭就不移動並扣分
            collided_rock = check_collision_with_targets(
                new_x, new_y, player_radius, rocks)
            for rock in rocks:
                if collided_rock:
                    now = time.time()
                    if now - player["last_hit_rock"] > 1.0:  # 每 1 秒最多扣一次
                        hit_sound.play()
                        player["score"] += rock["score"]
                        player["last_hit_rock"] = now
                        # 浮動文字顯示扣分
                        score_popups.append({
                            "text":
                            f"{rock['score']}",
                            "pos": (player["x"], player["y"] - 30),
                            "color": (84, 16, 4),  # 深紅色代表扣分
                            "start_time":
                            now
                        })

            if not collided_rock:
                player["x"] = new_x
                player["y"] = new_y

        # 星星更新與碰撞判斷
        new_stars = []
        for star in stars:
            # 星星超時自動換位置
            if time.time() - star["born_time"] > star_lifetime:
                new_stars.append(create_star())
                continue

            eaten = False
            for player in players:
                dx = player["x"] - (star["x"] + star_size // 2)
                dy = player["y"] - (star["y"] + star_size // 2)
                dist = (dx**2 + dy**2)**0.5
                if dist < player_radius + star_size // 2:
                    score_sound.play()
                    player["score"] += star["score"]
                    eaten = True
                    # 新增分數浮動提示
                    score_popups.append({
                        "text":
                        f"+{star['score']}",
                        "pos":
                        (star["x"] + star_size // 2, star["y"]),  # 顯示在星星位置上方
                        "start_time":
                        time.time(),
                        "color":
                        player["color"]
                    })
                    break

            if not eaten:
                new_stars.append(star)

        # 在主迴圈畫玩家和星星之後，新增顯示浮動分數提示：
        for popup in score_popups[:]:  # 複製列表遍歷，方便刪除元素
            elapsed = current_time - popup["start_time"]
            if elapsed > 1.0:  # 顯示超過1秒就移除
                score_popups.remove(popup)
            else:
                # 漂浮效果（向上移動 30 像素/秒）
                float_y = popup["pos"][1] - elapsed * 30
                text_surface = font.render(popup["text"], True, popup["color"])
                text_rect = text_surface.get_rect(center=(popup["pos"][0],
                                                          float_y))
                screen.blit(text_surface, text_rect)

        while len(new_stars) < star_count:
            new_stars.append(create_star())
        stars = new_stars

        # 畫出玩家
        for player in players:
            draw_pacman(screen, player["x"], player["y"], frames[frame_index],
                        player["color"], player["direction"])
            if player["stun_cooldown"] > time.time():
                stun_rect = stun_image.get_rect(center=(player["x"],
                                                        player["y"] - 30))
                screen.blit(stun_image, stun_rect)
        # 畫出星星
        for star in stars:
            screen.blit(star["img"], (star["x"], star["y"]))

        start_text = large_font.render("開始！", True, (255, 0, 0))
        
        if time.time() - start_time < 1.5:
            screen.blit(start_text, start_text.get_rect(center=(400, 300)))

        # 顯示分數時間
        for i, player in enumerate(players):
            text = font.render(f"{player['name']} 分數：{player['score']}", True,
                               WHITE)
            screen.blit(text, (20, 20 + i * 40))
        time_text = font.render(f"剩餘時間：{remain_time} 秒", True, WHITE)
        screen.blit(time_text, (550, 20))

        pg.display.update()

    # 遊戲結束畫面
    max_score = max(p["score"] for p in players)
    winner = [p for p in players if p["score"] == max_score]
    winner_text = font.render(f"遊戲結束！{winner[0]['name']}獲勝！", True,
                              winner[0]['color'])
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
    highscores.append({"name": winner["name"], "score": winner["score"]})

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
                    restart_sound.play()
                    waiting = False


# 重複遊戲主要邏輯
while True:
    main_game()
