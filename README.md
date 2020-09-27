# Breathe-Easy

PM 2.5 are microscopic pollutants (particulate matter with diameter less than 2.5 micrometres) which are a principle source of air pollution in developing countries.

This is a web-app https://breathe-easy.herokuapp.com to predict the PM 2.5 levels of Kolkata, India for the next 24 hours.

Data
----

I use hourly meteorological and air-pollution data obtained from AirNow and Wunderground.

Model
----

The model underlying the prediction is a random forest model. I also considered time series models (ARIMA) and Facebook Prophet before choosing this model.

Web-App and Deployment
----

The web-app was built using Plotly on Streamlit and deployed using Heroku.

Files
----

scraper_0.ipynb -- This is the web-scraper used to collect meteorological data.
analysis_1.ipynb -- This is the file which prepares the raw data as a dataframe for modelling.
analysis_2.ipynb -- This is the file which implements the random forest model.
analysis_3.ipynb -- This is the file which implements the ARIMA time series model.
breathe-easy.py -- This is the file which deploys the model.
