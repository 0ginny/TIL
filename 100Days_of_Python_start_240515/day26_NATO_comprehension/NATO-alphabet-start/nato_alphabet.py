import pandas as pd

#1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

nato_pd = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter : row.code for (i,row) in nato_pd.iterrows()}
# print(nato_dict)

#2. Create a list of the phonetic code words from a word that the user inputs.

def genernate_nato() :
    word = input("Enter a word : ").upper()
    try:
        nato_code = [nato_dict[alpha] for alpha in word]
    except KeyError :
        print('sorry, please input only alphabets')
        genernate_nato()
    else :
        print(nato_code)

genernate_nato()