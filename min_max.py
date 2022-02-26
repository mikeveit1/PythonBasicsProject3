print("How many integers would you like to enter?")
numberOfInts = int(input())
print("Please enter", numberOfInts, "integers.")
for i in range(0, numberOfInts):
    num = int(input())
    while i == 0:
        min = num
        max = num
        break
    if num > max:
        max = num
    if num < min:
        min = num
    i += 1
print("min:", min)
print("max:", max)