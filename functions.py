# 1. default arguments
# def fun(x , y = 20):
#     print(x)
#     print(y)

# fun(10)

# 2. keyword arguments
# fun( y = 50, x = 30)
# def student(fname, lname):
#     print(fname, lname)

# student(fname='Geeks', lname='Practice')
# student(lname='Practice', fname='Geeks')

# 3. positional arguments
# def nameAge(name, age):
#     print("Hi, I am", name)
#     print("My age is ", age)

# print("Case-1:")
# nameAge("Rudraksh", 21)

# print("\nCase-2:")
# nameAge(21, "Rudraksh")

# *args and **kwargs
'''
*args and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:

*args in Python (Non-Keyword Arguments)
**kwargs in Python (Keyword Arguments)
'''

# def myfun(*args, **kwargs):
#     print("non keyword arguments (*args) : ")
#     for arg in args:
#         print(arg)

#     print("keyword arguments: ")
#     for key, value in kwargs.items():
#         print(f" {key} = {value}")

# myfun("hi", 123, 4.5, True , fname = 'Rudraksh', lname = 'Kushwaha')


##FUNCTION WITHIN FUNCTION
# def f1():
#     s = 'I love solving DSA'
#     def f2():
#         print(s)
        
#     f2()
# f1()



##LAMBDA FUNCTION -- ANONYMOUS FUNCTION
#without lambda
# def cube(x):
#     return x*x*x

# print(cube(3))

#with lambda
# cube1 = lambda x:x*x*x
# print(cube1(4))


def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2

print(square_value(2))
print(square_value(-4))

