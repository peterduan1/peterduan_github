
""" Sorry, don't have time to finish python script! """

import snowflake.connector
import csv
import os

with open(r'C:\mydirectory\netflix_titles.csv', 'r') as originalfile:
    reader = csv.reader(f)
    headers = next(reader)
    num_new_file=3
    
    basefilename= os.path.splitext(originalfile)[0]
    newfilename=basefilename
    
    for x in range(num_new_file):
        newfilename=newfilename+x+'.csv'
        with open(newfilename, 'w', newline='') as f:
         writer = csv.writer(f)
         writer.writerow(headers)
         