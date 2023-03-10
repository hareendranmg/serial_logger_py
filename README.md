# Serial Data Logger

### Prerequisite
```pip install pyserial```


This script allows the user to select a serial port and read data from it continuously, while also logging the data to a file with timestamps.
The script first checks for available serial ports and displays them to the user. The user is prompted to select a port, and the script opens that port and creates a log file with the current timestamp.
The script then reads data from the port continuously, logs it to the file with a timestamp, and displays it to the user. 
If the user interrupts the script with Ctrl+C, a signal handler function is called to safely close the serial port and log file and exit the script. 
If there are no available serial ports, the script exits with a message. If the user enters an invalid port selection, the script prompts the user to try again. 
The script uses the pyserial library to communicate with the serial port.
