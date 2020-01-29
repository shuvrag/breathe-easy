import streamlit as st
import pandas as pd
import numpy as np

from scipy.stats import beta
import matplotlib.pyplot as plt
import hvplot.pandas  # noqa: F401
import holoviews as hv

hv.extension("bokeh")

st.header("Beta Distribution Tutorial")


from datetime import datetime
from string import ascii_letters

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
import seaborn as sns

# Not used below
from scipy import stats
from scipy.stats import gaussian_kde
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression

#fname_to_run = st.sidebar.selectbox(
#    "Select an app", fnames, format_func=format_func
#)

path = 'data/combined_data_1hr_lags.csv'
df = pd.read_csv(path)

df.rename(columns = {"Unnamed: 0": "Date"}, inplace = True)
df = df.set_index('Date (LT)')
df.index = pd.to_datetime(df.index)
df.dropna(inplace = True)
df = pd.get_dummies(df, columns = ['Month', 'Hour', 'Day'], drop_first = True)

st.title('Breathe-Easy PM\u2082\u22C5\u2085 Forecast')

#input_city = st.sidebar.selectbox("What city are you in?", ["Kolkata"])
input_city = st.selectbox("What city are you in?", ["Kolkata"])

input_date = st.text_input('What is the date and time you are thinking of running?', '2019-11-21 07:00:00')

input_datetime = pd.to_datetime(input_date)
st.write(input_datetime)

st.write('The particulate matter and weather forecast in ',input_city,' for the next 48 hours is as follows:')

st.sidebar.markdown(
    """
# Control Panel
"""
)
alpha_slider = st.sidebar.slider(
    "Value of alpha parameter",
    min_value=0.1,
    max_value=100.0,
    step=1.0,
    value=2.0,
)


pkl_filename = 'finalised_model.sav'
with open(pkl_filename, 'rb') as file:
    loaded_model = pickle.load(file)
#prediction = pickle_model.predict

#input = np.delete(df.loc[input_datetime].values, [40,50,60,70,80,90])
#output=loaded_model.predict([input])
#st.write(output[0])

for i in range(48):
    st.write("Time: ",input_datetime + timedelta(hours=i), "Particulate Matter Forecast:",df.loc[input_datetime + timedelta(hours=i)].values[0])

#index = df.index.get_loc(input_datetime, method='nearest')

#pkl_filename = 'finalised_model.sav'
#with open(pkl_filename, 'rb') as file:
#    pickle_model = pickle.load(file)
#prediction = pickle_model.predict

#st.write(df.loc[input_datetime])
#st.write(df.loc[input_datetime].Month_Nov)
#st.write(df.loc[input_datetime].values)
#st.write(df.loc[input_datetime].values[0])
