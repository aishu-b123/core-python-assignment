def book_seat(seat_number, available_seats, booked_seats):
    if seat_number in booked_seats:
        print(f"Seat {seat_number} is already booked.")
    else:
        booked_seats.append(seat_number)
        available_seats.remove(seat_number)
        print(f"Seat {seat_number} has been booked successfully.")

def cancel_seat(seat_number, available_seats, booked_seats):
    if seat_number not in booked_seats:
        print(f"Seat {seat_number} is not booked.")
    else:
        booked_seats.remove(seat_number)
        available_seats.append(seat_number)
        print(f"Seat {seat_number} has been canceled successfully.")

def display_available_seats(available_seats):
    print(f"Available seats: {sorted(available_seats)}")


total_seats = 10
available_seats = list(range(1, total_seats + 1))
booked_seats = []

while True:
    print("\nMenu:")
    print("1. Display Available Seats")
    print("2. Book a Seat")
    print("3. Cancel a Seat")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        display_available_seats(available_seats)
    elif choice == '2':
        seat_number = int(input("Enter seat number to book: "))
        book_seat(seat_number, available_seats, booked_seats)
    elif choice == '3':
        seat_number = int(input("Enter seat number to cancel: "))
        cancel_seat(seat_number, available_seats, booked_seats)
    elif choice == '4':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")


