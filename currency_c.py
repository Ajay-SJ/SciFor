# Importing tkinter and requests modules
import tkinter as tk
from tkinter import StringVar
import requests


# Function to perform conversion using an API and update the result on the GUI
def convert_currency():
    # Getting the values of the selected currencies and the amount
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = float(amount_entry.get())

    # Making a request to the exchange rate API with the from currency
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    # Getting the conversion rate for the to currency
    conversion_rate = data['rates'][to_currency]
    # Calculating the converted amount and rounding it to two decimal places
    converted_amount = round(amount * conversion_rate, 2)

    # Updating the result label with the converted amount
    result_label.config(text=f"{amount} {from_currency} Equals {converted_amount} {to_currency}")


# Creating the main window
root = tk.Tk()
root.title("Currency Converter")

# Creating StringVars for holding the currency types
from_currency_var = StringVar()
from_currency_var.set('USD')  # Default value

to_currency_var = StringVar()
to_currency_var.set('AUD')  # Default value

# Creating a label and an entry for the amount input
amount_label = tk.Label(root, text="Amount")
amount_label.grid(column=0, row=0)
amount_entry = tk.Entry(root)
amount_entry.grid(column=1, row=0)

# Creating dropdowns for selecting the currencies to convert from and to
currencies_list = (
'ALL', 'AFN', 'ARS', 'AWG', 'AUD', 'AZN', 'BSD', 'BBD', 'BYN', 'BZD', 'BMD', 'BOB', 'BAM', 'BWP', 'BGN', 'BND', 'KHR',
'CAD', 'KYD', 'CLP', 'CNY', 'COP', 'CRC', 'HRK', 'CUP', 'CZK', 'DKK', 'DOP', 'XCD', 'EGP', 'SVC', 'EUR', 'FKP', 'FJD',
'GHS', 'GIP', 'GTQ', 'GGP', 'GYD', 'HNL', 'HKD', 'HUF', 'ISK', 'INR')  # List of currencies

from_currency_dropdown = tk.OptionMenu(root, from_currency_var, *currencies_list)
tk.Label(root, text="From Currency").grid(column=0, row=1)
from_currency_dropdown.grid(column=1, row=1)

to_currency_dropdown = tk.OptionMenu(root, to_currency_var, *currencies_list)
tk.Label(root, text="To Currency").grid(column=0, row=2)
to_currency_dropdown.grid(column=1, row=2)

# Creating a button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(columnspan=2, row=3)

# Creating a label to display the result
result_label = tk.Label(root, text="")
result_label.grid(columnspan=2, row=4)

# Starting the main loop
root.mainloop()
