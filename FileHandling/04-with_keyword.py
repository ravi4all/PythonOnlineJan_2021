# file = open('file_3.txt', 'a')
# data = "\nthis is newly inserted data"
# file.write(data)
# file.close()

with open('file_2.txt', 'w') as file:
    # data = file.read()
    file.write("Hello world")
    # print(data)
