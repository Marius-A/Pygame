import pygame
import time
import random
 
pygame.init()


display_width = 1360
display_height = 755
 
black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue= (0,0,255)
 
 
car_width = 50
car_height = 100
 
gameDisplay = pygame.display.set_mode((display_width,display_height),pygame.FULLSCREEN)
pygame.display.set_caption('Toy car on street!')
clock = pygame.time.Clock()

#load sprites
#--------------------------------------------------
gameIcon = pygame.image.load('carIcon.png')

carImg = pygame.image.load('racecar.png')

en_carImg = pygame.image.load('policecar_left.png')
en_carImg2 = pygame.image.load('policecar_right.png')

bg_img1=pygame.image.load("bg.png").convert_alpha()
bg_img2=pygame.image.load("bg.png").convert_alpha()

men_img=pygame.image.load("bg.png").convert_alpha()
#--------------------------------------------------

#set game icon
#----------------------------------------
pygame.display.set_icon(gameIcon)
#----------------------------------------


pause = False
crash = True
 
#functions
#----------------------------------------------------------------

def other_cars_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged: "+str(count), True, white)
    gameDisplay.blit(text,(0,0))
 
def other_cars(x,y,sprite):
    gameDisplay.blit(sprite,(x,y))
 
def car(x,y):
    gameDisplay.blit(carImg,(x,y))
 
def text_objects(text, font):
    textSurface = font.render(text, True,bright_blue)
    return textSurface, textSurface.get_rect()
 
 
def crash():
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Play Again",display_width/2-200,450,100,50,green,bright_green,game_loop)
        button("Quit",display_width /2+100,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15) 

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
        
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False
    

def paused():
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue",display_width/2-200,450,100,50,green,bright_green,unpause)
        button("Quit",display_width /2+100,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)   


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.blit(men_img, (0, 0))
        
        largeText = pygame.font.SysFont("comicsansms",100)
        TextSurf, TextRect = text_objects("   Toy cars on street  ", largeText)
        TextRect.center = ((display_width/2),(display_height/2-100))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",display_width/2-200,450,100,50,green,bright_green,game_loop)
        button("Quit",display_width/2+100,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause

    x = (display_width * 0.45)
    y = (display_height * 0.8)
 
    x_change = 0
    y_change = 0
    sp_bg =5
    other_cars_startx = random.randrange(100, display_width-100)
    other_cars_starty = 0
    
    
    other_cars_width = 50
    other_cars_height = 100
 
    other_carsCount = 1
 
    dodged = 0
 
    gameExit = False
    
    y_b=0
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
#read key events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()
                if event.key == pygame.K_SPACE:
                    y_change = -2
                    
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_SPACE:
                    if y <display_height-100:
                        y_change = 1
                        if y >= display_height/2:
                            if sp_bg >= 5:
                                sp_bg -= 1
                                

        if y>=display_height-50:
            y_change=0

        x += x_change
        y += y_change
        
        if y >= display_height-150:
            y=display_height-150

        
        if y <= display_height/2:
            y=display_height/2
            if sp_bg <=10:
                sp_bg+=1

        gameDisplay.blit(bg_img1, (0,y_b))
        gameDisplay.blit(bg_img2,(0,y_b-display_height ))
        
#update background speed
        y_b = y_b + sp_bg

#car must not exceed half the screen
        if y_b >= display_height:
            y_b = 0

        if other_cars_startx < display_width/2:
            other_cars(other_cars_startx, other_cars_starty,en_carImg)
            other_cars_speed = 6
        else:
            other_cars(other_cars_startx, other_cars_starty,en_carImg2)	
            other_cars_speed = 2

        if y <= display_height/2:
            if other_cars_startx < display_width/2:
                if  other_cars_speed <= 12:
                    other_cars_speed += 1
            else:
                if  other_cars_speed <= 4:
                    other_cars_speed +=1
                    
#update car position
        other_cars_starty += other_cars_speed
        
#create cars
        car(x,y)
        other_cars_dodged(dodged)
 #border 
        if x >= display_width - car_width -50:
            x= display_width - car_width - 50
        if x <= car_width:
            x=car_width
 
        if other_cars_starty > display_height:
            other_cars_starty = 0 - other_cars_height
            other_cars_startx = random.randrange(100,display_width-100)
            dodged += 1
            other_cars_speed += 0.0005
            
 
#check colision
        if x > other_cars_startx and x < other_cars_startx + other_cars_width or x+car_width > other_cars_startx and x + car_width < other_cars_startx+other_cars_width:
            if y < other_cars_starty+other_cars_height and y+car_height > other_cars_starty: 
                crash()
        
        pygame.display.update()
        clock.tick(120)

game_intro()
game_loop()
pygame.quit()
quit()
