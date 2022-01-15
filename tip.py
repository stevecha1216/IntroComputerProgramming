"""
tip.py (6 points)
=====
Create a tip calculator.

1. Print out a nice welcome banner!
2. The program should ask the following:
   a. How many people?	
   b. How much did it cost?
   c. If there are less 6 people, ask: How was the service?  
   d. The values that the service can be are: terrible, poor, ok, good, great
3. If the number of people are greater than or equal to 6, the tip should 
   always be 20%, regardless of service (service should not be asked for if 
   there are greater than 6 people anyway) 
4. Otherwise (less than six people), calculate the tip using the following 
   table:
   * terrible = no tip (0%)
   * poor - 10%
   * ok - 15%
   * good - 20%
   * great - 25%
   * any other input - default to 20% and output a message saying that the
     default tip value will be used
5. Output the calculated tip.
6. Format the number calculated so that there are two decimal places and a
   dollar sign
   
__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name, the date, and your class section at the top of your
  file (above these instructions)

Example Output (consider text after the ">" user input):

Run 1: 
-----
                    ~~~~~~~
                /// WELCOME \\\
                    ~~~~~~~
 Perhaps I can help you calculate $$$ for yr tip! 

How many people? > 2
How much did it cost? > 25
How was the service (terrible, poor, ok, good, great)? > great
You should probably tip $6.25!

 
Run 2: 
-----
                    ~~~~~~~
                /// WELCOME \\\
                    ~~~~~~~
 Perhaps I can help you calculate $$$ for yr tip! 

How many people? > 4
How much did it cost? > 70
How was the service (terrible, poor, ok, good, great)? > meh
Couldn't understand meh service; using default 20 percent.
You should probably tip $14.00!

Run 3: 
-----
                    ~~~~~~~
                /// WELCOME \\\
                    ~~~~~~~
 Perhaps I can help you calculate $$$ for yr tip! 

How many people? > 200
How much did it cost? > 950
You should probably tip $190.00!
"""
#Banner
print("     ^^^^^^^     ")
print("  // Welcome \\\  ")
print("  \\\         //  ")
print("=" *10)
print("Perhaps I can help you calculate how much tip you should give!")
#Asks for number or people and the total cost
numppl = int(input("How many people?\n>"))
cost = int(input("How much did it cost?\n>"))
#If more than 5 ppl, 20 percent tip. Calculates tip
if numppl >= 6:
    print("You should give 20% tip. Let me calculate that for you.")
    print("You should give", "$" + format((cost * .2), ".2f"), "as tip")
#If less than 6 people, asks for service quality and calculates tip based on that
elif numppl < 6 and numppl > 0:
    quality = input("How was the service? (terrible, poor, ok, good, great) \n>")
    if quality == "terrible":
        percenttip = 0
    elif quality == "poor":
        percenttip = .10
    elif quality == "ok":
        percenttip = .15
    elif quality == "good":
        percenttip = .20
    elif quality == "great":
        percenttip = .25
    #If neither, default tip is 20 percent.
    else:
        percenttip = .20
        print("I did not recognize your response. The default tip rate is 20%.")
    tip = percenttip * cost
    print ("You should give", "$" + format(tip,".2f"), "as tip")
    
