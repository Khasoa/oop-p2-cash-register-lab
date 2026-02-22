#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    #Initialize discount using property validation
    self.discount = discount

    #Running total of all items
    self.total = 0

    #List of item names
    self.items = []

    #Store transaction history
    self.previous_transactions = []

  #Property getter for discount
  @property
  def discount(self):
    return self._discount
  
  #Property setter with validation
  @discount.setter
  def discount (self, value):
    if not isinstance(value, int) or value < 0 or value > 100:
      print("Not valid discount")
      self._discount = 0
    else:
      self._discount = value

   #Add item to register 
  def add_item(self, item, price, quantity = 1):
    total_price = price * quantity
    self.total += total_price
    for _ in range(quantity):
      self.items.append(item)

    self.previous_transactions.append({
      "item": item,
      "price": price,
      "quantity": quantity
    })

  #Apply percentage discount to total
  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
      return
    
    discount_amount = self.total * (self.discount / 100)
    self.total -= discount_amount
    
    print(f"After the discount, the total comes to ${int(self.total)}.")

    #Remove last transaction
    self.previous_transactions.pop()
    self.items.pop()

  #Undo last transaction
  def void_last_transaction(self):
    if not self.previous_transactions:
      print("No transaction to void.")
      return
    
    last = self.previous_transactions.pop()
    self.total -= last["price"] * last["quantity"]
    self.items.pop()
