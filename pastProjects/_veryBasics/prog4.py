
for i in range(10, 25):
    print("Now i is " + str(i) + " and i(sq) = " + str(i * i))
print("And finally, the value of i is " + str(i))

c = "Aviral Srivastava"
if "avi" in c:
    print("Found the substring in the string...!!!")
else:
    print("Substring not found.")

print(c[3:13] + " , " + c[:10])

marks = [39, 31, 28, 27, 34]
sum_marks = 0
avg_marks = 0
for temp in marks:
    sum_marks += temp
avg_marks = sum_marks / 5
percentage = (sum_marks / 200) * 100
print("Total marks = " + str(sum_marks))
print("Average marks = " + str(avg_marks))
print("Percentage = " + str(percentage) + "%")
