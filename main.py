# For installing the pytube
# pip install -r Requirement

import pytube
Downloading_URL = input("Enter the URL of the video you want to download: ")
youtube = pytube.YouTube(Downloading_URL)
steam = youtube.streams.get_highest_resolution()
print("Start Downloading")
steam.download()
print("Video downloaded")
