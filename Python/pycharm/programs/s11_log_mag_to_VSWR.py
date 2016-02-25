import csv
import matplotlib.pyplot as plot

# read csv file
file_r = open('0.csv', 'rb')   # open csv file
s11_read = csv.reader(file_r, delimiter=',')   # convert csv file to python reader object
file_w = open('0_modified.csv', 'wb')   # open csv file
s11_write = csv.writer(file_w, delimiter=',')   # convert csv file to python writer object

for row in s11_read:     # row carries all the row information
    if s11_read.line_num == 8:    # picks up the title
        s11_write.writerow(row)
    if s11_read.line_num >= 9:    # store real data that starts at line #9 into a new csv file
        if row[0] == 'END':     # check if row reaches the last one
            break
        print row[1]
        s11_write.writerow(row)

file_r.close()
file_w.close()
