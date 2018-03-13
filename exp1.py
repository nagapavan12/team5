
import serial
import RPi.GPIO as GPIO
import time
#ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser1=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser1.baudrate=9600


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
while True:
     
   
   

    
     read_ser1=ser1.readline()
     print(read_ser1)
     if(read_ser1==b'CARD AUTHORISED\r\n'):
      GPIO.output(11,True)
     if (read_ser1==b'CARD NOT Authorised\r\n'):
      GPIO.output(11,False)
      
             
    
 
   
     
 
 




 
