RPiPySerialArduToCSV.py
Who has access
W
K
System properties
Type
Text
Size
1 KB
Storage used
1 KB
Location
PySerialArduToCSV
Owner
me
Modified
Oct 7, 2021 by me
Opened
4:13 PM by me
Created
Nov 9, 2021 with Google Drive Web
Add a description
Viewers can download
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:18:51 2020

@author: Nern
"""

import serial
import datetime
import time

#formatting the filename as the current date, hours and minute
currtimedate = str(datetime.datetime.now())
date = currtimedate.split()[0]
currtime = currtimedate.split()[1]
splittime = currtime.split(":")
hourmin = splittime[0] + splittime[1]
filename = "/home/pi/Desktop/"+date+"-"+hourmin+".csv"

import csv
csvfile = open(filename,'a+')
filewrite = csv.writer(csvfile, delimiter=',')
filewrite.writerow(['Date & Time','Mass(g)'])

deviceID = ['/dev/ttyACM0', '/dev/ttyACM1']
ser = serial.Serial(deviceID[0], 9600)  # change accordingly to your serial port

print(ser.name, "is opened") #for debugging check which port is actually used


while True:
    try:
        summa = 0
        avg = 0
        ser.flushInput()
        
        for i in range (5): 
            ser_bytes = ser.readline() # reads the bytes of the serial input
        #   pls decode the bytes
            decoded = ser_bytes.decode("utf-8")
            massval = float(decoded)
            summa = summa + massval
            
        avg = summa / (i+1)
        print(avg)
        filewrite.writerow([datetime.datetime.now(),avg])
        csvfile.flush()


    except Exception as e:
        print(e) #using the ctrl-c to break the operation
 
print("terminating")
csvfile.close()

