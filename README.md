# You-Tube-downloader


pytube is a Python library that allows you to interact with the YouTube API and download videos. 
It provides various methods to interact with the YouTube API, such as streams, filter, get_highest_resolution, etc.

In the code snippet I provided earlier, the YouTube() function takes a YouTube video URL as an argument,
and creates an object (yt) that represents the video. The streams attribute of this object returns an iterable of all the available streams for the video.

The first() method of the streams attribute returns the first stream in the iterable, 
which is the highest quality video available for the given YouTube video URL.

os is a python built-in library that allows you to perform various file operations such as creating, 
renaming, deleting files, and directories. In this example we use os.getcwd() to get the current working directory to save the downloaded video in that location.

The download() method of the video object downloads the video to the specified location.

By using filter() method, you can filter the streams by various attributes like resolution, file_extension, 
etc and then you can choose the stream that match your criteria and download that stream.

get_highest_resolution() function will return the highest resolution available for the video, as long as it is available in YouTube.
