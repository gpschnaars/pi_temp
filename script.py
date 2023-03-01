import time
import board
from adafruit_dht import DHT22


def main():

	device = DHT22(board.D4, use_pulseio = False)

	while True:

		try:
			temp, humi = device.temperature, device.humidity
			print(
				f"{time.ctime()} ... ... Temp: {temp} C,  Humidity: {humi} %"
		)

		except RuntimeError as error:
			print(error.args[0])
			time.sleep(10)
			continue

		except Exception as error:
			dhtDevice.exit()
			raise error

		except KeyboardInterrupt:
			dhtDevice.exit()
			print("exiting ... ")
			break

		finally:
			time.sleep(10)


if __name__ == '__main__':

	main()