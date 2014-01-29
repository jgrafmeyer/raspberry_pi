import RPi.GPIO as GPIO
import time
import json
import urllib

url = ""

def blink(pin):
        GPIO.output(pin,True)
        time.sleep(5)
        GPIO.output(pin,GPIO.LOW)
        return

def pingReddit():
	try:
        	f = urllib.urlopen("http://www.reddit.com/r/all/new/.json");
    	except Exception:
        	return False
    	reddit_posts = json.loads(f.read().decode("utf-8"))["data"]["children"][0]
    	urlNew = reddit_posts["data"]["title"]
	print urlNew
	global url
	if urlNew != url:
		url = urlNew
		return True
	else:
		return False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

for i in range(0,100):
	if pingReddit() == True:
	        blink(11)
	time.sleep(1)

GPIO.cleanup() 