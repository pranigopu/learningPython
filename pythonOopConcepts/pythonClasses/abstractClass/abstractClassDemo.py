from abc import ABC, abstractmethod
# Abstract class to form a framework for all creatures
class mob(ABC):
    attributeNames = ("Name", "Class", "Nature", "Hit-points")
    @abstractmethod
    def action(self):
        pass
    def assignAttributes(self, values):
        i = 0
        for x in self.attributeNames:
            self.attributes[x], i = values[i], i + 1

# Creature 1: Goo-Blob
class gooBlob(mob):
    attributes = {}
    def __init__(self, name):
        super().assignAttributes((name, "Goo-Blob", "Hostile", 20))
    def action(self):
        print("{0} bounces & squishes menacingly.".format(self.attributes["Name"]))

# Creature 2: Stick Giant
class stickGiant(mob):
    attributes = {}
    def __init__(self, name):
        super().assignAttributes((name, "Stick Giant", "Neutral", 50))
    def action(self):
        print("{0} saunters absently.".format(self.attributes["Name"]))

# Creature 3: Feather Cat
class featherCat(mob):
    attributes = {}
    def __init__(self, name):
        super().assignAttributes((name, "Feather Cat", "Friendly", 10))
    def action(self):
        print("{0} tiptoes lightly.".format(self.attributes["Name"]))

def printDictionary(dictionary):
    for i in dictionary.items():
        print(i)
    print()

g = gooBlob("Shostakovich")
s = stickGiant("Tchaikovsky")
f = featherCat("Rachmaninoff")

print("\nAttributes of different creature-objects...")
printDictionary(g.attributes)
printDictionary(s.attributes)
printDictionary(f.attributes)

print("\nActions of different creature-objects...")
g.action()
s.action()
f.action()
print()