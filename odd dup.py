li=[1,2,3,4,1,2,3,1,2,3,5,5,6]
result=[]
for i in li:
    if(li.count(i)%2!=0):
        result.append(i)
print(result)
print(set(result))