1. Clone the repository
Python >= 2.7 tested

Dependencies: pyserial

Do pip install pyserial

Run the following

> python serial_emulator.py --type gps --file gps-data.txt --sample_time 1

**Example Output:**

The Pseduo device address: /dev/pts/*9* 

In another terminal, run
> minicom -D /dev/pts/ <slave_id>
