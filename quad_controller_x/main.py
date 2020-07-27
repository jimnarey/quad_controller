# Context managers are not supported (the with statement).
# Generators are not supported.
# If raise is used an argument must be supplied.
# Functions may have up to four arguments.
# Default argument values are not permitted.
# Floating point may be used but is not optimised.
import time
from machine import Pin, PWM
import utils

# With USB port facing down
SERVO_PINS_RGT = (2, 15, 4, 16, 17, 5, 18)
SERVO_PINS_LFT = (13, 14, 27, 26, 25, 33, 32)

# SERVO_PINS_RGT = (2, 15, 4, 16, 17, 5)
# SERVO_PINS_LFT = (13, 14, 27, 26, 25, 33)
SERVO_PINS = SERVO_PINS_LFT + SERVO_PINS_RGT

class Servo:
    
    freq = 50
    min = int(round(1023 / 20))
    max = int(round(1023 / 10))
    mid = int(round(1023 / 15))
    
    def __init__(self, pin_no, start_angle):
        super().__init__()
        self.pin = Pin(pin_no)
#         self.pwm = PWM(self.pin)
#         self.pwm.freq(Servo.freq)
        self.to_angle(start_angle)
        
    def to_angle(self, angle):
        angle = clip_input(angle, 0, 180)
        duty = int(((angle / 180) * Servo.min) + Servo.min)
        print(duty)
        self.pwm.duty(duty)
        
    def zero(self):
        self.to_angle(90)

def get_servos(servo_pins):
    return [Servo(servo_pin, 90) for servo_pin in servo_pins]
        

servos = get_servos(SERVO_PINS)


        