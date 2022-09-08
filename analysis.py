from array import array
import pandas as pd
import numpy as np
import os
import sys
import logging

data = pd.read_csv('clean_data.csv')

#generates country data
def get_country_data(country:list, directory_name:str, data = ''):
    country_name = [i.capitalize() for i in country]
    print(country_name)
    path = os.getcwd()
    new_dir = os.path.join(path, directory_name)
    status = False
    if not os.path.exists(directory_name):
        os.mkdir(new_dir)
    else:
        print('Directory Exists, data will be saved in existing directory')
    
    for i in country_name:
        if i not in list(data['location']):
            print('Unable to find the specified location')
        else:
            status = True
            print('Found location')
    print(status)
    if not status:
        print('Error, you gave an invalid country name')
    else:
        for i in country_name:
            country_data = data.loc[data['location'] == i]
            try:
                country_data.to_csv(i.lower() + '_covid_data.csv')
                print('Data generated successsfully')
            except Exception as e:
                logging.error('Failed to generate data: '+ str(e))
            return country_data