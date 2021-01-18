import vlc
import time
media = vlc.MediaPlayer("./song.mp3")
media.play()
time.sleep(5)
print("Playing Song...")
while media.is_playing():
	time.sleep(1)
media.stop()


# playlist = ['/path/to/song1.flac', '/path/to/song2.flac', 'path/to/song3.flac']

# for song in playlist:
#     player = vlc.MediaPlayer(song)
# 	player.play()
