
==========
**curser**
==========
--------------------------------
**the turtle module for pygame**
--------------------------------
    +-----------------------------------------------------------------------------------+
    |                                DESCRIPTION                                        |
    +===================================================================================+
    |                                                                                   |    
    |    curser is a python module based and complementary to pygame,                   |    
    |    who will give you analog functions as the turtle module implement              |
    |    in a pygame display to make easier the generation and the animation of         |
    |    forms like polygons, spirals, fractals and so soon.                            | 
    |    With abstraction of the coordinates computing throught an curser object,       |
    |    analog to the turtle, whose orientation is setable throught rotation functions |
    |    to the left or to the right from the number of wanted degrees with progressiv  |
    |    animated stroke drawing or not animated functions whose color and width are    |
    |    configurable.                                                                  |
    |                                                                                   |
    +-----------------------------------------------------------------------------------+
        
        - Instanciate the Curser class with the following arguments:
        
            * start_x: 
            
                + the start x coordinate from the curser start position.
                                                                                               
            * start_y: 
            
                + the start y coordinate from the curser start position.                 
                                                                                       
            * start_angle (default = 0)  : 
            
                + the start orientation from the curser.            
                                                                                            
            * color (default = (0, 0, 0)): 
            
                + the stroke and curser color given as a 3-elements tuple (red,green,blue).                              
                                                                                             
            * bg_color (default = (255, 255, 255)): 
            
                + the display background color given as a 3-elements tuple (red,green,blue).          
                    
            * stroke_width (default = 1): 
            
                + the stroke width in pixel(s) given as an integer.
                     
            * curser_down (default = True): 
            
                + a boolean value if the curser is down. 
        
        - to get an curser object who implement the following methods:
        
        - The module curser implement following functions for the displaying 
          of the curser, the strokes attributes and the background display screen:
            
            * show_curser()
                
                + Show the curser but does not put him down.
                  
                  ! The curser is visible per default. 
                  
            * hide_curser()
                
                + Hide the curser but does not raise him up, 
                  is simply to hide the curser for driving.
            
            * set_stroke_color(color)
                
                + set stroke and curser color to the argument color                      
                  who must be an 3-elements tuple (red,green,blue)  
                      
            * set_stroke_width(stroke_width)
              
                + set the stroke width to the stroke_width argument in pixels.
                  
                  ! The curser size will increase or decrease    
                  if you change the stroke width.              
                 
            * set_bg_color(bg_color)
            
                + Change the display background.                                                                
                  
                  ! You have to set the show_hook() method in the
                  mainloop to make it effectiv if you work with it.
           
        - The module curser implement following curser control functions 
          for the turtle curser control:
            
            * curser_up()
            
                + Raise the curser up and any curser moving method will not                                    
                  draw but the direction changings are effectiv.                     
                
                  ! This method does not hide the curser.
                
                                             
            * curser_down()
                
                + Put the curser down any moving method will draw on the display.              
                  
                  ! This method do not show the curser if he is hidden.          
            
            * set_curser_pos(x,y)
            
                + Set the curser position to the coordinates x,y.
            
        - The module curser implement following turtle moving and orientation functions:

            * mv_forward(px)
            
                + Move the curser forward in the current direction from px pixels.
                
            * mv_backward(px)
            
                + Move the curser backward in the opposite direction to the current from px pixels.
                
            * mv_left(degrees)
                
                + Turn the curser left from argument degrees degrees and update the current direction.

            * mv_right(degrees)
            
                + Turn the curser right from argument degrees degrees and update the current direction.
                 
            * anim_forward(px,speed)
            
                + Move the curser forward in current direction from one pixel every speed seconds (or fraction) from px pixels far what create an stroke drawning animation effect.
                
            * anim_backward(px,speed)  
            
                + move the curser backward in the opposite direction from one pixel every speed seconds (or fraction) from px pixels far what create an stroke drawning animation effect.

        - The module curser implement following functions for use of personnalized 
          coordinates container(s) giving you the control for the displayed forms were
          you can use to store your forms coordinates:

            * get_coords_forward(px)
            
                + Return the coordinates for a forward moving result from px pixels without drawing a stroke or move the curser.
                  
                  ! Use this method with your own coordinates container.
                
            * get_coords_backward(px)
            
                + Return the coordinates for a backward moving result from px pixels without drawing a stroke or move the curser.
                  
                  ! Use this method with your own coordinates container. 

            * get_curser_pos()
             
                + return the current curser position as (x,y). 
            


                                             
        - Import the module with the import directive: 
                                        
        ::  
    
            ###########################################################################
            # Python 2.7.3 (default, Apr 20 2012, 22:39:59)                           #
            # [GCC 4.6.3] on linux2                                                   #
            # Type "help", "copyright", "credits" or "license" for more information.  #
            # >>> import curser                                                       #
            # >>> # instanciate the Curser class like this                            #
            # >>> turtle=curser.Curser(800/2,600/2)                                   #
            # >>> # the object turtle will contains all the methods from the module   #
            ###########################################################################
  
        - or import the Curser class with the from import directive:
 
        :: 
       
            ###########################################################################
            # Python 2.7.3 (default, Apr 20 2012, 22:39:59)                           #
            # [GCC 4.6.3] on linux2                                                   #
            # Type "help", "copyright", "credits" or "license" for more information.  #
            # >>> from curser import Curser                                           #
            # >>> turtle=Curser(800/2,600/2)                                          #
            # >>> # the object turtle will contains all the methods from the module   #
            ###########################################################################
    

        - And enjoy to use this module, master and animate many forms with curser: 
          the turtle module for pygame.
        
        - Some examples scripts are deliver with the module to show you the power of curser. 

