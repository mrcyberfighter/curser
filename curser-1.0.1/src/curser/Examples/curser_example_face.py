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

# We need to import pygame because the module curser is 
# not entire imported only the Curser class is imported,
# and we need the pygame.locals so we import it.

import pygame
from pygame.locals import *
from sys import exit
from time import sleep
from curser import Curser

pygame.init()
screen=pygame.display.set_mode((800,600),0,32)

    
curser=Curser(400,300,270,(0,0,255),(0,0,0),1) # Initialise the Curser instance with following parameters Curser(start_x=400,start_y=300,start_angle=270,color=(0,0,255),bg_color=(0,0,0),stroke_width=1,curser_down=True) 
curser.hide_curser() # Hide the curser (the turtle)



    

# Set the curser at start position to draw the left eye from the face. 
curser.curser_up()  
curser.set_curser_pos(180+45,180) 
curser.curser_down()   


curser.mv_left(135) # Set the curser in the right direction for drawing the left eye
i=0
while i < 361 :
  curser.mv_right(i)             # Set the offset from the stroke  
  
  curser.mv_forward(90)          # Draw the first arm from the stroke  
  
  tmp_angle=curser.cur_angle+i   # Computing the offset for the second arm from the stroke
  curser.mv_left(tmp_angle)      # Set the offset for the second arm from the stroke 
  curser.mv_forward(90)          # Draw the second arm from the stroke
  curser.mv_right(tmp_angle)     # Reset the offset for the second arm from the stroke 
  
  curser.mv_left(i)              # Reset the offset from the stroke  
  
  # Reset the curser at start position to draw the left eye.
  curser.curser_up()  
  curser.set_curser_pos(180+45,180) 
  curser.curser_down()
  sleep(0.04)
  
  i += 5
  
  
# Set the curser at start position to draw the right eye from the face.   
curser.curser_up()  
curser.set_curser_pos(800-(180+45),180) 
curser.curser_down()    

curser.mv_right(90)  # Set the curser in the right direction for drawing the right eye
i=0
while i < 361 :
  curser.mv_right(i)             # Set the offset from the stroke         
  
  curser.mv_forward(90)          # Draw the first arm from the stroke  
  
  tmp_angle=curser.cur_angle+i   # Computing the offset for the second arm from the stroke
  curser.mv_left(tmp_angle)      # Set the offset for the second arm from the stroke 
  curser.mv_forward(90)          # Draw the second arm from the stroke
  curser.mv_right(tmp_angle)     # Reset the offset for the second arm from the stroke 
  
  curser.mv_left(i)              # Reset the offset from the stroke  
  
  # Reset the curser at start position to draw the right eye.
  curser.curser_up()  
  curser.set_curser_pos(800-(180+45),180) 
  curser.curser_down()
  sleep(0.04)
  i += 5
  
  
# Set the curser at start position to draw the noose from the face.   
curser.curser_up()  
curser.set_curser_pos(800/2,180+90+135) 
curser.curser_down()    

curser.mv_left(45) # Set the curser in the right direction for drawing the noose
i=0
while i < 181 :
  curser.mv_right(i)             # Set the offset from the stroke 
  
  curser.mv_forward(90)          # Draw the first arm from the stroke  
  
  tmp_angle=curser.cur_angle+i   # Computing the offset for the second arm from the stroke
  curser.mv_left(tmp_angle)      # Set the offset for the second arm from the stroke 
  curser.mv_forward(90)          # Draw the second arm from the stroke
  curser.mv_right(tmp_angle)     # Reset the offset for the second arm from the stroke 
  
  curser.mv_left(i)              # Reset the offset from the stroke  
  
  # Reset the curser at start position to draw the noose.
  curser.curser_up()  
  curser.set_curser_pos(800/2,180+90+135)
  curser.curser_down()
  sleep(0.04)
  i += 5
  
  
# Set the curser at start position to draw the mouth from the face.   
curser.curser_up()  
curser.set_curser_pos(800/2,360+90+15) 
curser.curser_down()

curser.mv_right(180) # Set the curser in the right direction for drawing the mouth
i=0
while i < 181 :
  curser.mv_right(i)             # Set the offset from the stroke 
  
  curser.mv_forward(90)          # Draw the first arm from the stroke  
  
  tmp_angle=curser.cur_angle+i   # Computing the offset for the second arm from the stroke
  curser.mv_left(tmp_angle)      # Set the offset for the second arm from the stroke 
  curser.mv_forward(90)          # Draw the second arm from the stroke
  curser.mv_right(tmp_angle)     # Reset the offset for the second arm from the stroke 
  
  curser.mv_left(i)              # Reset the offset from the stroke  
  
  # Reset the curser at start position to draw the mouth.
  curser.curser_up()  
  curser.set_curser_pos(800/2,360+90+15)
  curser.curser_down()
  sleep(0.04)
  i += 5
  
  
while True :
  # Loop unneeded in this example case but if you want to deal with events you need to set the show_hook() method in it.
  screen.fill((0))
  
  
  curser.show_hook() # Hook method from the curser module for diplaying what you want to draw
                     # Here we call it to keep the screen alive after the drawing loops
  for event in pygame.event.get() :
    if event.type == QUIT :
      exit()
      
  pygame.display.update()    