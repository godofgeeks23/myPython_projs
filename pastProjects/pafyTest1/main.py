import pafy
import vlc
import time
url = "https://www.youtube.com/watch?v=AO4Ak90fEzk"
video = pafy.new(url)
best = video.getbest()
print(best)
media = vlc.MediaPlayer(best.url)
time.sleep(5)
media.play()
print("Playing Video...")
while media.is_playing():
	time.sleep(1)
media.stop()
