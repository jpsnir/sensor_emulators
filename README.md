1. Clone the repository
Python >= 2.7 tested

Dependencies: pyserial

Do pip install pyserial

Run the following
> python serial_emulator.py -h 

displays help options and gives you the options to run the script. 

> python serial_emulator.py --file file --sample_time time
  
  
file  is a .txt file which you want to send through a pseudo device, 
sample_time is a positive number from (0,inf). 
**Example Output:**

The Pseduo device address: /dev/pts/*9* 

In another terminal, run
> minicom -D /dev/pts/ <slave_id>
