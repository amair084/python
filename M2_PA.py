#Aaron Mairel
#CIS150AB 28829
#9/15/2025
#Calculation of the price of 2 A Computers and 5 B Computers with tax included.


# Setting price for computers and setting tax
price_a = 3150
price_b = 1350.55

tax = 0.083 #8.3%

# Find total price of the order
total_order_price = ((price_a * 2) + (price_b * 5))
price_after_tax = total_order_price*(tax+1)

# Print the price for the customer

print(f"Your total is ${total_order_price:.2f}")
print(f"The price of each A Computer was ${price_a:.2f}")
print(f"The price of each B Computer was ${price_b:.2f}")
print(f"The tax on this order was ${tax*total_order_price:.2f} / 8.3%")