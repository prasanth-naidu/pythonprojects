li=[1,2,3,4,5,2,4,1]
result=[]
for i in li:
    if(li.count(i)>1):
        result.append(i)
print(result)
print(set(result))