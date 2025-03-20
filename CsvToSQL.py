import sqlite3
import pandas as pd

conn = sqlite3.connect('Subway_In_KL.db')
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS outlets')
c.execute('''CREATE TABLE outlets
                (name TEXT, address TEXT, operating_hours TEXT, waze_link TEXT, latitude REAL, longitude REAL)''')

df = pd.read_csv("Subway In Kuala Lumpur.csv")

for outlet in df.values:
    name, address, operating_hours, waze_link, latitude, longitude = outlet
    c.execute('INSERT INTO outlets (name, address, operating_hours, waze_link, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?)', 
                (name, address, operating_hours, waze_link, latitude, longitude))

conn.commit()
conn.close()