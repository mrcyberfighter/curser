################################################################################################
#                                            curser                                            #
################################################################################################   
# curser: A python module written in python implementing a turtle for pygame.                  #
# Name: curser                                                                                 #
# for: Python 2.*.*                                                                            #      
# Author: mrcyberfighter                                                                       #
# Release: 18 april 2013                                                                       #
# Version 1.0.1                                                                                #
# Revision: 20/08/2014                                                                         #
# Contact: mrcyberfighter@gmail.com                                                            #
#                                                                                              #
# Credits: Thank's to my mother and the doctors. Stay away from drugs: Drugs destroy your      #
#          brain and your life !!!                                                             #
################################################################################################
################################################################################################
#                                         Description:                                         #
################################################################################################
# 	curser is a python module based and complementary to pygame,                           #
# 	who will give you analog functions as the turtle module implement                      #
# 	in a pygame display to make easier the generation and the animation of                 #
# 	forms like polygons, spirals, fractals and so soon.                                    #
# 	With abstraction of the coordinates computing throught an curser object analog         #
# 	to the turtle whose orientation is setable throught rotation functions                 #
# 	to the left or to the right from the number of wanted degrees with progressiv          #
# 	animated stroke drawing or not animated functions whose color and width is             #
# 	configurable.                                                                          #
################################################################################################
################################################################################################
#                                            Usage:                                            #
################################################################################################
# Description: Instanciate the Curser class with the following arguments:                      #
#                                                                                              #
#             -start_x: the start x coordinate from the curser start position.                 #
#                                                                                              #
#             -start_y: the start y coordinate from the curser start position.                 #
#                                                                                              #
#             -start_angle (default = 0)  : the start orientation from the curser.             #
#                                                                                              #
#             -color (default = (0, 0, 0)): the stroke and curser color given as a 3-elements  #
#                                         tuple (red,green,blue).                              #
#                                                                                              #
#             -bg_color (default = (255, 255, 255)): the display background color given as a   #
#                                                  3-elements tuple (red,green,blue).          #
#                                                                                              #
#             -stroke_width (default = 1): the stroke width in pixel(s) given as an integer.   #
#                                                                                              #
#             -curser_down (default = True): a boolean value if the curser is down.            #
#                                                                                              #
#                                                                                              #
#             to get an curser object who implement the following methods to drawing:          #
#                                                                                              #
#                                                                                              #
#             -mv_forward(px) : move the curser forward in the current direction               #
#                               from px pixels.                                                #
#                                                                                              # 
#             -mv_backward(px): move the curser backward in the opposite direction to          #
#                               the current from px pixels.                                    #
#                                                                                              #
#             -mv_left(degrees): turn the curser left from argument degrees degrees and        #
#                                update the current direction.                                 #
#                                                                                              #
#             -mv_right(degrees): turn the curser right from argument degrees degrees and      #
#                                 update the current direction.                                #
#                                                                                              #
#             -anim_forward(px,speed): move the curser forward in current direction from one   #
#                                      pixel every speed seconds (or fraction) from px pixels  #
#                                      far what create an stroke drawning animation effect.    #
#                                                                                              #
#             -anim_backward(px,speed): move the curser backward in the opposite direction     #
#                                       from one pixel every speed seconds (or fraction) from  #
#                                       px pixels far what create an stroke drawning animation #
#                                       effect.                                                #
#                                                                                              # 
#             -get_coords_forward(px) : return the coordinates for a forward moving result     #
#                                       from px pixels without drawing a stroke or move the    #
#                                       curser.                                                #
#                                       ! Use this method with your own coordinates            #
#                                         container.                                           #
#                                                                                              #
#             -get_coords_backward(px) : return the coordinates for a backward moving result   #
#                                        from px pixels without drawing a stroke or move the   #
#                                        curser.                                               #
#                                        ! Use this method with your own coordinates           #
#                                          container.                                          #
#                                                                                              #
#             -show_hook(): hook method to set in the pygame mainloop if you use it, this      #
#                           is the core for displaying the curser and the driven strokes.      #
#                                                                                              #
#             -curser_up(): raise the curser up and any curser moving method will not          #
#                           draw but the direction changings are effectiv.                     #
#                           ! This method does not hide the curser.                            #
#                                                                                              #
#             -curser_down(): put the curser down any moving method will draw on the display.  #
#                             ! This method do not show the curser if he is hidden.            # 
#                                                                                              #
#             -hide_curser(): hide the curser but does not raise him up is simply to hide the  #
#                             curser for driving.                                              #
#                                                                                              #
#             -show_curser(): show the curser but does not put him down.                       #
#                             ! The curser is visible per default.                             #
#                                                                                              #
#             -set_bg_color(bg_color) : change the display background                          #
#                                       ! You have to set the show_hook() method in the        #
#                                         mainloop to make it effectiv if you work with it.    #
#                                                                                              #
#             -set_curser_pos(x, y) : set the curser position to the coordinates x,y           #
#                                                                                              #
#             -set_stroke_color(color) : set stroke and curser color to the argument color     #
#                                        who must be an 3-elements tuple (red,green,blue)      #
#                                                                                              #
#             -set_stroke_width(stroke_width) : set the stroke width to the stroke_width       #
#                                               argument in pixels.                            #
#                                               ! The curser size will increase or decrease    #
#                                                 if you change the stroke width.              #
#                                                                                              #
#             -get_curser_pos() : return the current curser position as (x,y).                 #
#                                                                                              #
#             -get_stroke_color() : return the current stroke and curser color as              #
#                                   (red,green,blue) tuple.                                    #
#                                                                                              #
#             -get_stroke_width() : return the current stroke width in pixels.                 #
#                                                                                              #
#             -get_bg_color() : return the current display background color as                 #
#                               (red,green,blue) tuple.                                        #
#                                                                                              #
################################################################################################
################################################################################################
#                                   import directives                                          #
################################################################################################
# To do: import the module with the import directive:                                          #
#        ###########################################################################           #
#        # Python 2.7.3 (default, Apr 20 2012, 22:39:59)                           #           #
#        # [GCC 4.6.3] on linux2                                                   #           #
#        # Type "help", "copyright", "credits" or "license" for more information.  #           #
#        # >>> import curser                                                       #           #
#        # >>> # instanciate the Curser class like this                            #           #
#        # >>> turtle=curser.Curser(800/2,600/2)                                   #           #
#        # >>> # the object turtle will contains all the methods from the module   #           #
#        ###########################################################################           #
#         or import the Curser class with the from import directive                            #
#        ###########################################################################           #
#        # Python 2.7.3 (default, Apr 20 2012, 22:39:59)                           #           #
#        # [GCC 4.6.3] on linux2                                                   #           #
#        # Type "help", "copyright", "credits" or "license" for more information.  #           #
#        # >>> from curser import Curser                                           #           #
#        # >>> turtle=Curser(800/2,600/2)                                          #           #
#        # >>> # the object turtle will contains all the methods from the module   #           #
#        ###########################################################################           #
#                                                                                              #
################################################################################################
################################################################################################
#                                         Installation:                                        #
################################################################################################
# Linux:   Extract the zip file and change the current directory to /curser-1.0.0              #
#          and run the installation file with:                                                 #
#          $ sudo python setup.py install                                                      #
################################################################################################
# Windows: Extract the zip file and change the current directory to your python installation   #
#          root directory (containing pyhton.exe and run the installation file with:           #
#          C:\Python27> python C:\...\curser-1.0.0\setup.py install                            #
################################################################################################
################################################################################################
#                                     License                                                  #
################################################################################################
#                                                                                              #
#           ########################################################################           #
#           # curser an turtle for the pygame module.                              #           #
#           # Copyright (C) 2014 Bruggemann Eddie                                  #           #
#           #                                                                      #           # 
#           # This file is part of curser.                                         #           #
#           # curser is free software: you can redistribute it and/or modify       #           #
#           # it under the terms of the GNU General Public License as published by #           #
#           # the Free Software Foundation, either version 3 of the License, or    #           # 
#           # (at your option) any later version.                                  #           #
#           #                                                                      #           #
#           # curser is distributed in the hope that it will be useful,            #           #
#           # but WITHOUT ANY WARRANTY; without even the implied warranty of       #           #
#           # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the         #           #
#           # GNU General Public License for more details.                         #           #
#           #                                                                      #           # 
#           # You should have received a copy of the GNU General Public License    #           #
#           # along with curser. If not, see <http://www.gnu.org/licenses/>        #           #
#           ########################################################################           #
#                                                                                              #
################################################################################################
################################################################################################