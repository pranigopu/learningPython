# MODULE CONTAINING REQUIRED FUNCTIONS
from shapeHandlingFunctions import *

# HELP FUNCTION
def help():
    print("------------\nAVAILABLE OPTIONS")
    print(">> create makes a new shape object.")
    print(">> formulae prints all formulae for the shape.")
    print(">> fun allows application of function for the shape.")
    print(">> ? shows available options in any section.")
    print(">> x enables you to exit from main code.")

# DICTIONARY OF FUNCTIONS
argOptions = {
    "formulae":shapeFormulae,
    "fun":shapeFunction}
noArgOptions = {
    "?":help,
    "x":exit}

# MAIN FUNCTION
x = 0
print("========================")
print("FUN WITH SHAPES\n(Enter '?' for help)")
while True:
    print("------------\nMAIN CODE")
    option = input(">> ")
    if option == "create": x = createShape()
    else:
        try: argOptions[option](x)
        except KeyError:
            try: noArgOptions[option]()
            except KeyError: print("Option unavailable!")