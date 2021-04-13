import os
from pytube import YouTube
from collections.abc import Mapping, Sequence
from typing import Callable, List, Optional, Union

from pytube import Caption, Stream
from pytube.helpers import deprecated

url = 'https://www.youtube.com/watch?v=g_vABx1-wWY'
yt = YouTube(url)
#yt.streams.filter(progressive=True).first().download() # 360p  or 720p
#yt.streams.filter(adaptive=True).first().download() # 1080p -full HD
#yt.streams.filter(only_audio=True).first().download() # mp4
#yt.streams.filter(file_extension='mp4').first().download() # 360p
# print(yt.streams.filter(progressive=True, subtype="mp4"))  

def select_download(a, select):

    resolutions = []

    for i in yt.streams.filter(progressive=True): 
        resolutions.append([i.itag, i.resolution, 'Video'])

    for i in yt.streams.filter(adaptive=True, only_video=True): 
        resolutions.append([i.itag, i.resolution, 'Video_Adaptive'])

    for i in yt.streams.filter(adaptive=True, only_audio=True): 
        resolutions.append([i.itag, i.resolution, 'Audio'])

    print(resolutions) 
    
    """
    url = ''
    if len(url) > 1:
        if a == resolutions[0]:
            select = yt.streams.filter(only_audio=True).first() # mp4
        elif a == resolutions[1]:
            select = yt.streams.filter(progressive=True).first() # 360p 
        elif a == resolutions[2]:
            select = yt.streams.filter(adaptive=True).first() # 1080p -full HD
    else:
        print('hay nhap url truoc khi tim kiem.')

    select.download()    
    print('download completed!')
    """