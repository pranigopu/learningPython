from abc import ABC, abstractmethod
class shape(ABC):
    # Surface area and volume abstract methods...
    @abstractmethod
    def sa(self): pass
    @abstractmethod
    def vol(self): pass
    # Value input function...
    def inp(self, p):
        output = p
        if input("Input parameters? (n to deny): ") == "n": return output
        for i in p.keys():
            try: output[i] = float(input("{0}: ".format(i)))
            except: output[i] = p[i]
        return output
    # Formula calculation methods...
    # 1. Simple calculations
    def calc(self, op, a, b):
        try: return {"+":a+b,"-":a-b,"*":a*b}[op] # Unproblematic operations
        except KeyError:
            """
            Possible problems in power and division...
            # Power may be exceedingly high
            # Possible division by zero
            """
            try: return {"^":a**b}[op]
            except:
                try: return {"/":a/b}[op]
                except: return "NaN"        
    # 2. Precedence of operators and brackets
    def precedence(self, op):
        try: return {"(":0, "+":1, "-":1, "*":2, "/":2, "^":3}[op]
        except KeyError: return -1 # For validation purposes
    # 3. Conversion from infix expression to postfix
    def infixToPostfix(self, exp, p):
        # Necessary variables, structures and modifications...
        p["pi"], exp = 3.14159, exp + ");"
        postfix, stack, tmp, i = [], ["("], str(), 0
        # Conversion process...
        while exp[i] != ";":
            # To store full numbers...
            if exp[i].isnumeric() or exp[i] == ".":
                tmp, i = exp[i], i + 1
                while exp[i].isnumeric() or exp[i] == ".":
                    tmp, i = tmp + exp[i], i + 1
                try: p[tmp] = float(tmp) # To ensure the numeric string is mapped with its value
                except: p[tmp] = tmp # In case of conversion error
                postfix.append(tmp)
            # To store full variable names...
            if exp[i].isalpha():
                tmp, i = exp[i], i + 1
                while exp[i].isalpha():
                    tmp, i = tmp + exp[i], i + 1
                postfix.append(tmp)
            # To store operators...
            if exp[i] == "(":
                stack.append(exp[i])
            elif exp[i] == ")":
                while stack[-1] != "(":
                    postfix.append(stack.pop())
                stack.pop() # Removing the left bracket
            else: # Here, operator should be encountered...
                while self.precedence(stack[-1]) >= self.precedence(exp[i]):
                    postfix.append(stack.pop())
                stack.append(exp[i])
            i = i + 1
        return (p, postfix)
    # 4. Evaluation of formula
    def formula(self, exp, p):
        (p, postfix), i = self.infixToPostfix(exp, p), 0
        while i < len(postfix):
            if self.precedence(postfix[i]) == -1:
                postfix[i], i = p[postfix[i]], i + 1
            else:
                tmp = self.calc(postfix[i], postfix[i - 2], postfix[i - 1])
                if tmp == "NaN": return tmp
                del(postfix[i], postfix[i - 1], postfix[i - 2])
                postfix.insert(i - 2, tmp)
                i = i - 1
        return postfix[i - 1]

class sphere(shape):
    p, _sa, _vol = {"r":0}, "4*pi*r^2", "(4/3)*pi*r^3"
    def __init__(self): self.p = super().inp(self.p)
    def sa(self): return super().formula(self._sa, dict(self.p))
    def vol(self): return super().formula(self._vol, dict(self.p))
class cylinder(shape):
    p, _sa, _vol = {"r":0, "h":0}, "2*pi*r*(r+h)", "pi*(r^2)*h"
    def __init__(self): self.p = super().inp(self.p)
    def sa(self): return super().formula(self._sa, dict(self.p))
    def vol(self): return super().formula(self._vol, dict(self.p))
class cone(shape):
    p, _sa, _vol = {"r":0, "h":0, "s":0}, "pi*r*(s+r)", "(1/3)*pi*(r^2)*h"
    def __init__(self): self.p = super().inp(self.p)
    def sa(self): return super().formula(self._sa, dict(self.p))
    def vol(self): return super().formula(self._vol, dict(self.p))
class rectangularPrism(shape):
    p, _sa, _vol = {"l":0, "w":0, "h":0}, "2*(l*w+w*h+h*l)", "l*w*h"
    def __init__(self): self.p = super().inp(self.p)
    def sa(self): return super().formula(self._sa, dict(self.p))
    def vol(self): return super().formula(self._vol, dict(self.p))
class triangularPrism(shape):
    p, _sa, _vol = {"b":0, "l":0, "w":0, "h":0, "s":0}, "b*h+2*l*s+l*b", "(1/2)*b*l*h"
    def __init__(self): self.p = super().inp(self.p)
    def sa(self): return super().formula(self._sa, dict(self.p))
    def vol(self): return super().formula(self._vol, dict(self.p))
"""
DUPLICATING DICTIONARY FOR PASSING AS ARGUMENT
___
We pass dict(self.p) and not self.p, because the associated dictionary is being modified in the function,
and since it is a collection, even if it is passed as an argument, the copy of the identifier is merely
another name for the same memory addresses i.e the same dictionary internally.
___
Hence, we create a new dictionary object with the same values using dict(self.p), and
pass that to the function so that the original dictionary remains untouched.
---*---*---
WHY WE NEED NOT DO THE SAME FOR STRINGS
___
Technically, a string are also a collection (of characters).
However, a string is also immutable. Hence, we need not worry about unwillingly changing the original string.
This also applies to other immutable collections such as tuples and frozen sets.
"""
if __name__ == "__main__":
    print("\nContains class definitions for various shapes.\n")