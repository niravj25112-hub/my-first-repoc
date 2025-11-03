#Name - Nirav Jain
#Enrollment no. - 2502140112

from sys import hash_info

from django.contrib.postgres.indexes import HashIndex

import time
from datetime import datetime

PARKING_RATES = {'hourly_rate': 10, 'daily_rate': 80}
# Vehicle types allowed
VEHICLE_TYPES = {'car', 'bike', 'van'}
# List to store vehicles
vehicles = []

# --- Password Protection ---
PASSWORD = 'nirav123'

def password_protect():
    for attempt in range(3):
        user_pass = input("Enter password: ")
        if user_pass == PASSWORD:
            print("Login successful.\n")
            return True
        else:
            print(f"Incorrect password. {2 - attempt} attempts left.")
    print("Too many failed attempts. Exiting.")
    return False

def checkin_vehicle():
    license_plate = input("Enter license plate: ")
    vehicle_type = input("Enter vehicle type (car/bike/van): ").lower()
    if vehicle_type not in VEHICLE_TYPES:
        print("Invalid vehicle type. Allowed types:", VEHICLE_TYPES)
        return
    checkin_time = datetime.now()
    # Check for duplicate license plate
    for v in vehicles:
        if v['license_plate'] == license_plate:
            print("Vehicle already checked in.")
            return
    vehicle = {
        'license_plate': license_plate,
        'vehicle_type': vehicle_type,
        'checkin_time': checkin_time
    }
    vehicles.append(vehicle)
    print("Vehicle checked in successfully.")

def checkout_vehicle():
    license_plate = input("Enter license plate to check out: ")
    for idx, v in enumerate(vehicles):
        if v['license_plate'] == license_plate:
            checkout_time = datetime.now()
            parked_hours = (checkout_time - v['checkin_time']).total_seconds() / 3600
            parked_hours = max(1, int(parked_hours))  # Round to at least 1 hour
            fee = parked_hours * PARKING_RATES['hourly_rate']
            print(f"Vehicle checked out. Total fee: ₹{fee:.2f}. Hours parked: {parked_hours}")
            vehicles.pop(idx)
            return
    print("Vehicle not found.")

def modify_vehicle():
    license_plate = input("Enter license plate to modify: ")
    for v in vehicles:
        if v['license_plate'] == license_plate:
            print("What do you want to modify?")
            print("1. Vehicle Type")
            choice = input("Choice (1): ")
            if choice == '1':
                new_type = input("Enter new type (car/bike/van): ").lower()
                if new_type in VEHICLE_TYPES:
                    v['vehicle_type'] = new_type
                    print("Vehicle type updated.")
                else:
                    print("Invalid type.")
            return
    print("Vehicle not found.")

def search_vehicle():
    search = input("Enter license plate or type to search: ").lower()
    found = False
    for v in vehicles:
        if search in v['license_plate'].lower() or search == v['vehicle_type']:
            print(f"- Plate: {v['license_plate']}, Type: {v['vehicle_type']}, Check-in: {v['checkin_time']}")
            found = True
    if not found:
        print("No matching vehicles found.")

def view_reports():
    print("\n--- Occupancy Report ---")
    type_counts = {v_type: 0 for v_type in VEHICLE_TYPES}
    for v in vehicles:
        type_counts[v['vehicle_type']] += 1
    for t in type_counts:
        print(f"{t.capitalize()}: {type_counts[t]} vehicle(s)")
    print(f"Total vehicles: {len(vehicles)}")

# --- Main Menu ---
def main_menu():
    while True:
        print("\n--- Parking Lot Menu ---")
        print("1. Check-in Vehicle (Add)")
        print("2. Check-out Vehicle (Delete)")
        print("3. Modify Vehicle Details")
        print("4. Search for a Vehicle")
        print("5. View Reports")
        print("6. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            checkin_vehicle()
        elif choice == '2':
            checkout_vehicle()
        elif choice == '3':
            modify_vehicle()
        elif choice == '4':
            search_vehicle()
        elif choice == '5':
            view_reports()
        elif choice == '6':
            print("Exiting Parking Lot System.")
            break
        else:
            print("Invalid choice. Try again.")

# --- Program Start ---
if __name__ == "__main__":
    if password_protect():
        main_menu()
