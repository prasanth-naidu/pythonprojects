"""n=int(input())
if n>0:
    print("positive")"""

"""s=input()
if s=="":
    print("empty string")"""
"""n=int(input())
if n>0:
    print("positive")
if n<0:
    print("negative")
if n==0:
    print("zero")"""
"""n=int(input())
root=(n**0.5)
if root*root==n:
    print("perfect square")"""

"""n=int(input())
cube=(n**(1/3))
if cube*cube*cube==n:
    print("perfect cube")"""

"""n=int(input())
if n%2==0 and n%3==0:
    print("divisible by 2 and 3")"""

"""n=int(input())
if n%3==0 or n%5==0:
    print("divisible by 3 or 5")"""

"""n=int(input())
if n%4==0:
    print("divisible by 4")"""

"""def leap_year(year):
    if (year%400==0) or (year%4==0 and year%100!=0):
        print("leap year")
    else:
        print("not a leap year")
leap_year(2020)"""

def check_alphabet(alpha):
    alpha=alpha.lower()
    if alpha.lower() in 'aeiou':
        print("vowel")
    else:
       print("consonant") 
check_alphabet('s') 

def century(year):
    if year%100==0:
        print("century")
    else:
        print("not a century")
century(500)

def vote(age):
    if age>=18:
        print("eligible to vote")
    else:
        print("not eligible to vote")
vote(20)

def check_number(num):
    if num>0:
        print("positive")
    else:
        print("non_positive")
check_number(-5)

def check_number(num):
    if num<1:
        print("not prime")
    else:
        count=0
        for i in range(1,num+1):
            if num%i==0:
                count+=1
        if count==2:
            print("prime")
        else:
            print("not prime")
check_number(9)

def largest(a,b):
    if a>b:
        print("a is largest")
    else:
        print("b is largest")
largest(10,20)

def smallest(a,b,c):
    if a<b:
        if a<c:
            print("a is smallest")
        else:
            print("c is smallest")
    else:
        if b<c:
            print("b is smallest")
        else:
            print("c is smallest")
smallest(10,20,30)

k="rgtj"
if k==k[::-1]:
    print("palindrome")
else:
    print("not a palindrome")

