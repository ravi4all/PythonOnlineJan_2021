import os

if os.path.exists('file_3.txt'):
    print("File already exist")
else:
    file = open('file_3.txt', 'x')
    data = "this is x mode"
    file.write(data)
    file.close()