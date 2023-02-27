# Set working directory and import libraries
import pandas as pd
import numpy as np

# Create lists for codes and years to parse through
code_list = ['1000','1001','1002','1003','1004']
code_year = ['22','22','22','22','22']

# Loop through each code + year file combination
for code, year in zip(code_list, code_year):
    df = pd.read_csv("code" + code + year + ".csv", sep=",")
    lst = np.unique(np.hstack(df['id'].str.split(','))).tolist()
    arr_t = np.array(lst).T
    lst_t = np.array(lst).T.tolist()
    export = pd.DataFrame (lst_t, columns = ['id'])
    export['code'] = code
    export['year'] = '20'+year
    export.to_csv('code' + code + year + '_output.csv')
