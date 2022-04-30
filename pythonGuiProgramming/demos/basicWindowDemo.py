import tkinter
# CREATING MAIN WINDOW OBJECT
"""
Syntax:
Tk(screenName=None,  baseName=None,  className='Tk',  useTk=1)
___
Function:
To create an object for the main window.
Returns a new Toplevel widget on the screen screenName.
All arguments are optional.
"""
w = tkinter.Tk(screenName = None,  baseName = None,  className = 'Tk',  useTk = 1)
"""
className:
Specifies the widget subclass.
'Tk' is the top-level i.e. highest parent widget.
The Tk class has many children (for different widgets)
which can specified using this option.
This value will be reflected as the window name.
"""
# WINDOW SPECIFICATIONS AND WIDGETS
"""
Window specifications and widgets are defined
before the function to start the application, which makes sense.
"""
# WINDOW SPECIFICATIONS
w.title("Basic window demo") # Window title (visible on the title bar of the window).
# Note that the length of this title determines the minimum width of the window.
w.geometry("200x60") # Window dimensions in pixels.
# WIDGETS
# Label...
"""
Syntax (for class constructor i.e. intialisation):
Label(parent, text, font, etc.)
NOTE: All arguments are optional.
___
Function:
A widget to display some text in a specified location for the specified window object.
"""
l1 = tkinter.Label(w, text = "Hello there!", font = ("Arial Italic", 20))
l1.grid(column = 0, row = 0) # Position of the label in the window.

l2 = tkinter.Label(w, text = "General Kenobi!", font = ("Helvetica Bold", 20))
l2.grid(column = 0, row = 1) # Position of the label in the window.

"""
NOTES ON GRID POSITION
___
The widgets are only placed when their grid location is specified.
The grid location is not an absolute point on the window.
It is relative to the other widgets.

In other words, the grid is created dynamically as more widgets are added,
and it is not the absolute size of the column and row values, but their ranks w.r.t.
other widgets that determines where the respective widget is placed.
"""
# STARTING APPLICATION
"""
Syntax:
mainloop()
___
Function:
Used when your application is ready to run.
mainloop() is an infinite loop used to run the application,
wait for an event to occur and process the event
as long as the window is not closed.
"""
tkinter.mainloop()
"""
mainloop() can be attached to an object, in order to create an application using the object's attributes and methods.
"""