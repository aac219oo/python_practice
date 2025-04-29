import pygame as pg
pg.init()
pg.mixer.init()

width, height = 640, 480
screen = pg.display.set_mode((width, height))
pg.display.set_caption("THIS IS TEST GAME")
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((187,252,255))

image = pg.image.load("images/PatrickStarSometimes.png")
image.convert()
bg.blit(image, (20, 10))

font = pg.font.Font("fonts/GenSenRounded2-B.ttc", 24)
text = font.render("測試", True, (255,0,0), (187,252,255))
bg.blit(text, (500,440))

pg.mixer.music.load("music/DG Pacino - Roll the Dice.mp3")
pg.mixer.music.play()

s = pg.mixer.Sound("music/DG Pacino - Roll the Dice (online-audio-converter.com).wav")
s.set_volume(0.7)
# s.play()

running = True
while running:
    screen.blit(bg, (0,0))
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()