import yt_dlp as yt

def download_videos(url):
    ydl_opts = {
        'format': 'best',
        'outtml':'Download Videos From Youtube/'+'%(title)s.%(ext)s',
    }

    with yt.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

url = 'https://www.youtube.com/watch?v=uWgFdwyYSWg'
download_videos(url)