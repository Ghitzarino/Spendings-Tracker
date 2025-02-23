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
    plt.ylabel("Spending ($)")
    plt.grid(True)

    plt.savefig(f"../plots/{user_email}/spending_by_days.png")

# Function to plot spendings by category for a specific user
def plot_spending_by_category(user_email, user_data):
    category_spending = user_data.groupby("Category")["Price"].sum()
    plt.figure(figsize=(8, 8))
    plt.pie(category_spending, labels=category_spending.index, autopct="%1.1f%%", startangle=140)
    plt.title(f"Spending by Category for {user_email}")

    plt.savefig(f"../plots/{user_email}/spending_by_category.png")

# Function to plot monthly spendings for a specific user
def plot_monthly_spending(user_email, user_data):
    user_data["Month"] = user_data["Date"].dt.to_period("M")  # Extract month
    monthly_spending = user_data.groupby("Month")["Price"].sum()
    plt.figure(figsize=(10, 6))
    monthly_spending.plot(kind="bar")
    plt.title(f"Monthly Spending for {user_email}")
    plt.xlabel("Month")
    plt.ylabel("Total Spending ($)")

    plt.savefig(f"../plots/{user_email}/monthly_spending.png")

# Function to plot daily spendings for a specific user
def plot_daily_spending_histogram(user_email, user_data):
    plt.figure(figsize=(10, 6))
    plt.hist(user_data["Price"], bins=10, edgecolor="black")
    plt.title(f"Daily Spending Distribution for {user_email}")
    plt.xlabel("Spending ($)")
    plt.ylabel("Frequency")

    plt.savefig(f"../plots/{user_email}/daily_spending.png")

# Function to plot cumulative spendings for a specific user
def plot_cumulative_spending(user_email, user_data):
    user_data["Cumulative Spending"] = user_data["Price"].cumsum()
    plt.figure(figsize=(10, 6))
    plt.plot(user_data["Date"], user_data["Cumulative Spending"], marker="o", linestyle="-")
    plt.title(f"Cumulative Spending for {user_email}")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Spending ($)")
    plt.grid(True)

    plt.savefig(f"../plots/{user_email}/cumulative_spending.png")