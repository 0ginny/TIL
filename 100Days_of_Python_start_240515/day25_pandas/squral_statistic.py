import pandas as pd

# data loading
data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
pd.set_option('max_columns', None)
# print(data)
# Primary Fur Color ; [nan 'Gray' 'Cinnamon' 'Black']
# squirrel count
fur_colors = data['Primary Fur Color'].unique()
# print(fur_colors[0])
print(data['Primary Fur Color'][data['Primary Fur Color'] == 'Black'].count())
fur_count_dict = {
    'Fur Color' : [],
    'Count' : []
}
for color in fur_colors[1:]:
    fur_count_dict['Fur Color'].append(color)
    count = data['Primary Fur Color'][data['Primary Fur Color'] == color].count()
    fur_count_dict['Count'].append(count)
count_data = pd.DataFrame(fur_count_dict)
print(count_data)

count_data.to_csv('squirrel_count.csv',index=False)