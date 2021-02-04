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
import argparse

class SerialEmulator:
    
    def __init__(self,type,file,sample_time):
        self.sample_time = sample_time 
        self.type = type 
        self.file = file 
        self.master = None
        
    def write_file_to_pt(self):
        f = open(self.file, 'r') 
        Lines = f.readlines()
        for line in Lines:
            #print(line)
            #print('def')
            line1 = line + '\r'
            os.write(self.master,str.encode(line1))
            time.sleep(self.sample_time) 
        f.close()
    
    def emulate_device(self):
        """Start the testing"""
        self.master,self.slave = pty.openpty() #open the pseudoterminal
        #print("master fd %s"%self.master)
        #print("slave fd %s"%slave)
        print("The Pseduo device address: %s"%os.ttyname(self.slave))
        #print("master id %s"%os.ttyname(self.master))
        try:
            while True:
                self.write_file_to_pt()
                
        except KeyboardInterrupt:
            os.close(self.master)
            os.close(self.slave)
            print("Terminated")
            pass
    
    def start_emulator(self):
        self.emulate_device()
    
if __name__=='__main__':
    
    # Some argument parsing required
    # arguments : filepath,baudrate,parity bits, hardware control, 
    # data output rate etc.
    parser = argparse.ArgumentParser(description='Command line options for Serial emulator.\
                                     Press Ctrl-C to stop execution')
    parser.add_argument('--type','-t', default='gps', dest='sim_type',type=str,
                        metavar='gps or imu',choices=['gps','imu'],
                        help='select type of serial emulator')
    parser.add_argument('-f','--file', required=True, type=str, dest='file',
                    help='sum the integers (default: find the max)')
    parser.add_argument('-s','--sample_time', default = 1, type=int, dest='sample_time',
                    metavar='value',help='input sample time in seconds')
    args = parser.parse_args()
    se = SerialEmulator(args.sim_type,args.file,args.sample_time)
    se.start_emulator()