# csv - comma seperated values
import csv

# data = [
#     {"name" : 'Tom', "dept" : 'IT'},
#     {"name" : 'John', "dept" : 'HR'},
#     {"name" : 'Shawn', "dept" : 'IT'},
#     {"name" : 'Harry', "dept" : 'HR'},
# ]
#
# with open('data.csv','w', newline='') as file:
#     writer = csv.writer(file)
#     for item in data:
#         writer.writerow(item.values())

with open('data.csv') as file:
    reader = csv.reader(file)
    for data in reader:
        print(data)
