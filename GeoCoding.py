import pandas as pd
from geopy.geocoders import GoogleV3
from shapely.geometry import Point
import geopandas as gpd

# No longer works because I disabled the API KEY
geolocator = GoogleV3(api_key='AIzaSyA-_CNvbUWGSSsHT58oHi2X2p4dDOWhspE')

def geocode_address(address):
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

df = pd.read_csv("Subway In Kuala Lumpur.csv")
df['Latitude'] = None
df['Longitude'] = None

for index, row in df.iterrows():

    lat, lon = geocode_address(row['Address'])

    df.at[index, 'Latitude'] = lat
    df.at[index, 'Longitude'] = lon

else:
    df.to_csv(r'Subway In Kuala Lumpur.csv',index = False)