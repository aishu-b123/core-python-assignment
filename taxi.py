
def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10 * distance
    return base_fare + distance_fare
distances = [5, 10, 3] 
total_fare = 0
for i, distance in enumerate(distances, start=1):
    fare = calculate_fare(distance)
    total_fare += fare
    print(f"Trip {i}: ${fare}")

print(f"Total Fare: ${total_fare}")
