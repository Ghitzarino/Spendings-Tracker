import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

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

    # Group data by email
    grouped_by_email = df.groupby("Email Address")

    # Print data for each user
    for email, group in grouped_by_email:
        print(f"Data for {email}:")
        print(group)
        print()

except Exception as e:
    print(f"An error occurred: {e}")