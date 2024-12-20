def calculate(cart):
    if not cart:
        return 0
    total= sum(cart.values())
    if len(cart) > 5:
        total *= 0.9  
    return total

cart= {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
total_price = calculate(cart)
print(f"Total Price: {total_price}")
