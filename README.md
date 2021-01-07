1. Clone the repository
Python 3.7 tested
Run the following

> python serial_emulator.py

> 
> master fd 3
slave fd 4
**slave id /dev/pts/28**
master id /dev/ptmx

In another terminal, run
> minicom -D /dev/pts/ <slave_id>
