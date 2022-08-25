import serial
import argparse

parser = argparse.ArgumentParser() #Creating ArgumentParser
parser.add_argument("-f", "--file", help="Name of the file to parse") # Creating file argument
parser.add_argument("-p", "--port", help="Port name to parse to") # Creating port argument
args = parser.parse_args() # Parsing arguments

if args.port: # Assign parsed port to portName
        portName = args.port
else: # Default Port
        portName = 'ttyAMA0'

if args.file: # Assign parsed file to fileName
        fileName = args.file
else: # There's no default file, return error
        print('Error')

ser = serial.Serial() # Creating serial
ser.baudrate = 115200 # Setting serial com baudrate
ser.port =('/dev/')+(portName) # Setting port
ser.open() # Opening communication

def serialPrint(fileName): # Defining serialPrint function
        with open(fileName) as datafile: # Opening selected file
                line = datafile.readline() # Reading first line of the file
                print(line) # Printing the parsed line to console
        ser.write(line.encode()) # Writing the line to serial

serialPrint(fileName) # Calling the print function
