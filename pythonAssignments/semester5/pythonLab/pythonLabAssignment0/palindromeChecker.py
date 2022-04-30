x = input("\nEnter a number or string: ")
max = int(len(x) / 2)
print(max)
for i in range(0, max):
    if x[i] != x[-(i + 1)]:
        i = max
        break
if i != max: print(x, "is a palindrome.")
else: print(x, "is not a palindrome.")