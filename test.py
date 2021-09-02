import math
import json


path = 'points.geojson'

with open(path) as f:
    data = json.load(f)

all_points = []
for feature in data['features']:
    all_points.append(feature['geometry']['coordinates'])

p1 = [-117.80, 37.24]
p2 = [-118.12, 37.15]

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dx = x1 - x2
    dy = y1 - y2

    return math.sqrt(dx * dx + dy * dy)

def closest_point(all_points, new_point):
    best_point = None
    best_distance = None

    for current_point in all_points:
        current_distance = distance(new_point, current_point)
        # print(current_distance)

        if best_distance is None or current_distance < best_distance:
            best_distance = current_distance
            best_point = current_point

    return best_distance, best_point;

my_position = [-56.0877799987793, -15.620722349120022]
dist, point = closest_point(all_points, my_position)


position = all_points.index(point)
print(data['features'][position]['properties']['marker-color'], point, dist)

def haversine_distance(point1, point2):
    R = 6371e3
    x1, y1 = point1
    x2, y2 = point2
    phi_x1 = x1 * math.pi / 180.0
    phi_x2 = x2 * math.pi / 180.0 
    dx = (x2 - x1) * math.pi / 180.0
    dy = (y2 - y1) * math.pi / 180.0

    a = math.sin(dx/2) * math.sin(dx/2) + math.cos(phi_x1) * math.cos(phi_x2) * math.sin(dy/2) * math.sin(dy/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

p1 = [-56.05550765991211,-15.60352823309596]
p2 = [-56.11249923706055, -15.585505930191367]
print('Distância em metros  ' ,haversine_distance(p1, p2))


