import matplotlib.pyplot as plt
import pandas as pd

# Function to plot spending by days for a specific user
def plot_spending_by_days(user_email, user_data):
    user_data["Date"] = pd.to_datetime(user_data["Date"])  # Convert to datetime
    user_data = user_data.sort_values(by="Date")  # Sort by date

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(user_data["Date"], user_data["Price (Ron)"], marker="o", linestyle="-")
    plt.title(f"Spending Over Time for {user_email}")
    plt.xlabel("Date")
    plt.ylabel("Spending (Ron)")
    plt.grid(True)

    plt.savefig(f"../plots/{user_email}/spending_by_days.png")

    plt.close()  # Close the plot to free memory

# Function to plot spendings by category for a specific user
def plot_spending_by_category(user_email, user_data):
    category_spending = user_data.groupby("Category")["Price (Ron)"].sum()
    plt.figure(figsize=(8, 8))
    plt.pie(category_spending, labels=category_spending.index, autopct="%1.1f%%", startangle=140)
    plt.title(f"Spending by Category for {user_email}")

    plt.savefig(f"../plots/{user_email}/spending_by_category.png")

    plt.close()  # Close the plot to free memory

# Function to plot monthly spendings for a specific user
def plot_monthly_spending(user_email, user_data):
    user_data["Month"] = user_data["Date"].dt.to_period("M")  # Extract month
    monthly_spending = user_data.groupby("Month")["Price (Ron)"].sum()
    plt.figure(figsize=(10, 6))
    monthly_spending.plot(kind="bar")
    plt.title(f"Monthly Spending for {user_email}")
    plt.xlabel("Month")
    plt.ylabel("Total Spending (Ron)")

    plt.savefig(f"../plots/{user_email}/monthly_spending.png")

    plt.close()  # Close the plot to free memory

# Function to plot daily spendings for a specific user
def plot_daily_spending_histogram(user_email, user_data):
    plt.figure(figsize=(10, 6))
    plt.hist(user_data["Price (Ron)"], bins=10, edgecolor="black")
    plt.title(f"Daily Spending Distribution for {user_email}")
    plt.xlabel("Spending (Ron)")
    plt.ylabel("Frequency")

    plt.savefig(f"../plots/{user_email}/daily_spending.png")
    
    plt.close()  # Close the plot to free memory

# Function to plot cumulative spendings for a specific user
def plot_cumulative_spending(user_email, user_data):
    user_data["Cumulative Spending"] = user_data["Price (Ron)"].cumsum()
    plt.figure(figsize=(10, 6))
    plt.plot(user_data["Date"], user_data["Cumulative Spending"], marker="o", linestyle="-")
    plt.title(f"Cumulative Spending for {user_email}")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Spending (Ron)")
    plt.grid(True)

    plt.savefig(f"../plots/{user_email}/cumulative_spending.png")

    plt.close()  # Close the plot to free memory

# Function to plot spending frequency by hour for a specific user
def plot_spending_frequency_by_hour(user_email, user_data):
    # Convert "Time" to datetime.time (if not already done)
    user_data["Time"] = pd.to_datetime(user_data["Time"], format="%H:%M:%S").dt.time

    # Extract the hour from the "Time" column
    user_data["Hour"] = pd.to_datetime(user_data["Time"].astype(str), format="%H:%M:%S").dt.hour

    # Count the frequency of spending by hour
    spending_frequency = user_data["Hour"].value_counts().sort_index()

    # Ensure all hours (0 to 23) are included, even if frequency is zero
    all_hours = pd.Series(index=range(24), dtype=int)  # Create a Series with all hours
    spending_frequency = spending_frequency.reindex(all_hours.index, fill_value=0)  # Fill missing hours with 0

    # Plot the data
    plt.figure(figsize=(10, 6))
    spending_frequency.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title(f"Spending Frequency by Hour for {user_email}")
    plt.xlabel("Hour of the Day")
    plt.ylabel("Number of Transactions")
    plt.xticks(range(24), [f"{hour}:00" for hour in range(24)], rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.savefig(f"../plots/{user_email}/spending_frequency_by_hour.png")

    plt.close()  # Close the plot to free memory