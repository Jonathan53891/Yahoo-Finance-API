import os
import yfinance as yf
import pandas as pd

def fetch_data():
    # List of ticker symbols
    ticker_symbols = ["AAPL", "MSFT", "GOOGL"]

    # Create an empty DataFrame
    data_frames = []

    # Loop through each ticker symbol
    for symbol in ticker_symbols:
        # Fetch data for the current ticker symbol
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d", start="2023-01-01", end="2023-05-31")

        # Add the ticker symbol as a column
        data["Ticker"] = symbol

        # Append the data to the list of DataFrames
        data_frames.append(data)

    # Concatenate all the DataFrames into a single DataFrame
    combined_data = pd.concat(data_frames)

    # Return the combined DataFrame
    return combined_data

# Fetch the data
data_frame = fetch_data()

# Define the folder path where you want to save the file
folder_path = r"C:\Users\jonat\Yahoo Finance Data"

# Create the folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# Define the file path with the folder and filename
file_path = os.path.join(folder_path, "data.xlsx")

# Export the fetched data to the specified file path
data_frame.to_excel(file_path, index=False)


'''import yfinance as yf
import pandas as pd

def fetch_data():
    # List of ticker symbols
    ticker_symbols = ["AAPL", "MSFT", "GOOGL"]

    # Create an empty DataFrame
    data_frames = []

    # Loop through each ticker symbol
    for symbol in ticker_symbols:
        # Fetch data for the current ticker symbol
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d", start="2023-01-01", end="2023-05-31")

        # Add the ticker symbol as a column
        data["Ticker"] = symbol

        # Append the data to the list of DataFrames
        data_frames.append(data)

    # Concatenate all the DataFrames into a single DataFrame
    combined_data = pd.concat(data_frames)

    # Return the combined DataFrame
    return combined_data

# Fetch the data
data_frame = fetch_data()

# Export the fetched data to an Excel file
data_frame.to_excel("data.xlsx", index=False)'''


'''import yfinance as yf
import schedule
import time
import pandas as pd

def fetch_data():
    # List of ticker symbols
    ticker_symbols = ["AAPL", "MSFT", "GOOGL"]

    # Create an empty DataFrame
    data_frame = pd.DataFrame()

    # Loop through each ticker symbol
    for symbol in ticker_symbols:
        # Fetch data for the current ticker symbol
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d", start="2023-01-01", end="2023-05-31")

        # Append the data to the DataFrame with a column indicating the ticker symbol
        data["Ticker"] = symbol
        data_frame = data_frame.append(data)

    # Return the combined DataFrame
    return data_frame

# Schedule the task to run every morning at 8:00 AM
schedule.every().day.at("08:00").do(fetch_data)

# Run an infinite loop to continuously check for scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)

    # Export the fetched data to an Excel file
    data_frame = fetch_data()
    data_frame.to_excel("Yahoo Finance Data.xlsx", index=False)'''