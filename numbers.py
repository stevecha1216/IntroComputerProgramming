"""
numbers.py (5 points)
=====
Write a program that outputs the number in the thousands, hundreds, tens and 
ones places of a number. 

1. Ask the user for a number
2. Calculate the numbers in the thousands, hundreds, tens and ones places
3. Output each place
4. One soution is to use some numeric operators to determine each place 
   (maybe % and // may help)
5. You may have to calculate each place separately
6. Don't worry about input that's not a positive whole number below 10,000

Example Output - Everything after the greater than sign (>) is user input:

Please enter a number
> 256

0 thousands
2 hundreds
5 tens
6 ones
"""
print("Please provide a number")
number = int(input("What is your number?"))

ones = int(number%10)
tens = int(((number%100) - ones)/10)
hundreds = int(((number%1000)-(number%100))/100)
thousands = int((((number%10000)-(number%1000))/1000))

print(thousands, "thousands")
print(hundreds, "hundreds")
print(tens, "tens")
print(ones, "ones")
