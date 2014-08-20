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

from curser import *

pygame.init()
screen=pygame.display.set_mode((800,600),0,32)




curser=Curser(400,300,270,(0,0,255),(0,0,0),1) # Initialise the Curser instance with following parameters Curser(start_x=400,start_y=300,start_angle=270,color=(0,0,255),bg_color=(0,0,0),stroke_width=1,curser_down=True) 

 
def show_spiral_anim_forward_8(x) :
  # Draw an half circle with segment length x
  i=0
  while i < 8 : 
    curser.mv_right(22.5)
    curser.anim_forward(x)
    
    i += 1   
 
def show_spiral_anim_forward_16(x) :
  # Draw an half circle with segment length x
  i=0
  while i < 16 : 
    curser.mv_right(11.25)
    curser.anim_forward(x)
    
    i += 1  
 
 
def show_spiral_anim_forward_32(x) :
  # Draw an half circle with segment length x
  i=0
  while i < 32 : 
    curser.mv_right(5.625)
    curser.anim_forward(x)
    
    i += 1   
 

def draw_anim_spiral_forward_32() :
  i=2
  while i < 28 :
    show_spiral_anim_forward_32(i) 
    
    i += 2

def draw_anim_spiral_forward_16() :
  i=5
  while i < 60 :
    show_spiral_anim_forward_16(i) 
    
    i += 5

def draw_anim_spiral_forward_8() :
  i=10
  while i < 120 :
    show_spiral_anim_forward_8(i) 
    
    i += 10    


    
draw_anim_spiral_forward_8()
sleep(2)               # No need to import sleep from the time module because the curser module import it
curser.reset_display() # Reset the display                 

#to reset the curser at the initial position
curser.curser_up()  
curser.set_curser_pos(400,300) 
curser.curser_down() 

sleep(2)               # No need to import sleep from the time module because the curser module import it

draw_anim_spiral_forward_16()
sleep(2)               # No need to import sleep from the time module because the curser module import it
curser.reset_display() # Reset the display

#to reset the curser at the initial position
curser.curser_up()  
curser.set_curser_pos(400,300) 
curser.curser_down() 

sleep(2)              # No need to import sleep from the time module because the curser module import it

draw_anim_spiral_forward_32()



while True :
  # Loop unneeded in this example case but if you want to deal with events you need to set the show_hook() method in it.
  screen.fill((0))
  
  
  curser.show_hook() # Hook method from the curser module for displaying what you want to draw
                     # Here we call it to keep the screen alive after the drawing loops
  for event in pygame.event.get() :
    if event.type == QUIT :
      exit()
      
  pygame.display.update()    