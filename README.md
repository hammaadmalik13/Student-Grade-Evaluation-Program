# Student-Grade-Evaluation-Program
A Python program designed to evaluate a student's grade based on the marks obtained in three subjects. The program takes the student's name and marks as input, calculates the average marks, determines the grade based on the average, and displays the student's name, average marks, and grade.

Program Flow

1. The program prompts the user to enter the student's name and marks in three subjects.
2. The calculate_average function calculates the average marks by summing the marks in the three subjects and dividing by 3.
3. The determine_grade function determines the grade based on the average marks using the following criteria:
    - A+: average marks ≥ 90
    - A: 80 ≤ average marks < 90
    - B: 70 ≤ average marks < 80
    - C: 60 ≤ average marks < 70
    - D: 50 ≤ average marks < 60
    - F: average marks < 50
  
Example Use Case

1. Run the program and enter the student's name: John Doe
2. Enter the marks in three subjects:
    - Subject 1: 85
    - Subject 2: 90
    - Subject 3: 78
3. The program displays the student's name, average marks, and grade:
    - Student's Name: John Doe
    - Average Marks: 84.33
    - Grade: A
