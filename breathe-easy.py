import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import timedelta
import plotly.graph_objects as go

timechoice = [' ', '00:00:00', '01:00:00', '02:00:00', '03:00:00',
        '04:00:00', '05:00:00', '06:00:00', '07:00:00',
'08:00:00', '09:00:00', '10:00:00', '11:00:00',
'12:00:00', '13:00:00', '14:00:00', '15:00:00',
'16:00:00', '17:00:00', '18:00:00', '19:00:00',
'20:00:00', '21:00:00', '22:00:00', '23:00:00']


t1 = '10:00:00'
t1 = pd.to_datetime(t1)
time=[]
time.append(t1)
for i in range(1,25):
    time.append(t1 + timedelta(hours=i))

#st.write(time)

#time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

time = ['10:00:00', '11:00:00',
'12:00:00', '13:00:00', '14:00:00', '15:00:00',
'16:00:00', '17:00:00', '18:00:00', '19:00:00',
'20:00:00', '21:00:00', '22:00:00', '23:00:00', 
'00:00:00', '01:00:00', '02:00:00', '03:00:00',
        '04:00:00', '05:00:00', '06:00:00', '07:00:00',
'08:00:00', '09:00:00']

#pm = [167, 191, 229, 249, 172, 171, 174, 105, 86, 67, 53, 56, 63, 61, 88, 139, 124, 98, 93, 111, 134, 97, 111, 101, 130]
pm = [166, 140, 113, 90, 87, 93, 90, 77, 76, 87, 116, 135, 144, 132, 105, 103, 143, 131, 154, 182, 184, 187, 157, 129, 118]

#st.header("Beta Distribution Tutorial")

st.title('Breathe-Easy PM\u2082\u22C5\u2085 Forecast')

#input_city = st.selectbox("What city are you in?", ["Kolkata"])

#input_date = st.text_input('What is the date and time you are thinking of going out?', '2020-01-11 15:00:00')

input_date = '2020-02-18 15:00:00'

input_date = pd.to_datetime(input_date)

#input_day = st.date_input('Choose the date when you want to go outside:', input_date)
input_day = st.date_input('Please choose the date when you want to go outside:')

#st.write(input_day)

#input_time = st.text_input('Choose the time when you want to go outside?', '10:00:00')
input_time = st.selectbox('Please choose the time when you want to go outside:', timechoice)

#in_date = pd.to_datetime(prediction, format = '%j')

#in_date = in_date.replace(year = 2020)

#input_datetime = pd.to_datetime(input_date)
#st.write(input_datetime)

input_date_time = str(input_day) + ' ' + input_time

#st.write('The particulate matter and weather forecast in Kolkata at', input_date_time, 'is:')

input_date_time = pd.to_datetime(input_date_time)

if input_time != ' ':
 
    st.write('The particulate matter forecast in Kolkata at', input_date_time, 'is:', pm[time.index(input_time)])

#    st.write('The particulate matter and weather forecast in Kolkata for the next 24 hours is as follows:')
#    st.write('The best particulate matter forecast in Kolkata is at:') 

    fig1 = go.Figure()

    # Add scatter trace for line
    fig1.add_trace(go.Scatter(
        x = time,
        y = pm,
        mode="lines",
        name="pollutant concentration",
hovertext=["Temp 82, Hmdty 82, PM2.5 166", "Temp 81, Hmdty 81, PM2.5 140", "Temp 79, Hmdty 79, PM2.5 113",
               "Temp 77, Hmdty 77, PM2.5 90", "Temp 73, Hmdty 73, PM2.5 87", "Temp 72, Hmdty 72, PM2.5 93",
               "Temp 70, Hmdty 70, PM2.5 90", "Temp 66, Hmdty 72, PM2.5 77", "Temp 64, Hmdty 70, PM2.5 76",
               "Temp 63, Hmdty 78, PM2.5 87", "Temp 63, Hmdty 83, PM2.5 116", "Temp 61, Hmdty 88, PM2.5 135",
               "Temp 61, Hmdty 82, PM2.5 144",
            "Temp 63, Hmdty 82, PM2.5 132", "Temp 68, Hmdty 88, PM2.5 105", "Temp 72, Hmdty 88, PM2.5 103",
               "Temp 77, Hmdty 82, PM2.5 143", "Temp 81, Hmdty 73, PM2.5 131", "Temp 82, Hmdty 64, PM2.5 154",
               "Temp 84, Hmdty 57, PM2.5 182", "Temp 84, Hmdty 51, PM2.5 184", "Temp 84, Hmdty 48, PM2.5 187",
               "Temp 82, Hmdty 42, PM2.5 157", "Temp 81, Hmdty 48, PM2.5 129", "Temp 77, Hmdty 42, PM2.5 118"
               ],

        hoverinfo="text",
        marker=dict(color="green"),
        showlegend=False
    ))

    fig1.update_layout(
        title="Pollution for the next 24 hours",
        xaxis_title="Time",
        yaxis_title="Conc. of PM 2.5 in micrograms/m^3",
        font=dict(
            family="Gravitas One, monospace",
            size=18,
            color="#7f7f7f"
        ),
        shapes=[
            go.layout.Shape(
                type="rect",
                # x-reference is assigned to the x-values
                xref="paper",
                # y-reference is assigned to the plot paper [0,1]
                yref="y",
                x0=0,
                y0=0,
                x1=1,
                y1=50,
                fillcolor="Green",
                opacity=0.4,
                layer="below",
                line_width=0,
            ),
            go.layout.Shape(
                type="rect",
                xref="paper",
                yref="y",
                x0=0,
                y0=50,
                x1=1,
                y1=100,
                fillcolor="Yellow",
                opacity=0.4,
                layer="below",
                line_width=0,
            ),
            go.layout.Shape(
                type="rect",
                xref="paper",
                yref="y",
                x0=0,
                y0=100,
                x1=1,
                y1=150,
                fillcolor="Orange",
                opacity=0.4,
                layer="below",
                line_width=0,
            ),
            go.layout.Shape(
                type="rect",
                xref="paper",
                yref="y",
                x0=0,
                y0=150,
                x1=1,
                y1=200,
                fillcolor="Red",
                opacity=0.4,
                layer="below",
                line_width=0,
            ),
            go.layout.Shape(
                type="rect",
                xref="paper",
                yref="y",
                x0=0,
                y0=201,
                x1=1,
                y1=300,
                fillcolor="Purple",
                opacity=0.4,
                layer="below",
                line_width=0,
            ),
            go.layout.Shape(
                type="rect",
                xref="paper",
                yref="y",
                x0=0,
                y0=300,
                x1=1,
                y1=500,
                fillcolor="Purple",
                opacity=0.4,
                layer="below",
                line_width=0,
            ),
    #        dict(
            go.layout.Shape(
                type="rect",
                xref="x",
                yref="y",
                x0=7,
                y0=0,
                x1=8,
                y1=pm[7],
                fillcolor="Blue",
                opacity=0.5,
                layer="below",
                line_width=0,
            )
            ]
    )

    st.write(fig1)
    #fig.show()

    fig2 = go.Figure()

    # Add scatter trace for line
    fig2.add_trace(go.Scatter(
        #x=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
        x = time,
#        y=[77, 81, 82, 82, 84, 82, 82, 79, 73, 75, 72, 72, 72, 68, 66, 64, 64, 64, 64, 63, 64, 63, 61, 61, 61],
        y = [82, 81, 79, 77, 73, 72, 70, 72, 70, 66, 64, 63, 63, 61, 61, 63, 68, 72, 77, 81, 82, 84, 84, 84, 82],
        mode="lines",
        name="temperature"
    ))

    fig2.update_layout(
        title="Temperature for the next 24 hours",
        xaxis_title="Time",
        yaxis_title="Temperature (in F)",
        font=dict(
            family="Gravitas One, monospace",
            size=18,
            color="#7f7f7f"
        )
    )

    st.write(fig2)

    fig3 = go.Figure()

    # Add scatter trace for line
    fig3.add_trace(go.Scatter(
#        x=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
x = time,
    #    y=[57, 51, 48, 45, 42, 42, 39, 44, 50, 57, 57, 60, 60, 68, 73, 77, 73, 73, 77, 77, 77, 82, 88, 88, 94],
    y = [82, 81, 79, 77, 73, 72, 70, 72, 70, 78, 83, 88, 82, 82, 88, 88, 82, 73, 64, 57, 51, 48, 42, 48, 42],
        mode="lines",
        name="humidity"
    ))

    fig3.update_layout(
        title="Humidity for the next 24 hours",
        xaxis_title="Time",
        yaxis_title="Humidity %",
        font=dict(
            family="Gravitas One, monospace",
            size=18,
            color="#7f7f7f"
        )
    )

    st.write(fig3)
    #fig.show()
