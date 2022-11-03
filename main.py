from moviepy.editor import VideoFileClip

from pytube import Playlist
def mp3():
    for i in range(len(mp4)):
        mp4_file = f'{mp4[i]}.mp4'
        mp3_file = f'{mp4[i]}.mp3'

        vc = VideoFileClip(mp4_file) 
        ac = vc.audio 
        ac.write_audiofile(mp3_file) 

    ac.close() #
    vc.close() 

mp4 = []
link = input("Wprowadź URL playlisty: ")
save = input("Gdzie  chcesz zapisać plik?(ścieszka do folderu) ")

yt_playlist = Playlist(link)

for video in yt_playlist.videos:
    video.streams.get_lowest_resolution().download()
    print("Video Downloaded: ", video.title)
    mp4.append(video.title)
    

print("All videos are downloaded.")
mp3()
