import pytube
from pytube import YouTube
import os
import pandas as pd

data = pd.read_csv('./main - Sheet1.csv',header = 0)
not_working = []
count = 0
for i, row in data.iterrows():
    q = row['Youtube']
    yt = YouTube(q)
    try :
        video = yt.streams.filter(only_audio=True).first()
    except pytube.exceptions.VideoUnavailable:
        not_working.append(q)
        print("video unavailable")
    else :
        out_file = video.download(output_path='./Audio')
        base, ext = os.path.splitext(out_file)
        new_file = base + '.wav'
        os.rename(out_file, new_file)
        count = count + 1
        print(q)
print(count)
