# Cardiovascular Disease Dataset

## import libraries

### data manipulation 
import pandas                   as pd

### other libraries
import warnings

## settings

### ignoring warnings
warnings.filterwarnings('ignore')

### pandas settings
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.max_columns', None)

## importing data 
data = pd.read_csv('../../data/raw/cardio_train.csv', sep = ';')

## preprocessing

# transforming `age` from days to years
data['age'] = data['age'] // 365

# ap_hi
data.drop(data[(data['ap_hi'] > data['ap_hi'].quantile(0.975)) | (data['ap_hi'] < data['ap_hi'].quantile(0.025))].index, inplace=True)

# ap_lo
data.drop(data[(data['ap_lo'] > data['ap_lo'].quantile(0.975)) | (data['ap_lo'] < data['ap_lo'].quantile(0.025))].index, inplace=True)

# height
data.drop(data[(data['height'] > data['height'].quantile(0.975)) | (data['height'] < data['height'].quantile(0.025))].index, inplace=True)

# weight
data.drop(data[(data['weight'] > data['weight'].quantile(0.975)) | (data['weight'] < data['weight'].quantile(0.025))].index, inplace=True)

# export to interim
data.to_csv('../../data/interim/cardio_interim.csv', index=False)
