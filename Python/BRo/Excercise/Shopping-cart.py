item = input("What would you like to buy?: ")

price = float(input("What is the price?: "))

quantity = int(input("How many you want?: "))

total = price * quantity

print(f"Your {quantity} {item}'s worth ${total} will be delivered at your house shortly")