import tkinter
import tkinter.ttk as ttk
from sympy import Symbol, Eq, solve, pprint
from numpy import linspace
from matplotlib.pyplot import scatter, show

# For parsing string as SymPy expression...
from sympy.parsing.sympy_parser import parse_expr as parse

# For embedding plot in GUI window...
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
#================================================
# GLOBAL VARIABLES
#------------------------
v = ["x", "y"] # Dependent variables (always same)
plotOptions = ["x-interval", "x-breaks"] # Plot customization options (made as a list for scalability)
params = [] # Independent parameters (any alphabet except x and y)
paramsValues = [] # Values given to the independent parameters by the user
paramsInputFrameWidgets = [] # Children widgets of the parameter input frame widget (defined later)
inputtedEquation = [''] # Inputted equation (given as a list so that changes are persistent)
#================================================
# HELPER FUNCTION DEFINITIONS
#------------------------
# Destroying widget's children, hence clearing it
# Ex. destroying all its children widgets
def destroyChildren(widget):
    for child in widget.winfo_children():
        child.destroy()

# Checking if inputted equation is valid
def isValidEquation():
    if inputtedEquation[0] == '': return False
    return True

# Checking if value is valid decimal number
def isDecimal(value):
    value = str(value).strip()
    # We have removed any leading or trailing spaces
    
    try:
        if value[0] == '-': value = value[1:]
    except: return False # Exception occurs when value is given as an empty string
    # Neglecting any possible negative signs at the start.

    points = 0 # Number of floating points detected
    for c in value:
        if not c.isnumeric(): return False
        if c == '.' and points == 0: points = points + 1
        elif c == '.' and points > 0: return False
    return True

# Performing the right function on the given plot option
def getInterval(s):
    default = [-10, 10]
    try:
        s = s.split(',')
        if len(s) != 2: return default
        return list(map(float, s))
    except: return default
def getPositiveInteger(s):
    try:
        s = abs(int(s))
        if s == 0: return 1
        if s > 500: return 500
        return s
    except: return 30 # Default
def getAppropriateValue(option, value):
    # We assume the option given is always valid, since it is internally handled
    n = {
        plotOptions[0]: getInterval, # x-interval
        plotOptions[1]: getPositiveInteger}[option](value) # x-break
    return n
#================================================
# MAIN FUNCTION DEFINITIONS
#------------------------
# Converting string equation input to SymPy equation
def processEquation():
    equation = equationEntry.get()
    equation = equation.replace("^", "**") # Replacing ^ with Python exponent operator
    #____________
    # Clearing all previous values of the global variables
    params.clear()
    paramsValues.clear()
    paramsInputFrameWidgets.clear()
    #____________
    # Identifying parameters
    for c in equation:
        if c.isalpha() and c not in params and c not in v:
            params.append(c)
    #____________
    try:
        # Clearing previous message (if any)
        equationValidityLabel["text"] = " "

        # Obtaining equation
        equation = equation.split("=")
        lhs, rhs = parse(equation[0].strip()), parse(equation[1].strip())
        # '.strip' removes leading and trailing spaces
        # Making a SymPy equation
        equation = Eq(lhs, rhs)
        inputtedEquation[0] = equation

        # Printing on console for testing...
        print("\nInputted equation...")
        pprint(equation)
    except:
        equationValidityLabel["text"] = "Invalid equation"
        inputtedEquation[0] = ''
#------------------------
# Identifying equation parameters & creating necessary entry and submit button widgets
def defineParamsAndOptions():
    # Clearing the previous elements of the parameter input frame
    destroyChildren(paramsInputFrame)
    """
    This will ensure that new parameter entry boxes will not be
    appended to the old ones,  but will instead replace them.
    """
    #____________
    # Obtaining the inputted equation (which will be stored in the global variable)
    processEquation()
    if not isValidEquation(): return # Aborting process if equation not valid
    # Otherwise, do the following...
    # Display equation in the title of the window
    root.title("Equation Grapher: " + equationEntry.get())
    # Display one of the following messages
    if len(params) > 0: equationValidityLabel["text"] = "Enter parameters & options"
    else: equationValidityLabel["text"] = "No equation parameters, enter plot options"
    #____________
    # Creating a list of parameter entry widgets under the 'paramsInputFrame' frame widget
    for p in params:
        paramsInputFrameWidgets.append(tkinter.Entry(paramsInputFrame, width=10))

    # Creating a list of plotting option entry widgets under the 'paramsInputFrame' frame widget
    for p in plotOptions:
        paramsInputFrameWidgets.append(tkinter.Entry(paramsInputFrame, width=10))

    # Creating a submit button for triggering a reading of the inputs
    paramsInputFrameWidgets.append(tkinter.Button(paramsInputFrame, text="SUBMIT", command=createPlot))

    # Creating a label for displaying error messages
    paramsInputFrameWidgets.append(tkinter.Label(paramsInputFrame))
    #____________
    # Fixing the layout of the elements within the frame
    i = 0 # Counter
    #......
    # Parameter entry boxes
    for p in params:
        # Label to indicate
        tkinter.Label(paramsInputFrame, text=p).grid(row=i, column=0, sticky="e")
        # Entry box (since the submit button at the end is excluded in this looping)
        paramsInputFrameWidgets[i].grid(row=i, column=1)
        i = i + 1
    #......
    # Plotting option entry boxes
    for p in plotOptions:
        # Label to indicate
        tkinter.Label(paramsInputFrame, text=p).grid(row=i, column=0, sticky="e")
        # Entry box (since the submit button at the end is excluded in this looping)
        paramsInputFrameWidgets[i].grid(row=i, column=1)
        i = i + 1
    #......
    # Submit button and message label
    # Submit button
    paramsInputFrameWidgets[-2].grid(row=i, column=1)
    # Label
    paramsInputFrameWidgets[-1].grid(row=i+1, column=1)
#------------------------
# Applying the inputted parameters to equation, obtaining x and y values, and plotting graph
# (Plot is embedded within the window)
def createPlot():
    # Clearing previous messages (if any)
    paramsInputFrameWidgets[-1]["text"] = " "
    #____________
    # Accessing and verifying the inputted equation
    equation = inputtedEquation[0]
    if not isValidEquation: return # Aborting process if equation not valid
    #____________
    # Substituting parameters with their inputted values
    for i, p in enumerate(params):
        value = paramsInputFrameWidgets[i].get()
        # Checking if value is a valid decimal number
        if not isDecimal(value):
            # Displaying error message
            paramsInputFrameWidgets[-1]["text"] = "Invalid constants"
            return
        equation = equation.subs({Symbol(p):value})
    
    # Printing on console for testing...
    print("\nParticular equation...")
    pprint(equation)
    #____________
    # Creating plot
    #......
    # Obtaining domain (if possible) from plot options
    # Slicing the list to obtain plot option entry widgets
    plotOptionWidgets = paramsInputFrameWidgets[len(params):]
    plotOptionsValues, i = [], 0
    for p in plotOptions:
        appropriateValue = getAppropriateValue(p, plotOptionWidgets[i].get())
        plotOptionsValues.append(appropriateValue)

        # Extra...
        # Replacing visible inputs with the obtained appropriate values
        """
        This would be a helpful visual when one or more inputs
        are empty or invalid, and are hence changed to defaults.
        """
        try: appropriateValue = ",".join(list(map(str, appropriateValue)))
        except: appropriateValue = str(appropriateValue)
        # If 'appropriateValue' is an iterable value, like a list, then
        # join each element (.join requires each element to be a string, hence we use 'map').
        plotOptionWidgets[i].delete(0, "end") # Removing
        plotOptionWidgets[i].insert(0, appropriateValue)
        i = i + 1
    """
    Note that the function 'getAppropriateValue' is designed to
    always return a usable value, no matter the argument.
    Hence, we have no exception handling here.
    """
    #......
    # Defining the x and y value lists within a given domain
    xInterval, xBreaks= plotOptionsValues[0], plotOptionsValues[1]
    domain = linspace(xInterval[0], xInterval[1], xBreaks)
    x, y = [], []
    for i in domain:
        tmp = equation.subs({Symbol(v[0]):i})
        solutions = list(solve(tmp, Symbol(v[1])))
        for s in solutions:
            try:
                s = float(s)
                x.append(i)
                y.append(s)
            except: pass # Passes for complex valued solutions
    #......
    # Creating plotting figure and widget
    # Following code adapted from: https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/
    figure = Figure(figsize=(4,4))
    myPlot = figure.add_subplot(111)
    myPlot.scatter(x, y)
    # Show axis lines
    myPlot.axhline(color="black")
    myPlot.axvline(color="black")
    # Show grid
    myPlot.grid()

    # Clearing the previous elements of the plot frame
    destroyChildren(plotFrame)
    """
    This will ensure that a new plot will not be appended to an old plot,
    but will instead replace it.
    """

    # Creating container for figure within plot frame
    canvas = FigureCanvasTkAgg(figure, master=plotFrame) 
    canvas.draw()
    # Packing the canvas in the plot frame
    canvas.get_tk_widget().pack()
#================================================
# MAJOR GUI ELEMENTS
#------------------------
# DEFINING WINDOW OBJECT
root = tkinter.Tk() # Initialisation
root.title("Equation Grapher") # Title bar text
root.geometry("500x600") # Dimensions
root.resizable(False, False) # Resizing not allowed in any direction
#------------------------
# EQUATION & PARAMETER INPUTS
#____________
equationInputFrame = tkinter.Frame(root)
# Equation entry box
equationEntry = tkinter.Entry(equationInputFrame, width=20)
# Processing the equation (i.e. defining the appropriate parameter entry boxes)
processButton = tkinter.Button(equationInputFrame, text="GO", command=defineParamsAndOptions)
# Packing within frame
tkinter.Label(equationInputFrame, text="Enter your equation...").pack() # Prompt
equationEntry.pack(side="left", anchor="n")
processButton.pack(side="left", anchor="n")
"""
We are using frame here for ease of packing.
"""

# Label to indicate whether equation was valid
equationValidityLabel = tkinter.Label(root)
# (We have also reused this to display prompt for parameter entry)
#____________
# Parameter input frame
paramsInputFrame = tkinter.Frame(root)
"""
We are using frame here to allow for easy dynamic addition and removal of widgets,
since the number parameters can change based on the equation.
Using a frame can help group all these dynamically added and removed widgets
so that the overall layout management becomes easier to define.
"""
#____________
# Plot container frame
plotFrame = tkinter.Frame(root)
#------------------------
# LAYOUT MANAGEMENT
# Heading
equationInputFrame.pack()
equationValidityLabel.pack()
paramsInputFrame.pack()
plotFrame.pack()
#================================================
# RUNNING THE APPLICATION IN AN INFINITE LOOP
#------------------------
root.mainloop()