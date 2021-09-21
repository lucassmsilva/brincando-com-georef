from sklearn.neighbors import BallTree
import numpy as np
import json

path = 'points.geojson'

with open(path) as f:
    data = json.load(f)

all_points = []
for feature in data['features']:
    all_points.append(feature['geometry']['coordinates'])

query_lats = [-56.0877799987793]
query_lons = [-15.620722349120022]
my_position = [-56.0877799987793, -15.620722349120022]

earth_radius = 6371e3
distance_desired = 2000

bt = BallTree(np.deg2rad(all_points), metric='haversine')
counter = bt.query_radius(np.deg2rad(np.c_[query_lats, query_lons]), r=distance_desired/earth_radius, count_only=True)
distances, indices = bt.query(np.deg2rad(np.c_[query_lats, query_lons]), k=int(counter))
meters = distances[0].tolist()
retorno = []

#  not work
# for i in range(len(indices)):
#     data['features'][indices[i]]['properties'] = ["distance", meters[i]]
#     retorno.append(data['features'][indices[i]])

print(data)

print(retorno)


# mapear pontos para GEOJSON format - usar isso aqui -> https://github.com/jazzband/geojson
# links uteis -> https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html