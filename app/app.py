# app/app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
from data_fetcher import fetch_data
from data_processor import process_data

# Parameter Initialization
today = datetime.date.today()
default_end_date = today
default_start_date = today
hourly_options = [f"{hour:02d}:00" for hour in range(24)]

# Set up page title and layout
st.set_page_config(page_title="Electricity Price Dashboard", layout="wide")

# App description
st.markdown("""
    This is a demo of a Streamlit app that fetches electricity market prices data from the Awattar API-Datenfeed: https://www.awattar.at/services/api. 
    It allows users to select custom date and time ranges, and visualize electricity prices over 
    multiple time frames. Users can choose between bar and step chart visualizations to explore the data.
""")

# Sidebar with date and time range filters
st.sidebar.header("Settings")


# Start datetime input
start_date = st.sidebar.date_input(label="Start Date", value=default_start_date)
start_hour = st.sidebar.selectbox(label="Start Time", options= hourly_options, index=0)

# End datetime input
end_date = st.sidebar.date_input(label="End Date", value=default_end_date)
end_hour = st.sidebar.selectbox(label="End Time", options= hourly_options, index=23)

# Fetch the data
response = fetch_data(start_date, end_date, start_hour, end_hour)

# Process the data
df = process_data(response)

# Chart type selector
chart_type = st.sidebar.radio(
    "Select Chart Type",
    ("Bar Chart","Step Chart"),
    index=0 # Sets "Bar Chart" as the default option
)

# Visualization
st.header("Electricity Price Visualization")


if chart_type == "Bar Chart":
    fig = px.bar(
                data_frame=df,
                x='start_datetime',
                y='marketprice',
                title="Electricity Marketprice Bar Chart",
                hover_data={'start_datetime': True, 'marketprice':True})
    fig.update_xaxes(title_text = "Timestamp")
    fig.update_yaxes(title_text = "Electricity Marketprice (€/Mwh)")
    fig.update_traces(hovertemplate='Timestamp: %{x|%Y-%m-%d %H:%M}<br>Marketprice: %{y} €/MWh')
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Step Chart":
    # Use px.line with step lines by setting line_shape to 'hv' for horizontal-vertical steps
    fig = px.line(
                data_frame=df,
                x='start_datetime',
                y='marketprice', 
                title="Electricity Marketprice Over Time (Step Plot)", 
                hover_data={'start_datetime': True, 'marketprice':True},
                line_shape='hv')
    fig.update_xaxes(title_text = "Timestamp")
    fig.update_yaxes(title_text = "Electricity Marketprice (€/Mwh)")
    fig.update_traces(hovertemplate='Timestamp: %{x|%Y-%m-%d %H:%M}<br>Marketprice: %{y} €/MWh')
    st.plotly_chart(fig, use_container_width=True)

# Footer note
st.markdown("Data source and processing handled in separate scripts.")
