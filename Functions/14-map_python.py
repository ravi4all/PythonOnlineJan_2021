def temp_convert(c):
    return 9/5 * c + 32

def hr_to_mins(hr):
    return hr * 60

def mins_to_sec(mins):
    return mins * 60

def min_to_hrs(mins):
    return mins / 60

temp = [30.44,35.55,30.23,28.77,24.5,32.4]
mins = [15,50,200,340,210]
hrs = [3.5, 2.8, 3, 5]

f = list(map(temp_convert, temp))
print(f)
m = list(map(min_to_hrs, mins))
print(m)





