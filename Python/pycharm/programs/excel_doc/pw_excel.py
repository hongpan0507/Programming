from xlrd import *
import win32com.client
import csv
import sys

xlApp = win32com.client.Dispatch("Excel.Application")
print "Excel library version:", xlApp.Version
filename = 'test_no_pw.xlsx'
# xlwb = xlApp.Workbooks.Open(filename)

print 'none'