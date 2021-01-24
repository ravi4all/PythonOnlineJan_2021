from datetime import datetime
import os, random, glob

helloIntent = ["hi", "hello", "hey", "hi there", "what's up"]
dateIntent = ["date", "today's date", "what's the date today", "please tell me date"]
timeIntent = ["time", "current time", "what's the time", "please tell me time"]

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg in helloIntent:
        print("What's up ?")
    elif msg in dateIntent:
        d = datetime.now().date()
        print(d.strftime('%d/%m/%y, %A'))
    elif msg in timeIntent:
        t = datetime.now().time()
        print(t.strftime('%H:%M:%S, %p'))
    elif msg == "play music":
        # 1. change directory
        os.chdir(r'C:\Users\asus\Music')
        # 2. get all mp3 files
        songs = glob.glob('*.mp3')
        songs.extend(glob.glob('*.wav'))
        songs.extend(glob.glob('*.ogg'))
        # 3. choose a random file
        song = random.choice(songs)
        # 4. startfile
        os.startfile(song)
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
