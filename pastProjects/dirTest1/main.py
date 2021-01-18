import os
path = os.getcwd()
print("The current working directory is " + path)
print(os.listdir('D:/Songs/'))  # list all files and folder in given path
print(os.path.isfile('./testfile.txt'))
print(os.path.isdir('./testfolder'))
print(os.path.exists('main.py'))
os.mkdir('./tf2')	  # create a folder
os.makedirs('./year/month/week')  # make dirs inside of dirs
os.rmdir('./tf1')  # delete an empty directory
os.remove('./testfile.txt')  # deletes a file
