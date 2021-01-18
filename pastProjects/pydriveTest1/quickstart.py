# My PyDrive Automated Bots to make the Drive Backup Task a breeze!
# VERSION 1: ONLY UPLOADS THE NEW FILE
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:  # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:  # Refresh them if expired
    gauth.Refresh()
else:  # Initialize the saved creds
    gauth.Authorize()

# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

filenamelist = ["MoviesDB.xlsx", "Passwords.kdbx"]
localfilelist = ["E:/Movies/MoviesDB.xlsx",
                 "C:/Users/Aviral/Documents/Passwords.kdbx"]
driveFolderlist = ["PC_Stuff", "Documents"]
for x in range(2):
    fileList = drive.ListFile(
        {'q': "'root' in parents and trashed=false"}).GetList()
    for file in fileList:
        if(file['title'] == driveFolderlist[x]):
            driveFolderID = file['id']
    print("Got Folder " + driveFolderlist[x] + "...")
    file1 = drive.CreateFile(
        {"title": filenamelist[x], 'parents': [{'id': driveFolderID}]})
    file1.SetContentFile(localfilelist[x])
    print("Uploading File " + filenamelist[x] + "...")
    file1.Upload()
    print("Done!")
