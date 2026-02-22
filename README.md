# Object Oriented Programming (OOP) Part 2 - Cash Register Lab

## Overview

This project implements a CashRegister class in Python to simulate the functionality of a simple e-commerce cash register system.

The application models real-world cash register behavior using object-oriented programming principles, including state management, encapsulation, and property validation.

## Features
1. Discount Handling

Accepts an optional discount percentage at initialization.

Validates that the discount is an integer between 0–100.

Defaults to 0 if invalid input is provided.

2. Item Management

Adds items with a price and optional quantity.

Automatically updates the running total.

Tracks items individually, including multiples.

3. Transaction History

Stores previous transactions with item name, price, and quantity.

Maintains internal transaction state for rollback operations.

4. Apply Discount

Applies percentage-based discount to the total.

Prints confirmation message:

After the discount, the total comes to $X.


Prints error message if no discount is available:

There is no discount to apply.

5. Void Last Transaction

Removes the most recent transaction.

Adjusts the total accordingly.

## Technologies Used

- Python 3

- Object-Oriented Programming

- @property and setter decorators

- Pytest for testing

## Running the Application
Install pytest (if needed)
pip install pytest

## Run tests

From the project root directory:

pytest


For verbose output:

pytest -v

## Example Usage
from cash_register import CashRegister

register = CashRegister(20)

register.add_item("Laptop", 1000)
register.apply_discount()

print(register.total)


Output:

After the discount, the total comes to $800.
800

## Concepts Demonstrated

- Class design and object state

- Encapsulation using properties

- Input validation

- Managing internal data structures

- Writing and running unit tests

