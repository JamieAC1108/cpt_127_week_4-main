#%%
'''

Below is a VERY simplistic example of how you can read a file in Python.

This is a very simple example and is not meant to be a complete solution.

Please run this to validate that you can read the file and see output.

'''


#%% Read File

with open('student_grades.csv','r') as f:

    for line in f.readlines ()[1:]:
        fields = line.replace('\n','').split(',')
        print(fields)

        id = fields[0]
        first_name = fields[1]
        last_name = fields[2]
        grade = int(fields[3])