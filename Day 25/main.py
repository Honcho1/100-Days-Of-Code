import pandas as pd

data = pd.read_csv("weather_data.csv")
average_temperature = data["temp"].mean()
print(average_temperature)