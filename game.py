import pygame
import time
import random
pygame.init()
LENGTH = 300
WIDTH = 600

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
GRAY = (120,120,120)
PINK = (255,192,203)
ORANGE = (255,128,0)
WHITE = (255,255,255)
BROWN = (156,102,31)

making = pygame.Rect

class Board :
    def __init__(self):
        self.score = 0
        self.is_coloured = list()
    def add(self,rectangles,color) :
        for rectangle in rectangles :
            self.is_coloured.append(rectangle) 
    def evaluation(self):
        for i in range(0,600,30):
            for j in range(0,300,30):
                if making(j,i,30,30) not in self.is_coloured :
                    break
                if j==270 :
                    self.score +=10
                    for k in range(0,300,30) :
                        self.is_coloured.remove(making(k,i,30,30))
                    for rectangle in self.is_coloured :
                        if rectangle.top <i :
                            rectangle.move_ip(0,30)
                    print(self.score)
    def display(self,screen) :
        for rectangle in self.is_coloured :
            pygame.draw.rect(screen,BROWN,rectangle)
    
                    
    
                    

class square :
    def __init__(self,i,j) :
        self.color = BLUE
        self.side = 30
        self.possibles = [[making(i,j,30,30),making(i+30,j,30,30),making(i,j+30,30,30),making(i+30,j+30,30,30)]]
        self.num = 0
        self.rectangles = self.possibles[self.num%4]
    def display(self,screen):
        for rectangle in self.rectangles :
            pygame.draw.rect(screen,self.color,rectangle)
    def move_rectangles(self,x,y):
        for pos in self.possibles :
            for rectangle in pos :
                rectangle.move_ip(x,y)
    def check_collisions(self,rects):
        for rectangle in self.rectangles :
            if rectangle.collidelist(rects) !=-1 :
                return True
        return False
    def contains_in_box(self):
        for rectangle in self.rectangles :
            if not making(0,0,300,600).contains(rectangle):
                return False
        return True
    def rotate(self,num_r) :
        pass
    
class el_right(square) :
    def __init__(self,i,j) :
        square.__init__(self,i,j)
        self.color = RED
        self.possibles = [[making(i,j,30,30),making(i,j+30,30,30),making(i-30,j+30,30,30),making(i-60,j+30,30,30)],
        [making(i,j,30,30),making(i-30,j,30,30),making(i,j+30,30,30),making(i,j+60,30,30)],
        [making(i,j,30,30),making(i-30,j,30,30),making(i-30,j-30,30,30),making(i+30,j,30,30)],
        [making(i,j,30,30),making(i,j+30,30,30),making(i,j+60,30,30),making(i+30,j+60,30,30)]]
        self.rectangles = self.possibles[self.num%4]
    def rotate(self,num_r) :
        self.num = self.num+num_r
        self.rectangles = self.possibles[self.num%4]

class el_left(square) :
    def __init__(self,i,j) :
        square.__init__(self,i,j)
        self.color = YELLOW
        self.possibles = [[making(i,j,30,30),making(i,j+30,30,30),making(i+30,j+30,30,30),making(i+60,j+30,30,30)],
        [making(i,j,30,30),making(i,j+30,30,30),making(i,j+60,30,30),making(i-30,j+60,30,30)],
        [making(i,j,30,30),making(i-30,j,30,30),making(i+30,j,30,30),making(i+30,j+30,30,30)],
        [making(i,j,30,30),making(i+30,j,30,30),making(i,j+30,30,30),making(i,j+60,30,30)]]
        self.rectangles = self.possibles[self.num%4]
    def rotate(self,num_r) :
        self.num+=num_r
        self.rectangles = self.possibles[self.num%4]
class  z_left(square) :
    def __init__(self,i,j) :
        square.__init__(self,i,j)
        self.color = GREEN
        self.possibles = [[making(i,j,30,30),making(i+30,j,30,30),making(i+30,j+30,30,30),making(i+60,j+30,30,30)],
        [making(i,j,30,30),making(i,j+30,30,30),making(i-30,j+30,30,30),making(i-30,j+60,30,30)]]
        self.rectangles = self.possibles[self.num%2]
    def rotate(self,num_r) :
        self.num+=num_r
        self.rectangles = self.possibles[self.num%2]
class z_right(square) :
    def __init__(self,i,j) :
        square.__init__(self,i,j)
        self.color = PINK
        self.possibles = [[making(i,j,30,30),making(i-30,j,30,30),making(i-30,j+30,30,30),making(i-60,j+30,30,30)],
        [making(i,j,30,30),making(i,j+30,30,30),making(i+30,j+30,30,30),making(i+30,j+60,30,30)]]
        self.rectangles = self.possibles[self.num%2]
    def rotate(self,num_r) :
        self.num+=num_r
        self.rectangles = self.possibles[self.num%2]
class rev_T(square) :
    def __init__(self,i,j) :
        square.__init__(self,i,j)
        self.color = ORANGE
        self.possibles = [[making(i,j,30,30),making(i,j+30,30,30),making(i+30,j+30,30,30),making(i-30,j+30,30,30)],
        [making(i,j,30,30),making(i,j+30,30,30),making(i-30,j+30,30,30),making(i,j+60,30,30)],
        [making(i,j,30,30),making(i+30,j,30,30),making(i-30,j,30,30),making(i,j+30,30,30)],
        [making(i,j,30,30),making(i,j+30,30,30),making(i+30,j+30,30,30),making(i,j+60,30,30)]]
        self.rectangles = self.possibles[self.num%4]
    def rotate(self,num_r) :
        self.num+=num_r
        self.rectangles = self.possibles[self.num%4]

class long_l(square) :
    def __init__(self,i,j) :
        square.__init__(self,i,j)
        self.color = GRAY
        self.possibles = [[making(i,j,30,30),making(i,j+30,30,30),making(i,j+60,30,30),making(i,j+90,30,30)],
        [making(i,j,30,30),making(i-30,j,30,30),making(i+30,j,30,30),making(i+60,j,30,30)]]
        self.rectangles = self.possibles[self.num%2]
    def rotate(self,num_r) :
        self.num+=num_r
        self.rectangles = self.possibles[self.num%2]

SIZE =(LENGTH,WIDTH)
scr = pygame.display.set_mode(SIZE)

CLOCK = pygame.time.Clock()

B = Board()
s = random.choice([square,el_left,el_right,z_left,z_right,rev_T,long_l])(90,0)
count = 1


while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                s.move_rectangles(30,0)
                if not s.contains_in_box() or s.check_collisions(B.is_coloured) :
                    s.move_rectangles(-30,0)
            elif event.key == pygame.K_LEFT :
                s.move_rectangles(-30,0)
                if not s.contains_in_box() or s.check_collisions(B.is_coloured):
                    s.move_rectangles(30,0)
            elif event.key == pygame.K_SPACE :
                s.rotate(1)
                if not s.contains_in_box() or s.check_collisions(B.is_coloured) :
                    s.rotate(-1)
    pygame.draw.rect(scr,WHITE,(0,0,300,600))
    s.display(scr)
    s.move_rectangles(0,3)
    if not s.contains_in_box() or s.check_collisions(B.is_coloured):
        s.move_rectangles(0,-3)
        if count <2 :
            count +=1
            CLOCK.tick(60)
            continue
        B.add(s.rectangles,s.color)
        s = random.choice([square,el_left,el_right,z_left,z_right,rev_T,long_l])(120,0)
        count =0
    B.evaluation()
    B.display(scr)
    pygame.display.update()
    CLOCK.tick(60)
    