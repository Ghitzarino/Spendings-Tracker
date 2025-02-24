import gspread  # type: ignore
import pandas as pd  # type: ignore
from google.oauth2.service_account import Credentials  # type: ignore

# Define the scope
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

def fetch_data():
    try:
        # Load credentials from the JSON file
        creds = Credentials.from_service_account_file("personal/credentials.json", scopes=SCOPES)

        # Authorize the client
        client = gspread.authorize(creds)

        # Open the Google Sheet by name
        sheet = client.open("Spendings-Tracker-answers").worksheet("main_sheet")  # Replace with your sheet name

        # Read data
        data = sheet.get_all_records()

        # Convert to a DataFrame
        df = pd.DataFrame(data)

        # Convert "Date and Time" to datetime
        df["Marcaj de timp"] = pd.to_datetime(df["Marcaj de timp"], format="%d.%m.%Y %H:%M:%S")

        # Extract Date and Time into separate columns
        df["Date"] = df["Marcaj de timp"].dt.date
        df["Time"] = df["Marcaj de timp"].dt.time

        # Drop the original "Marcaj de timp" column
        df = df.drop(columns=["Marcaj de timp"])

        # Update column name from "Adresă de e-mail" to "Email Address"
        df["Email Address"] = df["Adresă de e-mail"]
        df = df.drop(columns=["Adresă de e-mail"])

        return df
    
    except Exception as e:
        print(f"File data_fetch.py - An error occurred: {e}")