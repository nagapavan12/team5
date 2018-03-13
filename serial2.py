import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyACM2",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600
ser1=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser1.baudrate=9600
GPIO.setmode(GPIO.BOARD)
s1g=3
s1r=5
s2g=7
s2r=11
s3g=13
s3r=15
#rfid1=29
#rfid2=31
#rfid3=33
GPIO.setup(s1g, GPIO.OUT)
GPIO.setup(s1r, GPIO.OUT)
GPIO.setup(s2g, GPIO.OUT)
GPIO.setup(s2r, GPIO.OUT)
GPIO.setup(s3g, GPIO.OUT)
GPIO.setup(s3r, GPIO.OUT)
while True:
    
##  read_ser1=ser1.readline()
##  print(read_ser1)
##  
##      GPIO.output(11,True)
##  if (read_ser1==b'CARD NOT Authorised\r\n'):
##      GPIO.output(11,False)   



    
 rfid1=ser1.readline()
 print(rfid1)
 if (rfid1==b'CARD AUTHORISED\r\n'):
     
         time.sleep(5)
         GPIO.output(s1g,True)
         GPIO.output(s2r,True)
         GPIO.output(s3r,True)
         GPIO.output(s1r,False)
         GPIO.output(s2g,False)
         GPIO.output(s3g,False)
         time.sleep(15)
         GPIO.output(s1g,False)
         GPIO.output(s2r,False)
         GPIO.output(s3r,False)
 elif rfid2.available():
     time.sleep(5)
     GPIO.output(s1r,True)
     GPIO.output(s2g,True)
     GPIO.output(s3r,True)
     GPIO.output(s1g,False)
     GPIO.output(s1r,False)
     GPIO.output(s3g,False)
     time.sleep(15)
 elif rfid3.available():
     time.sleep(5)
     GPIO.output(s1r,True)
     GPIO.output(s2r,True)
     GPIO.output(s3g,True)
     GPIO.output(s1g,False)
     GPIO.output(s1g,False)
     GPIO.output(s3r,False)
     time.sleep(15)
 else:
     read_ser=ser.readline()
     print(read_ser)
     if(read_ser==b'A\r\n'):
         time.sleep(5)
         GPIO.output(s1g,True)
         GPIO.output(s2r,True)
         GPIO.output(s3r,True)
         GPIO.output(s1r,False)
         GPIO.output(s1g,False)
         GPIO.output(s3g,False)
         time.sleep(15)
    elif(read_ser==b'B\r\n'):
         time.sleep(5)
         GPIO.output(s1r,True)
         GPIO.output(s2g,True)
         GPIO.output(s3r,True)
         GPIO.output(s1g,False)
         GPIO.output(s1r,False)
         GPIO.output(s3g,False)
         time.sleep(15)
    elif(read_ser==b'B\r\n'):
        time.sleep(5)
        GPIO.output(s1r,True)
        GPIO.output(s2r,True)
        GPIO.output(s3g,True)
        GPIO.output(s1g,False)
        GPIO.output(s1g,False)
        GPIO.output(s3r,False)
        time.sleep(15)
