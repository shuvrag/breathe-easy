import streamlit as st
import pandas as pd
import numpy as np

from datetime import datetime
from string import ascii_letters

# Removing width limit
#pd.options.display.max_columns = None
import numpy as np
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
#%matplotlib inline

import pickle
from datetime import datetime
#from datetime import date
import calendar
from datetime import timedelta
#import seaborn as sns

# Not used below
#from scipy import stats
#from scipy.stats import gaussian_kde
#from sklearn import preprocessing
#from sklearn.model_selection import KFold
#from sklearn.linear_model import LinearRegression

#fname_to_run = st.sidebar.selectbox(
#    "Select an app", fnames, format_func=format_func
#)

st.title('Run-Air PM\u2082\u2085 Forecast')

input_city = st.selectbox("What city are you in?", ["Kolkata"])
#st.write(input_city)

#input_city = st.sidebar.selectbox("What city are you in?", ["Kolkata"])
#st.write(input_city)

input_date = st.text_input('What is the date and time you are thinking of running?', '2019-11-21 07:00:00')
#st.write(input_date)

path = '../pm_2.5_forecast/data/combined_data_1hr_lags.csv'
df = pd.read_csv(path)

#st.write(df.head())

pkl_filename = '../pm_2.5_forecast/finalised_model.sav'
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

input_datetime = pd.to_datetime(input_date)
st.write(input_datetime)

#df.index = pd.to_datetime(df.index)

#st.write(type(df.index))
#st.write(df.loc[input_datetime])

#for i in range(6):
    #st.write(i)
    #st.write(df.loc[input_datetime + timedelta(hours=i)].values[0])

#st.write(type(df.index))

#st.write(df.loc[input_datetime].values)

#index = df.index.get_loc(input_datetime, method='nearest')

#st.write(index)

#+ timedelta(hours=9)
#st.write(df.loc[input_datetime].values[0])

#st.write(df.head())

#prediction = pickle_model.predict

st.write('The particulate matter and weather forecast in ',input_city,' for the next 6 hours is as follows:')

for i in range(6):
    st.write("Time: ",input_datetime + timedelta(hours=i), "Particulate Matter Forecast:")



#st.write('The actual particulate matter and weather forecast in ',input_city,' for the next 6 hours is as follows:')


