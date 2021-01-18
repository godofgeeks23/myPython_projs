# functions in python

# def keyword is used in python to define a function
# syntax of a function in python:
# def <function-name>(<argument list>):
#     coding of the function

# function can be defined anywhere in program in python
# just remember that function should be called only after defining it

# example:


def add_two(a, b):
    return (a + b)


total = add_two(5, 4)
print(total)

total = add_two(5, add_two(2, 3))
print(total)

total = add_two("Aviral ", "Srivastava")
print(total)


def wish():
    print("Happy Birthday")


wish()

# to give default parameters in a function in python, see example:


def show_details(fname, sname, age=18):
    print(f"You are {fname} {sname} and are {age} years old.")


show_details("Aviral", "Srivastava")
show_details("Aviral", "Srivastava", 23)

# ---------------------------------------------------------------

# understanding the scope of variables

x = 1


def func1():
    x = 10
    return x


print("Global = {}, Local = {}".format(x, func1()))


def func2():
    global x
    x = 20
    return x


print("x = {}, func2() returned = {}, now x = {}".format(x, func2(), x))
