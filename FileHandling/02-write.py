file = open('file_2.txt','w')
# data = "Hello world this is Python"
data = ["Hello, ", "hi, ", "hey, "]
# file.write(data)
file.writelines(data)
file.close()
