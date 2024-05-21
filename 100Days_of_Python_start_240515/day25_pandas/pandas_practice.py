# # with 으로 weather data 불러오기
# with open('weather_data.csv', mode='r') as weather:
#     data = weather.read()
#
# print(data)

# 2. csv module 사용
import csv

with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in list(data)[1:]:
        temperatures.append(int(row[1]))
    print(temperatures)
