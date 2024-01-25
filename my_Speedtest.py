import speedtest
def get_speedtest():
	try:
		internet = speedtest.Speedtest()#download() &upload() this function give value in bits per second
		speed = f"Your network's Download Speed is {round(internet.download() / 1000000, 2)}MBps\n" \
			   f"Your network's Upload Speed is {round(internet.upload() / 1000000, 2)}MBps"
		return speed
	except (speedtest.SpeedtestException, KeyboardInterrupt) as e:
		return "unable to process, check your internet speed"
