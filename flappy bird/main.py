import pygame as p
import random
import time
p.init()
#display size
display_width=800
display_height=600
gameDisplay=p.display.set_mode((display_width,display_height))
p.display.set_caption("Flappt bird by Rahul")
clock=p.time.Clock()
#set color
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,128,0)
#set bird
birdImg=p.image.load("bird.jpg")
bird_width=71
bird_height=53
pipe_width=100
def bird(x,y):
    gameDisplay.blit(birdImg,(x,y))
def pipes(x,y):
    p.draw.rect(gameDisplay,green,[x,0,pipe_width,y])
    p.draw.rect(gameDisplay,green,[x,y+300,pipe_width,display_height])
def Text_object(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def message_display(text):
    largeText=p.font.Font("freesansbold.ttf",100)
    TextSurf,TextRect=Text_object(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    p.display.flip()
    time.sleep(2)
    game_loop()
def crash():
    message_display("you crashed")
def game_loop():
    bird_y=(display_height/2)
    bird_x=(display_width*0.15)
    game_exit=False
    pipe_x1=900
    pipe_x2=450
    pipe_y1= random.randrange(100,200)
    pipe_y2= random.randrange(100,200)
    while not game_exit:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                quit()
            if event.type == p.KEYDOWN:
                if event.key == p.K_UP:
                    bird_y-=110
                if(event.key==p.K_DOWN):
                    bird_y+=75
        bird_y+=10
        pipe_x1-=10
        pipe_x2-=10
        gameDisplay.fill(white)
        bird(bird_x,bird_y)
        pipes(pipe_x1,pipe_y1)
        pipes(pipe_x2,pipe_y2)
        
        if(bird_y<bird_height-10 or bird_y>display_height-bird_height-10):#and bird_y>display_height-bird_height):
            crash()
        b1=(bird_x+bird_width>=pipe_x1 and  bird_x+bird_width<=pipe_x1+pipe_width) and (bird_y+bird_height<=pipe_y1 and bird_y>=pipe_y1+300)
        b2=(bird_x+bird_width>=pipe_x2 and bird_x+bird_width<=pipe_x2+pipe_width) and (bird_y+bird_height<=pipe_y2 and bird_y+bird_height>=pipe_y2+300)
        if(b1 or b2):
            crash()
        if(pipe_x1<-100):
            pipe_x1=900
            pipe_y1= random.randrange(100,300)
        if(pipe_x2<-100):
            pipe_x2=900
            pipe_y2= random.randrange(100,300)
        p.display.update()
        clock.tick(10)
#crash()
game_loop()
