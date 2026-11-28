import pandas as pd

data = pd.read_csv("weather_data.csv")
monday_temperature = data.loc[data["day"] == "Monday", "temp"].iloc[0]
monday_temperature_fahrenheit = monday_temperature * 9 / 5 + 32
print(monday_temperature_fahrenheit)