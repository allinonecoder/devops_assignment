#score is float beacuse score can be 10.5 or 90.5.
score = float(input("Enter your score (0 to 100): "))
# as per condition if score is 90+ = A elseif score is between 80-89 then the >=80 will cover that case same for other condition and last fail F
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(grade)
