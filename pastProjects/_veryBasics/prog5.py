# demonstrate string formatting in python 3 and 3.6+
# name = "Aviral Srivastava"
# age = 18

# print("Hello " + name + " your age is " + str(age) + ".")
# print("Hello {} your age is {}.".format(name, age))
# print(f"Hello {name} your age is {age}.")

name, age = input("Enter name and age seperated by a space: ").split()
print("You are " + name + " and are " + str(age) + " years old...")

print()
name, age = input("Enter name and age seperated by a comma: ").split(',')
print("You are " + name + " and are " + str(age) + " years old...")

a = 10
b = 89
c = a / b
print("Division of {} by {} gives result {} .".format(a, b, round(c, 5)))
