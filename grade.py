#Steve Cha, Due 2/20/2019, 002

"""
grade.py - 3 points
=====
Translate a numeric grade to a letter grade.
1. Ask the user for a numeric grade.
2. Use the table below to calculate the corresponding letter:
    90-100 - A
    80-89  - B
    70-79  - C
    60-69  - D
     0-59  - F
3. Print out both the number and letter grade.
4. If the value is not numeric, allow the error to happen.
5. However, if the number is not within the ranges specified in the table, output:
    "Could not translate %s into a letter grade" where %s is the numeric grade"

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name, the date, and your class section at the top of your
  file (above these instructions)

Example Output (consider text after the ">" user input):

Run 1:
-----
What grade did you get?
> 59
Number Grade: 59
Letter Grade: F

Run 2:
-----
What grade did you get?
> 89
Number Grade: 89
Letter Grade: B

Run 3:
-----
What grade did you get?
> 90
Number Grade: 90
Letter Grade: A

Run 4:
-----
What grade did you get?
> -12
Couldn't translate -12 into a letter grade

"""


#ask for number grade
grade = int(input("What numeric grade did you get?\n>"))

#prints grades according to number provided
if grade >= 90 and grade <=100:
    print("Number Grade:", grade)
    print("Letter Grade: A")
elif grade >= 80 and grade <=89:
    print ("Number Grade::", grade)
    print("Letter Grade: B")
elif grade >= 70 and grade <=79:
    print("Number Grade:", grade)
    print("Letter Grade: C")
elif grade >= 60 and grade <=69:
    print ("Number Grade::", grade)
    print("Letter Grade: D")
elif grade >= 0 and grade <=59:
    print("Number Grade::", grade)
    print("Letter Grade: F")
else:
    print("Couldn't translate", grade, "into a letter grade")


