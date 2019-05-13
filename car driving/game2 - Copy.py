import random 
import time
import pygame as p

p.init()

display_width=800
display_height=600
#set color
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)


gameDisplay=p.display.set_mode((display_width,display_height))
p.display.set_caption("Race Game")
clock=p.time.Clock()

#make car and barrier
carImg=p.image.load("car2.png")
car_width=100
car_height=100
barrierImg=p.image.load("barrier.png")
barrier_width=60
barrier_height=72

def car(x,y):
    gameDisplay.blit(carImg,(x,y))
    
def barrier(x,y):
    gameDisplay.blit(barrierImg,(x,y))

    
def Text_object(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()


def message_display(text,size):
    largeText=p.font.Font("freesansbold.ttf",size)
    TextSurf,TextRect=Text_object(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    
    p.display.update()
    time.sleep(2)
    p.display.update()
    #game_loop()

def crash(myScore):
    message_display("You Crash",155)
    time.sleep(2)
    gameDisplay.fill(white)
    message_display("Score"+str(myScore),70)
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                quit()
            elif event.type== p.KEYDOWN:
                if event.key == p.K_SPACE:
                     startGame()
        gameDisplay.fill(red)
        
        message_display("press space for restart ",50)
        p.display.update()
    
def game_loop():
    x=(display_width*0.4)
    y=(display_height*0.88)
    x_barrier1=random.randint(0,350-barrier_width)
    x_barrier2=random.randint(370,750-barrier_width)
    y_barrier=0
    x_change=0
    y_change=0

    myScore=0
    
    game_exit=False
    while not game_exit:
        for event in p.event.get():
            #for exit from game
            if event.type == p.QUIT:
                p.quit()
                quit()

            if event.type== p.KEYDOWN:#check if any key is press
                if event.key == p.K_LEFT:
                    x_change=-10
                if event.key == p.K_RIGHT:
                    x_change=10
            
            if event.type== p.KEYUP:#check if any key is not press (lift up key) key press
                if event.key == p.K_LEFT or event.key == p.K_RIGHT:
                    x_change=0
                
        x +=x_change
        #increasing hardness of game 
        if(myScore<100):
            y_barrier+=8
        elif(myScore<150):
            y_barrier+=10
        elif(myScore<200):
            y_barrier+=15
        else:
            y_barrier+=20

        
        gameDisplay.fill(white)
        barrier(x_barrier1,y_barrier)
        barrier(x_barrier2,y_barrier)
        #show car   
        car(x,y)
        #for new barrier
        if(y_barrier>display_height-barrier_height):
            x_barrier1=random.randint(0,350-barrier_width)
            x_barrier2=random.randint(370,750-barrier_width)
            y_barrier=0
            myScore+=10 
        #checking if car is out of the window then out
        if(x> display_width-car_width or x<0):
            crash(myScore)

        #checking if car is touching barrier or not 
        barrier1=((x>=x_barrier1 and x<=x_barrier1+barrier_width)or(x+car_width>=x_barrier1 and x+car_width<=x_barrier1+barrier_width))
        barrier2=((x>=x_barrier2 and x<=x_barrier2+barrier_width)or(x+car_width>=x_barrier2 and x+car_width<=x_barrier2+barrier_width))
        b2=((y>=y_barrier and y<=y_barrier+barrier_height)or(y+car_height>=y_barrier and y+car_height<=y_barrier+barrier_height))
        if((barrier1 or barrier2) and b2):
            crash(myScore)
   
        p.display.update()
        clock.tick(30)


#game_loop()
def startGame():
    start_game=False
    while not start_game:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                quit()
            if event.type== p.KEYDOWN or event.type== p.KEYUP:
                game_loop()
        gameDisplay.fill(white)
        message_display("press any key",50)
        p.display.flip()
        clock.tick(30)



startGame()




p.quit()
quit()
