import sys,string
import time
from playsound import playsound

sa = sys.argv

if len(sys.argv) != 2:
	print("Usage: [ python ] alarm_clock.py duration_in_minutes")
	print("Example: [python ] alarm_clock.py 10")
	print("Use a value of 0 minutes for testing the alarm immediately.")
	print("Beeps a few times after duration is over.")
	print("Press Ctrl-c to terminate the alarm clock early")
	sys.exit(1)

try:
	minutes =int(sa[1])
except ValueError:
	print("Invalid numeric value (%s) for minutes" % sa[1])
	print("Should be an integer >= 0")
	sys.exit(1)

if minutes < 0:
	print("Invalid value for minutes, should be >= 0")
	sys.exit(1)

seconds = minutes * 60

if minutes == 1:
	unit_word = " minute "
else:
	unit_word = " minutes"


while True:
	count = 0
	try:
		if minutes > 0:
			print("alarm will ring after " + str(minutes) + unit_word)
			while count <= seconds:
				localtime = time.localtime()
				result = time.strftime("%I:%M:%S %p", localtime)
				print(result, end="", flush=True)
				print("\r", end="", flush=True)
				count += 1
				time.sleep(1)
			
			playsound('/home/abhishek/Music/alarm_beeps.mp3')
	except KeyboardInterrupt:
		print("Interurpted by user")
		sys.exit(1)


