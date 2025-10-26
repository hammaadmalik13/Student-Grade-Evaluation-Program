
name = input("Name: ")
mark1 = float(input("Python Program: "))
mark2 = float(input("Data Mining and Analysis: "))
mark3 = float(input("Computational Thinking: "))
mark4 = float(input("Mathematics: "))
mark5 = float(input("Decision Making "))

average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n ---Final Result---")
print("Name:", name)
print("Average Marks :", round(average, 3))
print("Grade Obtained:", grade)
