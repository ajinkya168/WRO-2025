import time
import board
import busio
from math import atan2, sqrt, pi
import adafruit_tcs34725
import math
import colorsys
class IMUandColorSensor:
	def __init__(self, scl, sda, frequency=400000):
		self.i2c1 = busio.I2C(scl, sda)
		self.prev_imu = 0

		self.sensor = adafruit_tcs34725.TCS34725(self.i2c1)
		self.sensor.gain = 60
		self.color_rgb = [0, 0, 0]
		self.r_norm = 0
		self.g_norm = 0
		self.b_norm = 0
		self.average_r = 0
		self.average_g = 0
		self.average_b = 0
		self.avg_orange = 0
		self.avg_blue = 0
	def get_color(self):
		#time.sleep(0.01)

		self.color_rgb = self.sensor.color_rgb_bytes
		total = (self.color_rgb[0] + self.color_rgb[1]+ self.color_rgb[2])
		color_hsv = colorsys.rgb_to_hsv(self.color_rgb[0], self.color_rgb[1], self.color_rgb[2])
		#color_hsv = colorsys.rgb_to_hsv(r_norm, g_norm, b_norm)
		hsv_r = color_hsv[0]*1800//1
		hsv_g = color_hsv[1]*100//1
		hsv_b = color_hsv[2]		
		
		self.r_norm = self.color_rgb[0]*100 // total
		self.g_norm = self.color_rgb[1]*100 // total
		self.b_norm = self.color_rgb[2]*100 // total
		
		'''self.average_r = (self.r_norm*0.8 + self.average_r*0.2) 
		self.average_g = (self.g_norm*0.8 + self.average_g*0.2) 
		self.average_b = (self.b_norm*0.8 + self.average_b*0.2) 
		
		self.r_norm = self.average_r
		self.g_norm = self.average_g
		self.b_norm = self.average_b'''
		
		if (self.r_norm == 0 and self.g_norm == 0 and self.b_norm == 0) or (hsv_r == 0 and hsv_g == 0 and hsv_b == 0):
			pass
		else:
			print(f"r:{self.r_norm} g:{self.g_norm} b:{self.b_norm}")
			print(f"hsv_r:{hsv_r} hsv_g: {hsv_g} hsv_b:{hsv_b}")
				
			if self.r_norm >= 70 and self.b_norm < 10 and self.g_norm < 15:
				#f_orange = 1
				return "Orange"
			elif  self.r_norm < 55 and self.b_norm > 15 and self.g_norm > 22:
				#f_blue = 1
				return "Blue"

			

				
			if hsv_r < 40 and hsv_g > 88 and hsv_b > 60:
				#f_orange =1 
				return "Orange"
			elif hsv_b <= 69 and hsv_g < 36:
				#f_blue = 1
				return "Blue"

			'''self.avg_orange = f_orange*0.5 + self.avg_orange*0.5
			self.avg_blue = f_blue*0.5 + self.avg_blue*0.5
			print(f"avg_o:{self.avg_orange} avg_b {self.avg_blue}")
			
			if self.avg_orange > 0.9:
				return "Orange"
			elif self.avg_blue > 0.9:
				return "Blue"
			else:
				return "White"'''

	def close(self):
		GPIO.cleanup()
