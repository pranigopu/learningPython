numbers = []
limit = int(input("\nEnter the number of values you want to compare: "))
for i in range(0, limit):
    numbers.append(float(input("Enter value: ")))
max = numbers[0]
for i in range(0, limit):
    if numbers[i] > max:
        max = numbers[i]
print("Largest number in the list is", max)