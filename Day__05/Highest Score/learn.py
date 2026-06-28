student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# INBUILT FUNCTION
total_scores = sum(student_scores)
print("Total Score:", total_scores)

# BY LOOP
sum=0
for score in student_scores:
    sum += score
print("Sum:", sum)

# MAX SCORE IN THE ARRAY
# inbuilt
print("Highest Score:", max(student_scores))

#loop
highest_score=0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print("Highest Score:", highest_score)