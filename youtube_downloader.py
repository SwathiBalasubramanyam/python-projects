from pytube import YouTube

SAVE_PATH = "/home/swathi/Downloads/youtube_downloads"

link = "https://youtube.com/shorts/akL53YfPTfI?si=ju1ohfkBdFSInLNj"

try:
    yt = YouTube(link)
except:
    print("Connection Error")

mp4_streams = yt.streams.filter(file_extension='mp4').all()

d_video = mp4_streams[-1]

try:
    d_video.download(output_path=SAVE_PATH)
    print('Video downloaded successfully!')
except:
    print("Some Error!")