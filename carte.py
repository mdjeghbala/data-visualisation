import pandas as pd
import folium

pop_data = pd.read_csv('radars.csv', sep=',')
print(pop_data)
print(pop_data.describe())
