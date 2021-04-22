import pandas as pd
import os, sys

def import_csv(year1, year2,cleaned):

    csv_file_list = []
    year2 += 1

    if cleaned == False:
        for year_samp in range(year1, year2):
            count = 0
            print(year_samp)
            #print(count)
            while count+2 < len(os.listdir('../Data/' + str(year_samp))):
                if count < 10:
                    csv_file_list.append('../Data/' + str(year_samp) + '/' + str(year_samp) + '_00000000000' + str(count))
                    count += 1
                    #print(count)
                else:
                    csv_file_list.append('../Data/' + str(year_samp) + '/' + str(year_samp) + '_0000000000' + str(count))
                    count += 1
                    #print(count)

        list_of_dataframes = []

        for filename in csv_file_list:
            list_of_dataframes.append(pd.read_csv(filename))

        merged_df = pd.concat(list_of_dataframes)

    else:
        for year_samp in range(year1, year2):
            count = 0
            print(year_samp)
            #print(count)
            while count < (year2 - year1):
                csv_file_list.append('../Data/' + str(year_samp) + '_new' + '.csv')
                count += 1

        list_of_dataframes = []

        for filename in csv_file_list:
            list_of_dataframes.append(pd.read_csv(filename))

        merged_df = pd.concat(list_of_dataframes)

    return(merged_df)

  # drop all 0 hieght waves, drop al waves higher tahn 10, 