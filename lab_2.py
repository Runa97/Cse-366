import numpy as np
import matplotlib.pyplot as plt

# Initialize parameters
average_price = 600  # example average price in BDT
critical_stock_level = 10
discount_threshold = 0.2  # 20% discount threshold
restock_quantity = 10  # minimum order quantity when stock is low

# Simulating the agent's percepts over time
prices = [600, 550, 520, 580, 490, 510, 480, 600, 470]  # example prices (in BDT)
stock_levels = [20, 20, 18, 15, 12, 8, 6, 15, 18]  # example stock levels

# Function to decide whether to order smartphones
def decide_order(current_price, current_stock, avg_price, discount_threshold, critical_stock_level, restock_quantity):
    # Check for significant price drop (20% or more)
    price_drop = (avg_price - current_price) / avg_price >= discount_threshold

    # If stock is critically low, prioritize restocking
    if current_stock < critical_stock_level:
        return restock_quantity

    # If price dropped significantly, and stock is not critically low, order more
    elif price_drop and current_stock >= critical_stock_level:
        # Order a quantity based on price drop and stock
        tobuy = max(10, int((avg_price - current_price) / avg_price * 20))  # ordering more based on price drop
        return tobuy
    else:
        return 0  # No need to order if no conditions met

# Apply decision rules to each percept
orders = []
for price, stock in zip(prices, stock_levels):
    order = decide_order(price, stock, average_price, discount_threshold, critical_stock_level, restock_quantity)
    orders.append(order)

# Plotting the stock levels and the orders over time
plt.figure(figsize=(10, 6))
plt.plot(prices, label="Price (BDT)", marker='o')
plt.plot(stock_levels, label="Stock Levels", marker='x')
plt.plot(orders, label="Orders", marker='s', linestyle='dashed')

plt.title("Smartphone Inventory Management")
plt.xlabel("Time")
plt.ylabel("Value (BDT / Stock / Orders)")
plt.legend(loc="upper left")
plt.grid(True)
plt.show()

# Display the results
for i, (price, stock, order) in enumerate(zip(prices, stock_levels, orders)):
    print(f"Time {i+1}: Price = {price} BDT, Stock = {stock}, Order = {order}")