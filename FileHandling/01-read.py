file = open('file_1.txt','r')
# data = file.read()

# will read only 10 characters
# data = file.read(10)

# will read one line at a time
# data = file.readline()

# will read all the lines seprated by '\n' and return a list
# data = file.readlines()

file.seek(40)
data = file.read(10)
print(data)
file.close()
