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

import pygame
from time import sleep
from math import cos, sin, pi, modf

class Curser :
  def __init__(self,start_x,start_y,start_angle=0,color=(0,0,0),bg_color=(255,255,255),stroke_width=1,curser_down=True) :
    '''Create a curser at position (start_x,start_y) pointed in direction start_angle'''
    
    if isinstance(start_x,int) or isinstance(start_x,float) :
      self.x=float(start_x)
    else :
      raise TypeError(int,float) 
    
    if isinstance(start_y,int) or isinstance(start_y,float) :
      self.y=float(start_y)
    else :
      raise TypeError(int,float) 
    
    if isinstance(start_angle,int) or isinstance(start_angle,float) :
      self.cur_angle=float(start_angle)
      self.prev_angle=float(start_angle)
    else :
      raise TypeError(int,float) 
    
    if isinstance(color,tuple) and len(color) ==  3 :
      for v in color :
	if v > 255 or v < 0 :
	  raise ValueError("(0-255,0-255,0-255)")
	
      self.stroke_color=color
      self.curser_color=color
    else :
      raise TypeError(tuple) 
     
    if isinstance(bg_color,tuple) and len(bg_color) ==  3 :
      for v in bg_color :
	if v > 255 or v < 0 :
	  raise ValueError("(0-255,0-255,0-255)")
	
      self.bg_color=bg_color
      
    else :
      raise TypeError(tuple)  
     
    if isinstance(stroke_width,int) :
      self.stroke_width=stroke_width
      self.curser_width=stroke_width
    else :
      raise TypeError(int)   
    
    if isinstance(curser_down,bool) :
      self.is_curser_down=curser_down
    else :
      raise TypeError(bool)   
    
    
    
    self._coords_table=[]
    self._coords=[]
    self._anim_coords=[]
    self._coords.append((self.x,self.y))
    self.show_curser_on=True
    if stroke_width < 2 :
      self._curser_size=8
      self._update_curser_dir_pos()
    else :
      self._curser_size=8+stroke_width
      self._update_curser_dir_pos()
    
    if self.is_curser_down :
      self._coords.append((self.x,self.y))
      
  
  def __doc__(self) :
    doc='''
    
    Instanciate the Curser class with the following arguments:                      

    -start_x: the start x coordinate from the curser start position.
    
    -start_y: the start y coordinate from the curser start position.
    
    -start_angle (default 0)  : the start orientation from the curser. 
    
    -color (default (0, 0, 0)): the stroke and curser color given as a 3-elements 
				tuple (red,green,blue).
    
    -bg_color (default (255, 255, 255)): the display background color given as a
					  3-elements tuple (red,green,blue).
    
    -stroke_width (default 1): the stroke width inn pixel(s) given as an integer.
    
    -curser_down (default True): a boolean value if the curser is down. 
      
    
    to get an curser object who implement the following methods to drawing:
    
    
    -mv_forward(px) : Move the curser forward in the current direction 
		      from px pixels.
    
    -mv_backward(px): Move the curser backward in the opposite direction to 
		      the current from px pixels.
    
    -mv_left(degrees): turn the curser left from argument degrees degrees and 
			update the current direction.
    
    -mv_right(degrees): turn the curser right from argument degrees degrees and
			  update the current direction.
    
    -anim_forward(px,speed): move the curser forward in current direction from one 
			      pixel every speed seconds (or fraction) from px pixels 
			      far what create an stroke drawning animation effect.
    
    -anim_backward(px,speed): 	move the curser backward in the opposite direction 
				from one pixel every speed seconds (or fraction) from 
				px pixels far what create an stroke drawning animation 
				effect.  
    
    -get_coords_forward(px) : 	return the coordinates for a forward moving from px
				pixels without drawing a stroke or move the curser.
				! Use this method with your own coordinates 
				  container.
    
    -get_coords_backward(px) : return the coordinates for a backward moving from 
				px pixels without drawing a stroke or move the 
				curser.
				! Use this method with your own coordinates 
				  container.
				
    -show_hook(): hook method to set in the pygame mainloop if you use it, this
		  is the core for displaying the curser and the driven strokes.
    
    -curser_up(): Raise the curser up and any curser moving method will not 
		  draw but the direction changings are effectiv.
		  ! This method does not hide the curser.
    
    -curser_down(): Put the curser down any moving method will draw on the display. 
		    ! This method do not show the curser if he is hidden.            
    
    -hide_curser(): Hide the curser but does not raise him up is simply to hide the
		    curser for driving.
    
    -show_curser(): Show the curser but does not put him down.
		    ! The curser is visible per default.
    
    -set_bg_color(bg_color) : Change the display background
				! You have to set the show_hook() method in the 
				  mainloop to make it effectiv if you work with it.
				
    -set_curser_pos(x, y) : set the curser position to the coordinates x,y         
    
    -set_stroke_color(color) : set stroke and curser color to the argument color 
				who must be an 3-elements tuple (red,green,blue) 
				
    -set_stroke_width(stroke_width) :  set the stroke width to the stroke_width 
					argument in pixels.
					! The curser size will increase or decrease
					  if you change the stroke width.
					
    -get_curser_pos() : return the current curser position as (x,y).
    
    -get_stroke_color() : return the current stroke and curser color as 
			   (red,green,blue) tuple.
    
    -get_stroke_width() : return the current stroke width.
    
    -get_bg_color() : return the current display background color as
		      (red,green,blue) tuple.
    '''
    print doc
   
  def __credits__(self) :
    credits='''
    author: Eddie Bruggemann
    mail: mrcyberfighter@gmail.com
    thanks: Thanks to my mother and to the doctors.
    Keep away from drugs: Drugs destroy your brain and your life
    '''
    print credits
  
  def __release__(self) :
    release='''Release: 18 april 2013'''
    print release
  
  def __revision__(self) :
    revision='''Revision: 20 august 2014'''
    print revision
  
  def __version__(self) :
    version='''Version 1.0.1'''
    print version
   
  def _get_pos(self,length,x,y,angle) :
    ''' Compute the next coords by moving '''  
    degrees=angle
    to_rad=degrees/180.0*pi
    x_pos=round(cos(to_rad)*length+x)
    y_pos=round(sin(to_rad)*length+y)

    return (x_pos,y_pos)
 
  
  def _get_curser_coords(self,pos,scale,length,x,y,start_pos) :
    '''Return a coords pair for curser computing'''
    degrees=360.0/scale * pos + start_pos
    to_rad=degrees/180.0*pi
    x_pos=round(cos(to_rad)*length+x)
    y_pos=round(sin(to_rad)*length+y)
    return (x_pos,y_pos)
  
  def _gen_curser(self,edges,length,x_center,y_center,start_point) :
    '''Generate the curser coords'''
  
    
    count_edges=edges
    diagonal_length=length
    x,y=x_center,y_center
    res=[]
    i=0
    while i <= count_edges :
      res.append(self._get_curser_coords(i+1,edges,diagonal_length,x,y,start_point))
      i += 1
    return res  
  
  def _update_curser_dir_pos(self) :
    '''Update the curser direction and position'''

    self.curser=[]
    self.curser.append((self._gen_curser(3,self._curser_size,self.x,self.y,self.cur_angle)[1]))
    self.curser.append((self._gen_curser(3,self._curser_size,self.x,self.y,self.cur_angle)[2]))
    self.curser.append((self._gen_curser(3,self._curser_size,self.x,self.y,self.cur_angle)[3]))
    self.curser.append((self.x,self.y))
  
  def _update(self,x,y) :
    '''Add the curser position to the drawline'''   
    self._coords.append((x,y))
    
  def mv_right(self,angle) :
    '''Turn the curser right from given degrees'''  
    
    if isinstance(angle,int) or isinstance(angle,float) :
      pass
    else :
      raise TypeError(int,float)  
    
    self.prev_angle=self.cur_angle
    if self.prev_angle+angle > 360 :
      self.cur_angle=self.prev_angle+angle-360.0
      
    elif self.prev_angle+angle < 0 :
      self.cur_angle=self.prev_angle+angle+360.0  
    else :
      self.cur_angle=self.prev_angle+angle
      
    if self.show_curser_on :
      self._update_curser_dir_pos()

  
  def mv_left(self,angle) :
    '''Turn the curser left from given degrees'''
    
    if isinstance(angle,int) or isinstance(angle,float) :
      pass
    else :
      raise TypeError(int,float)  
    
    self.prev_angle=self.cur_angle
    if self.prev_angle-angle > 360 :
      self.cur_angle=self.prev_angle-angle-360.0
      
    elif self.prev_angle-angle < 0 :
      self.cur_angle=self.prev_angle-angle+360.0  
    else :
      self.cur_angle=self.prev_angle-angle
    
    if self.show_curser_on :
      self._update_curser_dir_pos() 
    
    
  def mv_forward(self,px) :
    '''Move the curser forward for given pixels'''
    
    if isinstance(px,int) or isinstance(px,float) :
      pass
    else :
      raise TypeError(int,float)  
    
    self.x,self.y=self._get_pos(px,self.x,self.y,self.cur_angle)
    if self.show_curser_on :
      self._update_curser_dir_pos()
      
    if self.is_curser_down :
      self._update(self.x,self.y)
    self.show_hook()
    
  def mv_backward(self,px) :
    '''Move the curser backward for given pixels''' 
    if isinstance(px,int) or isinstance(px,float) :
      pass
    else :
      raise TypeError(int,float) 
    
    self.x,self.y=self._get_pos(px,self.x,self.y,abs(180.0-self.cur_angle))
    if self.show_curser_on :
      self._update_curser_dir_pos()
    if self.is_curser_down :
      self._update(self.x,self.y)
    self.show_hook()
    
  def get_coords_forward(self,px) :
    '''Return the curser position moved forward for given pixels''' 
    
    if isinstance(px,int) or isinstance(px,float) :
      pass
    else :
      raise TypeError(int,float)  
    
    self.x,self.y=self._get_pos(px,self.x,self.y,self.cur_angle)
    return (self.x,self.y)
    
  def get_coords_backward(self,px) :
    '''Return the curser position moved backward for given pixels''' 
    
    if isinstance(px,int) or isinstance(px,float) :
      pass
    else :
      raise TypeError(int,float)  
    
    self.x,self.y=self._get_pos(px,self.x,self.y,abs(180.0-self.cur_angle))
    return (self.x,self.y)
  
  def return_curser(self) :
    '''Switch the curser in inverse direction'''      
    self.mv_left(180)
  
  
    
    
  def show_hook(self) :
    '''Hook function to set in the pygame mainloop''' 
    pygame.display.get_surface().fill(self.bg_color)
    if len(self._coords)  > 1  :
      pygame.draw.lines(pygame.display.get_surface(),self.stroke_color,False,self._coords+self._anim_coords,self.stroke_width)
      
    if self._coords_table :
      for v in self._coords_table :
	if len(v) > 1 :
	  pygame.draw.lines(pygame.display.get_surface(),self.stroke_color,False,v,self.stroke_width)
    
    if self.show_curser_on :
      pygame.draw.polygon(pygame.display.get_surface(),self.curser_color,self.curser,0)
   
    pygame.display.update()
   
  def reset_display(self) :
    self._coords=[]
    self._anim_coords=[]
    self._coords_table=[]
    pygame.display.get_surface().fill(self.bg_color)
    pygame.display.update()
   
  def set_stroke_color(self,color) :
    '''Set the stroke color given as (red,green,blue)
       where red, green and blue can take values 0-255'''
    
    if isinstance(color,tuple) and len(color) ==  3 :
      pass  
    else :
      raise TypeError('(red,green,blue)',tuple) 
    
    for v in color :
      if v < 0 or v > 255 :
	raise ValueError("(0-255,0-255,0-255)") 
    
    self.stroke_color=color
    self.curser_color=color
  
  def set_stroke_width(self,stroke_width=1) :
    '''Set the stroke width given in pixels'''
    
    if isinstance(stroke_width,int) :
      self.stroke_width=stroke_width
    else :
      raise TypeError(int)
    
    if stroke_width < 0 :
      raise ValueError("< 0") 
    
    if stroke_width < 2 :
      self._curser_size=8
    else :
      self._curser_size=8+stroke_width
   
    self.show_hook()
  
  def set_bg_color(self,bg_color) :
    '''Set the display background color given as (red,green,blue)'''
    
    if isinstance(bg_color,tuple) and len(bg_color) ==  3 :
      pass
    else :
      raise TypeError('(red,green,blue)',tuple) 
    
    for v in bg_color :
      if v < 0 or v > 255 :
	raise ValueError("(0-255,0-255,0-255)") 
      
    self.bg_color=bg_color
    
    
  def get_stroke_color(self) :
    '''Return the stroke color'''
    return self.stroke_color
    
  def get_stroke_width(self) :
    '''Return the stroke width'''
    return self.stroke_width  
   
  def get_bg_color(self) :
    '''Return the display background color''' 
    return self.bg_color
    
  def curser_up(self) :
    '''Put the curser up 
      by moving the curser no strokes where driven'''
      
    self.is_curser_down=False
    if len(self._coords) > 1 :
      self._coords_table.append(self._coords)
      
    self._coords=[]
    
  def curser_down(self) :
    '''Put the curser down 
      by moving the curser the strokes where driven'''
    self.is_curser_down=True
    self._update(self.x,self.y)
    
  def set_curser_pos(self,x,y) :
    '''Set the curser at position x,y
       if the curser is down draw a stroke to x,y'''
    
    if (isinstance(x,int) or isinstance(x,float)) and (isinstance(y,int) or isinstance(y,float)) :
      self.x=x
      self.y=y
    else :
      raise ValueError(int,float)
    
    if not self.is_curser_down :
      if len(self._coords) > 1 : 
        self._coords_table.append(self._coords)
      self._coords=[]  
    self._update(x,y)
    #self.show_hook()
    
    
  def get_curser_pos(self) :
    '''Return the curser position'''
    return (self.y,self.y)
  
  
  def show_curser(self) :
    '''Show the curser, enabled per default
       ! if the curser is not put down, he is up, he is only visible not down.'''
    
    self.curser=[]
    self.curser.append((self._gen_curser(3,self._curser_size,self.x,self.y,self.cur_angle)[1]))
    self.curser.append((self._gen_curser(3,self._curser_size,self.x,self.y,self.cur_angle)[2]))
    self.curser.append((self._gen_curser(3,self._curser_size,self.x,self.y,self.cur_angle)[3]))
    self.curser.append((self.x,self.y))
    self.show_curser_on=True
    
    self.show_hook()
    
  def hide_curser(self) :
    '''hide the curser, disabled per default
       ! if the curser is not raise up, he is down, he is only invisible but still down.'''
    
    self.show_curser_on=False
    
    self.show_hook()
  
  def anim_forward(self,px,speed=0.0001) :
    '''Move forward 1 pixel per speed argument for animating stroke drawing'''
    
    if isinstance(px,int) :
      pass
    else :
      raise ValueError("px",int)
    
    if isinstance(speed,float) :
      pass
    else :
      raise ValueError("speed",float)
    
    i=0
    if not self.cur_angle.is_integer() :
      if  px >= 8 :
	if modf(self.cur_angle)[0] == 0.5 :
	  unit = 2
	  rest = px % 2
	elif (modf(self.cur_angle)[0] == 0.25 or modf(self.cur_angle)[0] == 0.75)  and px >= 4 :
	  unit = 4
	  rest = px % 4
	elif (modf(self.cur_angle)[0] == 0.625 or modf(self.cur_angle)[0] == 0.875 or modf(self.cur_angle)[0] == 0.375 ) and px >= 8 :
	  unit = 8
	  rest = px % 8
	else :
	  unit = 8
	  rest = px % 8
      elif px < 8 and px >= 4 :
	if modf(self.cur_angle)[0] == 0.5 :
	  unit = 2
	  rest = px % 2
	elif (modf(self.cur_angle)[0] == 0.25 or modf(self.cur_angle)[0] == 0.75)  and px >= 4 :
	  unit = 4
	  rest = px % 4
	elif (modf(self.cur_angle)[0] == 0.625 or modf(self.cur_angle)[0] == 0.875 or modf(self.cur_angle)[0] == 0.375 ) and px >= 8 :
	  unit = 4
	  rest = px % 4
	else :
	  unit = 4
	  rest = px % 4
      elif px < 4 and px >= 2 :
	unit = 2
	rest = px % 2
      else :
	unit = 1
	rest = 0
	
    else :
      if px >= 8 :
	quotient,rest=divmod(px,8)
	unit=px/quotient
      elif px < 8 and px >= 4 :
	quotient,rest=divmod(px,4)
	unit=px/quotient
      elif px < 4 and px >= 2 :
	quotient,rest=divmod(px,2)
	unit=px/quotient
      else :
	unit=1
	rest=0
	
    self._anim_coords=[]
    while i < px :
      if i == px-rest :
	unit=rest
      self.x,self.y=self._get_pos(unit,self.x,self.y,self.cur_angle)
      if self.show_curser_on :
        self._update_curser_dir_pos()
      if self.is_curser_down :
        self._anim_coords.append((self.x,self.y))
        self.show_hook()
      sleep(unit*speed)
      i += unit
    self._update(self.x,self.y)
    self._anim_coords=[]
    if self.show_curser_on :
      self._update_curser_dir_pos()
    
    
  def anim_backward(self,px,speed=0.0001) :
    '''Move backward 1 pixel per speed argument for animating stroke drawing'''
    
    if isinstance(px,int) :
      pass
    else :
      raise ValueError("px",int)
    
    if isinstance(speed,float) :
      pass
    else :
      raise ValueError("speed",float)
    
    i=0
    if not self.cur_angle.is_integer() :
      if  px >= 8 :
	if modf(self.cur_angle)[0] == 0.5 :
	  unit = 2
	  rest = px % 2
	elif (modf(self.cur_angle)[0] == 0.25 or modf(self.cur_angle)[0] == 0.75)  and px >= 4 :
	  unit = 4
	  rest = px % 4
	elif (modf(self.cur_angle)[0] == 0.625 or modf(self.cur_angle)[0] == 0.875 or modf(self.cur_angle)[0] == 0.375 ) and px >= 8 :
	  unit = 8
	  rest = px % 8
	else :
	  unit = 8
	  rest = px % 8
      elif px < 8 and px >= 4 :
	if modf(self.cur_angle)[0] == 0.5 :
	  unit = 2
	  rest = px % 2
	elif (modf(self.cur_angle)[0] == 0.25 or modf(self.cur_angle)[0] == 0.75)  and px >= 4 :
	  unit = 4
	  rest = px % 4
	elif (modf(self.cur_angle)[0] == 0.625 or modf(self.cur_angle)[0] == 0.875 or modf(self.cur_angle)[0] == 0.375 ) and px >= 8 :
	  unit = 4
	  rest = px % 4
	else :
	  unit = 4
	  rest = px % 4
      elif px < 4 and px >= 2 :
	unit = 2
	rest = px % 2
      else :
	unit = 1
	rest = 0
	
    else :
      if px >= 8 :
	quotient,rest=divmod(px,8)
	unit=px/quotient
      elif px < 8 and px >= 4 :
	quotient,rest=divmod(px,4)
	unit=px/quotient
      elif px < 4 and px >= 2 :
	quotient,rest=divmod(px,2)
	unit=px/quotient
      else :
	unit=1
	rest=0
	
    self._anim_coords=[]
    while i < px :
      if i == px-rest :
	unit=rest
      if 180-self.cur_angle > 180 :
	swap_angle=180-self.cur_angle
      else :
	swap_angle=self.cur_angle-180
	
      self.x,self.y=self._get_pos(unit,self.x,self.y,swap_angle)
      if self.show_curser_on :
        self._update_curser_dir_pos()
      if self.is_curser_down :
        self._anim_coords.append((self.x,self.y))
        self.show_hook()
      sleep(unit*speed)
      i += unit
    self._update(self.x,self.y)
    self._anim_coords=[]
    if self.show_curser_on :
      self._update_curser_dir_pos()
         
         
def __doc__() :
  doc='''
  
  Instanciate the Curser class with the following arguments:                      

  -start_x: the start x coordinate from the curser start position.
  
  -start_y: the start y coordinate from the curser start position.
  
  -start_angle (default 0)  : the start orientation from the curser. 
  
  -color (default (0, 0, 0)): the stroke and curser color given as a 3-elements 
			      tuple (red,green,blue).
  
  -bg_color (default (255, 255, 255)): the display background color given as a
					3-elements tuple (red,green,blue).
  
  -stroke_width (default 1): the stroke width inn pixel(s) given as an integer.
  
  -curser_down (default True): a boolean value if the curser is down. 
    
  
  to get an curser object who implement the following methods to drawing:
  
  
  -mv_forward(px) : Move the curser forward in the current direction 
		    from px pixels.
  
  -mv_backward(px): Move the curser backward in the opposite direction to 
		    the current from px pixels.
  
  -mv_left(degrees): turn the curser left from argument degrees degrees and 
		      update the current direction.
  
  -mv_right(degrees): turn the curser right from argument degrees degrees and
			update the current direction.
  
  -anim_forward(px,speed): move the curser forward in current direction from one 
			    pixel every speed seconds (or fraction) from px pixels 
			    far what create an stroke drawning animation effect.
  
  -anim_backward(px,speed):  move the curser backward in the opposite direction 
			      from one pixel every speed seconds (or fraction) from 
			      px pixels far what create an stroke drawning animation 
			      effect.  
  
  -get_coords_forward(px) : 	return the coordinates for a forward moving from px
			      pixels without drawing a stroke or move the curser.
			      ! Use this method with your own coordinates 
				container.
  
  -get_coords_backward(px) : return the coordinates for a backward moving from 
			      px pixels without drawing a stroke or move the 
			      curser.
			      ! Use this method with your own coordinates 
				container.
			      
  -show_hook(): hook method to set in the pygame mainloop if you use it, this
		is the core for displaying the curser and the driven strokes.
  
  -curser_up(): Raise the curser up and any curser moving method will not 
		draw but the direction changings are effectiv.
		! This method does not hide the curser.
  
  -curser_down(): Put the curser down any moving method will draw on the display. 
		  ! This method do not show the curser if he is hidden.            
  
  -hide_curser(): Hide the curser but does not raise him up is simply to hide the
		  curser for driving.
  
  -show_curser(): Show the curser but does not put him down.
		  ! The curser is visible per default.
  
  -set_bg_color(bg_color) : Change the display background
			      ! You have to set the show_hook() method in the 
				mainloop to make it effectiv if you work with it.
			      
  -set_curser_pos(x, y) : set the curser position to the coordinates x,y         
  
  -set_stroke_color(color) : set stroke and curser color to the argument color 
			      who must be an 3-elements tuple (red,green,blue) 
			      
  -set_stroke_width(stroke_width) :  set the stroke width to the stroke_width 
				      argument in pixels.
				      ! The curser size will increase or decrease
					if you change the stroke width.
				      
  -get_curser_pos() : return the current curser position as (x,y).
  
  -get_stroke_color() : return the current stroke and curser color as 
			  (red,green,blue) tuple.
  
  -get_stroke_width() : return the current stroke width.
  
  -get_bg_color() : return the current display background color as
		    (red,green,blue) tuple.
  '''
  print doc
  
def __credits__() :
  credits='''
  author: Eddie Bruggemann
  mail: mrcyberfighter@gmail.com
  thanks: Thanks to my mother and to the doctors.
  Keep away from drugs: Drugs destroy your brain and your life
  '''
  print credits

def __release__() :
  release='''Release: 18 april 2013'''
  print release
  
def __revision__(self) :
  revision='''Revision: 20 august 2014'''
  print revision  
  
def __version__() :
  version='''Version 1.0.1'''
  print version
    