import pytube

# Get the video URL from the user
🚀 Downloading_URL = input("🌟 Enter the URL of the video you want to download: ")

# Create a YouTube object
📺 youtube = pytube.YouTube(🚀 Downloading_URL)

# Get the highest resolution stream
🌈 stream = youtube.streams.get_highest_resolution()

# Let's get this party started!
print("🚀 Start Downloading")

# Download the video
🌊 stream.download()

# Hooray, your video is now on your device! 🎉📽️
print("🎬 Video downloaded")
