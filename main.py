import subprocess
import pygame
import sys 
from pygame.locals import *
from config.system_config import*
# from config import*

"""
画面に必要なもの
四つの操作ボタン
セレクト
エンター
バック
リセット
ボタンクラスを作成して

画面内に四つの操作ボタンを描画してクリック時のイベント:関数を決定する

画面イメージ
横長の画面の下段に四つのボタンを配置する


"""


pygame.init()
screen=screen=pygame.display.set_mode(SCREEN_SIZE)
#座標設定用の升目の設定が必要
#可視化用の升目を表示する処理も必要
#
def generate_grid_lines(screen,width,height):
    for x in range(height):
        ## 線: draw.line(surface, color, (start_x, start_y), (end_x, end_y), width=1)
        pygame.draw.line(screen,GREEN, (0,x*100), (width, x*100), 1)
        # print("xは"+str(x))
        # print("x*100は"+str(x*100))
        # pygame.draw()
#引数で指定した数値の割り算の結果を戻り値として返す
"""
100の10パーは10
100の12は12
200の50は100
200
200*50//100
"""
#
def format_percent(value:int,percent:int):
    r=value*percent//100
    return r 

print("デバッグ"+str(format_percent(100,10)))
#ボタンの定義
#レクト
select_button_rect=pygame.Rect(0,0,NORMALBUTTON_WIDTH,NORMALBUTTON_HEIGHT)
enter_button_rect=pygame.Rect(0,0,NORMALBUTTON_HEIGHT,NORMALBUTTON_WIDTH)
back_button_rect=pygame.Rect(0,0,NORMALBUTTON_HEIGHT,NORMALBUTTON_WIDTH)
reset_button_rect=pygame.Rect(0,0,NORMALBUTTON_HEIGHT,NORMALBUTTON_WIDTH)
#レクトの中央値を設定する
select_button_rect.center=(100,100)
is_run=True
while is_run:
    pygame.time.wait(1)#1ループ事の待機時間を設定
    screen.fill((0,0,0))#画面の塗りつぶ
    generate_grid_lines(screen,SCREEN_WIDTH,SCREEN_HEIGHT)
    pygame.draw.rect(screen,(255,255,255),select_button_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()


#thread分割の考え方