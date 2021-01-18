import shutil
import os
# shutil.rmtree('./files')  # deletes the folder with all its contents

original = r'./testfile.txt'
target = r'C:/Users/Aviral/Desktop/copiedfile.txt'
shutil.copyfile(original, target)  # copies file

original = r'./srcfolder'
target = r'C:/Users/Aviral/Desktop/testFolder'
shutil.copytree(original, target)  # copies folder

os.rename('./testfile.txt', './renamedfile.txt')  # rename file/folder

original = r'./renamedfile.txt'
target = r'C:/Users/Aviral/Desktop/movedfile.txt'
shutil.move(original, target)  # moves file and folders

os.replace("./testfile.txt", "C:/Users/Aviral/Desktop/testfile.txt")
