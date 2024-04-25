# Define a class for the Book data type
class Book:
    # Initialize the book with its id, title, and price
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price

    # Define a string representation of the book
    def __str__(self):
        return f"Book(id={self.id}, title={self.title}, price={self.price})"

# Define a list to store the books in the stock
stock = []

# Define a function to add a new book to the stock
def add_book(id, title, price):
    # Create a new book object with the given id, title, and price
    new_book = Book(id, title, price)
    # Append the new book to the stock list
    stock.append(new_book)
    # Print a confirmation message
    print(f"Added {new_book} to the stock.")

# Define a function to get a book from the stock based on its id, price, or title
def get_book(criteria, value):
    # Loop through the stock list
    for book in stock:
        # Check if the book matches the given criteria and value
        if getattr(book, criteria) == value:
            # Return the matching book
            return book
    # If no book is found, return None
    return None

# Define a function to show all the books in the stock
def show_books():
    # Print a header message
    print("The books in the stock are:")
    # Loop through the stock list
    for book in stock:
        # Print each book
        print(book)

# Define a function to delete a book from the stock based on its id, price, or title
def delete_book(criteria, value):
    # Loop through the stock list
    for i, book in enumerate(stock):
        # Check if the book matches the given criteria and value
        if getattr(book, criteria) == value:
            # Remove the book from the stock list
            stock.pop(i)
            # Print a confirmation message
            print(f"Deleted {book} from the stock.")
            # Return the deleted book
            return book
    # If no book is found, return None
    return None

# Define a function to show the options to the user and perform the operation based on the user's choice
def main():
    # Print a welcome message
    print("Welcome to Sophia's book store!")
    # Print the options
    print("Please choose one of the following options:")
    print("1. Add a new book to the stock")
    print("2. Get a book from the stock")
    print("3. Show all the books in the stock")
    print("4. Delete a book from the stock")
    print("5. Exit the program")
    # Get the user's choice
    choice = int(input("Enter your choice: "))
    # Validate the user's choice
    if choice not in range(1, 6):
        # Print an error message
        print("Invalid choice. Please try again.")
        # Call the main function again
        main()
    # If the user chooses to add a new book
    elif choice == 1:
        # Get the book details from the user
        id = input("Enter the book id: ")
        title = input("Enter the book title: ")
        price = float(input("Enter the book price: "))
        # Call the add_book function with the book details
        add_book(id, title, price)
        # Call the main function again
        main()
    # If the user chooses to get a book
    elif choice == 2:
        # Print the criteria options
        print("You can get a book based on its id, price, or title.")
        print("Please choose one of the following criteria:")
        print("1. Id")
        print("2. Price")
        print("3. Title")
        # Get the user's criteria
        criteria = int(input("Enter your criteria: "))
        # Validate the user's criteria
        if criteria not in range(1, 4):
            # Print an error message
            print("Invalid criteria. Please try again.")
            # Call the main function again
            main()
        # If the user chooses id
        elif criteria == 1:
            # Get the book id from the user
            id = input("Enter the book id: ")
            # Call the get_book function with the id
            book = get_book("id", id)
            # Check if the book is found
            if book is not None:
                # Print the book details
                print(f"The book with id {id} is {book}.")
            else:
                # Print a not found message
                print(f"There is no book with id {id} in the stock.")
            # Call the main function again
            main()
        # If the user chooses price
        elif criteria == 2:
            # Get the book price from the user
            price = float(input("Enter the book price: "))
            # Call the get_book function with the price
            book = get_book("price", price)
            # Check if the book is found
            if book is not None:
                # Print the book details
                print(f"The book with price {price} is {book}.")
            else:
                # Print a not found message
                print(f"There is no book with price {price} in the stock.")
            # Call the main function again
            main()
        # If the user chooses title
        elif criteria == 3:
            # Get the book title from the user
            title = input("Enter the book title: ")
            # Call the get_book function with the title
            book = get_book("title", title)
            # Check if the book is found
            if book is not None:
                # Print the book details
                print(f"The book with title {title} is {book}.")
            else:
                # Print a not found message
                print(f"There is no book with title {title} in the stock.")
            # Call the main function again
            main()
    # If the user chooses to show all the books
    elif choice == 3:
        # Call the show_books function
        show_books()
        # Call the main function again
        main()
    # If the user chooses to delete a book
    elif choice == 4:
        # Print the criteria options
        print("You can delete a book based on its id, price, or title.")
        print("Please choose one of the following criteria:")
        print("1. Id")
        print("2. Price")
        print("3. Title")
        # Get the user's criteria
        criteria = int(input("Enter your criteria: "))
        # Validate the user's criteria
        if criteria not in range(1, 4):
            # Print an error message
            print("Invalid criteria. Please try again.")
            # Call the main function again
            main()
        # If the user chooses id
        elif criteria == 1:
            # Get the book id from the user
            id = input("Enter the book id: ")
            # Call the delete_book function with the id
            book = delete_book("id", id)
            # Check if the book is deleted
            if book is not None:
                # Print a confirmation message
                print(f"Deleted {book} from the stock.")
            else:
                # Print a not found message
                print(f"There is no book with id {id} in the stock.")
            # Call the main function again
            main()
        # If the user chooses price
        elif criteria == 2:
            # Get the book price from the user
            price = float(input("Enter the book price: "))
            # Call the delete_book function with the price
            book = delete_book("price", price)
            # Check if the book is deleted
            if book is not None:
                # Print a confirmation message
                print(f"Deleted {book} from the stock.")
            else:
                # Print a not found message
                print(f"There is no book with price {price} in the stock.")
            # Call the main function again
            main()
        # If the user chooses title
        elif criteria == 3:
            # Get the book title from the user
            title = input("Enter the book title: ")
            # Call the delete_book function with the title
            book = delete_book("title", title)
            # Check if the book is deleted
            if book is not None:
                # Print a confirmation message
                print(f"Deleted {book} from the stock.")
            else:
                # Print a not found message
                print(f"There is no book with title {title} in the stock.")
            # Call the main function again
            main()
    # If the user chooses to exit the program
    elif choice == 5:
        # Print a goodbye message
        print("Thank you for using Sophia's book store. Have a nice day!")
        # Exit the program
        exit()

# Call the main function
main()
