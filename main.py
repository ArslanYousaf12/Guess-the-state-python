# with open("./weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)


import csv

with open("weather_data.csv") as file_data:
    data = csv.reader(file_data)
    for row in data:
        print(row)