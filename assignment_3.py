'''

For this assignment please do the following:

- Read in the student_grades.csv file

- calculate the average grade for the class

- for each student record calculate the difference between the student's grade and the average grade

- write the output to a new file called student_grade_differences.csv

'''
with open('student_grades.csv') as f:
    lines = f.readlines()

    if len(lines) > 0:
        grades = []

        for line in lines[1:]:
            row = line.split(',')
            grades.append(float(row[3].replace('\n','')))

        avg = sum(grades)/len(grades)

        differences = []

    with open('studentt_grade_differences.txt', 'w') as output_file:

        for i, grade in enumerate(grades):
            difference = grade - avg
            output_file.write(f'Student {i + 1}: Difference from Average = {difference: .2f}\n')