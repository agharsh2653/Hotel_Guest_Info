class Reservation:
    def __init__(self, registrationId, guestName, date_time, numGuest):
        self.registrationId = registrationId
        self.guestName = guestName
        self.date_time = date_time
        self.numGuest = numGuest

reservations = []

def addReservation():
    registrationId = int(input("Enter the reservation Id: "))
    guestName = input("Enter the name: ")
    date_time = input("Enter the date and time: ")
    numGuest = int(input("Enter the no of guest: "))
    reservation = Reservation(registrationId, guestName, date_time, numGuest)
    reservations.append(reservation)
    print("Reservation added successfully")

def cancelReservation():
    reservation_id = int(input("Enter the reservation Id to cancel: "))
    flag = False
    for res in reservations:
        if res.registrationId == reservation_id:
            flag = True
            reservations.remove(res)
            print(f"Reservation Id: {reservation_id} cancelled successfully")
            return
    if not flag:
        print("Invalid reservation ID. Please enter a valid ID.")

def displayReservation():
    if reservations:
        print("List of reservations:\n")
        for r1 in reservations:
            print(f"Reservation ID: {r1.registrationId}")
            print(f"Guest Name: {r1.guestName}")
            print(f"Date and Time: {r1.date_time}")
            print(f"No of Guests: {r1.numGuest}")
            print()
    else:
        print("No reservations found.")

while True:
    print("\nWelcome to the Hotel Guest Reservation System")
    print("1. Add Reservation")
    print("2. Display Reservations")
    print("3. Cancel Reservation")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    print()
    if choice == 1:
        addReservation()
    elif choice == 2:
        displayReservation()
    elif choice == 3:
        cancelReservation()
    elif choice == 4:
        print("Thank you for using Hotel Guest Reservation System")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
