import pandas as pd
import numpy as np
students = ['taha','bilal','owais','ali','vv']
roll = [212,253,245,300,600]

excel_file = pd.ExcelFile('bilal.xlsx') # Import the excel file in python environment
print(excel_file.sheet_names) #We can even see the sheet that we are working on using,

record = ['a']

# It take the data from sheet1 and pass it as it is to variable 'df'
n =0
for sheet in excel_file.sheet_names:
    df = excel_file.parse(sheet) #In order to load the sheet in the data frame, we can use,
    
    rec = pd.DataFrame()  # making record dataframe
    rec= df['names']
    record[n] = np.array(rec) # converting records to array
    record[n]=list(record[n]) # converting it to a list
    n +=1

print('Student\'s names in record:', record)



for rec in record:
    for student in students:
        if student in rec:
            print(student)
         






