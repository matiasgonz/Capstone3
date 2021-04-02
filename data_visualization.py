from import_files import *
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
sns.set_context("talk")
sns.set(rc={'figure.figsize':(11.7,8.27)})

# def make_visualizations():
dataframe = import_csv(2007,2017,True)

# #show all columns and show shape
# print(dataframe.info())
# print(dataframe.shape)

#masks
corr = dataframe.corr()
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

figs, axs = plt.subplots()

##corrlation matrix
#cmap = sns.diverging_palette(220, 10, as_cmap=True)
# axs = sns.heatmap(corr, mask=mask, cmap=cmap, center =0, square=True, linewidths=.5, cbar_kws={'shrink':.5})

#scatterplot
axs = sns.scatterplot(x=dataframe['air_temperature'].values, y=dataframe['wave_height'].values)
plt.title("Air_temperature vs, waev_height")
plt.xlabel("air_temperature")
plt.ylabel("wave_height")


#distribution plot
# axs = sns.distplot(dataframe['wave_height'])
# axs.set_xlim(1,10)

#sow and save visualizations
plt.savefig('Visualizations/scatter_tempvsheight.png')
plt.show()

    # return()