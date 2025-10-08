from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

def decompose_temperature(df):
	result = seasonal_decompose(df['Temperature'], model='additive', period=365)
	result.plot()
	plt.show()