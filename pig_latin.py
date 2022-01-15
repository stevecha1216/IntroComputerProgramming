#Steve Cha, 002, 4/3/2019
"""
pig_latin.py (6 points)
=====

Write a function called to_pig_latin that translates a word into pig latin. 

http://en.wikipedia.org/wiki/Pig_Latin

IPO for to_pig_latin function
-----
input (parameters): a string
processing: convert the string into pig latin
output (return value): a new string (in pig latin)

Our version of Pig Latin will follow these rules:
-----
* _IGNORE ANY STRING WITH NON-LETTER CHARACTERS_ (including spaces); it should
  just return the original string
* _THIS FUNCTION WILL NOT BREAK A STRING INTO SEPARATE WORDS_
* all letters automatically get converted to lowercase (just for implementation
  convenience)
* single letter words remain the same: "a" -> "a"
* any strings with non letter characters (including punctuation, numbers, white
  space) remain the same: "u mad bro" -> "u mad bro", "42" -> "42", "!" -> "!"
* empty string returns empty string: "" -> ""
* words that start with vowels just have "way" appended to them: "at" -> "atway"
* HINT - how to check for vowels? you can check if a character exists within a 
  string of all vowels
* words that start with sh, ch, th or qa have those two letters removed from 
  the beginning of the word, added to the end of the word, with "ay" added at 
  the end: "chillax" -> "illaxchay", "thimble" -> "imblethay"
* all other words (that start with a consonant, are greater than one letter in
  length, and only contain letters) will have the consonant taken away from 
  the front of the word, appended to the end of the word, with "ay" added to 
  the end: "yolo" -> "oloyay", "narwhal" -> "arwhalnay"
* write at least 4 assertions to test your program (use the conditions above as
  a guide)

Example:
-----
print(to_pig_latin(s))
# prints out...
"""

def to_pig_latin(word):
    length = int(len(word))
    #if single letter, returns the word
    if length == 1:
        return word
    #if empty string, returns empty string
    if word == "":
        return ""
    first = word[0]
    second = word[1]
    #if all characters are in alphabet
    if word.isalpha() == True:
        vowels = "aeuoi"
        consonants = "bcdfghjklmnpqrstvwxyz"
        #checks if first letter is vowel
        numvowels = vowels.count(first)
        #checks if first and second letters are consonants
        numconsonants1 = consonants.count(first)
        numconsonants2 = consonants.count(second)
        #converts to pig latin based on starting letters and returns the pig latin version of the word
        if numvowels > 0:
            end = "way"
            platin = word[0 : length] + end
            return platin
        if numconsonants1 > 0:
            end = "ay"
            if numconsonants2 > 0:
                platin = word[2 : length] + first + second + end
            elif numconsonants2 <= 0:
                platin = word[1 : length] + first + end
            return platin        
        if first == "q" and second == "a":
            end = "ay"
            platin = word[2 : length] + first + second + end
            return platin
#testing
print(to_pig_latin("hello"))
print(to_pig_latin("steve"))
print(to_pig_latin("spiderman"))
print(to_pig_latin("amplify"))

word = input("What word do you want me to translate?\n>")
print(to_pig_latin(word))
