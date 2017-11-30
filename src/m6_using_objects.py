"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Ethan Baker.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------
    center_point_1 = rg.Point(200, 100)
    window = rg.RoseWindow()
    circle_1 = rg.Circle(center_point_1, 20)
    circle_1.fill_color = 'red'
    circle_1.attach_to(window)

    center_point_2 = rg.Point(200, 200)
    circle_2 = rg.Circle(center_point_2, 30)
    circle_2.attach_to(window)

    window.render()

    window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------
    window = rg.RoseWindow()
    cpx = 200
    cpy = 200
    center_point = rg.Point(cpx, cpy)
    x1 = 20
    y1 = 50
    x2 = 100
    y2 = 100
    point1 = rg.Point(x1, y1)
    point2 = rg.Point(x2, y2)
    rectangle = rg.Rectangle(point1, point2)
    circle = rg.Circle(center_point, 20)
    circle.outline_thickness = 8
    rectangle.outline_thickness = 6

    circle.fill_color = 'blue'
    circle.attach_to(window)
    rectangle.attach_to(window)

    window.render()

    print(circle.outline_thickness)
    print(circle.fill_color)
    print(center_point)
    print(cpx)
    print(cpy)
    print(rectangle.outline_thickness)
    print('none')
    print((x2 + x1)/2, (y1 + y2)/2)
    print((x2 + x1)/2)
    print((y1 + y2)/2)

    window.close_on_mouse_click()


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    # ------------------------------------------------------------------
    window = rg.RoseWindow()
    point1 = rg.Point(100, 300)
    point2 = rg.Point(50, 250)
    point3 = rg.Point(40,200)
    point4 = rg.Point(70, 150)
    line1 = rg.Line(point1, point2)
    line2 = rg.Line(point3, point4)
    line2.thickness = 4
    midpoint2 = rg.Line.get_midpoint(line2)
    print(midpoint2)
    print((40 +70)/2)
    print((150 +200)/2)

    line1.attach_to(window)
    line2.attach_to(window)
    window.render()

    window.close_on_mouse_click()



# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
