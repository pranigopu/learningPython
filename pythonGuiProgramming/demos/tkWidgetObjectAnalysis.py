import tkinter
def listAttributes(widget, widgetName):
    print("========================")
    print(widgetName.upper() + " OBJECT ATTRIBUTES...")
    print("------------")
    for i in widget.keys():
        print(i, end = ": ")
        print(widget[i])
# Window...
w = tkinter.Tk()
w.title("Button demo")
listAttributes(w, "Tk")
# Label...
l = tkinter.Label(w, text = "My label :)")
listAttributes(l, "Label")
# Button...
def dummyFunction(): pass
b = tkinter.Button(w, text = "My button :)", command = dummyFunction)
listAttributes(b, "Button")
"""
Apparently, every widget object is a dictionary-like structure.
The keys are the attribute names, and each key i.e. attribute name is attached to a value.
This is why we cannot access the attributes of a widget object using __getAttribute__,
since its attributes are bundled in a dictionary-like structure.

To access the attribute values of a widget, we can either do...
widgetObject["attributeName"]
or
widgetObject.cget("attributeName")

You can change these accessed attributes for the object as...
widgetObject["attributeName"] = newValues (just as you would in a dictionary)
or
widgetObject.configure(attributeName = newValues)

NOTE:
config and configure have the same functionality.
"""