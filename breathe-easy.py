import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

#st.header("Beta Distribution Tutorial")

st.title('Breathe-Easy PM\u2082\u22C5\u2085 Forecast')

#input_city = st.selectbox("What city are you in?", ["Kolkata"])

st.write('The particulate matter and weather forecast in Kolkata for the next 12 hours is as follows:')

fig1 = go.Figure()

# Add scatter trace for line
fig1.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    y=[167, 191, 229, 249, 172, 171, 174, 105, 86, 67, 53, 56, 63],
    mode="lines",
    name="pollutant concentration",
    hovertext=["Temp 77, Hmdty 57, PM2.5 167", "Temp 77, Hmdty 57, PM2.5 191", "Temp 77, Hmdty 57, PM2.5 229",
               "Temp 77, Hmdty 57, PM2.5 249", "Temp 77, Hmdty 57, PM2.5 172", "Temp 77, Hmdty 57, PM2.5 171",
               "Temp 77, Hmdty 57, PM2.5 174", "Temp 77, Hmdty 57, PM2.5 105", "Temp 77, Hmdty 57, PM2.5 86",
               "Temp 77, Hmdty 57, PM2.5 67", "Temp 77, Hmdty 57, PM2.5 53", "Temp 77, Hmdty 57, PM2.5 56",
               "Temp 77, Hmdty 57, PM2.5 63"],
    hoverinfo="text",
    marker=dict(
        color="green"
    ),
    showlegend=False
))

fig1.update_layout(
    title="Pollution for the next 12 hours",
    xaxis_title="Hours from now",
    yaxis_title="Conc. of PM 2.5 in micrograms/m^3",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    ),
    shapes=[
        # 1st highlight during Feb 4 - Feb 6
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
            opacity=0.5,
            layer="below",
            line_width=0,
        ),
        # 2nd highlight during Feb 20 - Feb 23
        go.layout.Shape(
            type="rect",
            xref="paper",
            yref="y",
            x0=0,
            y0=50,
            x1=1,
            y1=100,
            fillcolor="Yellow",
            opacity=0.5,
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
            opacity=0.5,
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
            opacity=0.5,
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
            opacity=0.5,
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
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    y=[77, 81, 82, 82, 84, 82, 82, 79, 73, 75, 72, 72, 72],
    mode="lines",
    name="temperature"
))

fig2.update_layout(
    title="Temperature for the next 12 hours",
    xaxis_title="Hours from now",
    yaxis_title="Temperature (in F)",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)

st.write(fig2)

fig3 = go.Figure()

# Add scatter trace for line
fig3.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    y=[57, 51, 48, 45, 42, 42, 39, 44, 50, 57, 57, 60, 60],
    mode="lines",
    name="humidity"
))

fig3.update_layout(
    title="Humidity for the next 12 hours",
    xaxis_title="Hours from now",
    yaxis_title="Humidity %",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)

st.write(fig3)
#fig.show()
