#!/usr/bin/env python3

num_books_rented = int(input("Please enter the number of books rented: "))

rent_duration = int(input("Please enter the duration for which book was rented: "))

daily_rental_charge = 1

total_rent = num_books_rented * rent_duration * daily_rental_charge

print("Your total rent is:", total_rent)


