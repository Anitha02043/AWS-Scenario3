import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv('predicted_prices.csv')

# Calculate performance metrics
avg_price = round(df['predicted_price'].mean(), 2)
max_price = df['predicted_price'].max()
min_price = df['predicted_price'].min()
total_transactions = len(df)
unique_products = df['product'].nunique()

# Print metrics
print("=== Performance Metrics ===")
print(f"Average Price: {avg_price}")
print(f"Maximum Price: {max_price}")
print(f"Minimum Price: {min_price}")
print(f"Total Transactions: {total_transactions}")
print(f"Unique Products: {unique_products}")

# --------- Bar Chart: Product vs Predicted Price ---------
plt.figure(figsize=(8,5))
plt.bar(df['product'], df['predicted_price'], color='skyblue')
plt.title('Predicted Prices per Product')
plt.xlabel('Product')
plt.ylabel('Predicted Price')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('bar_chart.png')  # Saves chart as image
plt.show()  # Displays chart

# --------- Line Chart: Price Trend ---------
plt.figure(figsize=(8,5))
plt.plot(df['product'], df['predicted_price'], marker='o', color='orange')
plt.title('Price Trend Across Products')
plt.xlabel('Product')
plt.ylabel('Predicted Price')
plt.grid(True)
plt.tight_layout()
plt.savefig('line_chart.png')
plt.show()
