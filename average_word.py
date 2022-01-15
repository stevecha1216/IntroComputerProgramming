"""
average_word.py - 7 points
=====
Write a program that asks the user for words... and prints out the longest
word, the shortest word, and the average length of all of the words entered.

* Generate a random number between 3 and 6, inclusive - this will determine
  how many words to ask for.
* Say: "I'll need [number] words:"
* Proceed to ask for each word, one at a time: "Word #[number] please!"
* At the end, your program should print out:
    * the longest word (the most recently entered longest if there is a tie)
    * the shortest word (the most recently entered shortest if there is a tie)
    * the average length of all of the words
    * if all of the words are the same, then the longest and shortest word
      should be the same!
* comment your code (name, date and section on top, along with appropriate 
  comments in the body of your program)

Hint 1: what data do you need to keep track of in order to meet the
        requirements above?
Hint 2: how can you get the first word entered to be the longest and shortest?
        would it be helpful to do that?
Hint 3: sometimes intializing to an empty string, "", is useful
Hint 4: the empty string, "", has a length of 0
Hint 5: thankfully, words can't be a negative length!
Hint 6: YOU DON'T HAVE TO STORE ALL THE WORDS to determine which one is the
        longest and the shortest... think about the minimum you'd need to
        keep track of...

Example output below; everything after a greater than sign (>) is user input.

Run 1:
-----
I'll need 4 words:
Word #1 please!
> wow
Word #2 please!
> oh
Word #3 please!
> amazing
Word #4 please!
> program
Shortest: oh
Longest: program
Average Length: 4.75

Run 2:
-----
I'll need 3 words:
Word #1 please!
> hi
Word #2 please!
> hi
Word #3 please!
> hi
Shortest: hi
Longest: hi
Average Length: 2.0
"""
#Generates random number of words to provide
import random
min = 3
max = 6
numwords = random.randint (min, max)
print("Please provide", numwords, "words")

#Asks for the words and finds the lengths of them
word1 = input("What is word 1?\n>")
word2 = input("What is word 2?\n>")
word3 = input("What is word 3?\n>")
length1 = len(word1)
length2 = len(word2)
length3 = len(word3)

if numwords <= 3:
    word4 = ""
    word5 = ""
    word6 = ""
    length4 = 0
    length5 = 0
    length6 = 0
    
if numwords > 3:
    word4 = input("What is word 4?\n>")
    length4 = len(word4)
    length5 = 0
    length6 = 0
    if numwords > 4:
        word5 = input("What is word 5?\n>")
        length5 = len(word5)
        length6 = 0
        if numwords > 5:
            word6 = input("What is word 6?\n>")
            length6 = len(word6)

for i in [length6, length5, length4, length3, length2, length1]:
    if i == length1:
        if i >= length2 and i >= length3 and i >= length4 and i >= length5 and i >= length6:
            longest = word1
    if i == length2:
        if i >= length1 and i >= length3 and i >= length4 and i >= length5 and i >= length6:
            longest = word2
    if i == length3:
        if i >= length1 and i >= length2 and i >= length4 and i >= length5 and i >= length6:
            longest = word3
    if i == length4:
        if i >= length1 and i >= length2 and i >= length3 and i >= length5 and i >= length6:
            longest = word4
    if i == length5:
        if i >= length1 and i >= length2 and i >= length3 and i >= length4 and i >= length6:
            longest = word5
    if i == length6:
        if i >= length1 and i >= length2 and i >= length3 and i >= length4 and i >= length5:
            longest = word6
print("The longest word is:", longest)

for i in [length6, length5, length4, length3, length2, length1]:
    if i == length1:
        if i <= length2 and i <= length3 and i <= length4 and i <= length5 and i <= length6:
            shortest = word1
    if i == length2:
        if i <= length1 and i <= length3 and i <= length4 and i <= length5 and i <= length6:
            shortest = word2
    if i == length3:
        if i <= length1 and i <= length2 and i <= length4 and i <= length5 and i <= length6:
            shortest = word3
    if i == length4:
        if i <= length1 and i <= length2 and i <= length3 and i <= length5 and i <= length6:
            shortest = word4
    if i == length5:
        if i <= length1 and i <= length2 and i <= length3 and i <= length4 and i <= length6:
            shortest = word5
    if i == length6:
        if i <= length1 and i <= length2 and i <= length3 and i <= length4 and i <= length5:
            shortest = word6
print("The shortest word is:", shortest)

total = 0
for i in (length1, length2, length3, length4, length5, length6):
    total += i
average = (int(total) / int(numwords))
print("The average number of letters is:", int(average))

