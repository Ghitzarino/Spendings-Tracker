import os
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
from data_plotting import *

# Define the scope
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

try:
    # Load credentials from the JSON file
    creds = Credentials.from_service_account_file("../personal/credentials.json", scopes=SCOPES)

    # Authorize the client
    client = gspread.authorize(creds)

    # Open the Google Sheet by name
    sheet = client.open("Spendings-Tracker-answers").worksheet("main_sheet")  # Replace with your sheet name

    # Read data
    data = sheet.get_all_records()

    # Convert to a DataFrame
    df = pd.DataFrame(data)

    # Convert "Date and Time" to datetime
    df["Date and Time"] = pd.to_datetime(df["Date and Time"], format="%d.%m.%Y %H:%M:%S")

    # Extract Date and Time into separate columns
    df["Date"] = df["Date and Time"].dt.date  # Extract date
    df["Time"] = df["Date and Time"].dt.time  # Extract time

    # Drop the original "Date and Time" column
    df = df.drop(columns=["Date and Time"])

    # Group data by email
    grouped_by_email = df.groupby("Email Address")

    # Print data for each user
    for email, group in grouped_by_email:
        print(f"Data for {email}:")
        print(group)
        print()

    # Plot for each user
    for email, group in grouped_by_email:
        if (not os.path.exists(f"../plots/{email}")):
            os.mkdir(f"../plots/{email}")
            
        plot_spending_by_days(email, group)
        plot_spending_by_category(email, group)
        plot_monthly_spending(email, group)
        plot_cumulative_spending(email, group)
        plot_daily_spending_histogram(email, group)
        plot_spending_frequency_by_hour(email, group)

except Exception as e:
    print(f"An error occurred: {e}")