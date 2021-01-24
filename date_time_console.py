Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> datetime.datetime
<class 'datetime.datetime'>
>>> datetime.datetime.now()
datetime.datetime(2021, 1, 24, 11, 23, 56, 118792)
>>> datetime.datetime.now().date()
datetime.date(2021, 1, 24)
>>> datetime.datetime.now().time()
datetime.time(11, 24, 12, 869483)
>>> from datetime import datetime
>>> d = datetime.now().date()
>>> t = datetime.now().time()
>>> print(d)
2021-01-24
>>> print(t)
11:24:55.607798
>>> d.strftime('%d/%m/%y')
'24/01/21'
>>> d.strftime('%d/%m/%y, %a')
'24/01/21, Sun'
>>> d.strftime('%d/%m/%y, %A')
'24/01/21, Sunday'
>>> t.strftime('%H:%M:%S, %p')
'11:24:55, AM'
>>> import calendar
>>> print(calendar.month(2021,1))
    January 2021
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31

>>> import os
>>> import random
>>> os.listdir()
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python38.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll', 'vcruntime140_1.dll']
>>> os.getcwd()
'C:\\Python38'
>>> import glob
>>> glob.glob('*.mp3')
[]
>>> glob.glob('*.txt')
['LICENSE.txt', 'NEWS.txt']
>>> os.chdir('C:\Users\asus\Music')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.chdir('C:\\Users\\asus\\Music')
>>> os.chdir('C:/Users/asus/Music')
>>> os.chdir(r'C:\Users\asus\Music')
>>> os.listdir()
['01 Rock Tha Party - Rocky Handsome - 190Kbps.mp3', '5-Varlaam Varlaam Vaa-SenSongsMp3.Co.mp3', 'BIGGEST BASS DROP EVER! (EXTREME BASS TEST!!!).mp3', 'Billian-Billian-Guri.mp3', 'bye5.mp3', 'Cristiano Ronaldo - Faded Best Moments 2017 • 100.000 Subscribers.mp3', 'desktop.ini', 'Dub Theri Step with Lyrics   Theri   Vijay, Samantha, Amy Jackson   Atlee   G.V.Prakash Kumar.ogg', 'Ek Pal Ka Jeena-(Mr-Jatt.com).mp3', 'Kaththi Theme…The Sword of Destiny - Full Audio.ogg', 'music_1.ogg', 'Na Ja.mp3', 'open2.mp3', 'Shape of You.mp3', 'Street Fighter V Soundtrack - Main Menu.ogg', "Street Fighter V Soundtrack - Ryu's Theme.ogg", 'StreetFighter.mp3', 'time2.mp3', 'Vedalam - The Theri Theme Lyric   Ajith Kumar, Shruti Haasan   Anirudh.ogg', 'Voice And Sound Recorder']
>>> glob.glob('*.mp3')
['01 Rock Tha Party - Rocky Handsome - 190Kbps.mp3', '5-Varlaam Varlaam Vaa-SenSongsMp3.Co.mp3', 'BIGGEST BASS DROP EVER! (EXTREME BASS TEST!!!).mp3', 'Billian-Billian-Guri.mp3', 'bye5.mp3', 'Cristiano Ronaldo - Faded Best Moments 2017 • 100.000 Subscribers.mp3', 'Ek Pal Ka Jeena-(Mr-Jatt.com).mp3', 'Na Ja.mp3', 'open2.mp3', 'Shape of You.mp3', 'StreetFighter.mp3', 'time2.mp3']
>>> songs = glob.glob('*.mp3')
>>> random.choice(songs)
'5-Varlaam Varlaam Vaa-SenSongsMp3.Co.mp3'
>>> random.choice(songs)
'open2.mp3'
>>> random.choice(songs)
'BIGGEST BASS DROP EVER! (EXTREME BASS TEST!!!).mp3'
>>> random.choice(songs)
'time2.mp3'
>>> song = random.choice(songs)
>>> os.startfile
<built-in function startfile>
>>> os.startfile(song)
>>> song = random.choice(songs)
>>> os.startfile(song)
>>> song = random.choice(songs)
>>> os.startfile(song)
>>> import webbrowser
>>> webbrowser.open('facebook.com')
True
>>> 