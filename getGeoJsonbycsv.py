import json
import pandas as pd

path = 'points.geojson'


df = df = pd.read_csv(r'acidentes2020.csv',delimiter=';', skiprows=0, low_memory=False)

t = df.head()
t = t[['id', 'latitude', 'longitude']]

array = []
for row in df.iterrows():
    thisdict = {
      "type": "Feature",
      "properties": {
        "id": row[1].id,
      },
      "geometry": {
        "type": "Point",
        "coordinates": [ float(row[1].latitude.replace(',', '.')), float(row[1].longitude.replace(',', '.'))]
      }
    }

    array.append(thisdict);

import json

with open('acidentes2020.txt', 'w') as filehandle:
    json.dump(array, filehandle)

print('Finalizado')