from pytube import YouTube
x = input("Enter Youtube Code to Download")
print('http://youtube.com/watch?v='+x)
yt = YouTube('http://youtube.com/watch?v='+x)
videos = yt.streams
for i in videos:
    print(i)

y = input("Enter itag To download Video from Streams")
videos = yt.streams.get_by_itag(int(y)).download('F://pyyoutube-download/')
print(videos)