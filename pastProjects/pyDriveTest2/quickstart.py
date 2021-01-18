# # My PyDrive Automated Bots to make the Drive Backup Task a breeze!
# VERSION 2.0 - Now trash the existing file and then upload the new file
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()
gauth.SaveCredentialsFile("mycreds.txt")
drive = GoogleDrive(gauth)

filenamelist = ["MoviesDB.xlsx", "Passwords.kdbx"]
localfilelist = ["E:/Movies/MoviesDB.xlsx",
                 "C:/Users/Aviral/Documents/Passwords.kdbx"]
driveFolderlist = ["PC_Stuff", "Documents"]
for x in range(len(filenamelist)):
    fileList = drive.ListFile(
        {'q': "'root' in parents and trashed=false"}).GetList()
    for file in fileList:
        if(file['title'] == driveFolderlist[x]):
            driveFolderID = file['id']
            file_list = drive.ListFile(
                {'q': "'" + driveFolderID + "' in parents and trashed=False"}).GetList()
            for file1 in file_list:
                if file1['title'] == filenamelist[x]:
                    file1.Trash()
                    print("Trashed Old " + filenamelist[x] + ".")
    file1 = drive.CreateFile(
        {"title": filenamelist[x], 'parents': [{'id': driveFolderID}]})
    file1.SetContentFile(localfilelist[x])
    print("Uploading File " + filenamelist[x] + "...")
    file1.Upload()
    print("Done uploading " + filenamelist[x] + ".")
print("Task Completed Successfully!")
