import pygame as pg # 1. 파이게임 불러오기
import sys
from datetime import datetime
from datetime import timedelta



pg.init()           # 2. 초기화

                    # 3. 사용될 전역 변수 선언
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

x_size, y_size = (20, 20)
block_size = 20
size = [x_size * block_size, y_size * block_size]

screen = pg.display.set_mode(size)
pg.display.set_caption('Snake')


done = False
clock = pg.time.Clock()

block_positon =[0,0] # (y,x)
last_moved_time = datetime.now()
moving_direction = '' # East, West, South, North


def draw_block(screen,color,position):
    block = pg.Rect((position[0] * block_size , position[1] * block_size),
                    (block_size,block_size))
    pg.draw.rect(screen, color, block)

                    # 4. pygame 무한루프

def runGame():
    global done, last_moved_time, moving_direction

    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        
        for event in pg.event.get():        
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    block_positon[1] -= 1  # y 좌표에서 1뺀다
                    moving_direction ='N'
                    last_moved_time = datetime.now()  # 마지막 움직인시간 기록
                elif event.key ==pg.K_DOWN:
                    block_positon[1] += 1  # y 좌표에서 1더하기
                    moving_direction = 'S'
                    last_moved_time = datetime.now()
                elif event.key ==pg.K_LEFT:
                    block_positon[0] -= 1  # x 좌표에서 1빼기
                    moving_direction = 'W'
                    last_moved_time = datetime.now()
                elif event.key ==pg.K_RIGHT:
                    block_positon[0] += 1  # x 좌표에서 1더하기
                    moving_direction = 'E'
                    last_moved_time = datetime.now()
            
    # 마지막 움직인시간 에서 0.5초 보다 크면 자동으로 가던 방향으로 움직임
        if datetime.now() - last_moved_time >= timedelta(seconds=0.5):
            if moving_direction == 'N':
                block_positon[1] -=1
            elif moving_direction == 'S':
                block_positon[1] +=1
            elif moving_direction == 'W':
                block_positon[0] -=1
            elif moving_direction == 'E':
                block_positon[0] +=1
            last_moved_time =datetime.now() # 자동움직임 뒤에도 시간 기록
        
        draw_block(screen,GREEN,block_positon)
        pg.display.update()
            
runGame()
pg.quit()