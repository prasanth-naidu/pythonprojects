def remove_duplicates(arr):
    seen =[]
    dup = []
    for i in arr:
        if i in seen:
            dup.append(i)
        else:
            seen.append(i)
    return dup
arr=list(map(int,input().split()))
print(remove_duplicates(arr))