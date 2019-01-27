#!/usr/bin/env python3
from tkinter import *


class Calculator:
    def __init__(self, root):
        self.book_charges = {"regular": 1.5, "fiction": 3, "novels": 1.5}
        self.min_book_charges = {"regular": 2, "fiction": 0, "novels": 4.5}
        self.min_rent_days = {"regular": 2, "fiction": 0, "novels": 3}

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
        self.num_regbooksrented = Entry(root)
        self.num_regbooksrented.insert(0, "0")
        self.num_regbooksrented.grid(row=1, column=1, sticky=E, pady=4)
        self.regbook_rentduration = Entry(root)
        self.regbook_rentduration.insert(0, "0")
        self.regbook_rentduration.grid(row=1, column=2, sticky=E, pady=4)

        # fields for fiction book
        Label(root, text="Fiction").grid(row=2, sticky=W, padx=4)
        self.num_ficbooksrented = Entry(root)
        self.num_ficbooksrented.insert(0, "0")
        self.num_ficbooksrented.grid(row=2, column=1, sticky=E, pady=4)
        self.ficbook_rentduration = Entry(root)
        self.ficbook_rentduration.insert(0, "0")
        self.ficbook_rentduration.grid(row=2, column=2, sticky=E, pady=4)

        # fields for novels book
        Label(root, text="Novels").grid(row=3, sticky=W, padx=4)
        self.num_novbooksrented = Entry(root)
        self.num_novbooksrented.insert(0, "0")
        self.num_novbooksrented.grid(row=3, column=1, sticky=E, pady=4)
        self.novbook_rentduration = Entry(root)
        self.novbook_rentduration.insert(0, "0")
        self.novbook_rentduration.grid(row=3, column=2, sticky=E, pady=4)

        # fields for total rent
        Label(root, text="Total Rent").grid(row=4, column=1, sticky=W, padx=4)
        self.total_rent_field = Entry(root)
        self.total_rent_field.grid(row=4, column=2, sticky=E, pady=4)

        # fields for submit, quit and clear buttons
        self.submit_button = Button(root, text="Submit", command=(lambda: self.rent_calc())) \
            .grid(row=5, column=1, sticky=E, pady=4, padx=0)

        self.quit_button = Button(root, text="Quit", command=root.quit).grid(row=5, column=3, pady=4)
        # clear_button = Button(root, text="Clear").grid(row=5, column=2, pady=4,padx=0)

    def fetch_data(self):
        rented_books_data = []
        try:
            rented_books_data.append(
                ("regular", int(self.num_regbooksrented.get()), int(self.regbook_rentduration.get())))
            rented_books_data.append(
                ("fiction", int(self.num_ficbooksrented.get()), int(self.ficbook_rentduration.get())))
            rented_books_data.append(
                ("novels", int(self.num_novbooksrented.get()), int(self.novbook_rentduration.get())))
        except:
            print("Please enter Valid data")

        # print(rented_books_data)
        return rented_books_data

    def rent_calc(self):
        rented_books_data = self.fetch_data()
        total_rent = 0
        for row in rented_books_data:
            if row[0] in self.book_charges:
                if row[2] < self.min_rent_days[row[0]]:
                    partial_rent = row[1] * self.min_book_charges[row[0]]
                    total_rent = total_rent + partial_rent
                else:
                    if row[0] == "regular":
                        partial_rent = row[1] * 2 + row[1] * (row[2] - 2) * self.book_charges[row[0]]
                        total_rent = total_rent + partial_rent
                    else:
                        partial_rent = row[1] * row[2] * self.book_charges[row[0]]
                        total_rent = total_rent + partial_rent
            # print(total_rent)
        self.total_rent_field.delete(0, END)
        self.total_rent_field.insert(0, total_rent)

        # print(total_rent)


def main():
    # Get the root window object
    root = Tk()
    # Create the calculator
    # calc = Calculator(root)
    Calculator(root)
    # Run the app until exited
    root.mainloop()


main()
