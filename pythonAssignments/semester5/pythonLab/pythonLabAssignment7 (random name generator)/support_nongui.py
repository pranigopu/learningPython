from random import choice
def trim(s):
    i = 0
    if s.isspace(): return " " # If the whole string is full of spaces.
    # Removing leading spaces...
    while s[i].isspace(): i = i + 1
    s, i = s[i:], -1
    # Removing trailing spaces...
    while s[i].isspace(): i = i - 1
    if i != -1: s = s[:(i + 1)]
    return s
def getTopNames(c, n):
    names, c, i = "", c.upper(), 0 # N => selected names
    #----------------------
    # Getting n names starting from letter denoted by c.
    f = open("names.txt", "r")
    # We assume every line is a name, and hence every name ends with a newline character.
    name = f.readline()
    while name != "" and i < n:
        if name[0].upper() == c: names, i = names + name, i + 1
        name = f.readline()
    f.close()
    return trim(names)
def getRandomName(c): 
    N, c = [], c.upper() # N => selected names
    #----------------------
    # Getting all names starting from letter denoted by c...
    #------
    f = open("names.txt", "r")
    # We assume every line is a name, and hence every name ends with a newline character or is at the end of the file.
    name = f.readline()
    while name != "":
        if name[0].upper() == c: N.append(name)
        name = f.readline()
    #--------------------
    # Returning a random name...
    #------
    f.close()
    return trim(choice(N))
def alphabetList(): return tuple(map(chr, range(ord("A"), ord("Z") + 1)))