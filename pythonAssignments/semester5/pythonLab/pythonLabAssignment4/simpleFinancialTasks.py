pl = lambda l: l[1] - l[0] # Profit / loss
si = lambda l: l[0]*l[1]*l[2]/100
ci = lambda l: l[0]*((1 + l[1]/100)**l[2] - 1)
nameMap = {"pl":pl, "si":si, "ci":ci}

print("\nSIMPLE FINANCIAL TASKS\n")
print("Format:\nfunction;arg1;arg2...\n")
print("Functions:\npl;cp;sp\nsi;p;r;t\nci;p;r;t\nx to exit\n(Extra arguments will be ignored)\n")
while True:
    inp = input(">> ").split(";")
    if(inp[0] == "x"): break
    try: print("=", nameMap[inp[0]](tuple(map(float, inp[1:]))))
    except KeyError: print("Function not found!") # Wrong function name
    except NameError: print("Extraneous spaces in function name!") # Extra spaces around the function name
    except ValueError: print("Non-numeric arguments!") # Non-numeric arguments
    except IndexError:print("Insufficient number of arguments!") # Some index of inp would be out of bounds