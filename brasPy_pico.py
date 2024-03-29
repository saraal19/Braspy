from machine import Pin, UART,PWM
import utime
from time import sleep
pin_rx = machine.Pin(17)  # Remplacez par le numéro de broche RX souhaité
pin_tx = machine.Pin(16) 
uart = UART(0, tx=pin_tx, rx=pin_rx , baudrate=9600)
uart.init(bits=8, parity=None)
r = ""
#recive a commande
while True:
    r = uart.readline()
    print(r)
    sleep(0.5)
#define Pin
IN1 = Pin(2, Pin.OUT)
IN2 = Pin(3, Pin.OUT)
IN3 = Pin(4, Pin.OUT)
IN4 = Pin(5, Pin.OUT)

pins = [IN1, IN2, IN3, IN4]

IN1.low()
IN2.low()
IN3.low()
IN4.low()
# Configuration pour faire tourner le moteur d'un pas dans le sens des aiguilles d'une montre
#sequence = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
nbr_step=1
max_step=1000

pwm = PWM(Pin(0))

pwm.freq(50)
#The position is expected as a parameter

def setServoCycle (position):

    pwm.duty_u16(position)

    sleep(0.01)

while True:
    if r=="rotation 1":
        IN1.high()
        IN2.low()
        IN3.low()
        IN4.high()
        utime.sleep(0.001)
        #
        IN1.high()
        IN2.high()
        IN3.low()
        IN4.low()
        utime.sleep(0.001)
        #
        IN1.low()
        IN2.high()
        IN3.high()
        IN4.low()
        utime.sleep(0.001)
        #
        IN1.low()
        IN2.low()
        IN3.high()
        IN4.high()
        utime.sleep(0.001)
        nbr_step +=1
        if  nbr_step==500 :
            IN1.low()
            IN2.low()
            IN3.low()
            IN4.low()
        
    elif r=="rotation 2":
        # to turn off the pulse
        #pwm.duty_u16(60)
        for pos in range(1000,9000,50):
            setServoCycle(pos)
            
        for pos in range(9000,1000,-50):
            setServoCycle(pos)
    elif r=="stop":
        IN1.low()
        IN2.low()
        IN3.low()
        IN4.low()
        pwm.duty_u16(0)
     
