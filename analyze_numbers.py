#Steve Cha, 002, 3/27/2019
"""
analyze.py (8 points)
=====
Write a program that determines whether a number is:

* odd
* prime
* abundant

Do this by writing three functions.

FUNCTION 1: is_odd
An odd number is a number that is not evenly divisible by 2.

1. Write a function that takes one argument, an int. If the number is odd,
   return True. Otherwise, return False. Call the function is_odd.

2. Modul is helpful for this function.

FUNCTION 2: is_prime
A prime number is a number that has no positive divisors other than 1 and
itself. 17 is a prime number because it is only divisible by 1 and 17. 9 is 
not a prime number (it's a composite) because it's divisible by 1, 3, and 9.

1.  Write a function that takes one argument, an int. If the number is prime,
    return True. Otherwise, return False. Call the function is_prime.  

2.  Implement your function by testing every number between 1 and the number
    itself (don't include 1 or the number). You can optionally make your
    algorithm more efficient by choosing a number lower than the number itself
    (of course, you'll have to put some thought into what the lower limit is).

3   How do you know if one number is divisible by another? Use one of the numeric 
    operations we've used in the past (we've seen it before for determining odd
    or even).

4.  Once you find a number that divides evenly into the original number, you 
    know that the original number is not prime, so you can safely return False. 
    However, how do you know when you should return True (that is, when do you
    know that you can safely say the number is prime)?

5.  Make sure to try your function with a few test cases (for example 3 and
    5 are prime, but 9 and 169 are composite).

    If you'd like to test it on other numbers:

    http://en.wikipedia.org/wiki/List_of_prime_numbers

FUNCTION 3: is_abundant
A number is abundant if the sum of its factors (excluding itself) is greater
than the actual number it self. For example, the number 12 is abundant because
its factors, 2, 3, 4, and 6 (excluindg itself) are greater than 12.

1.  Write a function that takes one argument, an int. If the number is
    abundant, return True. Otherwise, return False. Call the function
    is_abundant.  

2.  Using an accumulator might be helpfulfor this function.

5.  Make sure to try your function with a few test cases. See the wikipedia
    article: http://en.wikipedia.org/wiki/Abundant_number

Finally... your actual program should ask the user for a number, and then use
the function that you've defined above.

Example Interaction (everything after > is user input):
=====
Run 1:
-----
Please enter a number:
> 9
9 is odd
9 is not prime
9 is not abundant

Run 2:
-----
Please enter a number:
> 12
12 is not odd
12 is not prime
12 is abundant
"""
#imports math function
import math
#pick a number
integer = int(input("Pick a number\n>"))
#determines if integer is odd or not
def is_odd (integer):
    odd = integer % 2
    if odd == 1:
        return True
    if odd == 0:
        return False
#prints result
oe = is_odd(integer)
if oe == True:
    print(integer, "is odd")
else:
    print(integer, "is not odd")

#determines if integer is prime or not
def is_prime (integer):
    if integer == 1:
        return False
    if integer == 2:
        return True
    if integer & 2 == 0:
        return False
    root = math.sqrt(integer)
    x = 3
    while x <= root:
        if integer % x == 0:
            return False
        x += 2
    return True
#prints results
pc = is_prime(integer)
if pc == True:
    print(integer, "is prime")
else:
    print(integer, "is not prime")

#determines if integer is abundant or not
def is_abundant(integer):
    factorsum = 0
    for i in range(1, integer + 1):
        if integer % i == 0:
            factorsum += i
    if factorsum > integer:
        return True
    elif factorsum < integer:
        return False
#prints results
an = is_abundant(integer)
if an == True:
    print(integer, "is abundant")
else:
    print(integer, "is not abundant")
    
