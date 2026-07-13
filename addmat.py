li=[[1,2,3],[4,5,6],[7,9,8]]
s=0
row=len(li)
col=len(li[0])
for i in range(row):
    for j in range(col):
     s=s+li[i][j]
print(s)