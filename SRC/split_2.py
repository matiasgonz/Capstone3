import numpy as np
import pandas as pd
from import_files import *
from sklearn.model_selection import TimeSeriesSplit

def time_test_split(wind):

    if wind = True:
        dataframe = pd.read_csv('../Data/wind.csv')

        X = dataframe.drop(columns=['wave_height','swell_height'], axis=1)
        Y = dataframe.drop(columns=['latitude','longitude','wind_direction_indicator',
        'wind_direction_true','wind_speed_indicator','wind_speed','present_weather','past_weather',
        'sea_level_pressure','amt_pressure_tend','air_temperature','sea_surface_temp',
        'wave_period','swell_direction','swell_period','swell_height','timestamp'], axis=1)

        tscv = TimeSeriesSplit()


        TimeSeriesSplit(gap=0, max_train_size=None, n_splits=8465, test_size=None)
        for train_index, test_index in tscv.split(X):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

    else:
        dataframe = import_csv(2017, 2017, True)

        X = dataframe.drop(columns=['wave_height','swell_height'], axis=1)
        Y = dataframe.drop(columns=['latitude','longitude','wind_direction_indicator',
        'wind_direction_true','wind_speed_indicator','wind_speed','present_weather','past_weather',
        'sea_level_pressure','amt_pressure_tend','air_temperature','sea_surface_temp',
        'wave_period','swell_direction','swell_period','swell_height','timestamp'], axis=1)

        tscv = TimeSeriesSplit()


        TimeSeriesSplit(gap=0, max_train_size=None, n_splits=51492, test_size=None)
        for train_index, test_index in tscv.split(X):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

    return(X_train, X_test, y_train, y_test)




    

