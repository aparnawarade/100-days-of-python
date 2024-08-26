"""
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is *z*."
e.g.
name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5
L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3
Love Score = 53
Print: "Your score is 53."
"""
print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is their name? ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name=name1.lower()+name2.lower()
count_true=name.count("t")+name.count("r")+name.count("u")+name.count("e")
count_love=name.count("l")+name.count("o")+name.count("v")+name.count("e")
score=int(str(count_true)+str(count_love))
if 10>score  or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif 40<=score<=50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


