import pandas as pd

data = pd.read_csv("weather_data.csv")
maximum_temperature = data["temp"].max()
print(maximum_temperature)