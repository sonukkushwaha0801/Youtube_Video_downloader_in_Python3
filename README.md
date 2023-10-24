# Youtube_Video_downloader_in_Python3
#### Downloading a Video using the Pytube Library:
<ol>
  <li>📥 First, import the Pytube library:</li>
  `import pytube`
  <li>🌐 Ask the user to input the URL of the video they want to download:</li>
  `Downloading_URL = input("Enter the URL of the video you want to download: ") `
  <li>📽️ Create a Pytube YouTube object for the provided URL:</li>
  `youtube = pytube.YouTube(Downloading_URL)`
  <li>📺 Get the stream with the highest resolution available for the video:</li>
  ` stream = youtube.streams.get_highest_resolution()`
  <li>📥 Display a message to indicate that the download is starting:</li>
   `print("Start Downloading")`
  <li>📥🔽 Download the video using the selected stream:</li>
  `stream.download()`
  <li>🎉 Display a message to confirm that the video has been downloaded:</li>
  `print("Video downloaded")`
</ol>
This code will prompt the user for a video URL, download the video with the highest resolution available, and inform the user when the download is complete.
