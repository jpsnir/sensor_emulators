# -*- coding: utf-8 -*-
"""
Spyder Editor
 create pseudo serial ports using pseudoterminals
 
Author: Jagatpreet Singh
Created on: Jan 7, 2021
"""

import os, pty
from serial import Serial
import threading
import time 

sample_time = 1
new_line = "\n"

def read_file(master):
    f = open('gps-data.txt', 'r') 
    Lines = f.readlines()
    for line in Lines:
        #print(line)
        #print('def')
        line1 = line + '\r'
        os.write(master,str.encode(line1))
        time.sleep(sample_time) 
    f.close()
'''
def read_file(master):
    with open('test.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            os.write(master,str.encode(line.rstrip('\n')))
            os.write(master,str.encode(new_line.rstrip('\n')))
            line = reader.readline()
            time.sleep(sample_time)
            
    #print("Reads input file to be sent on pseudo serial port device")
'''
    
def test_serial():
    """Start the testing"""
    master,slave = pty.openpty() #open the pseudoterminal
    s_name = os.ttyname(slave) #translate the slave fd to a filename
    ser = Serial(s_name, 9600, timeout=1)
    print("master fd %s"%master)
    print("slave fd %s"%slave)
    print("slave id %s"%s_name)
    print("master id %s"%os.ttyname(master))
    
    #create a separate thread that listens on the master device for commands

    count = 0
    try:
        while True:
            read_file(master)
            #read_file() goes here
            #os.write(master,str.encode('count %d\r\n'%count)) 
            #count += 1
            
            
    except KeyboardInterrupt:
        print("Terminated")
        pass
    #open a pySerial connection to the slave
    

if __name__=='__main__':
    
    # Some argument parsing required
    # arguments : filepath,baudrate,parity bits, hardware control, 
    # data output rate etc.
    
    test_serial()