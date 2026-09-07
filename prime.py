arr = list(map(int,input().split()))
smallest = arr[0]
for element in arr:
    if arr[0] < element:
        element = smallest
print(smallest)
