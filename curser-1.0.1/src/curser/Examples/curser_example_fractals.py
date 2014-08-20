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
from sys import exit
from time import sleep

from curser import *


pygame.init()
screen=pygame.display.set_mode((800,600),0,32) 

curser=Curser(400,300,270,(0,0,255),(0,0,0),1) # Initialise the Curser instance with following parameters Curser(start_x=400,start_y=300,start_angle=270,color=(0,0,255),bg_color=(0,0,0),stroke_width=1,curser_down=True) 

curser.hide_curser() # Hide the curser (the turtle)

def draw_fractal(x) :
  
  curser.curser_up()  
  curser.set_curser_pos(800/2,600/2)   #set the curser in the middle from the display
  curser.curser_down()   

  i=0
  curser.mv_left(x)                    #set offset for not overlapping fractals
  while i < 361 :
    # Loop to draw an fractal 
    curser.mv_right(i)                 # Offset for the fractal
    
    curser.mv_forward(140)             # Draw the first arm from the stroke
    
    tmp_angle=curser.cur_angle+i       # Computing offset for the second arm from the stroke
    curser.mv_left(tmp_angle)          # Set the offset for the second arm from the stroke
    curser.mv_forward(140)             # Draw the second arm from the stroke animated with a call to sleep(). 
    curser.mv_right(tmp_angle)         # Reset the offset for the second arm from the stroke
    
    curser.mv_left(i)                  # Reset the offset from the fractal
    
    curser.curser_up()  
    curser.set_curser_pos(800/2,600/2) # Reset the curser in the midlle of the display  
    curser.curser_down()
    
    sleep(0.02)
    i += 5
  curser.mv_right(x)                   # Reset offset for not overlapping fractals 


i=0
while i < 361 :
  # Loop to draw an fractal every 45 degrees
  draw_fractal(i)
  i += 45
  
curser.reset_display() # Reset the display
sleep(2)               # No need to import sleep from the time module because the curser module import it
  
i=0
while i < 361 :
  # Loop to draw an fractal every 5 degrees
  draw_fractal(i)
  i += 5

  
while True :
  # Loop unneeded in this example case but if you want to deal with events you need to set the show_hook() method in it.
  screen.fill((0))
  
  
  curser.show_hook() # Hook method from the Curser module for displaying what you want to draw
                     # Here we call it to keep the screen alive after the drawing loops
  for event in pygame.event.get() :
    if event.type == QUIT :
      exit()
      
  pygame.display.update()    