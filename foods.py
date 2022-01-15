
"""
foods.py (5 points)
=====

Write a program that:

* asks the user for their three favorite vegetables.
* prints out every vegetable separated by commas, in the order entered
* prints out every vegetable again, in reverse order, each on a separate line
* prints out every vegetable again, in reverse order, each on a separate line 
  with an exclamation point at the end
* use print to do this
    * for now, do not use string concatenation to do this
    * specifically, use keyword arguments in the print function call (see 
      module #1 on formatting with print) to replicate the formatting below


Example Interaction
=====
Please enter your first favorite vegetable
> zucchini  
Please enter your second favorite vegetable
> cauliflower
Please enter your third favorite vegetable
> chocolate ice cream


zuccchini, cauliflower, chocolate ice cream

chocolate ice cream
cauliflower
zucchini

chocolate ice cream!
cauliflower!
zucchini!
"""

veggie1 = input("What is your favorite vegetable?\n")
veggie2 = input("What is your second favorite vegetable?\n")
veggie3 = input("What is your third favorite vegetable?\n")
print()

print("Now watch the veggie magic happen!")
print()

print(veggie1, veggie2, veggie3, sep=",")
print()

print(veggie3, veggie2, veggie1, sep= "\n")
print()

print(veggie3, veggie2, veggie1, sep="!\n", end="!")

