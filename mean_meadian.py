"""arr=[1,2,3,4,5,6]
n=len(arr)
print("mean:",sum(arr)/len(arr))
if n%2!=0:
    print("median:",arr[n//2])
else:
    print("median:",(arr[n//2])+(arr[n//2]-1)/2)"""

"""def occurance(s1,s2):
    if not (s1.islower() and s2.islower()):
        print("false")
        return False
    count=0
    for i in s2:
        for j in range(0,len(s1)):
            if i==s1[j]:
                count+=1
    return count
s1="soryu"
s2="lokry"
print(occurance(s1,s2))"""

age=10
if age>18:
    print("eligible")

print("not eligible")