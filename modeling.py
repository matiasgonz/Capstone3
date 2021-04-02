from import_files import *
#from train_test_split import *
from keras.models import Sequential
from keras.layers import Dense, BatchNormalization, Dropout
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from keras.optimizers import SGD
import numpy as np


def normalized(df):
    normalized_df = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        normalized_df[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return (normalized_df)

def create_model():

    model = Sequential()
    drop_rate = .1
    
    model.add(Dense(32, kernel_initializer='normal', activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(drop_rate))

    model.add(Dense(256, kernel_initializer='normal', activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(drop_rate))

    model.add(Dense(64, kernel_initializer='normal',activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(drop_rate))

    model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
    
    model.compile(loss='mean_squared_error', optimizer='adam')

    return(model)

if __name__ == '__main__':

    dataframe = import_csv(2007,2008,True)

    dataframe_time = dataframe[['wind_direction_true', 'amt_pressure_tend', 'air_temperature', 'sea_level_pressure', 'wave_height']].copy()

    normalized_df = normalized(dataframe_time)

    X = normalized_df[['wind_direction_true', 'amt_pressure_tend', 'air_temperature', 'sea_level_pressure']].copy()
    y = normalized_df[['wave_height']].copy()   

    seed = 3
    np.random.seed(seed)
    est = KerasRegressor(build_fn=create_model, epochs=30, batch_size=500, verbose=0)

    kfold = KFold(n_splits=3, random_state=seed)
    value = cross_val_score(est, X, y, cv=kfold)

    print('mean squared error: %.5f (%.5f) MSE' % (value.mean(), value.std()))


