#Steve Cha, Due 2/13, 
"""
change_puhleese.py (15 points)
=====
You're the manager of a tiny boutique that sells Python related gifts and 
knick-knacks (like plush Python stuffed animals, Guido Van Rossum bobble head
dolls, etc. ). Unfortunately, you don't have any paper bills on hand, you only 
have coins! 

To help you calculate change, you reprogram you cash register to print out the 
exact change that's needed, broken down by quarters, dimes, nickels and pennies.

Here's what your program should do:

1. Ask the cashier for information regarding the items purchased. It will 
   assume that everyone buys exactly three items (!?). For every item:
   a. ask for name of the item
   b. ask for the price (assume that users will always enter a number with a 
      decimal point)
   c. ask for quantity (assume that users will always enter a whole number)
2. Ask the cashier for how much the user paid. Assume that the amount paid
   is at least as much as the total owed (including sales tax)
3. Print out a receipt that contains the following information:
   a. name, price, quantity and total cost per item purchased
   b. the total cost of all of the items
   c. the sales tax based on the cost of all of the items - sales tax in the
      city is 8.875%
   d. the total amount owed, including sales tax
   e. the total amount paid
   f. the change owed, followed by a break down of how many quarters, dimes, 
      nickels and pennies will be given back
      * it will always print out the number of coins for each denomination, 
        even if the quantity is 0
   g. __IT IS OK IF SOME OF YOUR CALCULATIONS ARE OFF BY 1 CENT__
4. The receipt should be in the following format:
   a. the width of the receipt is 30 characters long total
   b. it has a center aligned title: PREMIER PYTHON PLAZA RECEIPT
   c. followed by a line created by equal signs that's 30 characters long (===)
      * __DO NOT TYPE OUT__ 30 ='s ... use what we learned about Python types,
        operators, etc. to do this
   d. print out the costs per item...
   e. print out another line created by equal signs
   f. print out the calculations for total item cost, sales tax, etc.
   g. print out another line created by equal signs
   h. print out the number of quarters, dimes, etc.
   i. "headings" in a line are left justified: item name x quantity ... cost
   j. prices / costs:
      * are right justified
      * have a dollar sign
      * have two decimal places
      * hint: you may have to use format more than once to get the decimal
        places... but then you'll need to add a dollar and format again!
   k. assume that all item names and costs are less than 30 characters long
   l. see the sample interaction below
      * everything after the > (greater than sign) is user input
      * the receipt is at the end
      * __YOUR OUTPUT SHOULD MATCH THE OUTPUT BELOW!__
5. __COMMENT YOUR SOURCE CODE__ by 
   a. briefly describing sections of your program (for example "# calculates the number of quarters, dimes, nickels and pennies" could go above the part of your code that runs those calculations). 
   b. include your name, the date, and your class section at top of your file (above everything else)

What is the name of the first item?
> Guido Van Rossum Bobble Head
How much does the first item cost?
> 10
How many are being purchased?
> 3
What is the name of the second item?
> Python Stuffed Animal
How much does the second item cost?
> 29.99
How many are being purchased?
> 1
What is the name of the third item?
> Hello World T-Shirt
How much does the third item cost?
> 12.50
How many are being purchased?
> 3
How much was paid?
> 150.03
....
4388
175
<class 'int'>
                          PREMIER PYTHON PLAZA RECEIPT
================================================================================
3 x Guido Van Rossum Bobble Head                                          $30.00
1 x Python Stuffed Animal                                                 $29.99
3 x Hello World T-Shirt                                                   $37.50
================================================================================
TOTAL COST OF ITEMS                                                       $97.49
SALES TAX                                                                  $8.65
AMOUNT OWED                                                              $106.14
AMOUNT PAID                                                              $150.03
CHANGE                                                                    $43.89
================================================================================
CHANGE:
175 x quarters
1 x dimes
0 x nickels
4 x pennies
"""





#Asks for items, prices, quantity
item1 = input("What is your first item?\n>")
item1price = float(input("What is the price of " +item1 + "?\n>"))
quantity1 = int(input("How many of " + item1 + " did you buy?\n>"))
item2 = input("What is your second item?\n>")
item2price = float(input("What is the price of " + item2 + "?\n>"))
quantity2 = int(input("How many of " + item2 + " did you buy?\n>"))
item3 = input("What is your third item?\n>")
item3price = float(input("What is the price of " + item3 + "?\n>"))
quantity3 = int(input("How many of " + item3 + " did you buy?\n>"))
#Asks for total amount paid
amountpaid = float(input("How much did you pay in total?\n>"))
#Calculates the total prices for each item
item1totalprice = item1price * quantity1
item2totalprice = item2price * quantity2
item3totalprice = item3price * quantity3
#Calculates the total price
totalprice = item1totalprice + item2totalprice + item3totalprice
salestax = totalprice * 0.08875
amountowed = totalprice + salestax
#Calculates the change user will receive
change = amountpaid - amountowed

#spacing purposes
print()
print()

#Receipt start
print("Here is your receipt!")
#Organizational spacing
print("=" * 40)
#Prints the item, its quantity, and the prices
print(format(str(quantity1) + " x " + str(item1), '<30'), format("$" + format(item1totalprice, '.2f'), '<30'))
print(format(str(quantity2) + " x " + str(item2), '<30'), format("$" + format(item2totalprice, '.2f'), '<30'))
print(format(str(quantity3) + " x " + str(item3), '<30'), format("$" + format(item3totalprice, '.2f'), '<30'))
#Organizational Spacing
print("=" * 40)
#Prints the total cost, tax, amoutn owed, amount paid, and change
print(format("TOTAL COST OF ITEMS", '<30'), format("$" + format(totalprice, '.2f'), '<30'))
print(format("SALES TAX", '<30'), format("$" + format(salestax, '.2f'), '<30'))
print(format("AMOUNT OWED", '<30'), format("$" + format(amountowed, '.2f'), '<30'))
print(format("AMOUNT PAID", '<30'), format("$" + format(amountpaid, '.2f'), '<30'))
print(format("CHANGE", '<30'), format("$" + format(change, '.2f'), '<30'))
#Organizational Spacing
print("=" * 40)
#Calculates how many quarters you will get
quarters = int(change / .25)
print("CHANGE:")
print("Quarters x " + str(quarters))
#Calculates how many dimes you will get
dimes = int((change % .25)/.10)
print("Dimes x " + str(dimes))
#Calculates how many nickels you will get
nickels = int(((change % .25) % .10) / .05)
print("Nickels x " + str(nickels))
#Calculates how many pennies you will get
pennies = float((((change % .25) %.10) %.05) / .01)
print("Pennies x " + str(int(pennies)))
