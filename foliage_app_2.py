import streamlit as st
import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim
import pickle
from datetime import datetime
from datetime import date
import calendar
import rasterio

st.title('Foliage app')

user_input = st.text_input("Which location do you want to search? Enter a location like 'Burlington, Vermont'", "Burlington, VT")
geolocator = Nominatim(user_agent="my-application")
try:
    location = geolocator.geocode(user_input)
    #print(loc.raw)
    print('Coordinates: ', location.latitude, location.longitude)
    st.write("Found: ", location)
except:
    st.write("Couldn't find this location. Try a different town name?")
    location = geolocator.geocode('Burlington, Vermont')
x = location.longitude
y = location.latitude

user_input2 = st.text_input("For which year?", "2018")
st.write(user_input2)

#Map the input location
map_data = pd.DataFrame(columns=['lat', 'lon'])
map_data.loc[0] = [location.latitude, location.longitude]

#######################################################################
#load in and fit the model for that location, come up with a prediction:
def foliage_prediction(x, y, InYear):
    tmin = []
    ppt = []
    year = pd.to_datetime(InYear).year
    day_of_year = 365
    st.write('predicting for: ', x, y, 'in ', year)
    if calendar.isleap(year):
        days = 366
        Fdays = 29
    else:
        days = 365
        Fdays = 28

    #pull data for that location, that year
    with rasterio.open("/Users/elizabethspriggs/Insight/Foliage/Datasheets/stacked_PRISM/tmin_{}.bil".format(year)) as raster:
        for val in raster.sample([(x, y)], indexes = range(1,day_of_year+1)): tmin.append(val)

    #pull data for that location, that year
    with rasterio.open("/Users/elizabethspriggs/Insight/Foliage/Datasheets/stacked_PRISM/ppt_{}.bil".format(year)) as raster:
        for val in raster.sample([(x, y)], indexes = range(1,day_of_year+1)): ppt.append(val)

    #Get average minimum temperature of Jan-Feb
    start = date(year=year, month=1, day=1)
    end = date(year=year, month=2, day=Fdays)
    tmin_JF = tmin[0][start.timetuple().tm_yday:end.timetuple().tm_yday].mean()

    #Get avg minimum temperature for March-May
    start = date(year=year, month=3, day=1)
    end = date(year=year, month=5, day=31)
    tmin_MAM = tmin[0][start.timetuple().tm_yday:end.timetuple().tm_yday].mean()

    #Avg minimum temperature May-July
    start = date(year=year, month=5, day=1)
    end = date(year=year, month=7, day=31)
    tmin_MJJ = tmin[0][start.timetuple().tm_yday:end.timetuple().tm_yday].mean()

    #Avg minimum temperature August
    start = date(year=year, month=8, day=1)
    end = date(year=year, month=8, day=31)
    tmin_A = tmin[0][start.timetuple().tm_yday:end.timetuple().tm_yday].mean()

    #Days in August below 4 degrees C
    start = date(year=year, month=8, day=1)
    end = date(year=year, month=8, day=31)
    A_below4 = sum(tmin[0][start.timetuple().tm_yday:end.timetuple().tm_yday]<=4)

    #Amount of August rain
    start = date(year=year, month=8, day=1)
    end = date(year=year, month=8, day=31)
    ppt_A = ppt[0][start.timetuple().tm_yday:end.timetuple().tm_yday].sum()

    #Amount of July rain
    start = date(year=year, month=7, day=1)
    end = date(year=year, month=7, day=31)
    ppt_J = ppt[0][start.timetuple().tm_yday:end.timetuple().tm_yday].sum()

    #Amount of May-July rain
    start = date(year=year, month=5, day=1)
    end = date(year=year, month=7, day=31)
    ppt_MJJ = ppt[0][start.timetuple().tm_yday:end.timetuple().tm_yday].sum()

    #Amount of March-May rain
    start = date(year=year, month=3, day=1)
    end = date(year=year, month=5, day=31)
    ppt_MAM = ppt[0][start.timetuple().tm_yday:end.timetuple().tm_yday].sum()

    #Amount of Jan-Feb rain
    start = date(year=year, month=1, day=1)
    end = date(year=year, month=2, day=Fdays)
    ppt_JF = ppt[0][start.timetuple().tm_yday:end.timetuple().tm_yday].sum()


    return(tmin_JF,tmin_MAM,tmin_MJJ,tmin_A,A_below4,ppt_A,ppt_J,ppt_MJJ,ppt_MAM,ppt_JF)

#st.write(location.longitude, location.latitude, user_input2)

output = foliage_prediction(location.longitude, location.latitude, user_input2)

pkl_filename = '/Users/elizabethspriggs/Insight/Foliage/basic_linear_model.pkl'
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)
st.write('The best fall foliage should be around:')

prediction = pickle_model.predict(np.array(output).reshape(1,-1))[0]
month = pd.to_datetime(prediction, format = '%j').month
day = pd.to_datetime(prediction, format = '%j').day
st.write(calendar.month_name[month], day, user_input2)

#st.write(pickle_model.predict(np.array(output).reshape(1,-1)))
#
#
# ##################################################################
 # Adding code so we can have map default to the center of the data
midpoint = (np.average(map_data['lat']), np.average(map_data['lon']))
st.deck_gl_chart(
            viewport={
                'latitude': midpoint[0],
                'longitude':  midpoint[1],
                'zoom': 5
            },
            layers=[{
                'type': 'ScatterplotLayer',
                'data': map_data,
                'radiusScale': 1,
   'radiusMinPixels': 4,
                'getFillColor': [248, 24, 148],
            }]
        )
