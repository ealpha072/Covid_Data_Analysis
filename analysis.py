import pandas as pd
import numpy as np
import os
import sys
import logging

data = pd.read_csv('clean_data.csv')

#generates country data
def get_country_data(country, directory_name, data = ''):
    country_name = country.lower()
    path = os.getcwd()
    new_dir = os.path.join(path, directory_name)
    if not os.path.exists(directory_name):
        os.mkdir(new_dir)
    else:
        print('Directory Exists, data will be saved in existing directory')
        
    options_to_check = [i for i in list(data['location']) if i[0].lower() == country_name[0]][0]
    
    if len(options_to_check) == 0:
        print('Error, you gave an invalid country name')
        print(options_to_check)
    else:
        country_data = data.loc[data['location'] == country]
        try:
            #
            country_data.to_csv(new_dir + country_name + 'covid_data.csv')
            print('Data generated successsfully')
        except Exception as e:
            logging.error('Failed to generate data: '+ str(e))
        return country_data