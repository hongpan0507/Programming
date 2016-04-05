import csv

file1_r = open('reflect_s11_discrete_RI_no_deembedding.csv', 'rb')  # open the file for reading
# file1_r = open('TRL_Reflect_S11_ReIm.csv', 'rb')  # open the file for reading; ECEN452 model
s11_r = csv.DictReader(file1_r, delimiter=',')   # convert cvs file to python list
file1_w = open('reflect_s11_discrete_no_freq.csv', 'wb')   # open the file for writing
s11_w = csv.writer(file1_w, delimiter=',')   # convert cvs file to python list
file2_w = open('reflect_s11_weight.csv', 'wb')   # open the file for writing
s11_w_w = csv.writer(file2_w, delimiter=',')   # convert cvs file to python list

for row in s11_r:
    row_temp = [row['re(S(1,1)) []'], row['im(S(1,1)) []']]
    s11_w.writerow(row_temp)
    s11_w_w.writerow('1')

file1_r.close()
file1_w.close()
file2_w.close()
