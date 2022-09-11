from array import array
import pandas as pd
import numpy as np
import os
import sys
import logging

data = pd.read_csv('clean_data.csv')

#generates country data
def get_country_data(country:list, directory_name:str, data = data):
    country_name = [i.capitalize() for i in country]
    path = os.getcwd()
    new_dir = os.path.join(path, directory_name)
    status = [False for i in range(0, len(country_name))]
    new_status = []
    
    if not os.path.exists(directory_name):
        os.mkdir(new_dir)
    else:
        print('Directory Exists, data will be saved in existing directory')
    
    for i in country_name:
        if i not in list(data['location']):
            print('Unable to find the specified location {}'.format(i))
        else:
            new_status.append(True)
            print('Found location')
    if len(new_status) == len(status):
        for i in country_name:
            country_data = data.loc[data['location'] == i]
            try:
                country_data.to_csv(os.path.join(new_dir,'{}_covid_data.csv'.format(i.lower())))
                print(i, 'Data generated successsfully')
            except Exception as e:
                logging.error('Failed to generate data: '+ str(e))
                
get_country_data(['Uganda, Kenya'], 'Country Data', data)