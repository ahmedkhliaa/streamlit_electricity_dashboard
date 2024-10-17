# Electricity Price Dashboard

This Streamlit app provides a dynamic and interactive dashboard for visualizing electricity prices. It fetches data from the Awattar API-Datenfeed: https://www.awattar.at/services/api and allows users to explore price trends over customizable date and time ranges. Users can switch between different visualization types to suit their preferences.

## Features

- **Customizable Date and Time Filters**: Select specific date ranges and hourly intervals to view electricity prices over multiple time frames.
- **Interactive Visualizations**: Choose between bar and step chart visualizations to explore the data interactively.
- **Data Source Integration**: The app seamlessly fetches electricity price data from the Awattar API-Datenfeed and processes it for display.

## Installation

To run this app locally, follow these steps:

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/electricity-price-dashboard.git
   cd electricity-price-dashboard

2. **Install the required packages**:
   ```bash
    pip install -r requirements.txt

3. **Run the Streamlit app**:
   ```bash
   streamlit run app/app.py
