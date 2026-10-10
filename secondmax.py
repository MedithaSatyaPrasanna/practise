n = int(input())
arr = list(map(int, input().split()))

max_val = arr[0]
smax = -1

for i in range(n):
    if arr[i] > max_val:
        smax = max_val
        max_val = arr[i]

    elif arr[i] > smax and arr[i] < max_val:
        smax = arr[i]

print("Second Max:", smax)