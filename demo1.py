n = int(input("Enter size: "))

arr = []
for i in range(n):
    arr.append(int(input()))

maximum = arr[0]

for i in range(n):
    if arr[i] > maximum:
        maximum = arr[i]

print("Max element:", maximum)
