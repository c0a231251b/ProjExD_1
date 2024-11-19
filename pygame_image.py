import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))#(横、縦)
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #サーフェイス=bg_img
    #こうかとん画像2.pngを読み込み、surfaceを生成
    bg_img2=pg.transform.flip(bg_img,True,False)
    kk_img=pg.image.load("fig/3.png")
    kk_img=pg.transform.flip(kk_img,True,False)

    #こうかとんをsurfaceでRect
    kk_rect=kk_img.get_rect()
    kk_rect.center=(300,200)


    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x=-(tmr%3200)
        y=0

        key_lst=pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            dis=0
            y=-1
           # kk_rect.move_ip((0,-1))
        if key_lst[pg.K_DOWN]:
            dis=0
            y=1
            #kk_rect.move_ip((0,1))
        #演習課題2


        if key_lst[pg.K_LEFT]:
            dis=-1
            #kk_rect.move_ip((-1,0))
        if key_lst[pg.K_RIGHT]:
            dis=1
           # kk_rect.move_ip((1,0))
        #演習課題1
        else:
            dis=-1
        kk_rect.move_ip(dis,y)






        


        screen.blit(bg_img, [x, 0]) #blitで画面表示
        screen.blit(bg_img2,[x+1600,0])
        screen.blit(bg_img,[x+3200,0])#こうかとん画面表示
        screen.blit(bg_img2,[x+4800,0])
        # screen.blit(kk_img,[300,200])
        screen.blit(kk_img,kk_rect)
        pg.display.update()
        tmr += 1        
        clock.tick(200)#フレームレート


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()