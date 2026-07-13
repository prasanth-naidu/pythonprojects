student_name = input("enter the student name:")

sub1 = int(input("enter the marks:"))
sub2 = int(input("enter the marks:"))
sub3 = int(input("enter the marks:"))

total = sub1+sub2+sub3
average = sub1+sub2+sub3/3
percentage=(total/300)*100

print(total)
print(average)
print(percentage)

if percentage >= 35:
    print("pass")
else:
    print("fail")
    