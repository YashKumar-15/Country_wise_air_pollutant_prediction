import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import warnings
warnings.filterwarnings('ignore')

# reading dataset
df = pd.read_csv('data.csv', sep=';')

#  filter required features from df
df2 = df[['Last Updated','Country Label','Value']]

# removing null values from Country Label
df3 = df2.dropna(subset='Country Label')

# rename column
df3.rename(columns={'Last Updated':'date_timestamp'},inplace=True)

# getting datetime in 'dd-mm-yyy' format
df3['date_timestamp'] = df3['date_timestamp'].astype(str)
df3['date_timestamp'] = pd.to_datetime(df3['date_timestamp'],errors='coerce')

df3['date'] = df3['date_timestamp'].apply(lambda x: x.strftime('%d-%m-%Y'))
# df3['year'] = df3['date_timestamp'].apply(lambda x: x.strftime('%Y'))
df3.drop(columns=['date_timestamp'],inplace=True)

# sort values according to date
df3 = df3.sort_values(by='date', ascending=True)

# exporting pre_processed data
df3.to_csv('filtered_data.csv', index=False)