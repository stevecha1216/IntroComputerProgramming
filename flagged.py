"""
flagged.py - 7 points
=====
Create a program that generates a pattern for a flag.

* ask the user for a width of the flag
    * the width should be greater than 0
    * if it isn't, ask again until the user enters a valid value
* then... ask the user for a character
    * the character can be any character except empty string
    * it can even be multiple characters!
    * if it's an empty string, ask again until the user enters a valid 
      character
* construct a flag based on the input (notice the relationship between the
  width and the number of times the character appears horizontally below)
    * hint: string format, string repetition, and/or len may help
    * hint: the spaces in the interior must take the number of characters
      in the "character" input into account!
* comment your code (name, date and section on top, along with appropriate 
  comments in the body of your program)

Run 1 (invalid width, ask again):
-----
Hi, I'm flaggy the flagmaker. Let's make a flag.
What's the width of your flag?
> -1
Let's try that again, but this time with something less negative.
What's the width of your flag?
...

Run 2 (invalid character, empty response, ask again):
-----
Hi, I'm flaggy the flagmaker. Let's make a flag.
What's the width of your flag?
> 5
What character(s) do you want to use?
>
Let's try that again, but this time with maybe more character(s).
What character(s) do you want to use?
>

Run 3 (money flag!)
-----
Hi, I'm flaggy the flagmaker. Let's make a flag.
What's the width of your flag?
> 5
What character(s) do you want to use?
> $
$$$$$
 $$$$
  $$$
   $$
    $
   $$
  $$$
 $$$$
$$$$$

Run 3 (less money flag!)
-----
Hi, I'm flaggy the flagmaker. Let's make a flag.
What's the width of your flag?
> 4
What character(s) do you want to use?
> $
$$$$
 $$$
  $$
   $
  $$
 $$$
$$$$

Run 4 (ugh, even less money flag!)
-----
Hi, I'm flaggy the flagmaker. Let's make a flag.
What's the width of your flag?
> 1
What character(s) do you want to use?
> $
$

Run 5 (character has multiple characters in it)
-----
Hi, I'm flaggy the flagmaker. Let's make a flag.
What's the width of your flag?
> 3
What character(s) do you want to use?
> --o
--o--o--o
   --o--o
      --o
   --o--o
--o--o--o
"""

#Let's make a flag
print("Hi! I'm flaggy the flagmaker. Let's make a flag.")

#Asks for width, if invalid, asks again
x = 0
while x == 0:
    width = int(input("What width would you like the flag to be?\n"))
    if width > 0:
        x = 1
    else:
        x = 0
        print("I need a number greater than 0")
#Tells width
print("Your width is:", width)

#Asks for character. If empty string, repeatss. If valid, prints character
y = 0
while y == 0:
    character = input("Please provide a character. It can even be multiple characters\n>")
    if character == "":
        print("Invalid Character. Try again.")
        y = 0
    else:
        print("Cool. Your character is:", character)
        y = 1

#Prints out flag
characterlength = int(len(character))
print("|" + ((("=" * characterlength) + "=") * (width)) + "|")
for i in range(width, 1, -1):
    print(("|" + (" " * characterlength * (width - i)) + (" " * (width - i)) + (" " + str(character)) * i) + "|")
for i in range(1, width +1 , 1):
    print(("|" + (" " * characterlength * (width - i)) + (" " * (width - i)) + (" " + str(character)) * i) + "|")
print("|" + ((("=" * characterlength) + "=") * (width)) + "|")
    

