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
