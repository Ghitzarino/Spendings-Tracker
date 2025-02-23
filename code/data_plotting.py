import matplotlib.pyplot as plt # type: ignore
import pandas as pd # type: ignore
from datetime import datetime

# Function to plot spendings by category for a specific user
def plot_spending_by_category(user_email, user_data):
    category_spending = user_data.groupby("Category")["Price (Ron)"].sum()

    # Plot the data
    plt.figure(figsize=(8, 8))
    plt.pie(category_spending, labels=category_spending.index, autopct="%1.1f%%", startangle=140)
    plt.title(f"Spending by Category for {user_email}")

    plt.savefig(f"plots/{user_email}/spending_by_category.png")

    plt.close()

# Function to plot monthly spendings for a specific user
def plot_monthly_spending(user_email, user_data):
    user_data["Month"] = user_data["Date"].dt.to_period("M")  # Extract month
    monthly_spending = user_data.groupby("Month")["Price (Ron)"].sum()

    # Plot the data
    plt.figure(figsize=(10, 6))
    monthly_spending.plot(kind="bar", edgecolor="black", color="pink")
    plt.title(f"Monthly Spending for {user_email}")
    plt.xlabel("Month")
    plt.ylabel("Total Spending (Ron)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.savefig(f"plots/{user_email}/monthly_spending.png")

    plt.close()

# Function to plot daily spendings for a specific user
def plot_daily_spending(user_email, user_data):
    # Convert the "Date" column to datetime format
    user_data["Date"] = pd.to_datetime(user_data["Date"])

    # Filter data for the current month
    current_month = datetime.now().month
    current_year = datetime.now().year
    user_data = user_data[
        (user_data["Date"].dt.month == current_month) & 
        (user_data["Date"].dt.year == current_year)
    ]

    # Group by day and calculate the sum of spendings
    daily_spending = user_data.groupby(user_data["Date"].dt.day)["Price (Ron)"].sum()

    # Ensure all days of the month are included, even if spending is zero
    all_days = pd.Series(index=range(1, 32), dtype=float)  # Days 1 to 31
    daily_spending = daily_spending.reindex(all_days.index, fill_value=0)  # Fill missing days with 0

    # Plot the data as a bar graph
    plt.figure(figsize=(10, 6))
    daily_spending.plot(kind="bar", edgecolor="black", color="pink")
    plt.title(f"Daily Spending for {user_email} (Current Month)")
    plt.xlabel("Day of the Month")
    plt.ylabel("Total Spending (Ron)")
    plt.xticks(range(31), [f"{day}" for day in range(1, 32)], rotation=0)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.savefig(f"plots/{user_email}/daily_spending.png")
    
    plt.close()

# Function to plot cumulative spendings for a specific user
def plot_cumulative_spending(user_email, user_data):
     # Create a new row with cumulative spending = 0 at the earliest date
    start_row = pd.DataFrame({
        "Date": [user_data["Date"].min() - pd.Timedelta(days=1)],
        "Price (Ron)": [0],
        "Cumulative Spending": [0]
    })

    # Concatenate the start row with the user data
    user_data = pd.concat([start_row, user_data], ignore_index=True)

    # Calculate cumulative spending
    user_data["Cumulative Spending"] = user_data["Price (Ron)"].cumsum()

     # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(user_data["Date"], user_data["Cumulative Spending"], marker="o", linestyle="-", color="pink")
    plt.title(f"Cumulative Spending for {user_email}")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Spending (Ron)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.savefig(f"plots/{user_email}/cumulative_spending.png")

    plt.close()

# Function to plot spending frequency by hour for a specific user
def plot_spending_frequency_by_hour(user_email, user_data):
    # Extract the hour from the "Time" column
    user_data["Hour"] = pd.to_datetime(user_data["Time"].astype(str), format="%H:%M:%S").dt.hour

    # Count the frequency of spending by hour
    spending_frequency = user_data["Hour"].value_counts().sort_index()

    # Ensure all hours (0 to 23) are included, even if frequency is zero
    all_hours = pd.Series(index=range(24), dtype=int)
    spending_frequency = spending_frequency.reindex(all_hours.index, fill_value=0)

    # Plot the data
    plt.figure(figsize=(10, 6))
    spending_frequency.plot(kind="bar", edgecolor="black", color="pink")
    plt.title(f"Spending Frequency by Hour for {user_email}")
    plt.xlabel("Hour of the Day")
    plt.ylabel("Number of Transactions")
    plt.xticks(range(24), [f"{hour}:00" for hour in range(24)], rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.savefig(f"plots/{user_email}/spending_frequency_by_hour.png")

    plt.close()