import pygame 	#importing library pygame

def checkCollision(x,y,tX,tY):
	global screen,textWin
	collisionState = False
	if y >= tY and y <= tY + 30:
		if x >= tX and x <= tX + 30:
			screen.blit(textWin, (450 - textWin.get_width()/2,350 - textWin.get_height()/2))
			x = 800 - 30/2
			y = 650
			collisionState = True
		elif x + 30 >= tX and x + 30 <= tX + 30:
			screen.blit(textWin, (450 - textWin.get_width()/2,350 - textWin.get_height()/2))
			x = 800 - 30/2
			y = 650
			collisionState = True
	elif y + 30 >= tY and y + 30 <= tY + 30:
		if x >= tX and x <= tX + 30:
			screen.blit(textWin, (450 - textWin.get_width()/2,350 - textWin.get_height()/2))
			x = 800 - 30/2
			y = 650
			collisionState = True
		elif x + 30 >= tX and x + 30 <= tX + 30:
			screen.blit(textWin, (450 - textWin.get_width()/2,350 - textWin.get_height()/2))
			x = 800 - 30/2
			y = 650
			collisionState = True

pygame.init()	#calling method init()

#setting up displa, with screen size 900x700
screen = pygame.display.set_mode((900,700))
#--------------------------------------------------------------------------------------
finished = False

x = 800 - 30/2
y = 650

#to ceck the index value of the key pressed
#print pygame.K_SPACE

#load the image 
playerImage = pygame.image.load("index.png")

#change the size of the image
playerImage = pygame.transform.scale(playerImage, (30,30))

#convert into reqd format
#playerImage = playerImage.convert()
playerImage = playerImage.convert_alpha()

#--------------------------------------------------------------------------------------
#Adding Background image
backGroundImage = pygame.image.load("images.jpeg")
backGroundImage = pygame.transform.scale(backGroundImage, (900,700))
screen.blit(backGroundImage, (0,0))

#Adding the treasure
tImage = pygame.image.load("treasure.png")
tImage = pygame.transform.scale(tImage, (30,30))
tImage = tImage.convert_alpha()

tX = 150 - 30/2
tY = 100
screen.blit(tImage, (tX,tY) )

#----------------------------------------------------------------------------------------
#Adding text
font = pygame.font.SysFont("comicsans", 60)
textWin = font.render("Great Job!", True, (0,0,0))

frame = pygame.time.Clock()

#while our game is not finished
while finished == False:
	for event in pygame.event.get():
		#pass
#---------------------------------------------------------------------------------------
		if event.type == pygame.QUIT:
			finished = True
#---------------------------------------------------------------------------------------
#to get the keys pressed during the game, stored as arrays/listsss
	pressedKeys = pygame.key.get_pressed()
				#[....,Up,DOWN,LEFT,SPACE,.....]
	if pressedKeys[pygame.K_UP] == 1:
		#y += 5     # to move up
		y -= 5		# to move down
	if pressedKeys[pygame.K_LEFT] == 1:
		x -= 5
	if pressedKeys[pygame.K_RIGHT] == 1:
		x += 5
	if pressedKeys[pygame.K_DOWN] == 1:
		y += 5
#to draw a rectangle on the screen
	#rectOne = pygame.Rect(x,y,30,30)	#(x,y,width,height)
#to define the color of the shape
#the pygame objectdraw.rect takes in an RGB value, 
#for which we create a tuple, that can take
#multiple inputs as variable
	color = (0,0,255)	#tuple-RGB
	#black = (0,0,0)	#black color to fill the screen
	white = (255,255,255)
	#screen.fill(white)
	screen.blit(backGroundImage, (0,0))
	screen.blit(tImage, (tX,tY) )
	screen.blit(playerImage, (x,y))
	
#(the screen in which you want to display, color of the shape, the shape created)
	#pygame.draw.rect(screen,color,rectOne)
#refresh/update the display to show a rectangle
	pygame.display.flip()
	frame.tick(30)
#---------------------------------------------------------------------------------------
#changes on lines above the while loop and above recOne variable
#---------------------------------------------------------------------------------------
#To move the rectangle - 
		#1. check the index of the key presses the is stored in
		#	the array presedKeys
		#2. if space/(or any key presses[as long as you know the index position])
		#	change y position
		#(see what happens then go to next step and explain the difference observed)
		#3. fill the screen with black everytime the space key is pressed
	#changes in code are as follows
	#pressedKeys = ....
	#if..........
	#color = .....
	#black....
	#....
	#pygame........
#---------------------------------------------------------------------------------------
#Loading the player
#		#1. Change the frame rate
		#	add the following line before the while loop - frame = pygame.time.Clock()
		#2. Athe the last line add frame.tck(30) -- reduces the frame rate by 1/30th of the time
		#3. to load the image, add three lines before the while loop -- starts with playerImage
		#4. insert image in the game(screen) -- use screen.blit() command
		#5. [optional] change the background to white
#---------------------------------------------------------------------------------------
#Loading the background
#		#1. Remove the background of the player image
		#	playerImage.convert_alpha()
		#2. Change the size of the player according to you requirements
		#3. Add the background image
		#	Lines added as backGroundImage
		#4. Replace the screen.fill(white) by screen.blit
		#5. Make changes to the code, to make the player move up when
		#	space key is pressed, and change the x,y coordinates for the 
		#	player
#---------------------------------------------------------------------------------------
# Checking collision
		#write this code after the last .blit inside the while loop
		#if y >= tY and y <= tY + 30:
		#	if x >= tX and x <= tX + 30:
		#		.
		#		.
		#	elif x + 30 >= tX and x + 30 <= tX + 30:
		#		.
		#		.
		#elif y + 30 >= tY and y + 30 <= tY + 30:
		#	if x >= tX and x <= tX + 30:
		#		.
		#		.
		#	elif x + 30 >= tX and x + 30 <= tX + 30:
		#		.
		#		.
#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------