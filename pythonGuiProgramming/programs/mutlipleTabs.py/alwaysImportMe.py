# ALL THE LIBRARIES AND VARIABLES USE BY EVERY OTHER FILE HERE
from tkinter import *   
from tkinter.ttk import *             
from tkinter.ttk import Combobox
# Root window for the tab controller
root = Tk()
root.title("Lab test 2")
# Tab controller
# This will serve as the root for the frames that must be placed in tabs.
tabControl = Notebook(root)