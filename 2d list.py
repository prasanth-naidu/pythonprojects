def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        c = a+b
        a=b
        b=c

res = fibonacci(5)
print(res)