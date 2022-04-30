# Not the most efficient factorial function, but I wanted to use recursion and include negative integer functionality.
def factorial(n):
    sign = 1
    if n < 0:
        sign = -1
        n = -n
    if n == 0:
        return 1
    return sign * n * factorial(n - 1)

# Not the most efficient power function, but I wanted to use recursion and include negative power functionality.
def power(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return float(1 / a * power(a, n - 1))
    return a * power(a, n - 1)

# Adds all integers in an open interval
def addIntegersBetween(a, b):
    sum = a + 1
    if a + 1 < b:
        return sum + addIntegersBetween(a + 1, b)
    return 0