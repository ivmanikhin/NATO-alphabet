student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)
# print(student_data_frame)
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

alphabet = pd.read_csv('nato_phonetic_alphabet.csv')
dict_list = alphabet.to_dict('records')
nato_dict = {item['letter']: item['code'] for item in dict_list}
nato_dict = {item['letter']: item['code'] for item in alphabet.to_dict('records')}
print(nato_dict)
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

