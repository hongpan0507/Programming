import csv
import numpy as np

csv_file = open('./data/data.csv', 'w', newline='')   # create and open csv file for writing, no additional newline
csv_w = csv.writer(csv_file, delimiter=',')   # open csv file with csv writer

# column header
csv_w.writerow(['Freq(Hz)', 's21 unwrapped phase(Deg)'])


col1 = [1, 2, 3]
col2 = [4, 5, 6]
col = []
col.append(col1)
col.append(col2)
temp_row = []
for i in range(0, len(col[0])):
    for j in range(0, len(col)):
        temp_row.append(col[j][i])

    csv_w.writerow(temp_row)
    temp_row = []

# csv_file.close()
