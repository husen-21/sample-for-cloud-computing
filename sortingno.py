# Sorting Numbers using User Input

numbers = []

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers.sort()

print("Sorted Numbers:", numbers)
