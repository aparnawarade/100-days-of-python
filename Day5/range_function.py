"""
You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:
i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
Also, we will constrain the inputs to only take numbers from 0 to a max of 1000."""
target = int(input("Enter a number between 0 and 1000"))  #
# 🚨 Do not change the code above ☝️

# Write your code here 👇
if target == 0 or target == 1:
  print(0)
sum = 0
for i in range(2, target + 1, 2):
  sum += i
print(sum)
