a = "Hi I am Aviral and learning python programming language for past 1 week."
b = " And in my journey of learning it, I have to say that I have and enjoyed "
c = "too much working in this beautiful language."
d = " Moreover, what adds to my delight is the combination of sublime text 3 "
e = "with python and having the beautiful Boxy Monokai theme infront of my "
f = "eyes. The ability of sublime which allows embedding of the python console"
g = " and the command line into itself through the sublime_repo is absolutley "
h = "amazing. The above tools mentioned help to increase my productivity in "
i = "python, and keep me involved in the joy of coding. And the last and the "
j = "most, the Anaconda IDE for python with its real time debugging and "
k = "autocompletion feature makes the work too easy and blazing fast."
m = " In short, coding python, in sublime text 3 feels like heaven..."
n = "Therefore, may God bless the developers of python and sublime text, plus"
o = " all the developers I have unknowningly missed."

p = a + b + c + d + e + f + g + h + i + j + k + m + n + o

print(p)
max_char = 'a'
max_count = 0

print("Paragraph contains: ", end=' ')
for q in "abcdefghijklmnopqrstuvwxyz":
    print("{} {}'s, ".format(p.count(q), q), end=' ')
    if max_count < p.count(q):
        max_count = p.count(q)
        max_char = q
print()
print(f"'{max_char}' occurs max number of times({max_count}) above.")
