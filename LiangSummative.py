# Name: Lawrence Liang
# Mar 30 2021
# Class ICS3U1-03
# Description: Summative Assignment

import pygame, random, math

#Window display
pygame.init()
width = 800
height = 600
SIZE = (width, height)
screen = pygame.display.set_mode(SIZE)

#Colours
WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = (252, 15, 3)
YELLOW = 234, 237, 31
LIGHTGREEN = 51, 201, 42
GREEN = 4, 189, 9
DARKGREEN = 2, 168, 7
BLUE = 7, 147, 222
LIGHTSKYBLUE = 157, 219, 252
SKYBLUE = 99, 201, 255
CYAN = 66, 189, 255
DARKBLUE = 23, 94, 122
TAN = 242, 213, 191
BROWN = 140, 100, 76
GREY = 197, 198, 199
DARKGREY = 117, 117, 117

def drawCharacterDown(colour,location,yValue):
   #Placeholder for attacking 
   if colour == 1:
      #Body
      pygame.draw.rect(screen,BLUE,(location-25,yValue-95,50,45),0)
      #Head
      pygame.draw.circle(screen, TAN, (location, yValue - 100), 25)
      #eyes
      pygame.draw.line(screen,BLACK,(location-10,yValue-95),(location-10,yValue - 115),5)
      pygame.draw.line(screen,BLACK,(location+10,yValue-95),(location+10,yValue - 115),5)
      #Arms
      pygame.draw.line(screen,TAN,(location-28,yValue-65),(location-28,yValue - 95),1)
      pygame.draw.line(screen,TAN,(location+28,yValue-65),(location+28,yValue - 95),1)
   if colour == 2:
      #Arms
      pygame.draw.arc(screen,TAN,(location-40,yValue-95,30,40),math.pi//2,2*math.pi)  
      pygame.draw.arc(screen,TAN,(location+5,yValue-95,30,40),-math.pi//2,math.pi) 
      pygame.draw.rect(screen,DARKGREY,pygame.Rect(location+5,yValue-95,20,40))
      #Body
      pygame.draw.rect(screen,BLUE,(location-25,yValue-95,50,40),0)
      pygame.draw.circle(screen, TAN, (location, yValue - 100), 25)      
      #Leg
      pygame.draw.line(screen,DARKBLUE,(location-15,yValue-55),(location-15,yValue-30),20)
      pygame.draw.line(screen,DARKBLUE,(location+15,yValue-55),(location+15,yValue-30),20)      
      #Tool/recycler
      pygame.draw.rect(screen,GREEN,(location-25,yValue-75,50,30),0)
      pygame.draw.rect(screen,YELLOW,(location-25,yValue-45,50,5),0)
      recyclePic = pygame.image.load("recyclingSymbol.png")
      screen.blit(recyclePic, pygame.Rect(location-25,yValue-75,50,30))      
      #eyes
      pygame.draw.line(screen,BLACK,(location-10,yValue-95),(location-10,yValue - 115),5)
      pygame.draw.line(screen,BLACK,(location+10,yValue-95),(location+10,yValue - 115),5)      
def drawCharacterLeft(colour,location,yValue):
   #Placeholder for attacking 
   if colour == 1:
      pygame.draw.rect(screen,DARKGREY,(location-25,yValue-95,50,40),0)
      pygame.draw.rect(screen,BLUE,(location-25,yValue-95,50,40),0)
      pygame.draw.circle(screen, TAN, (location, yValue - 100), 25)
      #eyes
      pygame.draw.line(screen,BLACK,(location-10,yValue-95),(location-10,yValue - 115),5)

def drawCharacterRight(colour,location,yValue):
   #Placeholder for attacking 
   if colour == 1:
      pygame.draw.rect(screen,DARKGREY,(location-25,yValue-95,50,40),0)
      pygame.draw.rect(screen,BLUE,(location-25,yValue-95,50,40),0)
      pygame.draw.circle(screen, TAN, (location, yValue - 100), 25)
      #eyes
      pygame.draw.line(screen,BLACK,(location+10,yValue-95),(location+10,yValue - 115),5)

def drawCharacterUp(colour,location,yValue):
   #Placeholder for attacking 
   if colour == 1:
      pygame.draw.circle(screen, TAN, (location, yValue - 100), 25)
      pygame.draw.rect(screen,BLUE,(location-25,yValue-95,50,30),0)

#Animated leg movement
def legs (location,yValue):
   pygame.draw.line(screen,DARKBLUE,(location-15,yValue-55),(location-15,yValue-20),20)
   pygame.draw.line(screen,DARKBLUE,(location+15,yValue-55),(location+15,yValue-30),20)   
def legsUp (location,yValue):
   pygame.draw.line(screen,DARKBLUE,(location-15,yValue-55),(location-15,yValue-30),20)
   pygame.draw.line(screen,DARKBLUE,(location+15,yValue-55),(location+15,yValue-20),20)      

def enemy(enemyX,enemyY,enemyHealth,still): 
   #pygame.draw.rect(screen,RED, pygame.Rect(enemyX-20, enemyY-120,90,80)) #reference for hitbox of enemy
   pygame.draw.rect(screen, GREY, pygame.Rect(enemyX, enemyY - 100,50,40), 0)
   #ARMS
   pygame.draw.line(screen,BLACK,(enemyX,enemyY-90),(enemyX-20,enemyY-50),5)
   pygame.draw.line(screen,BLACK,(enemyX+50,enemyY-90),(enemyX+70,enemyY-50),5)
   #Monitor
   pygame.draw.rect(screen,SKYBLUE,(enemyX+5, enemyY-95,40,30),0)
   #Cracked screen
   pygame.draw.line(screen,DARKBLUE,(enemyX+15, enemyY-75), (enemyX+15, enemyY-95),5)
   pygame.draw.line(screen,DARKBLUE,(enemyX+15, enemyY-75), (enemyX+8, enemyY-70),5)
   #Eyebrows of computer
   pygame.draw.line(screen,BLACK,(enemyX+5,enemyY-95),(enemyX+20,enemyY-80),5)
   pygame.draw.line(screen,BLACK,(enemyX+45,enemyY-95),(enemyX+30,enemyY-80),5)     
   if still == False:
      if enemyPosition[enemyXCounter] >= x:
         enemyPosition[enemyXCounter] -=3
      if enemyPosition[enemyXCounter] <= x:
         enemyPosition[enemyXCounter] +=3      
      if enemyHealth >=0:
         return enemyHealth
      if enemyHealth <= 0:
         return enemyHealth

def enemyUp(enemyX,enemyY,enemyHealth,still): 
   #pygame.draw.rect(screen,RED, pygame.Rect(enemyX-20, enemyY-120,90,80)) #reference for hitbox of enemy
   pygame.draw.rect(screen, GREY, pygame.Rect(enemyX, enemyY - 100,50,40), 0)
   #ARMS
   pygame.draw.line(screen,BLACK,(enemyX,enemyY-90),(enemyX-20,enemyY-50),5)
   pygame.draw.line(screen,BLACK,(enemyX+50,enemyY-90),(enemyX+70,enemyY-50),5)
   #Monitor
   pygame.draw.rect(screen,SKYBLUE,(enemyX+5, enemyY-95,40,30),0)
   #Cracked screen
   pygame.draw.line(screen,DARKBLUE,(enemyX+15, enemyY-75), (enemyX+15, enemyY-95),5)
   pygame.draw.line(screen,DARKBLUE,(enemyX+15, enemyY-75), (enemyX+8, enemyY-70),5)
   #Eyebrows of computer
   pygame.draw.line(screen,BLACK,(enemyX+5,enemyY-95),(enemyX+20,enemyY-80),5)
   pygame.draw.line(screen,BLACK,(enemyX+45,enemyY-95),(enemyX+30,enemyY-80),5)     
   if still == False:
      if enemyPosition[enemyYCounter] >= y:
         enemyPosition[enemyYCounter] -=1
      if enemyPosition[enemyYCounter] <= y:
         enemyPosition[enemyYCounter] +=1      
      if enemyHealth >=0:
         return enemyHealth
      if enemyHealth <= 0:
         return 0

def smartEnemy(enemyX,enemyY,enemyHealth,still):  
   pygame.draw.rect(screen, GREY, pygame.Rect(enemyX, enemyY - 100,50,40), 0) 
   #ARMS
   pygame.draw.line(screen,BLACK,(enemyX,enemyY-90),(enemyX-20,enemyY-80),5)
   pygame.draw.line(screen,BLACK,(enemyX+50,enemyY-90),(enemyX+70,enemyY-80),5)
   #Monitor
   pygame.draw.rect(screen,DARKGREEN,(enemyX+5, enemyY-95,40,30),0)
   #Cracked screen
   pygame.draw.line(screen,DARKBLUE,(enemyX+15, enemyY-75), (enemyX+15, enemyY-95),5)
   pygame.draw.line(screen,DARKBLUE,(enemyX+15, enemyY-75), (enemyX+8, enemyY-70),5)   
   #Eyebrows of computer
   pygame.draw.line(screen,BLACK,(enemyX+5,enemyY-80),(enemyX+20,enemyY-95),5)
   pygame.draw.line(screen,BLACK,(enemyX+45,enemyY-80),(enemyX+30,enemyY-95),5)
   #Enemy tracking
   if still == False:
      if enemyPosition[enemyXCounter] >= x and enemyPosition[enemyYCounter] >= y:
         enemyPosition[enemyXCounter] -=2
         enemyPosition[enemyYCounter] -=2
      if enemyPosition[enemyXCounter] <= x and enemyPosition[enemyYCounter] >= y:
         enemyPosition[enemyXCounter] +=2  
         enemyPosition[enemyYCounter] -=2  
      if enemyPosition[enemyXCounter] >= x and enemyPosition[enemyYCounter] <= y:
         enemyPosition[enemyXCounter] -=2  
         enemyPosition[enemyYCounter] +=2
      if enemyPosition[enemyXCounter] <= x and enemyPosition[enemyYCounter] <= y:
         enemyPosition[enemyXCounter] +=2
         enemyPosition[enemyYCounter] +=2      
      if enemyHealth >=0:
         return enemyHealth
      if enemyHealth <= 0:
         return 0

def bossEnemy (bossX,bossY):
   pygame.draw.rect(screen,BLACK,pygame.Rect(bossX-10,bossY-110,220,170))
   pygame.draw.rect(screen,GREY,pygame.Rect(bossX,bossY-100,200,150)) 
   #Eyeball
   pygame.draw.circle(screen,WHITE,(bossX+50,bossY-50),35)
   pygame.draw.circle(screen,BLACK,(bossX+50,bossY-50),5)   
   pygame.draw.circle(screen,WHITE,(bossX+150,bossY-50),35)
   pygame.draw.circle(screen,BLACK,(bossX+150,bossY-50),5)
   #panelling
   pygame.draw.line(screen,DARKGREY,(bossX+10,bossY),(bossX+10,bossY-30),5)
   pygame.draw.line(screen,DARKGREY,(bossX+170,bossY+30),(bossX+170,bossY+10),5)
   #Eyebrow
   pygame.draw.line(screen,BLACK,(bossX,bossY-100),(bossX+100,bossY-70),20)
   pygame.draw.line(screen,BLACK,(bossX+200,bossY-100),(bossX+100,bossY-70),20)
   
   #Exposed circuit
   #reference for hitbox of enemy
   pygame.draw.rect(screen,GREEN,pygame.Rect(bossX+50,bossY,100,50))
   pygame.draw.line(screen,YELLOW,(bossX+50,bossY+10,),(bossX+70,bossY+10),5)   
   pygame.draw.line(screen,YELLOW,(bossX+70,bossY+10,),(bossX+90,bossY+20),5)  
   pygame.draw.line(screen,YELLOW,(bossX+120,bossY+10,),(bossX+140,bossY+10),5)   
   pygame.draw.line(screen,YELLOW,(bossX+120,bossY+10,),(bossX+110,bossY+20),5)     
   pygame.draw.line(screen,YELLOW,(bossX+80,bossY+30,),(bossX+80,bossY+50),5)
   pygame.draw.circle(screen,RED,(bossX+90,bossY+30),3)
   pygame.draw.circle(screen,RED,(bossX+120,bossY+30),3)
   pygame.draw.circle(screen,SKYBLUE,(bossX+140,bossY+10),3)
   if bossHp == 0:
      return 0

def drawTaskBar():
   #Player stats
   pygame.draw.rect(screen, BLACK, (0, 0, width, height//5))
   pygame.draw.rect(screen,GREY,(10,10,width//3,height//6))
   pygame.draw.rect(screen,GREY,(300,10,width//3,height//6))    
   #Health
   timerText = fontTimer.render("          -Health-" , 1, RED)
   screen.blit(timerText, pygame.Rect(10,10,width//3,height//6))
   #Timer
   pygame.draw.rect(screen,YELLOW,(590,10,width//4,height//6))
   timerText = fontTimer.render("       -Timer- " , 1, RED)
   screen.blit(timerText, pygame.Rect(590,10,width//4,height//6))
   #Inventory
   inventoryText = fontTimer.render("       -Inventory- " , 1, RED)
   screen.blit(inventoryText, pygame.Rect(300,10,width//3,height//6)) 
   #number of defeated enemies
   numDefeatedText = fontTimer.render(str(itemCounter) , 1, LIGHTGREEN)
   screen.blit(numDefeatedText, pygame.Rect(350,50,width//3,height//6))
   #numbe of item collected
   numItemText = fontTimer.render(str(itemCollected) , 1, BLUE)
   screen.blit(numItemText, pygame.Rect(width//1.9,50,width//3,height//6))
   
   #defeated enemies text
   defeatedNameText = itemFont.render(itemList[2] , 1, LIGHTGREEN)
   screen.blit(defeatedNameText, pygame.Rect(320,80,width//3,height//6))  
   
   #item text
   itemNameText = itemFont.render(itemList[1] , 1, BLUE)
   screen.blit(itemNameText, pygame.Rect(width//1.99,80,width//3,height//6))
   
def drawItemClock (clockX,clockY):
   pygame.draw.circle(screen,YELLOW,(clockX,clockY),20)
   pygame.draw.circle(screen,WHITE,(clockX,clockY),15)

def drawItemHeart (heartX,heartY):
   pygame.draw.circle(screen,RED,(heartX,heartY),20)
   
def displayItemWindow (windowX,windowY,item):
   pygame.draw.rect(screen,GREY,(windowX+20,windowY,100,20))
   statText = itemFont.render((item), 1, BLACK) 
   screen.blit(statText, pygame.Rect(windowX+20,windowY,100,20))        
   pygame.display.flip()   

def wall(wallX,wallY,wallSizeX,wallSizeY):
   pygame.draw.rect(screen,BROWN,(wallX//2.6,wallY//2,wallSizeX,wallSizeY))

def startMenu():
   backgroundPic = pygame.image.load("WasteBackground.png") # done once
   screen.blit(backgroundPic, pygame.Rect(0,0,width,height))   
   pygame.display.set_caption("E-Waste Dungeon: Environment Theme")
   
   #Title
   pygame.draw.rect(screen,BLUE,pygame.Rect(width//2-230,height//4,width//1.8,height//10))
   titleText = titleFont.render("SAVE THE EARTH!", 1, LIGHTGREEN) 
   screen.blit(titleText, pygame.Rect(width//2-230,height//4,width//4,height//6))  
   
   escText = escFont.render("Press Escape(esc) to exit game", 1, RED) 
   screen.blit(escText, pygame.Rect(width//1.6,height//1.11,100,100))    
   
   mouseWidth, mouseHeight = pygame.mouse.get_pos()
   mousePress = pygame.mouse.get_pressed()[0]   
   #start Button
   pygame.draw.rect(screen,RED,(width//2-80,height//2,150,100))
   startButton=pygame.Rect(width//2-80,height//2,150,100)
   startText = startFont.render("PLAY", 1, BLACK) 
   screen.blit(startText, pygame.Rect(width//2-55,height//1.8,150,100)) 
   
   #How to play button
   pygame.draw.rect(screen,RED,(width//2-80,height//1.4,150,100))
   howToButton=pygame.Rect(width//2-80,height//1.4,150,100)
   howToText = howToFont.render("HOW", 1, BLACK) 
   screen.blit(howToText, pygame.Rect(width//2-35,height//1.35,150,100))    
   howToText = howToFont.render("TO PLAY", 1, BLACK) 
   screen.blit(howToText, pygame.Rect(width//2-45,height//1.25,150,100))   
   #if player presses start button
   if startButton.collidepoint(mouseWidth,mouseHeight):
      pygame.draw.rect(screen,YELLOW,(width//2-80,height//2,150,100))
      startText = startFont.render("PLAY", 1, WHITE) 
      screen.blit(startText, pygame.Rect(width//2-55,height//1.8,150,100))       
      if evnt.type == pygame.MOUSEBUTTONDOWN:
         mouseWidth, mouseHeight = evnt.pos
         mouseButton = evnt.button 
         buttonPressSound.play()
         return False
   #if player presses how to button
   if howToButton.collidepoint(mouseWidth,mouseHeight):
      pygame.draw.rect(screen,YELLOW,(width//2-80,height//1.4,150,100))
      howToText = howToFont.render("HOW", 1, WHITE) 
      screen.blit(howToText, pygame.Rect(width//2-35,height//1.35,150,100))
      howToText = howToFont.render("TO PLAY", 1, WHITE) 
      screen.blit(howToText, pygame.Rect(width//2-45,height//1.25,150,100))      
      if evnt.type == pygame.MOUSEBUTTONDOWN:
         buttonPressSound.play()
         return True   

def instructionsMenu():
   screen.fill(WHITE)
   #mouse x and y points
   mouseWidth, mouseHeight = pygame.mouse.get_pos()
   mousePress = pygame.mouse.get_pressed()[0]   

   #play Button
   pygame.draw.rect(screen,RED,(width//1.3,height//60,250,100))
   playButton=pygame.Rect(width//1.2,height//60,150,100)
   playText = startFont.render("PLAY", 1, BLACK) 
   screen.blit(playText, pygame.Rect(width//1.2,height//60,150,100)) 
   instructionsText = titleFont.render("How to Play: ", 1, LIGHTGREEN) 
   pygame.draw.rect(screen,DARKBLUE,(width//80,height//60,300,60))
   screen.blit(instructionsText, pygame.Rect(width//80,height//60,150,100))   
   #Keys
   wKeyText = keyFont.render("W: UP", 1, BLUE) 
   screen.blit(wKeyText, pygame.Rect(width//8,height//6,150,100))  
   SKeyText = keyFont.render("S: DOWN", 1, BLUE) 
   screen.blit(SKeyText, pygame.Rect(width//8,height//4,150,100))  
   AKeyText = keyFont.render("A: LEFT", 1, BLUE) 
   screen.blit(AKeyText, pygame.Rect(width//8,height//3,150,100))  
   DKeyText = keyFont.render("D: RIGHT", 1, BLUE) 
   screen.blit(DKeyText, pygame.Rect(width//8,height//2.4,150,100))   
   jKeyTextOne = keyFont.render("J: Attack", 1, RED) 
   screen.blit(jKeyTextOne, pygame.Rect(width//2,height//6,150,100))    
   jKeyTextTwo = keyFont.render("/Picking Up E-Waste", 1, RED)
   screen.blit(jKeyTextTwo, pygame.Rect(width//2,height//4.5,150,100)) 
   kKeyText = keyFont.render("K: Use Special items", 1, GREEN)
   screen.blit(kKeyText, pygame.Rect(width//2,height//3,150,100))    
   
   #wall
   wall(width//4,height//1.5+200,200,50)
   mudText = bossFont.render("Mud/Battery Acid: ", 1, RED)
   screen.blit(mudText, pygame.Rect(width//13.5,height//1.7,150,100))    
   mudText = bossFont.render("Slow down player movement. ", 1, RED)
   screen.blit(mudText, pygame.Rect(width//13.5,height//1.6,150,100))    
   #Different enemy types
   enemyText = bossFont.render("Cracked Monitor: ", 1, RED)
   screen.blit(enemyText, pygame.Rect(width//13.5,height//1.3,150,100))      
   enemy(width//11,height//1.2,enemiesHp,True) 
   enemyText = bossFont.render("Only move in one direction.",1,RED)
   screen.blit(enemyText, pygame.Rect(width//17.5,height//1.25,150,100))
   
   enemyText = bossFont.render("Smartphone: ", 1, RED)
   screen.blit(enemyText, pygame.Rect(width//3,height//1.3,150,100))      
   enemyText = bossFont.render("Can move any direction.", 1, RED)
   screen.blit(enemyText, pygame.Rect(width//3.5,height//1.25,150,100))   
   smartEnemy(width//3,height//1.2,enemiesHp,True) 
   
   #Boss enemy
   enemyText = bossFont.render("Broken Mircowave:", 1, GREEN)
   screen.blit(enemyText, pygame.Rect(width//2,height//1.3,150,100)) 
   enemyText = bossFont.render("Has a large Hp, heals if you attack anywhere else", 1, GREEN)
   screen.blit(enemyText, pygame.Rect(width//2,height//1.25,150,100))    
   enemyText = bossFont.render("besides the exposed circuit.", 1, GREEN)
   screen.blit(enemyText, pygame.Rect(width//2,height//1.2,150,100))       
   bossEnemy(width//2,height//1.5)
   
   #items
   drawItemHeart(width//11,height//1.1)
   itemStatText = bossFont.render(itemHeartStats, 1, RED)
   screen.blit(itemStatText, pygame.Rect(width//8,height//1.1,150,100))    
   
   drawItemClock(width//3,height//1.1)
   itemStatText = bossFont.render(itemClockStats, 1, RED)
   screen.blit(itemStatText, pygame.Rect(width//2.8,height//1.1,150,100))      
   #If player press play
   if playButton.collidepoint(mouseWidth,mouseHeight):
      pygame.draw.rect(screen,YELLOW,(width//1.3,height//60,250,100))
      startText = startFont.render("PLAY", 1, WHITE) 
      screen.blit(startText, pygame.Rect(width//1.2,height//60,150,100))       
      if evnt.type == pygame.MOUSEBUTTONDOWN:
         mouseWidth, mouseHeight = evnt.pos
         mouseButton = evnt.button 
         buttonPressSound.play()
         return False   
def gameOver():
   screen.fill(GREY)
   earthDyingPic = pygame.image.load("GameOver.png")
   screen.blit(earthDyingPic, pygame.Rect(0,0,width,height))   
   gameOverText = fontTimer.render("GAME OVER", 1, BLACK) 
   screen.blit(gameOverText, pygame.Rect(width//2-100,height//2,width//4,height//6)) 
   
   #mouse positions 
   mouseWidth, mouseHeight = pygame.mouse.get_pos()
   mousePress = pygame.mouse.get_pressed()[0]   
   
   #restart Button
   pygame.draw.rect(screen,RED,(width//2-80,height//1.5,150,100))
   restartButton=pygame.Rect(width//2-80,height//1.5,150,100)
   restartText = startFont.render("QUIT", 1, BLACK) 
   screen.blit(restartText, pygame.Rect(width//2-55,height//1.8+100,150,100)) 
   
   winText = fontTimer.render("Your Score: "+str(score), 1, RED) 
   screen.blit(winText, pygame.Rect(width//2-100,height//2+50,width//4,height//6)) 
   
   resText = escFont.render("Press r to restart game", 1, RED) 
   screen.blit(resText, pygame.Rect(width//1.6,height//1.11,100,100))
   
   if restartButton.collidepoint(mouseWidth,mouseHeight):
      pygame.draw.rect(screen,YELLOW,(width//2-80,height//1.5,150,100))
      restartText = startFont.render("QUIT", 1, WHITE) 
      screen.blit(restartText, pygame.Rect(width//2-55,height//1.8+100,150,100))       
      if evnt.type == pygame.MOUSEBUTTONDOWN:
         mouseWidth, mouseHeight = evnt.pos
         mouseButton = evnt.button 
         return False
   pygame.display.flip()    

#Text
fontTimer = pygame.font.SysFont("Arial",30)
itemFont = pygame.font.SysFont("Arial",11)
bossFont = pygame.font.SysFont("Arial",15)

#start menu fonts
titleFont = pygame.font.SysFont("Arial",50)
startFont = pygame.font.SysFont("Arial",40)
escFont = pygame.font.SysFont("Arial",20)
keyFont = pygame.font.SysFont("Arial",40)
howToFont = pygame.font.SysFont("Arial",20)
#Sound collection
pickUpSound = pygame.mixer.Sound("pickUp.wav")
buttonPressSound = pygame.mixer.Sound("buttonPress.wav")
enemyDefeatedSound = pygame.mixer.Sound("EnemyDefeatedPickUp.wav")

#On and off switches to turn off loop or main if statements
running = True
switch = False
enemyDefeated = False
fiveWave = True

#GUI boolean values
startGUI = True
instructionGUI = False

#player game states
key_left = False
key_right = False
key_up = False
key_down = False

playerWon = False

myClock = pygame.time.Clock()
running = True
bodyCollected = True

#Item boolean values
itemClockCollected = True
itemHeartCollected = True

#Showing different character look
colour = 1

playerHp = 500

# enemy boss components
bossHp = 200
bossLimit = 200
bossPosition = [500,300]
bossPoints = 0

#All List

# item list from a file
itemList = []
itemFile = open("item.txt","r")

for line in itemFile:
   item= line.rstrip("\n")  
   itemList.append(item)
   if line == "":
      break
itemFile.close()

#Enemy types 
enemiesHp = [100,0]
smartEnemiesHp = [150,0]
enemyPosition = [10,400,600,500,480,500,0,0]

#Positions of special items / objects
itemClockPositions = [random.randint(200,600),random.randint(200,400),0,0]
itemHeartPositions = [random.randint(200,600),random.randint(200,400),0,0]

wallPosition = [random.randint(100,1600),random.randint(200,800)]
randomWallList = [random.randint(100,200),random.randint(50,250)]

itemCollected = 0

#Player starting point
x = width//2
y = height//2

#Counter variables for enemies X and y Values
legCounter = 0
enemyXCounter = 0
enemyYCounter = 1
enemyHpCounter = 0

itemCounter = 0
waveCounter = 1
numOfDefeated = 0

clockCounter = 250

#player Boundary
vel = [5, 795,220,595]

itemClockStats = "Gives player 100s"
itemHeartStats = "Gives Player 50Hp"

#main game Loop
while running:
   #Quit game 
   for evnt in pygame.event.get():
      keys = pygame.key.get_pressed()
      if evnt.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
         running = False   
   #When Player doesn't press start 
   if startGUI:
      keys = pygame.key.get_pressed()
      startMenu()    
      if startMenu() == False:
         startGUI = False
      if startMenu():
         startGUI = False
         instructionGUI = True
      pygame.display.flip()
   #Instruction page
   if startGUI == False and instructionGUI:
      instructionsMenu()
      if instructionsMenu() == False:
         instructionGUI = False
      pygame.display.flip()
   #main selection, player move enemy AI etc
   if startGUI == False and instructionGUI == False: 
      #if player wins
      if bossHp <= 0:
         playerWon = True
         pygame.time.wait(1000)
         score = itemCounter*50 + bossPoints + (itemCollected*20)+ (playerHp*10//2) 
         winningPic = pygame.image.load("WorldSaved.png")
         screen.blit(winningPic, pygame.Rect(0,0,width//2,height))            
         winText = fontTimer.render("You Win!", 1, RED) 
         screen.blit(winText, pygame.Rect(width//2-50,height//2,width//4,height//6))   
         winText = fontTimer.render("Your Score: "+str(score), 1, RED) 
         screen.blit(winText, pygame.Rect(width//2-80,height//1.7,width//4,height//6)) 
         clockText = fontTimer.render("Your Time: "+str(clockCounter//1)+"s", 1, RED)
         screen.blit(clockText, pygame.Rect(width//2-80,height//1.5,width//4,height//6))           
         #closing game
         for evnt in pygame.event.get():
            if evnt.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
               running = False         
             
         pygame.display.flip()

      #if player loses   
      if clockCounter <= 0 or playerHp <= 0:
         playerWon = True
         #Total points earned in one game
         score = itemCounter*10 + bossPoints + (itemCollected*20)
         keys = pygame.key.get_pressed()
         gameOver()                  
         #Restart key, resets all changing values
         if keys[pygame.K_r]:
            playerWon = False
            startGUI = True
            #On and off switches to turn off loop or main if statements
            running = True
            switch = False
            enemyDefeated = False
            
            #GUI boolean values
            startGUI = True
            instructionGUI = False
            
            #player game states
            key_left = False
            key_right = False
            key_up = False
            key_down = False
            
            playerWon = False
            
            #Enemy types 
            enemiesHp = [100,0]
            smartEnemiesHp = [150,0]
            enemyPosition = [10,400,600,500,480,500,0,0]
            
            #Positions of special items / objects
            itemClockPositions = [random.randint(200,600),random.randint(200,400),0,0]
            itemHeartPositions = [random.randint(200,600),random.randint(200,400),0,0]
            
            wallPosition = [random.randint(100,1600),random.randint(200,800)]
            randomWallList = [random.randint(100,200),random.randint(50,250)]
            
            itemCollected = 0
            
            #Player starting point
            x = width//2
            y = height//2
            
            #Counter variables for enemies X and y Values
            legCounter = 0
            enemyXCounter = 0
            enemyYCounter = 1
            enemyHpCounter = 0
            
            itemCounter = 0
            waveCounter = 1
            numOfDefeated = 0
            
            clockCounter = 250            
            running = True
            bodyCollected = True
            
            #Item boolean values
            itemClockCollected = True
            itemHeartCollected = True
            
            #Showing different character look
            colour = 1
            
            playerHp = 500
            
            # enemy boss components
            bossHp = 200
            bossLimit = 200
            bossPosition = [500,300]
            bossPoints = 0  
         if gameOver() == False: 
            break
      if playerWon == False:
         #Collision
         clockBox = pygame.Rect(itemClockPositions[0]-10,itemClockPositions[1]-10,20,20)
         heartBox = pygame.Rect(itemHeartPositions[0]-10,itemHeartPositions[1]-10,20,20)
         #player hit box
         playerBody = pygame.Rect(x-25,y-95,50,40)
         playerAttkBody = pygame.Rect(enemyPosition[enemyXCounter]-20, enemyPosition[enemyYCounter]-120,90,80)  
         
         screen.fill(DARKGREY)
         #key inputs to WASD
         drawTaskBar()
         keys = pygame.key.get_pressed()
         wallCollide = pygame.Rect(wallPosition[0]//2.6,wallPosition[1]//2,randomWallList[0],randomWallList[1])
         wall(wallPosition[0],wallPosition[1],randomWallList[0],randomWallList[1])  
         
         #animate leg movement
         if legCounter %2 == 0 and keys[pygame.K_j] == False:
            legs(x,y)
         elif legCounter %2 != 0 and keys[pygame.K_j] == False:
            legsUp(x,y)
         drawCharacterDown(colour,x,y) 
         if keys[pygame.K_a] and x > vel[0]:
            key_left = True
            #colour is a placeHolder for a different purpose
            legCounter +=3
            drawCharacterLeft(colour,x,y)      
         if keys[pygame.K_d] and x < vel[1]:
            key_right = True
            #colour is a placeHolder for a different purpose
            legCounter +=3
            drawCharacterRight(colour,x,y)      
         if  keys[pygame.K_w] and y > vel[2]:
            key_up = True
            #colour is a placeHolder for a different purpose
            legCounter +=3
            drawCharacterUp(colour,x,y)      
         if keys[pygame.K_s] and y< vel[3]:
            key_down = True
            #colour is a placeHolder for a different purpose
            legCounter +=3
            drawCharacterDown(colour,x,y)         
         #player resting position
         if keys[pygame.K_j] == False:
            colour = 1
            
         #Moves player depending on input    
         if key_left == True:
            if playerBody.colliderect(wallCollide):
               x-=2
            else:
               x = x - 5
         if key_right == True:
            if playerBody.colliderect(wallCollide):
               x+=2
            else:
               x = x + 5
         if key_up == True:
            if playerBody.colliderect(wallCollide):
               y-=2            
            else :
               y = y - 5
         if key_down == True:
            if playerBody.colliderect(wallCollide):
               y+=2            
            else:
               y = y + 5
            
         if x <= SIZE[0] and y <= SIZE[1]:
            key_left = False
            key_right = False
            key_up = False
            key_down = False
         #items     
         #clock
         if itemClockCollected == False:
         
            if keys[pygame.K_k] == True:
               drawItemClock(itemClockPositions[2],itemClockPositions[3])
         
            if keys[pygame.K_k] == False:
               drawItemClock(0,itemClockPositions[3])   
         
         elif itemClockCollected == True and waveCounter == 5:
            
            if playerBody.colliderect(clockBox) == True:
               displayItemWindow (itemClockPositions[0],itemClockPositions[1],itemClockStats)      
               #When item is picked up
            if keys[pygame.K_k] == True and playerBody.colliderect(clockBox) == True:
               #playing sound effect when item is picked up 
               pickUpSound.play()            
               drawItemClock(itemClockPositions[2],itemClockPositions[3])
               itemClockCollected = False
               itemCollected += 1
               clockCounter += 100
           
            elif keys[pygame.K_k] == False:
               drawItemClock(itemClockPositions[0],itemClockPositions[1]) 
               itemClockCollected == False
         
         #heal
         if itemHeartCollected == False:
            if keys[pygame.K_k] == True:
               drawItemHeart(itemHeartPositions[2],itemHeartPositions[3])
         
            if keys[pygame.K_k] == False:
               drawItemHeart(itemHeartPositions[2],itemHeartPositions[3])   
         
         elif itemHeartCollected == True and waveCounter%2 != 0:
            if playerBody.colliderect(heartBox) == True:
               displayItemWindow (itemHeartPositions[0],itemHeartPositions[1],itemHeartStats)
         
            #when item is picked up
            if keys[pygame.K_k] == True and playerBody.colliderect(heartBox) == True:
               pickUpSound.play()      
               drawItemHeart(itemHeartPositions[2],itemHeartPositions[3])
               itemCollected += 1
               itemHeartCollected = False
               playerHp += 50
            
            elif keys[pygame.K_k] == False:
               drawItemHeart(itemHeartPositions[0],itemHeartPositions[1]) 
         if waveCounter == 5 and fiveWave == True:
            itemHeartCollected = True
            fiveWave = False
         #Boss 
         if waveCounter == 5:
            bossHitBox = pygame.Rect(bossPosition[0]+50,bossPosition[1],100,50) #remember to change
            bossBody = pygame.Rect(bossPosition[0],bossPosition[1]-100,200,150)            
            #player attacking boss
            if keys[pygame.K_j]:
               if playerBody.colliderect(bossHitBox): 
                  bossHp -=5
               if playerBody.colliderect(bossBody): 
                  bossHp +=.5            
            #Boss Health bar
            pygame.draw.rect(screen,GREY,pygame.Rect(300,120,width//3,height//12))
            bossHealth = bossFont.render("Giant Broken Mircowave HP:"+str(bossHp),1,RED)
            screen.blit(bossHealth, pygame.Rect(325,120,width//3,height//6)) 
            if bossHp < bossLimit:
               pygame.draw.rect(screen,RED,pygame.Rect(325,140,bossHp,height//25))
            if bossHp >= bossLimit:
               pygame.draw.rect(screen,YELLOW,pygame.Rect(325,140,bossLimit,height//25))
            if bossHp > 0:
               if bossBody.colliderect(playerBody):
                  playerHp -= 2
               #boss tracking player
               if bossPosition[0] >= x and bossPosition[1] >= y:
                  bossPosition[0] -=1
                  bossPosition[1] -=1
               if bossPosition[0] <= x and bossPosition[1] >= y:
                  bossPosition[0] +=1  
                  bossPosition[1] -=1  
               if bossPosition[0] >= x and bossPosition[1] <= y:
                  bossPosition[0] -=1  
                  bossPosition[1] +=1
               if bossPosition[0] <= x and bossPosition[1] <= y:
                  bossPosition[0] +=1
                  bossPosition[1] +=1           
            #Drawing of boss
            bossEnemy(bossPosition[0],bossPosition[1]) 
            if bossHp <= 0:
               #adding points to the score
               bossPoints = random.randint(100,150)         
         
         #enemy
         enemyBody = pygame.Rect(enemyPosition[enemyXCounter], enemyPosition[enemyYCounter] - 100,50,40)
         if waveCounter == 1 or waveCounter == 3 or waveCounter == 5:
            #resets variables
            enemyXCounter = 0
            enemyYCounter = 1            
            if enemiesHp[0] > 0:  
               enemy(enemyPosition[enemyXCounter],enemyPosition[enemyYCounter],enemiesHp[0],False)
            if waveCounter == 3:
               enemyXCounter += 2
               enemyYCounter += 2
               if enemiesHp[1] > 0:
                  enemyUp(enemyPosition[enemyXCounter],enemyPosition[enemyYCounter],enemiesHp[1],False)                
            #Enemy attacking Player
            if enemyBody.colliderect(playerBody) and enemiesHp[0] > 0:
               playerHp -=1
            if waveCounter >= 3:
               enemyBodySecond = pygame.Rect(enemyPosition[0], enemyPosition[1] - 100,50,40)
               if enemyBodySecond.colliderect(playerBody) and enemiesHp[1]> 0:
                  playerHp -=1      
            #Player attacking enemy
            if keys[pygame.K_j]:    
               colour = 2
                #Attack
               enemyBody = pygame.Rect(enemyPosition[0]-20, enemyPosition[1]-120,90,80)  
               if playerBody.colliderect(enemyBody):
                  enemiesHp[0] -=1                   
               if waveCounter == 5:
                  if playerBody.colliderect(enemyBody):
                     enemiesHp[1] -=1                     
               if waveCounter == 3: 
                  enemyBodySecond = pygame.Rect(enemyPosition[enemyXCounter]-20, enemyPosition[enemyYCounter]-120,90,80)
                  if playerBody.colliderect(enemyBodySecond):
                     enemiesHp[1] -= 1                    
            if enemiesHp[0] <= 0 and enemiesHp[1] <= 0 and switch == False:
               if waveCounter == 3:
                  itemCounter += 1
                  enemiesHp = [100,0]  
               if waveCounter == 5:
                  switch = True
               else:
                  #resets values of normal enemy
                  enemyDefeatedSound.play()                  
                  enemyXCounter = 0
                  enemyYCounter = 1
                  enemyPosition = [10,400,600,500,480,500,0,0]
                  enemiesHp = [100,100]
                  itemCounter += 1                  
                  waveCounter +=1
               #Gives new positions for wall/object
               wallPosition = [random.randint(100,1600),random.randint(200,800)]
               randomWallList = [random.randint(100,200),random.randint(50,250)]                  
      
         #Smart enemy
         if waveCounter == 2 or waveCounter == 4 or waveCounter == 5:
            if waveCounter == 5:
               #changing set of positions
               enemyXCounter += 2
               enemyYCounter += 2
            else:
               #Reset counter variable
               enemyXCounter = 0
               enemyYCounter = 1       
               
            if smartEnemiesHp[0] > 0:
               smartEnemy(enemyPosition[enemyXCounter],enemyPosition[enemyYCounter],smartEnemiesHp[0],False)
            if waveCounter == 4:
               #changing set of positions
               enemyXCounter += 2
               enemyYCounter += 2                     
               if smartEnemiesHp[1] > 0:
                  smartEnemy(enemyPosition[enemyXCounter],enemyPosition[enemyYCounter],smartEnemiesHp[1],False)              
            
                 #Player attacking enemy
            if keys[pygame.K_j]:    
               colour = 2
               #Attack collision of enemy hit boxes
               if waveCounter == 5:
                  hitEnemyBody = pygame.Rect(enemyPosition[enemyXCounter]-20, enemyPosition[enemyYCounter]-120,90,80)               
               if waveCounter != 5:
                  hitEnemyBody = pygame.Rect(enemyPosition[0]-20, enemyPosition[1]-120,90,80)
               hitEnemyBodySecond = pygame.Rect(enemyPosition[enemyXCounter]-20, enemyPosition[enemyYCounter]-120,90,80)
               
               if playerBody.colliderect(hitEnemyBody):
                  smartEnemiesHp[0] -=1   
               if waveCounter == 4: 
                  if playerBody.colliderect(hitEnemyBodySecond):
                     smartEnemiesHp[1] -= 1   
            if smartEnemiesHp[0] <= 0 and smartEnemiesHp[1] <= 0 and enemyDefeated == False:
               enemyDefeatedSound.play()                  
               itemCounter +=1
               #Resets values of smart enemies
               if waveCounter == 4:
                  itemCounter += 1
                  smartEnemiesHp = [150,150]
               enemyXCounter = 0
               enemyXCounter = 1
               if waveCounter == 5:
                  enemyDefeated = True
               else:
                  waveCounter +=1
               if waveCounter == 2 or waveCounter == 3:
                  smartEnemiesHp = [150,150]
               #New wall position
               wallPosition = [random.randint(100,1600),random.randint(200,800)]
               randomWallList = [random.randint(100,200),random.randint(50,250)]                 
            #Enemy attacking Player
            if enemyBody.colliderect(playerBody) and smartEnemiesHp[0]> 0:
               playerHp -=1
            if waveCounter ==4:
               enemyBodySecond = pygame.Rect(enemyPosition[0], enemyPosition[1] - 100,50,40)
               if enemyBodySecond.colliderect(playerBody) and smartEnemiesHp[1]> 0:
                  playerHp -=1      
               if enemyBodySecond.colliderect(enemyBody):
                  enemyPosition[enemyXCounter]-=25
         
         #Show enemy health 
         if waveCounter == 1:
            enemyHealth = bossFont.render("Cracked Montior: "+str(enemiesHp[0]),1,RED)
            screen.blit(enemyHealth, pygame.Rect(width//16,height//5,width//3,height//6))          
         if waveCounter == 3:
            enemyHealth = bossFont.render("Cracked Montior x2: "+str(enemiesHp),1,RED)
            screen.blit(enemyHealth, pygame.Rect(width//16,height//5,width//3,height//6))            
         if waveCounter == 2:
            enemyHealth = bossFont.render("SmartPhone: "+str(smartEnemiesHp[0]),1,RED)
            screen.blit(enemyHealth, pygame.Rect(width//16,height//3.75,width//3,height//6))               
         if waveCounter == 4:
            enemyHealth = bossFont.render("SmartPhone X2: "+str(smartEnemiesHp),1,RED)
            screen.blit(enemyHealth, pygame.Rect(width//16,height//3.75,width//3,height//6))     
         if waveCounter == 5:
            enemyHealth = bossFont.render("Cracked Montior: "+str(enemiesHp[0]),1,RED)
            screen.blit(enemyHealth, pygame.Rect(width//16,height//5,width//3,height//6))          
            enemyHealth = bossFont.render("SmartPhone: "+str(smartEnemiesHp[0]),1,RED)
            screen.blit(enemyHealth, pygame.Rect(width//16,height//3.75,width//3,height//6))            
           #TASKBAR
         drawTaskBar()
         
         #Timer
         clockText = fontTimer.render("         "+str(clockCounter), 1, RED)
         screen.blit(clockText, pygame.Rect(590,55,width//4,height//6))
         
         #Shows Players Hp
         playerHealth = fontTimer.render("        "+str(playerHp), 1, RED)
         screen.blit(playerHealth, pygame.Rect(60,55,width//3,height//6))    
         
         #Timer going down
         clockCounter -=.1  
         #Covers up decimal places
         pygame.draw.rect(screen,BLACK,pygame.Rect(737,50,100,50))
         pygame.draw.rect(screen,YELLOW,pygame.Rect(737,50,53,50))
         
         pygame.display.flip()
         myClock.tick(60)   
pygame.quit()

