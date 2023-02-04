from pytube import YouTube
import os

# URL of the video to download
url = "put here"

# Download the video
yt = YouTube(url)
video = yt.streams.first()
video.download(os.getcwd())

print("Video downloaded successfully!")
