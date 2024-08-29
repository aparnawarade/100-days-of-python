"""
Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output
The highest score in the class is: 91

"""
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
#print(f"The highest score in the class is: {max(student_scores)}")
max_score = student_scores[0]
for score in student_scores:
  if score > max_score:
    max_score = score
print(f"The highest score in the class is: {max_score}")
