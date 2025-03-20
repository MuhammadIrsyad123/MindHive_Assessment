import requests
import re
import json
from bs4 import BeautifulSoup
import pandas as pd

url = "https://subway.com.my/find-a-subway"

response = requests.get(url)
html_text =response.text
data = re.search(r'"markerData":(\[.*?\}\]),', html_text)
data = json.loads(data.group(1))

subway_header = ["Names","Address","Operating Hours","Waze Link"]
df = pd.DataFrame(columns = subway_header)

for d in data:

    soup = BeautifulSoup(d["infoBox"]["content"], "html.parser")
    address = soup.find_all('p')[0].text if soup.find_all('p') else 'N/A'

    if "Kuala Lumpur" in address:

        name = soup.h4.text if soup.h4 else 'N/A'
        operating_hour = soup.find_all('p')[1].text if len(soup.find_all('p')) > 1 else 'N/A'
        waze_link = soup.find_all('a')[2]['href'] if len(soup.find_all('a')) > 1 else 'N/A'

        row = [name,address,operating_hour,waze_link]
        length = len(df)
        df.loc[length] = row

else:
    df.to_csv(r'Subway In Kuala Lumpur.csv',index = False)

