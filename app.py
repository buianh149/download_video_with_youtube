
from flask import Flask
from pytube import YouTube
from flask import render_template
import requests
app = Flask(__name__)

@app.route("/", methods=["post"])
def select_on():
    
    url = 'https://www.youtube.com/watch?v=_tuIR5HVvI8'
    yt = YouTube(url)
    videos = []
    video_adaps = []
    audios = []
    for i in yt.streams.filter(progressive=True): 
        videos.append([i.itag, i.resolution])

    for i in yt.streams.filter(adaptive=True, only_video=True): 
        video_adaps.append([i.itag, i.resolution, i.mime_type])
 
    for i in yt.streams.filter(adaptive=True, only_audio=True): 
        audios.append([i.itag, i.audio_codec])
    
    # resolutions = requests.post('resolutions')
    return render_template('download.html', videos=videos, video_adaps=video_adaps, audios=audios)

if __name__ == '__main__': 
    app.run(debug=True)

    
