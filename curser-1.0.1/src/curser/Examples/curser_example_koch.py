#!/usr/bin/python
# -*- coding: utf-8 -*-

########################################################################
# curser an turtle for the pygame module                               # 
# Copyright (C) 2014 Bruggemann Eddie                                  #
#                                                                      #
# This file is part of curser.                                         #
# curser is free software: you can redistribute it and/or modify       #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or    #  
# (at your option) any later version.                                  #
#                                                                      #
# curser is distributed in the hope that it will be useful,            #
# but WITHOUT ANY WARRANTY; without even the implied warranty of       #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the         #
# GNU General Public License for more details.                         #
#                                                                      #
# You should have received a copy of the GNU General Public License    #
# along with curser. If not, see <http://www.gnu.org/licenses/>        #
########################################################################

# No need to import pygame because the module curser import it,
# but if you need the pygame.locals you have to import it.

from pygame.locals import *
from random import randint
from sys import exit

from curser import *


pygame.init()
screen=pygame.display.set_mode((800,600),0,32)




curser=Curser(240,200,0,(0,0,255),(0,0,0),1) # Initialise the Curser instance with following parameters Curser(start_x=400,start_y=300,start_angle=270,color=(0,0,255),bg_color=(0,0,0),stroke_width=1,curser_down=True) 

      
def von_koch(length,n) :
  if n == 1 :
    data.append(curser.get_coords_forward(length)) # Storing the coordinates return from the get_coords_forward() method in your own container
  else :
    d=length/3.
    von_koch(d,n-1) 
    curser.mv_left(60)
    von_koch(d,n-1)
    curser.mv_right(120)
    von_koch(d,n-1)
    curser.mv_left(60)
    von_koch(d,n-1)
  
def kocher(length,n) :
  
  for i in range(3) :
    von_koch(length,n)
    curser.mv_right(120)
        
    
data=[]      # Create a container for storing the coordinates from the koch star
anim_data=[] # Create a container for storing the coordinates from the koch star for animating

kocher(300,6)

i=0
fill=False
while True :
  screen.fill((curser.get_bg_color()))
  if i == len(data) :
    fill=True
  elif i < len(data) :
    anim_data.append(data[i])
  
  if len(anim_data) > 1 and not fill:
    pygame.draw.lines(screen,curser.get_stroke_color(),False,anim_data,1)
  
  elif fill :
    control=randint(0,256+128)
    pygame.draw.polygon(screen,(randint(0,255),randint(0,255),randint(0,255)),anim_data,0)
    if control == 0 :
      fill=False
      anim_data=[]
      i=0
      
  for event in pygame.event.get() :
    if event.type == QUIT :
      exit()
      
  i += 1
  sleep(0.01)
  pygame.display.update()    