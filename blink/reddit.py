import RPi.GPIO as GPIO
import time
import json
import urllib

def main():
	try:
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(11, GPIO.OUT)
		GPIO.setup(13, GPIO.OUT)
		for i in range(0,50):
			link = pingReddit()
			title = link["data"]["title"]
			print title
			nsfw = link["data"]["over_18"]
			if nsfw == True:
				blink(13)
			else:
				blink(11)
	finally:
		GPIO.cleanup() 
	return

def blink(pin):
        GPIO.output(pin, True)
        time.sleep(1)
        GPIO.output(pin, False)
	time.sleep(1)
        return

def pingReddit():
	try:
        	f = urllib.urlopen("http://www.reddit.com/r/wtf/new/.json");
	except Exception:
		return False
	reddit_link = json.loads(f.read().decode("utf-8"))["data"]["children"][0]
	return reddit_link

main()