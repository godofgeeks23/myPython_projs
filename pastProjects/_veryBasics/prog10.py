# program to demonstrate some functions in python and ...
# ... the functioning of the loops in python (while and for)


def show_table(n):
    for i in range(1, 11):
        print("{} x {} = {}".format(n, i, n * i))


show_table(8)


def extract_sum(string):
    sum = 0
    for char in string:
        if char in "0123456789":
            sum += int(char)
    print(f"The sum of all numbers found in the entered string is = {sum}")


extract_sum("I am 18 years old and study in class 12th")


def print_fibonacci(n):
    print("The first {} fibonacci numbers are: ".format(n))
    first = 1
    second = 1
    print("1, 1", end="")
    for i in range(1, n - 1):
        third = first + second
        first = second
        second = third
        print(", " + str(third), end="")


print_fibonacci(12)
print()

counter = 0
while counter < 10:
    counter = counter + 1
print("At the end of the while loop, counter = {}".format(counter))

counter = 0
for counter in range(1, 10):
    pass
print("At the end of the for loop, counter = {}".format(counter))
