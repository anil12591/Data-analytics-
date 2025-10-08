import pandas as pd
from Data_cleaning import clean_data
from Visualization import plot_temperature
from Decomposition import decompose_temperature

# Load dataset
df = pd.read_csv('Time series Analysis/daily_temperature.csv', parse_dates=['Date'])
df.set_index('Date', inplace=True)

# Clean data
df = clean_data(df)

# Visualize data
plot_temperature(df)

# Decompose time series
decompose_temperature(df)