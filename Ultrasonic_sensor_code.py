import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 
TRIG = 21
ECHO = 20
 
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
 
def distance():
	GPIO.output(TRIG, False)
	time.sleep(0.5)
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	pulse_start = time.time()
	while GPIO.input(ECHO)==0:
    		pulse_start = time.time()
	while GPIO.input(ECHO)==1:
    		pulse_end = time.time()
	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance, 2)
 
	return distance
 
print(distance())
 
GPIO.cleanup()




# #!/usr/bin/env python3
# from gpiozero import DistanceSensor
# from time import sleep

# # Initialize the DistanceSensor using GPIO Zero library
# # Trigger pin is connected to GPIO 17, Echo pin to GPIO 27
# sensor = DistanceSensor(echo=27, trigger=17)

# try:
#     # Main loop to continuously measure and report distance
#     while True:
#         dis = sensor.distance * 100  # Measure distance and convert from meters to centimeters
#         print('Distance: {:.2f} cm'.format(dis))  # Print the distance with two decimal precision
#         sleep(0.3)  # Wait for 0.3 seconds before the next measurement

# except KeyboardInterrupt:
#     # Handle KeyboardInterrupt (Ctrl+C) to gracefully exit the loop
#     pass
