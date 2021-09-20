# program 1
# import tkinter as tk
# def main ():
#     root = tk.Tk()
#     root.title("Welcome Page Interface")
#     root.minsize(width = 500, height = 400)
#     root.maxsize(width = 700, height = 500)

#     button2 = tk.Label(root, text = "Welcome", width = 150, height = 10, relief=tk.RAISED)
#     button2.pack(padx = 1, pady = 10 )

#     username_frame = tk.Frame(root)
#     label = tk.Label(username_frame, text="Username")
#     label.pack(side=tk.LEFT)
#     button3 = tk.Entry(username_frame, width = 20)
#     button3.pack(side=tk.LEFT)
#     username_frame.pack(padx = 10, pady = 50 )

#     button4 = tk.Entry(root, width = 30)
#     button4.pack(padx = 10, pady = 20 )

#     button5 = tk.Button(root, text = "Continue to the next page", width = 30, height = 1)
#     button5.pack(padx = 10, pady= 20 )

#     root.mainloop()

# if __name__ == "__main__":
#     main()

# program 2
# import tkinter as tk
# r = tk.Tk()
# r.title('Welcome Page')
# w = tk.Label(r, text='This is my GUI')
# button1 = tk.Button(r, text='Hello World', width=25)
# button2 = tk.Button(r, text='Exit', width=25, command=r.destroy)
# w.pack()
# button1.pack()
# button2.pack()
# r.mainloop()

# program 3
# cursor property is used to change mouse cursor over a element. 
# from tkinter import *
# import tkinter
# top = Tk()
# B1 = Button(top, text="circle", relief=RAISED, cursor="circle")
# B2 = Button(top, text="plus", relief=RAISED, cursor="plus")
# B1.pack()
# B2.pack()
# top.mainloop()

# program 4
# from tkinter import *
# def add_numbers():
#     res=int(e1.get())+int(e2.get())
#     label_text.set(res)
# window = Tk()
# label_text=StringVar();
# Label(window, text="Enter First Number:").grid(row=0, sticky=W)
# Label(window, text="Enter Second Number:").grid(row=1, sticky=W)
# Label(window, text="Result of Addition:").grid(row=3, sticky=W)
# result=Label(window, text="", textvariable=label_text).grid(row=3,column=1, sticky=W)
# e1 = Entry(window)
# e2 = Entry(window)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# b = Button(window, text="Calculate", command=add_numbers)
# b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
# mainloop()

# program 5
from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Welcome to TutorialsPoint")
window.geometry('400x400')
window.configure(background = "grey");
a = Label(window ,text = "First Name").grid(row = 0,column = 0)
b = Label(window ,text = "Last Name").grid(row = 1,column = 0)
c = Label(window ,text = "Email Id").grid(row = 2,column = 0)
d = Label(window ,text = "Contact Number").grid(row = 3,column = 0)
a1 = Entry(window).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
d1 = Entry(window).grid(row = 3,column = 1)
def clicked():
   res = "Welcome to " + txt.get()
   lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=4,column=0)
window.mainloop()