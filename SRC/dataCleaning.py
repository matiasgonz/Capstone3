import pandas as pd
import os, sys
from import_files import *

#import csv using import_files.py
dataframe = import_csv(2007,2007)

#drop columns
dataframe.drop(columns=['year', 'month', 'day', 'hour', 'imma_version', 'attm_count', 
'time_indicator', 'latlong_indicator', 'ship_course', 'ship_speed', 'country_code',
'national_source_indicator', 'id_indicator', 'callsign', 'visibility_indicator','visibility',
'characteristic_of_ppp','indicator_for_temp', 'wind_direction_indicator', 'wind_speed_indicator',
'wind_speed', 'present_weather', 'past_weather', 'sea_surface_temp', 'wave_direction',
'wave_period', 'swell_direction', 'swell_period', 'swell_height', 
'wbt_indicator', 'wetbulb_temperature', 'dpt_indicator', 'dewpoint_temperature',
'sst_measurement_method', 'total_cloud_amount','lower_cloud_amount','low_cloud_type',
'cloud_height_indicator','cloud_height','middle_cloud_type','high_cloud_type',
'box_system_indicator', 'ten_degree_box_number', 'one_degree_box_number','deck','source_id','platform_type',
'dup_status','dup_check','track_check','pressure_bias','wave_period_indicator',
'swell_period_indicator','second_country_code','adaptive_qc_flags','nightday_flag',
'trimming_flags','ncdc_qc_flags','external','landlocked_flag','source_exclusion_flags',
'unique_report_id','release_no_primary','release_no_secondary','release_no_tertiary',
 'release_status_indicator','intermediate_reject_flag'], axis=1, inplace=True)



#display all rows
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# # import singular csv for testing purposes
# dataframe = pd.read_csv('Data/2017_new.csv')

# # display nans in percentage
# percent_missing = dataframe.isnull().sum() * 100 / len(dataframe)
# print(percent_missing)

#drop nans
df = dataframe.dropna()
print(df.info())

# #export csv 
df.to_csv('Data/2007_new.csv', index = False)