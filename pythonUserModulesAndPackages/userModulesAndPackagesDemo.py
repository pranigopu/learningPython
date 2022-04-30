import demoModule as dm
# ALTERNATE WAYS
# import demoModule - Refer to module elements with prefix "demoModule."
# from demoModule import... - Import specific elements. No prefix needed for referring to them.
# from demoModule import * - Import all elements. No prefix needed for referring to them.

import demoMathPackage as dmp
# NOTES
# The modules in the package must be handled based on the "__init__.py" file's contents.
# In this case, the module elements are available through the package name as thought the package were the module.

import demoGreetingPackage as dgp
import demoGreetingPackage.archaicGreetings as dgpag
# Check the text file notes for more information.

# Testing the functions
print("\nTesting module...")
dm.greet("Hondo")
print(dm.sumSquared(3, 4))

print("\nTesting package 1...")
print(dmp.sum(563, 278))
print(dmp.factorial(7))
print(dmp.addIntegersBetween(23, 70))

print("\nTesting package 2...")
dgp.informalGreet1("Obi-Wan Kenobi")
dgp.formalGreetings.formalGreet2("Darth", "Sidious")
dgp.formalGreet1("Mr.", "Lava")
dgpag.archaicGreet2("Anakin")