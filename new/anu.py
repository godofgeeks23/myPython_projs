# for random quick python questions that my love asks
def sol(m, n) :
    for k in range(m, n+1): 
        i = 1 << 31
        while(i > 0) :
            if((k & i) != 0) :
                print("1", end = "")
            else :
                print("0", end = "")
            i = i // 2
        print()
             
m = int(input())
n = int(input())
sol(m,n)
print()
