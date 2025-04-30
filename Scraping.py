import pandas as pd

# Load your dataset
df = pd.read_csv(r"Bankinfo\bank_transactions_data_2.csv",
                 parse_dates=["TransactionDate", "PreviousTransactionDate"])

# ##################################################
# 1. **Customer-Level Summary Table**
# This table aggregates each customer's transaction data and provides key insights such as:
# - Total amount spent
# - Average transaction amount
# - Number of transactions
# - First and last transaction date
# - Age and occupation (most common occupation if multiple listed)
# It helps identify high-value customers and understand their spending habits.
# Ensure 'TransactionDate' is a datetime column

df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
customer_summary = df.groupby("AccountID").agg({
    # Number of transactions per Account
    "TransactionID": "count",

    # Total Amount of transactions per Account
    "TransactionAmount": "sum",

    # Average amount of transactions per Account
    "TransactionAmount": "mean",
    # Account holders Age
    "CustomerAge": "first",

    # General Occupation of Account holder
    "CustomerOccupation": lambda x: x.mode().iloc[0] if not x.mode().empty else None
}).reset_index()
# 2. **Transaction-Pattern Analysis Table**
# This table shows different transactions per Account once linked with customer-summar table in power Bi
Transaction_chart = df.groupby("TransactionID").first()
Transaction_chart.reset_index(inplace=True)
# ##################################################
# 3. **Transaction-Type Analysis Table**
# This table provides insights into the different types of transactions (e.g., purchase, refund, etc.)
# and the amount of money associated with each type.
# - It shows how many of each type of transaction occurred and the total/average amounts.
# - Useful for understanding what types of transactions drive the business.

transaction_type_summary = df.groupby("TransactionType").agg({
    # Number of transactions per type
    "TransactionID": "count",
    # Average amount per transaction type
    "TransactionAmount": "mean"
}).reset_index()
transaction_type_summary.columns.values[1] = "Total_Count"

# Calculate percentage of each transaction type
total_txn = df.shape[0]
transaction_type_summary["Percentage"] = (
    transaction_type_summary["Total_Count"] / total_txn * 100).round(2)
print(transaction_type_summary)
# ##################################################
# 4. **Channel Comparison Table**
# This table compares transaction data based on different channels (e.g., web, mobile app, in-person).
# - It looks at total transactions per channel, the average transaction amount, and total money spent.
# - It also includes the average transaction duration (if available), useful for performance and engagement analysis.
# - This helps to see which channels perform best or need more attention.

channel_summary = df.groupby("Channel").agg({
    # Total number of transactions per channel
    "TransactionID": "count",
    # Average amount per transaction by channel
    "TransactionAmount": "mean",
    # Total amount spent by channel
}).reset_index()
channel_summary.columns.values[1] = "Count_of_transactions"
channel_summary.columns.values[2] = "Mean_sum_of_transactions"
print(
    Transaction_chart)


# ##################################################
# Export to CSV for use in excel for SQL Analysis, Then export to Power Bi
# Save customer summary to CSV
customer_summary.to_csv("customer_summary.csv", index=False)
# Save Transaction chart to CSV
print(customer_summary)
Transaction_chart.to_csv("Info_Chart.csv", index=False)
# Save transaction-type summary to CSV
transaction_type_summary.to_csv("transaction_type_summary.csv", index=False)
# Save channel comparison summary to CSV
channel_summary.to_csv("channel_summary.csv", index=False)
