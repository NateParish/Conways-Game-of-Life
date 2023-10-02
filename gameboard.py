import pygame
from vars import SCREENWIDTH, SCREENHEIGHT, TILEWIDTH, TILEHEIGHT, COLUMNCOUNT, ROWCOUNT, RED, GRIDLINECOLOR, XOFFSET, XPAD, YOFFSET, YPAD, BUTTONFONT, BUTTONCORNERRADIUS, BUTTONTEXTXOFFSET, BUTTONFONTCOLOR
from vars import BUTTONTEXTYOFFSET, BUTTONHIGHLIGHTCOLOR

class Grid():
     def __init__(self, x, y, color):

         self.start = x
         self.end = y
         self.originalColor = RED
         self.color = color

     def draw(self, window):
         pygame.draw.line(window, self.color, self.start, self.end, 1 )



def create_grid(window, gridlines):

    startXpos = XOFFSET + XPAD
    startYpos = YOFFSET + YPAD
    endXpos = startXpos + COLUMNCOUNT * TILEWIDTH
    endYpos = startYpos + ROWCOUNT * TILEHEIGHT

    for i in range(0,int(COLUMNCOUNT)+1):
        startPoint = ((startXpos + (TILEWIDTH * i), startYpos))
        endPoint = ((startXpos + (TILEWIDTH * i), endYpos))      
        gridlines.append(Grid(startPoint, endPoint, GRIDLINECOLOR))

    for i in range(0,int(ROWCOUNT)+1):
        startPoint = (startXpos, startYpos + (TILEHEIGHT * i))
        endPoint = (endXpos, startYpos + (TILEWIDTH * i))      
        gridlines.append(Grid(startPoint, endPoint, GRIDLINECOLOR))


class Button():

     def __init__(self, x, y, width, height, color, label):
         self.x = x
         self.y = y
         self.width = width
         self.height = height
         self.originalColor = color
         self.color = color
         self.label = label

     def draw(self, window):

         pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), int(self.height/2), BUTTONCORNERRADIUS)
         label = BUTTONFONT.render(self.label, 1, (BUTTONFONTCOLOR))
         window.blit(label, (self.x + BUTTONTEXTXOFFSET, self.y + BUTTONTEXTYOFFSET))

     def highlight(self, mousePos):

         self.color = self.originalColor

         if self.x <= mousePos[0]:
             if self.x + self.width > mousePos[0]:
                 if self.y <= mousePos[1]:
                    if self.y + self.height > mousePos[1]:
                        self.color = (BUTTONHIGHLIGHTCOLOR)
     
     def button_function(self, mousePos, clicked, runSimulation):
           
         if self.x <= mousePos[0]:
             if self.x + self.width > mousePos[0]:
                 if self.y <= mousePos[1]:
                    if self.y + self.height > mousePos[1]:
                        if clicked == True:
                            if runSimulation == True:
                                runSimulation = False
                            else:
                                runSimulation = True
        
         return(runSimulation)
