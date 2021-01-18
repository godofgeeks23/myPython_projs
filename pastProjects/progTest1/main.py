# this will open programs on the pc
import subprocess
# subprocess.call(['C:\Program Files\Mozilla Firefox\\firefox.exe'])
# note that 'subprocess.call()' pauses till the pgoram action is finished
# so to continue the script action, use 'subproces.Popen()' instead
subprocess.Popen(['C:\Program Files\Mozilla Firefox\\firefox.exe', '-new-tab'])
p = subprocess.Popen('notepad')
p.terminate()
# os.system("TASKKILL /F /IM firefox.exe")  # close a running process
