def str_int(a):
    int(a)

a=input()
x=str_int(a)
print(x)

# Define a function to convert string to integer
def str_to_int(s):
    return int(s)

# Call the function
result = str_to_int("123")
print(result)        # Output: 123
print(type(result))  # Output: <class 'int'>
