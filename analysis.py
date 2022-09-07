import pandas as pd
import numpy as np
import os

data = pd.read_csv('clean_data.csv')

#generates country data
def get_country_data(country, directory_name, data = ''):
    country_name = country.lower()
    options_to_check = [i for i in list(data['location']) if i[0].lower() == country_name[0]][0]
    path = os.getcwd()
    print(path)
    new_dir = os.path.join(path, directory_name)
    if not os.path.exists(directory_name):
        os.mkdir(new_dir)
    else:
        print('Directory Exists')
    if len(options_to_check) == 0:
        print('Error, you gave an invalid country name')
        print(options_to_check)
    else:
        country_data = data.loc[data['location'] == country]
        return country_data