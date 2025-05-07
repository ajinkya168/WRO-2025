import os




os.system('sudo pkill pigpiod')
os.system('sudo pigpiod')
import pigpio

pwm = pigpio.pi()
pwm.set_mode(12, pigpio.OUTPUT)  # Set pin 12 as an output
pwm.set_mode(20, pigpio.OUTPUT)  # Set pin 20 as an output
pwm.hardware_PWM(12, 100, 0)
pwm.set_PWM_dutycycle(12, 0)  # Set duty cycle to 50% (128/255)

total_power = 0
prev_power = 0
power = int(input("Enter power: "))

try:
	while True:
			total_power = (power * 0.1) + (prev_power * 0.9)
			prev_power = total_power
			pwm.set_PWM_dutycycle(12, 2.55 * total_power)  # Set duty cycle to 50% (128/255)
except KeyboardInterrupt:
	total_power = 0
	prev_power = 0
	pwm.set_PWM_dutycycle(12, 2.55 * total_power)  # Set duty cycle to 50% (128/255)
