# with open("./weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)


# import csv

# with open("weather_data.csv") as file_data:
#     data = csv.reader(file_data)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             # print(row[1])
#             temperature = int(row[1])
#             temp.append(temperature)
        
# print(temp)

import pandas

# data = pandas.read_csv("weather_data.csv")
# Data frames are like table in excel
# Series are like column
# print(type(data))
# print(data)
# # print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict) 
# temp_list = data["temp"].to_list()
# print(temp_list)
# average_temp = round( sum(temp_list) / len(temp_list))
# print(average_temp)
# total_temps = 0
# count = 0
# for temp in temp_list:
#     count = count + 1
#     total_temps = total_temps + temp

# print(total_temps)
# print(count)

# average_temp = int(total_temps / count)
# print(average_temp)

# average = data['temp'].mean()
# print(average)

# max = data["temp"].max()
# print(max)

# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# temp_degree = monday.temp
# temp_farh = temp_degree * 9/5 + 32
# print(temp_farh)

# data_dict = {
#     "students": ["Amy", "james", "Angela"],
#     "Scores": [76,56,65]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")


data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
temp_list = data.temp.to_list
average = data.temp.mean()
max_temp = data.temp.max()
monday = data[data.day == "Monday"]
temp_max = data[data.temp == data.temp.max()]

temp = monday.temp
print(temp)


student_dict = {
    "students": ["Arslan", "kamran", "Ali"],
    "Scores": [56,77,34],
}

data_frame = pandas.DataFrame(student_dict)
print(data_frame)
data_frame.to_csv("Abc.csv")
