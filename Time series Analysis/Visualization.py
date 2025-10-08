import matplotlib.pyplot as plt

def plot_temperature(df):
	plt.figure(figsize=(14, 6))
	plt.plot(df['Temperature'], label='Daily Temperature')
	plt.title('Daily Temperature Over Time')
	plt.xlabel('Date')
	plt.ylabel('Temperature (°C)')
	plt.legend()
	plt.grid(True)
	plt.show()