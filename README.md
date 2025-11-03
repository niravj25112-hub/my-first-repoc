# my-first-repoc
🚗 Parking Lot Management System

Author: Nirav Jain
Enrollment No.: 2502140112

📘 Overview

This is a Python-based Parking Lot Management System that allows users to manage vehicle check-ins, check-outs, modifications, and reports with password protection.
It is a menu-driven console application built using Python’s standard libraries.

🧠 Features

✅ Password Protection — Only authorized users can access the system (default password: nirav123)
✅ Vehicle Check-In — Add new vehicles with type and license plate
✅ Vehicle Check-Out — Calculate parking fee based on time parked
✅ Modify Vehicle Details — Change vehicle type for an existing entry
✅ Search Functionality — Find vehicles by license plate or type
✅ Reports — View total occupancy and count by vehicle type
✅ Real-Time Clock — Uses Python’s datetime for accurate check-in and check-out timing

⚙️ Technology Used

Language: Python 3

Libraries:

datetime — for handling timestamps

time — for timing operations

sys, django.contrib.postgres.indexes — imported (but optional in this script)

🧩 Vehicle Types

The system supports:

🚗 Car

🏍️ Bike

🚐 Van

💰 Parking Rates
Type	Rate
Hourly	₹10/hour
Daily (approx.)	₹80/day

(Hourly rate used for calculation)
