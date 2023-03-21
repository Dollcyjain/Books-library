import sys

lend_dict = {}
add_dict = {}
return_dict = {}


class Library:
    def __init__(self, aname, abooklist):
        self.name = aname
        self.booklist = abooklist
        print(f"***Welcome to {self.name}***")

    def display_book(self):
        print(f"The books of {self.name} are:\n")
        for index, item in enumerate(self.booklist):
            print(f"{index + 1}. {item}")

    def lend_book(self):
        book_name = input("Enter the book name you want to lend: ")
        name_of_person = input("Enter your name: ")
        for item in self.booklist:
            if book_name == item:
                print(f"You have successfully lent {book_name} book")
                lend_dict[book_name] = name_of_person
                break
        else:
            print("We have not this book in our stock.")

    def add_book(self):
        a_book = input("Enter the book name you want to donate: ")
        giver = input("Enter your name: ")
        add_dict[a_book] = giver
        self.booklist.append(a_book)

    def return_book(self):
        returner = input("Enter your name: ")
        r_book = input("Enter the book name you want to return: ")
        for key, value in enumerate(lend_dict):
            if key == r_book and value == returner:
                print("You have successfully returned ", r_book)
                del lend_dict[key]
                return_dict[r_book] = returner
                break
        else:
            print("You have never lent this book. So, you can't return it.")


def display(obj):
    Library.display_book(obj)


def lend(obj):
    Library.lend_book(obj)


def add(obj):
    Library.add_book(obj)


def give_back(obj):
    Library.return_book(obj)


def terminate():
    yon = input("Type 'y' for exiting the library and 'n' for choosing option again: ")
    if yon == 'y':
        sys.exit()
    elif yon == 'n':
        func()
    else:
        print("Invalid input!!")


def func():
    print("\n\nWhat do you want to do:")
    print("1. Display books\n2. Lend book\n3. Donate book\n4. Return book")
    choice = int(input())
    if choice == 1:
        display(mylibrary)
        terminate()
    elif choice == 2:
        lend(mylibrary)
        terminate()
    elif choice == 3:
        add(mylibrary)
        terminate()
    elif choice == 4:
        give_back(mylibrary)
        terminate()
    else:
        print("Invalid option!!")
        terminate()


books = ["Harry Potter", "The story of Annie Frank", "The truth of Experiments", "Wings of Fire"]
mylibrary = Library("Dollcy Library", books)
func()
