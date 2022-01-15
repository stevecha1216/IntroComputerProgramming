"""
exercises.py (3 points)
=====
* these three exercises are from the end of Chapter 2 in "How to Think Like a 
  Computer Scientist"
  * http://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html#exercises
  * do problems #1, #2 and #7
"""

"""
How to Think Like a Computer Scientist - Chapter 2 

1. Take the sentence: All work and no play makes Jack a dull boy. Store each 
   word in a separate variable, then print out the sentence on one line using
   print.

(write this out as code outside of and below this comment)
=============================================================================
"""
variable1 = ("All")
variable2 = ("work")
variable3 = ("and")
variable4 = ("no")
variable5 = ("play")
variable6 = ("makes")
variable7 = ("Jack")
variable8 = ("a")
variable9 = ("dull")
variable10 = ("boy")

print(variable1, variable2, variable3, variable4, variable5,variable6,variable7,variable8,variable9,variable10 + ".")


"""
How to Think Like a Computer Scientist - Chapter 2 

2. Add parentheses to the expression 6 * 1 - 2 to change its value from 4 to 
   -6.

(write this out as code outside of and below this comment)
=============================================================================
"""
#(6*1-2)
print (6 * 1 - 2)

#(6*(1-2))
print(6 * (1 - 2))


"""
How to Think Like a Computer Scientist - Chapter 2 

7. You look at the clock and it is exactly 2pm. You set an alarm to go off in 
   51 hours. At what time does the alarm go off? (Hint: you could count on 
   your fingers, but this is not what we’re after. If you are tempted to count
   on your fingers, change the 51 to 5100.) 

   * Use an expression consisting of Python values and operators
   * Use a 24 hour clock ... so start off by thinking of 2pm as 14 (no need
     to add am or pm)  
   * Hint: consider using modulo

(write this out as code outside of and below this comment)
=============================================================================
"""
time = 14 #2pm
alarm_time = 51
hours_in_day = 24
print ((time + alarm_time)% hours_in_day)


"""
REMEMBER... Run this file; make sure there are no syntax errors
"""
