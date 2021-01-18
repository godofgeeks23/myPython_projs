# get info about a youtube video and downlaod it
import pafy
url = "https://www.youtube.com/watch?v=IUyrlM1qkGU"
video = pafy.new(url)
print("Title: " + video.title)
print("Views: " + str(video.viewcount))
print("Likes vs Dislikes: " + str((video.likes / video.dislikes)))
print("Available Streams - ")
streams = video.streams
for s in streams:
    size = str(round(s.get_filesize() / 1048576, 3)) + "MB"
    print("Details: " + s.resolution + "," + s.extension + "," + size)
# streams[0].download(quiet=False)
