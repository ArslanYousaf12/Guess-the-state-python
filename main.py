# with open("./weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)


import csv

with open("weather_data.csv") as file_data:
    data = csv.reader(file_data)
    temp = []
    for row in data:
        if row[1] == "temp":
            continue
        print(row[1])
        temperature = int(row[1])
        temp.append(temperature)
        
print(temp)