# Import tkinter and math modules
import tkinter as tk
import math

# Create the main window and set its title and size
window = tk.Tk()
window.title("Scientific Calculator Using Python Tkinter")
window.geometry("800x800")
window.configure(bg="white")
window.resizable(False, False)

# Create a frame to hold the widgets
frame = tk.Frame(window, bg="white")
frame.grid()

# Create a string variable to store the display value
display_var = tk.StringVar()

# Create an entry widget for the display
display = tk.Entry(frame, textvariable=display_var, width=30, bg="lightgray", fg="black", font=("Arial", 20), justify="right")
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Create a function to handle the number buttons
def number_click(num):
    # Get the current display value
    value = display_var.get()
    # Append the number to the value
    value += str(num)
    # Set the new display value
    display_var.set(value)

# Create a function to handle the operator buttons
def operator_click(op):
    # Get the current display value
    value = display_var.get()
    # Append the operator to the value
    value += op
    # Set the new display value
    display_var.set(value)

# Create a function to handle the equal button
def equal_click():
    # Get the current display value
    value = display_var.get()
    # Try to evaluate the value as an expression
    try:
        # Evaluate the value using the eval() function
        result = eval(value)
        # Set the display value to the result
        display_var.set(result)
    # If there is an error, show a message
    except:
        display_var.set("Error")

# Create a function to handle the clear button
def clear_click():
    # Set the display value to an empty string
    display_var.set("")

# Create a function to handle the delete button
def delete_click():
    # Get the current display value
    value = display_var.get()
    # Delete the last character of the value
    value = value[:-1]
    # Set the new display value
    display_var.set(value)

# Create a function to handle the decimal button
def decimal_click():
    # Get the current display value
    value = display_var.get()
    # Check if the value already has a decimal point
    if "." not in value:
        # Append a decimal point to the value
        value += "."
        # Set the new display value
        display_var.set(value)

# Create a function to handle the scientific buttons
def scientific_click(func):
    # Get the current display value
    value = display_var.get()
    # Try to evaluate the value as a number
    try:
        # Evaluate the value using the eval() function
        num = eval(value)
        # Apply the scientific function to the number using the math module
        result = getattr(math, func)(num)
        # Set the display value to the result
        display_var.set(result)
    # If there is an error, show a message
    except:
        display_var.set("Error")

# Create a list of number buttons
numbers = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("0", 4, 0),
]

# Create the number buttons using a loop
for number, row, column in numbers:
    # Create a button with the number as the text
    button = tk.Button(frame, text=number, width=5, height=2, bg="white", fg="black", font=("Arial", 15), command=lambda num=number: number_click(num))
    # Place the button on the grid
    button.grid(row=row, column=column, padx=5, pady=5)

# Create a list of operator buttons
operators = [
    ("+", 1, 3),
    ("-", 2, 3),
    ("*", 3, 3),
    ("/", 4, 3),
    ("=", 4, 2),
    ("C", 1, 4),
    ("Del", 2, 4),
    (".", 4, 1),
]

# Create the operator buttons using a loop
for operator, row, column in operators:
    # Create a button with the operator as the text
    button = tk.Button(frame, text=operator, width=5, height=2, bg="lightblue", fg="black", font=("Arial", 15), command=lambda op=operator: operator_click(op) if op not in ["=", "C", "Del", "."] else equal_click() if op == "=" else clear_click() if op == "C" else delete_click() if op == "Del" else decimal_click())
    # Place the button on the grid
    button.grid(row=row, column=column, padx=5, pady=5)

# Create a list of scientific buttons
scientifics = [
    ("sin", 5, 0),
    ("cos", 5, 1),
    ("tan", 5, 2),
    ("log", 5, 3),
    ("ln", 5, 4),
    ("sqrt", 6, 0),
    ("pi", 6, 1),
    ("e", 6, 2),
    ("^", 6, 3),
    ("%", 6, 4),
]

# Create the scientific buttons using a loop
for scientific, row, column in scientifics:
    # Create a button with the scientific function as the text
    button = tk.Button(frame, text=scientific, width=5, height=2, bg="lightgreen", fg="black", font=("Arial", 15), command=lambda func=scientific: scientific_click(func) if func in ["sin", "cos", "tan", "log", "ln", "sqrt"] else display_var.set(math.pi) if func == "pi" else display_var.set(math.e) if func == "e" else operator_click("**") if func == "^" else operator_click("%"))
    # Place the button on the grid
    button.grid(row=row, column=column, padx=5, pady=5)

# Start the main loop
window.mainloop()
