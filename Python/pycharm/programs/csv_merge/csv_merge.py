# Python 3.5
# Merge multiple cvs files and eliminate duplicate; Duplicate quantities are added

import glob
import csv
import os

''' merge all the items with duplicates '''
BOM_list = []  # place holder for data from csv file
record = 0  # use to tag an item after an item has been merged with another item with the same part number
            # 0 == not have been merged; 1 == merged
path = glob.glob("*.csv")   # read cvs file names
for i in range(len(path)):  # going through each csv file
    csv_file_r = open(path[i], 'r', newline='')   # open the file for reading
    csv_read = csv.DictReader(csv_file_r)   # read as csv file
    for row in csv_read:    # going through rows in the csv file
        row['record'] = 0   # assign each row with a record of "0" at the beginning
        row['file_ID'] = i  # add file ID for debugging; the source of csv file where the data comes from
        BOM_list.append(row)    # merge into a list
    csv_file_r.close()

print("total number of items in the list before sort: " + str(len(BOM_list)))  # debug

''' eliminate the duplicates and add duplicate quantity together '''
updated_BOM = []  # place holder for data from csv file
count = 0   # updated_BOM list index
for i in range(len(BOM_list)):  # going through each item in the list
    if BOM_list[i]['record'] == 0:  # if the item has not been merged
        BOM_list[i]['record'] = 1  # mark that the item has been compared
        # print(BOM_list[i])  # debug
        updated_BOM.append(BOM_list[i])  # add to a updated BOM
        for j in range(len(BOM_list)):  # going through each item in the list
            if BOM_list[j]['record'] == 0:  # if the item has not been merged
                if i != j:  # do not compare an item to itself
                    if BOM_list[i]['PART NUMBER'] == BOM_list[j]['PART NUMBER']:    # merge the items with the same part number
                        BOM_list[j]['record'] = 1  # mark that the item has been merged
                        updated_BOM[count]['QTY.'] = int(BOM_list[i]['QTY.']) + int(BOM_list[j]['QTY.']) # update quantity after merge
                        # print(BOM_list[j])  # debug
        count += 1  # keep track of updated_BOM index

print("total number of items in the list after merge: " + str(len(updated_BOM)))  # debug

''' remove unnecessary keys in the dict '''
for i in range(len(updated_BOM)):
    updated_BOM[i].pop('record')
    updated_BOM[i].pop('file_ID')
    updated_BOM[i].pop('ITEM NO.')
    # print(updated_BOM[i])

''' output to a csv file '''
file_name = './updated_BOM/updated_BOM.csv'
os.makedirs(os.path.dirname(file_name), exist_ok=True)
csv_file_w = open('./updated_BOM/updated_BOM.csv', 'w', newline='')   # open file for writing
field_name = updated_BOM[0].keys()  # extract the keys as the field name
csv_write = csv.DictWriter(csv_file_w, fieldnames=field_name, delimiter=',')    # set csv file parameter
csv_write.writeheader()     # write the headers first
for i in range(len(updated_BOM)):
    csv_write.writerow(updated_BOM[i])
csv_file_w.close()

# todo
# fixme
