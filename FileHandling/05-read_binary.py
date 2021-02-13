with open('song.mp3', 'rb') as file:
    data = file.read()
    # print(data)

with open('song_2.mp3', 'wb') as file:
    file.write(data)
