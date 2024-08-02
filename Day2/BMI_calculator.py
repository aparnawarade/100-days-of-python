"""
1.75
80
means: weight = 80 and height = 1.75

Example Output 1
26
Since: 80 ÷ (1.75 x 1.75) = 26.122448979591837
"""

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
weight_f=float(weight)
height_f=float(height)**2
print(round(weight_f/height_f))
