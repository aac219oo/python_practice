import pygame as pg, time

pg.mixer.init()
pg.mixer.music.load("music/SpongeBob SquarePants - Stadium Rave A.mp3")   #背景音樂
pg.mixer.music.play(-1, 0)  #一直播放

width, height = 640, 480
screen = pg.display.set_mode((width,height))
pg.display.set_caption("This my pgGame!")

bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255,177,27))
image= pg.image.load("images/Squidward.png")
image.convert()
bg.blit(image, ((width/2)-(image.get_width()/2), (height/2)-image.get_height()/2))

#screen.blit(bg, (0,0))
#pg.display.update()

running = True
moving = False
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            #pg.mixer.music.load("mp3/pika.mp3")
            #pg.mixer.music.play()
            #time.sleep(3)
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            pg.mixer.music.load("music/button01a.mp3")
            pg.mixer.music.play()
            if moving == True:
                moving = False
            else:
                moving = True
        if event.type == pg.MOUSEBUTTONDOWN:
            pg.mixer.music.load("music/button01b.mp3")
            pg.mixer.music.play()
        if moving:
            position = pg.mouse.get_pos()
            bg.fill((255,177,27))
            bg.blit(image, (position[0]-image.get_width()/2,position[1]-image.get_height()/2))
    screen.blit(bg, (0,0))
    pg.display.update()
pg.quit()
