start = 0
text = 'hello world, this is python'

count = text.count('o')

for i in range(count):
    index = text.index('o', start)
    start = index + 1
