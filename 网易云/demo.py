from urllib.request import urlretrieve

song_url = 'http://music.163.com/song/media/outer/url?id=1311782175'
path = 'D:\桌面\python-公开课\网易云\music\demo.mp3'

urlretrieve(song_url, path)