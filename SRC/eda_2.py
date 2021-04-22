import pandas as pd
import os, sys
from import_files import *
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
sns.set_context("talk")
sns.set(rc={'figure.figsize':(11.7,8.27)})

def scatterplot(col1, col2, year1, year2, windspeed):

    if windspeed == False:
        dataframe = import_csv(year1, year2,True)
    else:
        dataframe = pd.read_csv('../Data/wind.csv')

    figs, axs = plt.subplots()

    axs = sns.scatterplot(x=dataframe[str(col1)], y=dataframe[str(col2)])
    plt.title(str(col1) + 'vs' + str(col2))
    plt.xlabel(str(col1))
    plt.ylabel(str(col2))

    plt.show()

    return()

def corr_matrix(year1, year2):

    dataframe = import_csv(year1, year2,True)
    
    corr = dataframe.corr()
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    figs, axs = plt.subplots()

    axs = sns.heatmap(corr, mask=mask, cmap=cmap, center =0, square=True, linewidths=.5, cbar_kws={'shrink':.5})

    plt.show()

    return()

def dist_plot(col, year1, year2):

    dataframe = import_csv(year1, year2, True)

    figs, axs = plt.subplots()

    axs = sns.histplot(dataframe[str(col)])

    plt.show()

    return()

if __name__ == "__main__":

    # dist_plot('wave_height', 2017, 2017)
    dataframe = import_csv(2017, 2017, True)

    print(dataframe.wave_height.value_counts())


    # scatterplot('wave_height', 'wind_speed_indicator', 2017, 2017, True)
    # scatterplot('wave_height', 'wind_speed', 2017, 2017, True)
    # scatterplot('wind_speed', 'wind_speed_indicator', 2017, 2017, True)

    # dataframe = pd.read_csv('../Data/wind.csv')
    # corr = dataframe.corr()
    # mask = np.zeros_like(corr, dtype=np.bool)
    # mask[np.triu_indices_from(mask)] = True

    # cmap = sns.diverging_palette(220, 10, as_cmap=True)

    # figs, axs = plt.subplots()

    # axs = sns.heatmap(corr, mask=mask, cmap=cmap, center =0, square=True, linewidths=.5, cbar_kws={'shrink':.5})

    # plt.show()

    # print(dataframe.count())

    # figs, axs = plt.subplots()

    # axs = sns.distplot(dataframe['wind_speed_indicator'])

    # axs = sns.scatterplot(x=dataframe['wind_speed'].values, y=dataframe['wave_height'].values)

    # plt.show()

    # dataframe = import_csv(2007,2017,True)

    # print('imported')

    # print(dataframe.info())

    # df = dataframe[dataframe.wind_speed_indicator == 4]

    # # dataframe.drop(dataframe[dataframe['wind_speed_indicator'] < 4].index, inplace = True)

    # print('dropped')

    # print(df.info())

    # df.to_csv('../Data/wind.csv', index = False)

    # print('exported')


    # figs, axs = plt.subplots()

    # axs = sns.scatterplot(x=dataframe['wind_speed'].values, y=dataframe['wave_height'].values)
    # plt.title('wind_speed' + 'vs' + 'wave_height')
    # plt.xlabel('wave_height')
    # plt.ylabel('wind_speed')

    # plt.show()

  


    


    