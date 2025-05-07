import os
os.system('sudo pkill pigpiod')
os.system('sudo pigpiod')

from TFmini import TFmini

sum_d = 0
prev_distance = 0
i = 0
avg_d = 0
if __name__ == "__main__":
	try:
		tfmini = TFmini(23, 24, 25, 27)

		while True:
			tfmini.getTFminiData()
			
			avg_d = (tfmini.distance_right* 0.01) + (avg_d * 0.99)
			print(
				f"average: {avg_d} head : {tfmini.distance_head}, left: {tfmini.distance_left}, right: {tfmini.distance_right} back:{tfmini.distance_back} sum_horizontal:{tfmini.distance_right + tfmini.distance_left}")
	except Exception as e:
		print(e)

