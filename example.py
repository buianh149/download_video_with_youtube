from pytube import YouTube
import os
import requests
import json

url = 'https://www.youtube.com/watch?v=Bh2lnFf-uFQ'
yt = YouTube(url)
print(yt.streams.filter(file_extension='mp4')
#yt.streams.filter(progressive=True).first().download() # 360p  
#yt.streams.filter(adaptive=True).first().download() # 1080p -full HD
#yt.streams.filter(only_audio=True).first().download() # mp4
#yt.streams.filter(file_extension='mp4').first().download() # 360p

"""
videos = []
video_adaps = []
audios = []
for i in yt.streams.filter(progressive=True): 
    videos.append([i.itag, i.resolution])
    print(videos)
    print("--------------------------------")

for i in yt.streams.filter(adaptive=True, only_video=True): 
    video_adaps.append([i.itag, i.resolution])
    print(video_adaps)
    print("--------------------------------")

for i in yt.streams.filter(adaptive=True, only_audio=True): 
    audios.append([i.itag, i.audio_codec])
    print(audios)
    print("--------------------------------")
"""