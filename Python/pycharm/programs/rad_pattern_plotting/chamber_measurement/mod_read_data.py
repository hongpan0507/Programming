from math import pi


# data format = [[frequency],[angle],[horizontal radiation[], vertical radiation[]]]
def read_data(csv_read, data):
    for row in csv_read:   # row contains the row data
        # horizontal pol
        if row[0] == 'Horizontal' and row[1] == 'Angle  (\xb0)':
            # angle
            for i in range(2, len(row)-1):  # subtract by 1 because of the starting point
                data[1].append(float(row[i])/180*pi)  # angle; convert from degree to rad
    
            csv_read.next()  # skip this row
            temp_row = csv_read.next()
            while temp_row[1] != '':
                temp = []
                data[0].append(float(temp_row[1]))      # frequency
                for i in range(2, len(temp_row)-1):   # subtract by 1 because of the starting point
                    temp.append(float(temp_row[i]))      # raw power; dBm
                data[2][0].append(temp)      # raw power; dBm
                temp_row = csv_read.next()
    
        # vertical pol
        if row[0] == 'Vertical' and row[1] == 'Angle  (\xb0)':
            csv_read.next()  # skip this row
            temp_row = csv_read.next()
            while temp_row[1] != '':
                temp = []
                data[0].append(float(temp_row[1]))      # frequency
                for i in range(2, len(temp_row)-1):   # subtract by 1 because of the starting point
                    temp.append(float(temp_row[i]))      # raw power; dBm
                data[2][1].append(temp)      # raw power; dBm
                temp_row = csv_read.next()

    return data
