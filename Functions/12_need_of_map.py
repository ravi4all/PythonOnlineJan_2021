def temp_convert(c):
    return 9/5 * c + 32

def hr_to_mins(hr):
    return hr * 60

def mins_to_sec(mins):
    return mins * 60

def min_to_hrs(mins):
    return mins / 60

# f = temp_convert(30.55)
# print("Temperature is",f)

temp = [30.44,35.55,30.23,28.77,24.5,32.4]
f = []
for t in temp:
    f.append(temp_convert(t))

print(f)

mins = [15,50,200,340,210]
hrs = []
for m in mins:
    hrs.append(min_to_hrs(m))

print(hrs)
