import pygame as pg # 1. 파이게임 불러오기
import sys
from datetime import datetime
from datetime import timedelta



pg.init()           # 2. 초기화

                    # 3. 사용될 전역 변수 선언
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
GRAY = (200,200,200)

FIELD_W, FIELD_H = (20, 20)
block_size = 20
size = [FIELD_W * block_size, FIELD_H * block_size]

screen = pg.display.set_mode(size)
pg.display.set_caption('Snake')


done = False
clock = pg.time.Clock()
last_moved_time = datetime.now()

KEY_DIRECTION ={pg.K_UP:'N', pg.K_DOWN:'S', pg.K_LEFT:'W', pg.K_RIGHT:'E'}

def draw_grid():
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(screen, GRAY,
                        (x * block_size, y * block_size, block_size,block_size), 1)
                


def draw_block(screen,color,position):
    block = pg.Rect((position[0] * block_size , position[1] * block_size),
                    (block_size,block_size))
    pg.draw.rect(screen, color, block)


class Snake:
    def __init__(self):
        self.positions = [(2,0),(1,0),(0,0)] # 뱀의 위치 (2,0)이 머리
        self.direction = ''

    def draw(self):
        for position in self.positions:
            draw_block(screen, GREEN, position)
    
    def move(self):
        head_position =self.positions[0]
        y, x = head_position
        if self.direction =='N':
            self.positions=[(y-1,x)] + self.positions[:-1]
        elif self.direction =='S':
            self.positions=[(y+1,x)] + self.positions[:-1]
        elif self.direction =='W':
            self.positions=[(y,x-1)] + self.positions[:-1]
        elif self.direction =='E':
            self.positions=[(y,x+1)] + self.positions[:-1]

class Apple:
    def __init__(self, position =(5,5)):
        self.position= position

    def draw(self):
        draw_block(screen,RED, self.position)

                    # 4. pygame 무한루프

def runGame():
    global done, last_moved_time
    
    # 게임 시작시 뱀과 사과를 초기화
    snake = Snake()
    apple = Apple()

    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        
        for event in pg.event.get():        
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if event.key in KEY_DIRECTION:
                    snake.direction = KEY_DIRECTION[event.key]  
                    print(snake.direction)
            
    # 마지막 움직인시간 에서 0.5초 보다 크면 자동으로 가던 방향으로 움직임
        if datetime.now() - last_moved_time >= timedelta(seconds=0.5):
           snake.move
        #    last_moved_time =datetime.now() # 자동움직임 뒤에도 시간 기록
        
        draw_grid()
        snake.draw()
        apple.draw()
        pg.display.update()
            
runGame()
pg.quit()