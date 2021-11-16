# youtube-dl

A simple Tkinter app used to convert Youtube videos (works with a lot of other websites as well) to *.mp3* or *.mp4* using the ```youtube-dl.exe``` and ```ffmpeg.exe``` libraries 

To use this app, you need to download the youtube-dl executable and place both the ```youtube-dl.exe``` and ```youtube_dl_GUI.py``` files in the same location (for Windows).
```ffmpeg``` or ```avconv``` is required to download the audio part of a video.
You need to install eyed3 (```pip install eyed3```) so that the program will be able to edit the ID3 metadata of the *.mp3 file it downloads.

```youtube-dl``` executable : https://youtube-dl.org/
```yt-dlp``` executable : https://github.com/yt-dlp/yt-dlp#installation
```ffmpeg``` binaries : https://ffmpeg.org/download.html

Edit : Replaced ```youtube-dl``` with ```yt-dlp```
