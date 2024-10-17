"""
This file contains the function which fetches the electricity prices based on the user input.
"""
import requests
import json
from datetime import datetime




def fetch_data(start_date, end_date, start_hour, end_hour):
    
    # This is the required format: "YYYY-MM-DD HH:MM:SS"

    # Construct start and end datetime strings based on input dates and time range
    start_datetime = f"{start_date} {start_hour}:00"
    end_datetime = f"{end_date} {end_hour}:00"

    # Convert the strings to datetime objects
    dt_start = datetime.strptime(start_datetime, "%Y-%m-%d %H:%M:%S")
    dt_end = datetime.strptime(end_datetime, "%Y-%m-%d %H:%M:%S")

    # Convert to Unix timestamps in milliseconds
    start_timestamp = int(dt_start.timestamp() * 1000)
    end_timestamp = int(dt_end.timestamp() * 1000)

    # Construct the API request URL
    api_url = f"https://api.awattar.at/v1/marketdata?start={start_timestamp}&end={end_timestamp}"

    response = requests.get(api_url).json()

    return response



