#Steve Cha, Due 2/13,
"""
multiply.py (3 points)
=====
Write a program that:

* asks the user for a number
* prints out a table of that number multiplied by the first 7 prime numbers:  
  2, 3, 5, 7, 11, 13, 17
* it will format the output so that the original number and the prime number are
  left aligned
* the product is right aligned
  * when using format, don't change the width to align the product
  * keep the width constant
* __COMMENT YOUR SOURCE CODE__ by 
   * briefly describing parts of your program 
   * include your name, the date, and your class section at top of your file 
     (above everything else)

Example interaction (everything after > is user input):
-----
Give me a number
> 17
17 * 2             34
17 * 3             51
17 * 5             85
17 * 7            119
17 * 11           187
17 * 13           221
17 * 17           289
"""
#Asks for number
number = int(input("Please provide me with a number\n>"))
#spacing
print()
#number times each number, formatted so they are spaced well
print(format (str(number) + " * 2", "<20"), format(number *2, ">20"))
print(format (str(number) + " * 3", "<20"), format(number *3, ">20"))
print(format (str(number) + " * 5", "<20"), format(number *5, ">20"))
print(format (str(number) + " * 7", "<20"), format(number *7, ">20"))
print(format (str(number) + " * 11", "<20"), format(number *11, ">20"))
print(format (str(number) + " * 13", "<20"), format(number *13, ">20"))
print(format (str(number) + " * 17", "<20"), format(number *17, ">20"))
