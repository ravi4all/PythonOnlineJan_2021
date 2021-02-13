try:
    file = open('file_1.txt', 'w')
    file.write("Hello world")
    data = file.read()
    print(data)

except BaseException as ex:
    print(ex)

finally:
    print("I will always execute")
    file.close()