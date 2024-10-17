import pandas as pd

def process_data(response):

    data = response["data"]
    df = pd.DataFrame(data)

    #First convert to UTC
    df['start_datetime'] = pd.to_datetime(df['start_timestamp'], unit='ms').dt.tz_localize('UTC')
    df['end_datetime'] = pd.to_datetime(df['end_timestamp'], unit='ms').dt.tz_localize('UTC')
    
    # Convert from UTC to my local timezone
    df['start_datetime'] = df['start_datetime'].dt.tz_convert('Europe/Berlin')
    df['end_datetime'] = df['end_datetime'].dt.tz_convert('Europe/Berlin')
    
    return df
