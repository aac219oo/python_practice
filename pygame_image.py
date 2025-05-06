import pygame as pg
pg.init()
pg.mixer.init()

width, height = 640, 480
screen = pg.display.set_mode((width, height))
pg.display.set_caption("有的時候我就是好想逃離那一切")
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((187,252,255))

image = pg.image.load("images/PatrickStarSometimes.png")
image.convert()
img_width, img_height = image.get_size()
margin_left = (width - img_width) / 2
margin_top = (height - img_height) / 2
bg.blit(image, (margin_left, margin_top))


font = pg.font.Font("fonts/GenSenRounded2-B.ttc", 24)
text = font.render("派大星", True, (253,139,165), (187,252,255))
text_width, text_height = text.get_size()
text_margin_left = (width - text_width) / 2
text_margin_top = 10
bg.blit(text, (text_margin_left, text_margin_top))

pg.mixer.music.load("music/SpongeBob SquarePants - Stadium Rave A.mp3")
pg.mixer.music.play()

#匯入wav 
# s = pg.mixer.Sound("music/SpongeBob SquarePants - Stadium Rave A.wav")
# s.set_volume(0.7)
# s.play()

running = True
while running:
    screen.blit(bg, (0,0))
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit()