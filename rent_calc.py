#!/usr/bin/env python3
from tkinter import *


def fetch_data():
    rented_books_data = []
    rented_books_data.append(("regular", int(num_regbooksrented.get()), int(regbook_rentduration.get())))
    rented_books_data.append(("fiction", int(num_ficbooksrented.get()), int(ficbook_rentduration.get())))
    rented_books_data.append(("novels", int(num_novbooksrented.get()), int(novbook_rentduration.get())))
    #print(rented_books_data)
    return rented_books_data


def rent_calc(book_charges, min_book_charges, min_rent_days):
    rented_books_data = fetch_data()
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
        #print(total_rent)
    total_rent_field.delete(0, END)
    total_rent_field.insert(0, total_rent)
    # print(total_rent)


if __name__ == '__main__':
    book_charges = {"regular": 1.5, "fiction": 3, "novels": 1.5}
    min_book_charges = {"regular": 2, "fiction": 0, "novels": 4.5}
    min_rent_days = {"regular": 2, "fiction": 0, "novels": 3}

    root = Tk()
    root.title("Rent Management System")

    # Defines the width and height of the window
    root.geometry("400x200")

    # Define the Rent attributes
    Label(root, text="Type of books").grid(row=0, column=0, sticky=W, padx=4)
    Label(root, text="No. of books rented").grid(row=0, column=1, sticky=W, padx=4)
    Label(root, text="Rent duration").grid(row=0, column=2, sticky=W, padx=4)

    # fields for regular book
    Label(root, text="Regular").grid(row=1, sticky=W, padx=4)
    # num_regbooksrented = Entry(root).grid(row=1, column=1, sticky=E, pady=4) # this doesn't work
    num_regbooksrented = Entry(root)
    num_regbooksrented.insert(0, "0")
    num_regbooksrented.grid(row=1, column=1, sticky=E, pady=4)
    regbook_rentduration = Entry(root)
    regbook_rentduration.insert(0, "0")
    regbook_rentduration.grid(row=1, column=2, sticky=E, pady=4)

    # fields for fiction book
    Label(root, text="Fiction").grid(row=2, sticky=W, padx=4)
    num_ficbooksrented = Entry(root)
    num_ficbooksrented.insert(0, "0")
    num_ficbooksrented.grid(row=2, column=1, sticky=E, pady=4)
    ficbook_rentduration = Entry(root)
    ficbook_rentduration.insert(0, "0")
    ficbook_rentduration.grid(row=2, column=2, sticky=E, pady=4)

    # fields for novels book
    Label(root, text="Novels").grid(row=3, sticky=W, padx=4)
    num_novbooksrented = Entry(root)
    num_novbooksrented.insert(0, "0")
    num_novbooksrented.grid(row=3, column=1, sticky=E, pady=4)
    novbook_rentduration = Entry(root)
    novbook_rentduration.insert(0, "0")
    novbook_rentduration.grid(row=3, column=2, sticky=E, pady=4)

    # fields for total rent
    Label(root, text="Total Rent").grid(row=4, column=1, sticky=W, padx=4)
    total_rent_field = Entry(root)
    total_rent_field.grid(row=4, column=2, sticky=E, pady=4)

    # fields for submit, quit and clear buttons
    submit_button = Button(root, text="Submit",
                           command=(lambda: rent_calc(book_charges, min_book_charges, min_rent_days))) \
        .grid(row=5, column=1, sticky=E, pady=4, padx=0)

    quit_button = Button(root, text="Quit", command=root.quit).grid(row=5, column=3, pady=4)
    # clear_button = Button(root, text="Clear").grid(row=5, column=2, pady=4,padx=0)

    root.mainloop()


