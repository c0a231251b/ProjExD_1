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
    kk_img=pg.image.load("fig/2.png")
    kk_img=pg.transform.flip(bg_img,True,False)

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0]) #blitで画面表示
        pg.display.update()
        tmr += 1        
        clock.tick(10)#フレームレート


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()