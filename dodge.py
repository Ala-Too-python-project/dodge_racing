import pygame
import time
import random

pygame.init()

display_width=800
display_height=600

black=(0,0,0)
white=(255,255,255)

red=(150,0,0)
green=(0,150,0)
blue=(0,0,255)
light_red=(255,0,0)
light_green=(0,255,0)

pause=False

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Dodge race")
clock=pygame.time.Clock()

car_image=pygame.image.load("nsx.png")
icon_image=pygame.image.load("bgr.jpg")
pygame.display.set_icon(icon_image)

def things_dodged(count):
	font=pygame.font.SysFont(None,30)
	text=font.render("Dodged: "+str(count), True, green)
	gameDisplay.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh,color):
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def car(x,y):
	gameDisplay.blit(car_image,(x,y))

def text_objects(text,font,color):
	textSurface=font.render(text, True, color)
	return textSurface,textSurface.get_rect()

def message_display(text):
	largeText=pygame.font.Font(None,120)
	TextSurf,TextRect =text_objects(text,largeText,red)
	TextRect.center=((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	pygame.display.update();
	time.sleep(1)
	game_loop()
	
def button(text,color,acolor,x,y,w,h,action=None):
	mouse=pygame.mouse.get_pos()
	click=pygame.mouse.get_pressed()
	#print(click)
	if mouse[0]<x+w and mouse[0]>x and mouse[1]<y+h and mouse[1]>y:
		pygame.draw.rect(gameDisplay,acolor,(x,y,w,h))
		if click[0]==1 and action != None:
			action()
	else:
		pygame.draw.rect(gameDisplay,color,(x,y,w,h))
	smallText=pygame.font.Font("freesansbold.ttf",25)
	TextSurf,TextRect=text_objects(text,smallText,black)
	TextRect.center=((x+w/2),(y+h/2))
	gameDisplay.blit(TextSurf,TextRect)
	
def crash():
	largeText=pygame.font.Font("freesansbold.ttf",70)
	TextSurf,TextRect =text_objects("YOU CRASHED",largeText,blue)
	TextRect.center=((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		button("PLAY AGAIN!",red,light_red,200,450,160,50,game_loop)
		button("Quit",green,light_green,500,450,100,50,quit)

		pygame.display.update()
		clock.tick(70)
def game_intro():
	intro=True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			gameDisplay.fill(white)
			largeText=pygame.font.Font("freesansbold.ttf",100)
			TextSurf,TextRect =text_objects("CAR RASH",largeText,black)
			TextRect.center=((display_width/2),(display_height/2))
			gameDisplay.blit(TextSurf,TextRect)
			button("Play",red,light_red,200,450,100,50,game_loop)
			button("Quit",green,light_green,500,450,100,50,quit)

			pygame.display.update()
			clock.tick(70)

def unpause():
	global pause
	pause=False

def paused():
	global pause
	pause=True
	largeText=pygame.font.Font("freesansbold.ttf",70)
	TextSurf,TextRect =text_objects("PAUSED",largeText,black)
	TextRect.center=((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		button("CONTINUE",red,light_red,200,450,160,50,unpause)
		button("Quit",green,light_green,500,450,100,50,quit)

		pygame.display.update()
		clock.tick(70)


def game_loop():
		x=(display_width * 0.40)
		y=(display_height * 0.767)
		i=0
		car_width=120
		x_change=0
		dodged=0

		thing_width=100
		thing_startx=random.randrange(0,display_width-thing_width)
		thing_starty=-600
		thing_speed=4
		thing_height=100

		crashed=False
