import RPi.GPIO as GPIO
import time
import json
import urllib

url = ""

def main():
	try:
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(11, GPIO.OUT)
		for i in range(0,50):
			if pingReddit() == True:
			        blink(11)
			time.sleep(1)
	finally:
		GPIO.cleanup() 
	return

def blink(pin):
        GPIO.output(pin, True)
        time.sleep(5)
        GPIO.output(pin, False)
        return

def pingReddit():
	try:
        	f = urllib.urlopen("http://www.reddit.com/r/all/new/.json");
    	except Exception:
        	return False
    	reddit_links = json.loads(f.read().decode("utf-8"))["data"]["children"][0]
    	urlNew = reddit_links["data"]["url"]
	print urlNew
	global url
	if urlNew != url:
		url = urlNew
		return True
	else:
		return False

main()