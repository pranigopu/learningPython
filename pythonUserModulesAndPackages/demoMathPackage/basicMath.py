def sum(a, b):
    return a + b
def difference(a, b):
    if a - b < 0:
        return b - a
    return a - b
def product(a, b):
    return a * b
def quotient(a, b):
    if b == 0:
        print("Zero denominator!")
        return 0
    return int(a / b)