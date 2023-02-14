import pandas as pd
from scipy.stats import rankdata
import category_encoders as ce
from sklearn.preprocessing import MinMaxScaler
import awswrangler as wr
# get the parameters first
import sys
from awsglue.utils import getResolvedOptions
print("I am inside Glue now: ")
args = getResolvedOptions(sys.argv,
                          ['JOB_NAME',
                           's3_input_dataset'])
s3_input_dataset = args['s3_input_dataset']
print("The s3 input file is: " + s3_input_dataset)
# Let's first load the data into a Pandas dataframe so it is easy for us to work with it
wine_raw_df = wr.s3.read_csv(s3_input_dataset, sep=';',header=0)
# We can use a simple pandas imputation technique to replace the missing values in price to a mean value
wine_raw_df['price'] = wine_raw_df['price'].fillna(wine_raw_df['price'].mean())
# designation also has a lot of null values let us impute using mode
wine_raw_df['designation'] = wine_raw_df['designation'].fillna('Reserve')
wine_raw_df = wine_raw_df.drop(['province','region_1','region_2'],axis=1)
# drop the rows where country and points are null
wine_raw_df = wine_raw_df.dropna(axis=0, subset=['country'])
wine_raw_df = wine_raw_df.dropna(axis=0, subset=['points'])
# Frequency encoding for designation
# first get a list of value counts for each designation type
desg_val_counts = wine_raw_df['designation'].value_counts()
# how frequently does each value occur across the entire dataset
desg_freq = desg_val_counts/len(wine_raw_df)
# Finally let us use a ranking of these frequency encoded values to prevent issues with categories with similar frequencies
wine_raw_df['designation_freq'] = rankdata(wine_raw_df.designation.map(desg_freq))
# first get a list of value counts for each winery type
win_val_counts = wine_raw_df['winery'].value_counts()
# how frequently does each value occur across the entire dataset
win_freq = win_val_counts/len(wine_raw_df)
# Finally let us use a ranking of these frequency encoded values to prevent issues with categories with similar frequencies
wine_raw_df['winery_freq'] = rankdata(wine_raw_df.winery.map(win_freq))
# target encdoing
tar_enc = ce.TargetEncoder(wine_raw_df['variety'])
wine_raw_df['variety_transformed'] = tar_enc.fit_transform(wine_raw_df['variety'], wine_raw_df['price'])
# lets us move to a new dataframe and drop the categorical columns we transformed
wine_ready_df = wine_raw_df.drop(['designation','variety','winery'], axis=1)
# there are 48 unique countries we are going to see whole bunch of features now
one_enc = ce.OneHotEncoder(wine_ready_df['country'])
result = one_enc.fit_transform(wine_ready_df['country'])
wine_encod_df = pd.concat([wine_ready_df,result],axis=1)
# drop the country column
wine_encod_df.drop(['country'], axis=1, inplace=True)
# Define the min max scaler to scale features to values between 0 and 1
wine_features_scaler = MinMaxScaler()
wine_scaled_arr = wine_features_scaler.fit_transform(wine_encod_df)
# assign scaled results back to a dataframe and voila your feature engineering dataset is ready
wine_scaled_df = pd.DataFrame(data=wine_scaled_arr, columns=wine_encod_df.columns)
# write to CSV file in a S3 bucket
s3_glue_out = ''
temp = s3_input_dataset.split('/')[6]
s3_mod = s3_input_dataset.replace(temp,'')
if 'glue-in' in s3_mod:
    s3_glue_out = s3_mod.replace('glue-in','glue-out')
wr.s3.to_csv(wine_scaled_df, s3_glue_out+'wine_scaled.csv', header=True, index=False)