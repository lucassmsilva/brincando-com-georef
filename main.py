from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from sklearn.neighbors import BallTree
import numpy as np
import json
import pandas as pd

path = 'points.geojson'


df = df = pd.read_csv(r'acidentes2020.csv',delimiter=';', skiprows=0, low_memory=False)

t = df.head()
t = t[['id', 'latitude', 'longitude']]
result = t.to_json(orient="records")
parsed = json.loads(result)
print(json.dumps(parsed, indent=4)  )


with open(path) as f:
    data = json.load(f)

all_points = []
for feature in data['features']:
    all_points.append(feature['geometry']['coordinates'])

earth_radius = 6371e3
bt = BallTree(np.deg2rad(all_points), metric='haversine')


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/", response_class=ORJSONResponse)
async def items(lat: float, lon: float, distance_desired: float = 2000.0):
    counter = bt.query_radius(np.deg2rad(np.c_[lat, lon]), r=distance_desired/earth_radius, count_only=True)
    distances, indices = bt.query(np.deg2rad(np.c_[lat, lon]), k=int(counter))
    meters = distances[0].tolist()
    indices = indices[0].tolist()
    meters = [m * earth_radius for m in meters]
    positions = [all_points[i] for i in indices]
    return {
        "distance": meters,
        "positions": positions,
    }


# pip install -U scikit-learn
# install pandas
# install fast api && uvicorn && ORJSONResponse
# execute
# $ python -m uvicorn main:app
# try
# http://127.0.0.1:8000/items/?lat=-56.0877799987793&lon=-15.620722349120022
