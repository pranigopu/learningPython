import numpy as np
A = np.random.rand(2, 4)
# The range of random values is 0-1.
# To increase the magnitude and make the elements integers...
A = (A * 10).astype(int)

print("\nNUMPY ARRAY HANDLING")
print("========================")
print("Random array:\nA =")
print(A)
print("========================")
# SQUARE ROOT ARRAY
B = np.sqrt(A)
print("Square roots of elements A:\nB =")
print(B)
print("========================")
# CONCATENTATION OF ARRAYS
C = np.concatenate((A, B), axis = None)
# axis = None ensures that the resultant is a 1D array

print("Concatenation of A and B:\nC = [")
for i in C: print(i, end = ",\n")
print("]")
print("========================")
print("Number of even values in C =", np.sum(C % 2 == 0))
print("Number of odd values in C =", np.sum(C % 2 == 1))
print("\n")