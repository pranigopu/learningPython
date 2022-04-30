# MODULE WITH REQUIRED CLASSES
from shapeClasses import *

# DICTIONARY OF SHAPES
shapes = {
    "sphere":sphere,
    "cylinder":cylinder,
    "cone":cone,
    "r-prism":rectangularPrism,
    "t-prism":triangularPrism}

# FUNCTIONS
def printShapes():
    print("------------\nAVAILABLE SHAPES")
    for i in shapes.items():
        print(i)
def createShape():
    print("------------\nCREATE SHAPE")
    x = input(">> ")
    try: x = shapes[x]()
    except KeyError:
        if x == "?": printShapes()
        else: print("Shape not found!")
    else: print("Shape created.")
    return x
def shapeFormulae(x):
    try:
        print("------------\nSHAPE FORMULAE")
        print("Surface area:", x._sa)
        print("Volume:", x._vol)
    except: print("No shape created yet!")
def printFunctions():
    print("------------\nAVAILABLE SHAPE FUNCTIONS")
    print(">> sa for surface area")
    print(">> vol for volume")
def shapeFunction(x):
    print("------------\nSHAPE FUNCTIONS")
    try:
        functions = {"sa":x.sa, "vol":x.vol}
        # The above immediately checks if the shape is created
        inp = input(">> ")
        try: print(functions[inp]())
        except KeyError:
            if inp == "?": printFunctions()
            else: print("Function not found!")
    except: print("No shape created yet!")
if __name__ == "__main__":
    print("\nContains extra functions for handling shape objects created in 'shapeClasses.py'.\n")