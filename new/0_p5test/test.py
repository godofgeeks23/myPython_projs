# function to return number of steps required in tower of hanoi
def steps(n):
    if n == 1:
        return 1
    else:
        return 2 * steps(n-1) + 1
print(steps(3))
