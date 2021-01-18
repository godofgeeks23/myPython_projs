import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
s = "Hi There! I am Python"
speaker.Speak(s)
