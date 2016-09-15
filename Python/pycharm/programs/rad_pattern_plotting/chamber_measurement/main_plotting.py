# Program Function:
#   read measured radiation pattern csv file
#   organize the data into [[frequency],[angle],[horizontal radiation[], vertical radiation[]]]
#   normalize radiation pattern data
#   plot data

import csv
from mod_norm_rad import norm_rad
from mod_plot import polar_plot
from mod_read_data import read_data
from matplotlib import pyplot as plot

# ***************************** CSV Simulated Data *****************************
# file1 = open('simulated_state_0_s11.csv', 'rb')  # open the file for reading
# sim_csv_s11_mag_state0 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
# *************************************************************************

# ***************************** CSV Measured Data *****************************
file1 = open('state0_horizontal_polCSV.csv', 'rb')  # open the file for reading
measured_csv_rad_state0 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('state1_horizontal_polCSV.csv', 'rb')  # open the file for reading
measured_csv_rad_state1 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('state2_horizontal_polCSV.csv', 'rb')  # open the file for reading
measured_csv_rad_state2 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('state3_horizontal_polCSV.csv', 'rb')  # open the file for reading
measured_csv_rad_state3 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('state4_horizontal_polCSV.csv', 'rb')  # open the file for reading
measured_csv_rad_state4 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('state5_horizontal_polCSV.csv', 'rb')  # open the file for reading
measured_csv_rad_state5 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('state6_horizontal_polCSV.csv', 'rb')  # open the file for reading
measured_csv_rad_state6 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
file1 = open('state7_horizontal_polCSV.csv', 'rb')  # open the file for reading
measured_csv_rad_state7 = csv.reader(file1, delimiter=',')   # convert cvs file to python list
# *************************************************************************

# extract information from csv and store in the following lists for plotting and processing
measured_rad_state0 = [[], [], [[], []]]    # [[frequency],[angle],[horizontal radiation[], vertical radiation[]]]
measured_rad_state1 = [[], [], [[], []]]    # [[frequency],[angle],[horizontal radiation[], vertical radiation[]]]
measured_rad_state2 = [[], [], [[], []]]    # [[frequency],[angle],[horizontal radiation[], vertical radiation[]]]
measured_rad_state3 = [[], [], [[], []]]    # [[frequency],[angle],[horizontal radiation[], vertical radiation[]]]
measured_rad_state4 = [[], [], [[], []]]    # [[frequency],[angle],[horizontal radiation[], vertical radiation[]]]
measured_rad_state5 = [[], [], [[], []]]    # [[frequency],[angle],[horizontal radiation[], vertical radiation[]]]
measured_rad_state6 = [[], [], [[], []]]    # [[frequency],[angle],[horizontal radiation[], vertical radiation[]]]
measured_rad_state7 = [[], [], [[], []]]    # [[frequency],[angle],[horizontal radiation[], vertical radiation[]]]

# ***************************** Simulated Data *****************************

# *************************************************************************

# ***************************** Measured Data *****************************
# for row in measured_csv_rad_state7:   # row contains the row data
#     print "line number = " + str(measured_csv_rad_state7.line_num)
#     print row   # print out all the info to check on the line numbers

# organize data
measured_rad_state0 = read_data(measured_csv_rad_state0, measured_rad_state0)
measured_rad_state1 = read_data(measured_csv_rad_state1, measured_rad_state1)
measured_rad_state2 = read_data(measured_csv_rad_state2, measured_rad_state2)
measured_rad_state3 = read_data(measured_csv_rad_state3, measured_rad_state3)
measured_rad_state4 = read_data(measured_csv_rad_state4, measured_rad_state4)
measured_rad_state5 = read_data(measured_csv_rad_state5, measured_rad_state5)
measured_rad_state6 = read_data(measured_csv_rad_state6, measured_rad_state6)
measured_rad_state7 = read_data(measured_csv_rad_state7, measured_rad_state7)

# find max and normalize
for i in range(0, len(measured_rad_state0[2][0])):
    measured_rad_state0[2][0][i], measured_rad_state0[2][1][i] = norm_rad(measured_rad_state0[2][0][i], measured_rad_state0[2][1][i])

for i in range(0, len(measured_rad_state1[2][0])):
    measured_rad_state1[2][0][i], measured_rad_state1[2][1][i] = norm_rad(measured_rad_state1[2][0][i], measured_rad_state1[2][1][i])

for i in range(0, len(measured_rad_state2[2][0])):
    measured_rad_state2[2][0][i], measured_rad_state2[2][1][i] = norm_rad(measured_rad_state2[2][0][i], measured_rad_state2[2][1][i])

for i in range(0, len(measured_rad_state3[2][0])):
    measured_rad_state3[2][0][i], measured_rad_state3[2][1][i] = norm_rad(measured_rad_state3[2][0][i], measured_rad_state3[2][1][i])

for i in range(0, len(measured_rad_state4[2][0])):
    measured_rad_state4[2][0][i], measured_rad_state4[2][1][i] = norm_rad(measured_rad_state4[2][0][i], measured_rad_state4[2][1][i])

for i in range(0, len(measured_rad_state5[2][0])):
    measured_rad_state5[2][0][i], measured_rad_state5[2][1][i] = norm_rad(measured_rad_state5[2][0][i], measured_rad_state5[2][1][i])

for i in range(0, len(measured_rad_state6[2][0])):
    measured_rad_state6[2][0][i], measured_rad_state6[2][1][i] = norm_rad(measured_rad_state6[2][0][i], measured_rad_state6[2][1][i])

for i in range(0, len(measured_rad_state7[2][0])):
    measured_rad_state7[2][0][i], measured_rad_state7[2][1][i] = norm_rad(measured_rad_state7[2][0][i], measured_rad_state7[2][1][i])
# *************************************************************************

# ***************************** plotting **********************************
n = 0
n = polar_plot(n, "State 0", measured_rad_state0)
n = polar_plot(n, "State 1", measured_rad_state1)
n = polar_plot(n, "State 2", measured_rad_state2)
n = polar_plot(n, "State 3", measured_rad_state3)
n = polar_plot(n, "State 4", measured_rad_state4)
n = polar_plot(n, "State 5", measured_rad_state5)
n = polar_plot(n, "State 6", measured_rad_state6)
n = polar_plot(n, "State 7", measured_rad_state7)
plot.show()
# *************************************************************************

file1.close()
