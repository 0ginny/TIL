import pandas as pd
import random

students = ['Angela','John','Son']

data_dict = { name : random.randint(1,100)  for name in students}
print(data_dict)

data = pd.DataFrame({
    'student' : data_dict.keys(),
    'score' : data_dict.values()
})

for (idx, row) in data.iterrows():
    if row.student == 'Angela':
        print(row.score)

new_dict = { row.student : row.score for (idx,row) in data.iterrows()}
print(new_dict)