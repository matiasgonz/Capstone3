import pandas as pd
import os, sys
from import_files import *

def drop_data(year1, year2, cleaned):
    #import csv using import_files.py
    dataframe = import_csv(year1, year2, cleaned)
    
    dataframe.drop(columns=['year', 'month', 'day', 'hour', 'imma_version', 'attm_count', 
    'time_indicator', 'latlong_indicator', 'ship_course', 'ship_speed', 'country_code',
    'national_source_indicator', 'id_indicator', 'callsign', 'visibility_indicator','visibility',
    'characteristic_of_ppp','indicator_for_temp','wbt_indicator', 'wetbulb_temperature', 'dpt_indicator', 'dewpoint_temperature',
    'sst_measurement_method', 'total_cloud_amount','lower_cloud_amount','low_cloud_type',
    'cloud_height_indicator','cloud_height','middle_cloud_type','high_cloud_type',
    'box_system_indicator', 'ten_degree_box_number', 'one_degree_box_number','deck','source_id','platform_type',
    'dup_status','dup_check','track_check','pressure_bias','wave_period_indicator',
    'swell_period_indicator','second_country_code','adaptive_qc_flags','nightday_flag',
    'trimming_flags','ncdc_qc_flags','external','landlocked_flag','source_exclusion_flags',
    'unique_report_id','release_no_primary','release_no_secondary','release_no_tertiary',
    'release_status_indicator','intermediate_reject_flag', 'wave_direction'], axis=1, inplace=True)

    df = dataframe.dropna()

    print(df.info())
    percent_missing = df.isnull().sum() * 100 / len(df)
    print(percent_missing)

    df.to_csv('../Data/' + str(year1) + '_new.csv', index = False)


if __name__ == "__main__":

    count = 2009

    while count <= 2017:
        drop_data(count, count, False)
        count += 1
    