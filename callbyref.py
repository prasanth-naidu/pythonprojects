def add(li):
    li[0]=999
    li.pop()
    li.append(4567)
li=[1,2,3,4]
add(li)
print(li)

a=[1,2,3,4]
add(li)
print(li)