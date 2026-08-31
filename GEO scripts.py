#### Polygon tests

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


#### GPS examples

# https://docs.microsoft.com/en-us/azure/azure-maps/how-to-search-for-address

import geopy.distance

coords_1 = (52.2296756, 21.0122287)
coords_2 = (52.406374, 16.9251681)

geopy.distance.distance(coords_1, coords_2).km

# calc distance
def get_coordinates(lat_1, lon_1, coordinates_2):
    coords_1 = (lat_1, lon_1)
    coords_2 = coordinates_2

    return geopy.distance.distance(coords_1, coords_2).km

# check
coords_1 = (52.2296756, 21.0122287)
coords_2 = (52.406374, 16.9251681)
get_coordinates(coords_1[0], coords_1[1], coords_2)

help(geopy.distance.distance)


######## nearest store
%pip install geopy

import pandas as pd
import geopy.distance

dim_df_pandas = dim_df[['location_code', 'latitude', 'longitude', 'geo_country_iso_code']].toPandas()

def get_distance(lat1, lon1, lat2, lon2):
    try:
        coords_1 = (lat1, lon1)
        coords_2 = (lat2, lon2)
        return geopy.distance.geodesic(coords_1, coords_2).km
    except:
        pass#print('error')

get_distance(55.570278000, 13.058056000, 55.607795282231486, 13.003181411432589)
#test
dim_df_pandas['distance'] = dim_df_pandas.apply(lambda x: get_distance(55.570278000, 13.058056000, x['latitude'], x['longitude']), axis=1)
dim_df_pandas.sort_values('distance')

def get_nearest_store(store_country, store_code, store_latitude, store_longitude):
    try:
        dim_df_pandas['distance'] = dim_df_pandas.apply(lambda x: get_distance(store_latitude, store_longitude, x['latitude'], x['longitude']), axis=1)
        output = dim_df_pandas[dim_df_pandas['location_code'] != store_code].sort_values('distance')

        output_location_code = output.iloc[0]['location_code']
        output_distance = output.iloc[0]['distance']

        return output_distance#, output_location_code
    except:
        pass#print('error')

#test
get_nearest_store('SE', 'SE0326', 55.570278000, 13.058056000)
dim_df_pandas['nearest_store_distance'] = dim_df_pandas.apply(lambda x: get_nearest_store(x['geo_country_iso_code'], x['location_code'], x['latitude'], x['longitude']), axis=1)
dim_df_pandas


#####

def get_distance(lat1, lon1, lat2, lon2):
    try:
        coords_1 = (lat1, lon1)
        coords_2 = (lat2, lon2)
        return geopy.distance.geodesic(coords_1, coords_2).km
    except:
        pass
    #print(coords_1)
    #print(geopy.distance.geodesic(coords_1, coords_2).km)

get_distance(55.570278000, 13.058056000, 55.607795282231486, 13.003181411432589)



