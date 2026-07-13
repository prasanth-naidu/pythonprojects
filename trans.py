li=[[1,2,3],4,5,6]
row=len(li)
col=len(li[0])
sum=0
for i in range(col):
    for j in range(row):
        print(li[i][j],end=" ")
print()