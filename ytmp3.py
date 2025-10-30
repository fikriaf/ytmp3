# importing packages
import os, sys, time
from threading import Thread
import yt_dlp
from pytube import YouTube


def show_loading():
    while loading_flag:
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.2)
        sys.stdout.write("\b\b\b   \b\b\b")
        sys.stdout.flush()
        time.sleep(0.5)


destination = r"C:\Users\Fikri\Music"
while True:
    # url input from user
    url = str(input("\nMasukkan Link Youtube: \n>> "))
    yt = YouTube(url)

    loading_flag = True
    loading_thread = Thread(target=show_loading)
    loading_thread.start()
    try:
        print("[ Memulai Unduhan... ]")
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "C:\\Users\\Fikri\\Music\\%(title)s.mp3",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        loading_flag = False
        loading_thread.join()
        print("[Successfully Downloaded]")
    except Exception as e:
        print("[Upgrade Library YT-DLP]")
        os.system("pip uninstall yt_dlp")
        os.system("pip install yt_dlp")
        print("[ Mengulang Unduhan... ]")
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "C:\\Users\\Fikri\\Music\\%(title)s.mp3",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        loading_flag = False
        loading_thread.join()
        print("[Successfully Downloaded]")
