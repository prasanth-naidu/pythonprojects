li=[[1,2,3],[4,5,6],[7,8,9]]
s1=0
s2=0
row=col=3
for i in range(3):
    for j in range(3):
        if i==j:
            s1+=li[i][j]
            if(i+j)==row-1:
                s2+=li[i][j]
print("sum of diagonal1= ",s1)
print("sum of diagonal1= ",s2)