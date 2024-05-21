# # with 으로 weather data 불러오기
# with open('weather_data.csv', mode='r') as weather:
#     data = weather.read()
#
# print(data)

# # 2. csv module 사용
# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in list(data)[1:]:
#         temperatures.append(int(row[1]))
#     print(temperatures)

# 3. pandas 사용 : https://pandas.pydata.org/docs/
import pandas as pd

data = pd.read_csv('weather_data.csv')
# data_dict = data.to_dict()
# print(data_dict)
temp_list = data['temp'].to_list()
print(temp_list)
temp_mean = data['temp'].mean()
# print(temp_mean)
temp_max = data['temp'].max()
# print(temp_max)
row_temp_max = data[data['temp'] == temp_max]
# print(row_temp_max)

monday = data[data['day'] == 'Monday']
mon_temp = int(monday.temp)
mon_f = mon_temp  * 9 / 5 + 32
print(mon_f)

# create dataframe
data_dict = {
    'student' :['Amy', 'John'],
    'score' :[80,90]
}
data = pd.DataFrame(data_dict)
print(data)
# to csv
data.to_csv('new_data.csv',index=False)