
def find_max(array):
    max=0;
    vart=0
    for i in range(len(array)):
        if array[i]>max:
            max=array[i]
            vart=i
    return vart

matrix = [['a','b','c','d','e'],['f','g','h','i','j'], ['k','l','m','n','o'],['p','q','r','s','t'], ['u','v','w','x','y']]

def decrypt(cipher, a,b,c,d):
    output = ""
    for i in range(len(cipher)):
        if(matrix[a].count(cipher[i])>0):
            output +=matrix[b][matrix[a].index(cipher[i])]
        elif(matrix[b].count(cipher[i])>0):
            output += matrix[a][matrix[c].index(cipher[i])]
        elif(matrix[c].count(cipher[i])>0):
            output += matrix[d][matrix[c].index(cipher[i])]
        elif(matrix[d].count(cipher[i])>0):
            output += matrix[c][matrix[d].index(cipher[i])]
        else:
            output += cipher[i]
    return output

pairs = [[0,1,2,3],[0,1,2,4],[0,1,3,4],
[0,2,1,3],[0,2,1,4],[0,2,3,4],
[0,3,1,2],[0,3,1,4],[0,3,2,4],
[0,4,1,2],[0,4,1,3],[0,4,2,3],
[1,2,3,4],[1,3,2,4],[1,4,2,3]]

wordlist = ['this', 'is', 'a', 'of','the','an','was','where','how','then','there','their','hi','as','in']


def count_vowels(string):
    vowels = ['a','e','i','o','u']
    count = 0
    for i in range(len(string)):
        if string[i] in vowels:
            count += 1
    return count

t = int(input())
while t>0:
    cipher = input()
    array = [0]*len(pairs)
    for i in range(len(pairs)):
        output = decrypt(cipher,pairs[i][0],pairs[i][1],pairs[i][2],pairs[i][3])
        for word in wordlist:
            if word in output.split():
                array[i] += 1
    maxindex = find_max(array)
    print(count_vowels(decrypt(cipher,pairs[maxindex][0],pairs[maxindex][1],pairs[maxindex][2],pairs[maxindex][3])))
    t-=1