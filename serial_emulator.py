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
    
    def __init__(self,file,sample_time):
        self.sample_time = sample_time  
        self.file = file 
        self.master = None
        
    def write_file_to_pt(self):
        f = open(self.file, 'r') 
        Lines = f.readlines()
        for line in Lines:
            line1 = line + '\r'
            os.write(self.master,str.encode(line1))
            time.sleep(self.sample_time) 
        f.close()
    
    def emulate_device(self):
        """Start the emulator"""
        self.master,self.slave = pty.openpty() #open the pseudoterminal
        print("The Pseudo device address: %s"%os.ttyname(self.slave))
        try:
            while True:
                self.write_file_to_pt()
                
        except KeyboardInterrupt:
            self.stop_simulator()
            pass
    
    def start_emulator(self):
        self.emulate_device()

    def stop_simulator(self):
        os.close(self.master)
        os.close(self.slave)
        print("Terminated")
        
    
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Command line options for Serial emulator.\
                                     Press Ctrl-C to stop execution')
    parser.add_argument('-f','--file', required=True, type=str, dest='file',
                    help='data file to simulate device')
    parser.add_argument('-s','--sample_time', default = 1, type=float, dest='sample_time',
                    metavar='value',help='input sample time in seconds')
    
    args = parser.parse_args()
    if (args.sample_time <= 0):
        print("sample time must be positive.Setting it to default 1 second")
        args.sample_time = 1
    se = SerialEmulator(args.file,args.sample_time)
    se.start_emulator()
