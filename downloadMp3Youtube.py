import yt_dlp

print('Insira a URL da música que você deseja baixar: ')
url = input()

# download the video as mp3 preferably with 128kbps


def baixarVideo(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '128',
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


baixarVideo(url)
