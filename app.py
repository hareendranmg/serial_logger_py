# pip install pyserial
import serial.tools.list_ports
import time
import datetime
import signal
import sys

file = None  # Define file in the global scope
ser = None  # Define ser in the global scope

def signal_handler(sig, frame):
    print("\nExiting...")
    if file:
        file.close()
    if ser and ser.is_open:
        ser.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Display available serial ports
ports = list(serial.tools.list_ports.comports())
if len(ports) == 0:
    print("No serial ports found")
    sys.exit(0)

print("Available serial ports:")
for i, port in enumerate(ports):
    print(f"{i+1}: {port}")

# Ask user to select a port
while True:
    try:
        selection = int(input("Enter the number of the serial port you want to use (or press Ctrl+C to exit): "))
        port = ports[selection - 1].device
        break
    except (ValueError, IndexError):
        print("Invalid selection. Please try again.")
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

# Open serial port and create file
ser = serial.Serial(port, 115200, timeout=0.05)
filename = datetime.datetime.now().strftime("data_%Y-%m-%d_%H-%M-%S.%f.txt")
file = open(filename, "w")

# Continuously read from serial port and write to file
try:
    while True:
        data = ser.readline().decode().strip()
        if data:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            print(f"[{timestamp}] {data}")
            file.write(f"[{timestamp}] {data}\n")
except KeyboardInterrupt:
    print("\nExiting...")
    if file:
        file.close()
    if ser and ser.is_open:
        ser.close()
    sys.exit(0)
