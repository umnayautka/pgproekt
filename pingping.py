from pygame import *

screen = display.set_mode((800,600))
display.set_caption('ФпсПонг')
screen.fill((0,0,255))

clock = time.Clock()
game = True
while game:
    clock.tick(60)
    for e in event.get():
        if e.type == QUIT:
            game = False 

display.update()