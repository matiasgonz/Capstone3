from google.cloud import bigquery
import os 
from astropy.table import Table
import pandas as pd
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/matiasgonzalez/Documents/dsi/Capstones/capstone2/sound-octagon-308723-9cf2f4f29d00.json"

# def import_data()
client = bigquery.Client()
dataset_ref = client.dataset('noaa_icoads', project='bigquery-public-data')
data = client.get_dataset(dataset_ref)

# icoads_core_2001_2004 = client.get_table(data.table('icoads_core_2001_2004'))
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

# # print(type(icoads_core_2017))
# df_icoads_core_2017 = icoads_core_2017.to_dataframe()

# print(type(icoads_core_2017))
# print(type(df_icoads_core_2017))

QUERY = """
        SELECT *
        FROM `bigquery-public-data.noaa_icoads.icoads_core_2017`
        """

df = client.query(QUERY).to_dataframe()

print(type(df))