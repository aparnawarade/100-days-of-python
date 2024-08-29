"""
Example input
[156, 178, 165, 171, 187]

Example Output 1
total height = 857
number of students = 5
average height = 171
"""
# Input a Python list of student heights
student_heights = [180, 124, 165, 173, 189, 169, 146]
# 🚨 Don't change the code above 👆
total_sum=sum(student_heights)
total_students=len(student_heights)
# Write your code below this row 👇
print(f"total height = {total_sum}")
print(f"number of students = {total_students}")
print(f"average height = {round(total_sum/total_students)}")



