import os
from data_plotting import *
from data_fetch import *

# Title of the dashboard
# st.title("Spending Tracker Dashboard")

def main():
    try:
        df = fetch_data()

        # Group data by email
        grouped_by_email = df.groupby("Email Address")

        # Print data for each user
        for email, group in grouped_by_email:
            print(f"Data for {email}:")
            print(group)
            print()

        # Plot for each user
        for email, group in grouped_by_email:
            if (not os.path.exists(f"plots/{email}")):
                os.mkdir(f"plots/{email}")
                
            plot_spending_by_category(email, group)
            plot_daily_spending(email, group)
            plot_monthly_spending(email, group)
            plot_cumulative_spending(email, group)
            plot_spending_frequency_by_hour(email, group)


    except Exception as e:
        print(f"File main.py - An error occurred: {e}")


if __name__ == '__main__':
    main()