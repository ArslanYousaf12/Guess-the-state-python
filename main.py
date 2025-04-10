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

# import pandas

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

import pandas

data = pandas.read_csv("Squirrel_Data.csv")
# print(data["Primary Fur Color"])
gray_data = data[data["Primary Fur Color"] == "Gray"]
gray_row = gray_data["Primary Fur Color"].size

cinnamon_data = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_row = cinnamon_data["Primary Fur Color"].size

black_data = data[data["Primary Fur Color"] == "Black"]
print(black_data)
black_row = black_data["Primary Fur Color"].size


color_dict = {
  "Fur Color": ["grey", "red", "black"],
  "Count": [gray_row, cinnamon_row, black_row]
}

data_frame = pandas.DataFrame(color_dict)
data_frame.to_csv("squirrel_colors_data.csv")