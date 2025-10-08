
import pandas as pd

def clean_data(df):
	# Check for missing values
	print(df.isnull().sum())
	# Fill or drop missing values
	df['Temperature'] = df['Temperature'].fillna(method='ffill')
	return df