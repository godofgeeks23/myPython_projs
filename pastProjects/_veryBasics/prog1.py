# x = 10
# y = 20
# print("hi there! i am python!!!")
# print("the sum is: "+str(x+y))

# import turtle
# turtle.setup(900,500,100,100)
# turtle.fd(50)
# for i in range(10,20):
# 	turtle.fd(50)

from tkinter import *
root = Tk()
frame = Frame(root)
button1 = Button(frame, text="Aviral")
button2 = Button(frame, text="Python")
button3 = Button(frame, text="Click Me")
label1 = Label(frame, text="I am a Label")
button1.pack()
button2.pack()
button3.pack()
label1.pack()
frame.pack()
root.mainloop()

# testVar = input("does it work?")
# print("It works!!! "+testVar)

# a = 10
# b = 20
# name = "Aviral"
# surname = "Srivastava"
# print("Hello " + name + " " + surname)
# print()
# print("sum = " + str(a + b))
# print("dividing the numbers...Result = " + str(a / b))
# print(surname[:3])
