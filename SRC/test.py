import pandas as pd
import os, sys
from import_files import *


df = import_csv(2007,2017,True)
print(df.info())
# from keras.models import Sequential
# from keras.layers import Dense, BatchNormalization, Dropout
# from keras.wrappers.scikit_learn import KerasRegressor
# from sklearn.model_selection import cross_val_score
# from sklearn.model_selection import KFold
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import Pipeline
# from keras.optimizers import SGD

# def get_file_paths(year1, year2):
#     year2 += 1
#     data =pd.DataFrame(pd.read_csv('Data/2017/2017_000000000000'))
#     for year_samp in range(year1, year2):
#         count = 0
#         print(year_samp)
#         print(count)
#         if count <= len(os.listdir('Data/' + str(year_samp))):
#             # if count == 0:
#             #     data = pd.read_csv('Data/' + str(year_samp) + '/' + str(year_samp) + '_00000000000' + str(count))
#             if count <= 10:
#                 data2 = pd.read_csv('Data/' + str(year_samp) + '/' + str(year_samp) + '_00000000000' + str(count))
#                 data.append(data2)
#                 count += 1
#             else:
#                 data3 = pd.read_csv('Data/' + str(year_samp) + '_0000000000' + str(count))
#                 data.append(data3)
#                 count += 1

#     return(data.year.unique())

# print(get_file_paths(2007,2017))

#csv_file_list = ["Data/2007/2007_000000000000", "Data/2013/2013_000000000000", "Data/2017/2017_000000000000"]

# csv_file_list = []
# year1 = 2007
# year2 =2008
# year2 += 1
# for year_samp in range(year1, year2):
#     count = 0
#     print(year_samp)
#     print(count)
#     while count+2 < len(os.listdir('Data/' + str(year_samp))):
#         if count < 10:
#             csv_file_list.append('Data/' + str(year_samp) + '/' + str(year_samp) + '_00000000000' + str(count))
#             count += 1
#             print(count)
#         else:
#             csv_file_list.append('Data/' + str(year_samp) + '/' + str(year_samp) + '_0000000000' + str(count))
#             count += 1
#             print(count)

# list_of_dataframes = []
# for filename in csv_file_list:
#     list_of_dataframes.append(pd.read_csv(filename))

# merged_df = pd.concat(list_of_dataframes)

# print(merged_df.year.unique())      


#def get_file_paths():
# files = {}

# for year in range(2007,2018):
#     for item in os.listdir('Data/' + str(year)):
#         if files[year]:
#             files[year] = append('Data/' + str(year) + '/' + str(item))
#         else:
#             files[year] = 'Data/' + str(year) + '/' + str(item)

# print(files)

    # return()

#def get_dataframes():
# for idx, item in files.items():
#     for paths in item:
#         df = pd.read_csv(paths)

# file_names = {}

# for files_count in range(0, 48):
#     if files_count < 10:
#         file_names[files_count] = 'Data/2007_0000000000' + '0' + str(files_count)
#         files_count += 1
#     else:
#         file_names[files_count] = 'Data/2007_0000000000' + str(files_count)
#         files_count += 1
        

# for idx, path in file_names.items():
#     if idx == 0:
#         df_2007 = pd.read_csv(path)
#     else:
#         df_2007 = pd.concat([pd.read_csv(path)])



# df_2017_1 = pd.read_csv('Data/2017_000000000003')

# df_2007 = pd.read_csv('Data/2007_000000000000')

# print (df_2017.info())
# print (df_2007.info())

# from google.cloud import bigquery
# import os 
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/matiasgonzalez/Documents/dsi/Capstones/capstone2/sound-octagon-308723-f96030db959c.json"

# client = bigquery.Client()
# dataset_ref = client.dataset('noaa_icoads', project='bigquery-public-data')
# data = client.get_dataset(dataset_ref)

#all tables present in dataset
#print([i.table_id for i in client.list_tables(data)])

#field names and data types
# icoads_core_2001 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2002 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2003 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2004 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2005 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2006 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2007 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2008 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2009 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2010 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2011 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2012 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2013 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2005 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2006 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2007 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2008 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2009 = client.get_table(data.table('icoads_core_2017'))
# icoads_core_2017 = client.get_table(data.table('icoads_core_2017'))

# list1 = [range(2005, 2017)]

# print([i.name+", type: "+i.field_type for i in icoads_core_2017.schema])
