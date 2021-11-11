import pandas as pd

# Create a dictionary in this format:

dict_list = pd.read_csv('nato_phonetic_alphabet.csv').to_dict('split')['data']
print(dict_list)
nato_dict = {item[0]: item[1] for item in dict_list}
print(nato_dict)

# Create a list of the phonetic code words from a word that the user inputs.

user_name = list(input("What's your name?").upper())
print(user_name)
output = [nato_dict[letter] for letter in user_name]
print(output)