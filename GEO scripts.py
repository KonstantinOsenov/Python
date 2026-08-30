%pip install shapely

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np

lons_lats_vect = np.column_stack((lons_vect, lats_vect)) # Reshape coordinates
polygon = Polygon(lons_lats_vect) # create polygon

test_polygon_coord = [
    [ 17.950630602337089, 59.364384436796399 ],
    [ 17.950225253275526, 59.363855946117425 ],
    [ 17.951051729065806, 59.363459263179038 ],
    [ 17.952283554154082, 59.363591065995436 ],
    [ 17.952688923144546, 59.364119554034239 ],
    [ 17.95186244711817, 59.364516241896901 ],
    [ 17.950630602337089, 59.364384436796399 ]
]

polygon = Polygon(test_polygon_coord) # create polygon
polygon

point = Point(17.952306718800717, 59.36417301519245 ) # create point

print(polygon.contains(point)) # check if polygon contains point
print(point.within(polygon)) # check if a point is in the polygon 
