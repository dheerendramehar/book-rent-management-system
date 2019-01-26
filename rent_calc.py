#!/usr/bin/env python3

# num_books_rented = int(input("Please enter the number of books rented: "))
# rent_duration = int(input("Please enter the duration for which book was rented: "))
# daily_rental_charge = 1
# total_rent = num_books_rented * rent_duration * daily_rental_charge
# print("Your total rent is:", total_rent)

# Three kind of Books: regular, fiction and novels with different rents
# book_types = [regular,fiction,novels]

def rent_calc(rented_books_data, book_charges, min_book_charges, min_rent_days):
    total_rent = 0
    for row in rented_books_data:
        if row[0] in book_charges:
            if row[2] < min_rent_days[row[0]]:
                partial_rent = row[1] * min_book_charges[row[0]]
                total_rent = total_rent + partial_rent
            else:
                if row[0] == "regular":
                    partial_rent = row[1] * 2 + row[1] * (row[2] - 2) * book_charges[row[0]]
                    total_rent = total_rent + partial_rent
                else:
                    partial_rent = row[1] * row[2] * book_charges[row[0]]
                    total_rent = total_rent + partial_rent
        # print(total_rent)
    return total_rent


def main():
    book_charges = {"regular": 1.5, "fiction": 3, "novels": 1.5}
    min_book_charges = {"regular": 2, "fiction": 0, "novels": 4.5}
    min_rent_days = {"regular": 2, "fiction": 0, "novels": 3}
    rented_books_data = []
    print("Please enter the books rented in the following format")
    print("book_type num_books_rented rent_duration")
    for i in range(0, 3):
        book_type, num_book_rented, rent_duration = input().split()
        rented_books_data.append((book_type, int(num_book_rented), int(rent_duration)))
    # print(rented_books_data)

    total_rent = rent_calc(rented_books_data, book_charges, min_book_charges, min_rent_days)

    print("Your total rent is:", total_rent)


main()

