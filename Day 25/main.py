import pandas as pd

data = pd.read_csv("weather_data.csv")
maximum_temperature_row = data[data["temp"] == data["temp"].max()]
print(maximum_temperature_row)