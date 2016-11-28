import cv2
import time
import os
import datetime
import requests
from s3_upload_file import upload_to_s3
from goprohero import GoProHero
from bs4 import BeautifulSoup
import subprocess
from fbrecog import recognize

access_token = "EAACEdEose0cBAEpbrjlnvFZBLemSZAwZBJ2eP1Jcboqn5ftbedBjVzd9CMFM175ZApaZBZA7IVo7zZAh9neUQuoc46ogOQb81ZCpSQsfq3ZBg7UOO1LdxT5TVPzUDyAlZA80pg4RB6VHNoddcLL7LA2thfwADDY11H4rZBZCDYjItQeYLAZDZD"
cookie = "datr=fPqQVfDF5cEMKwcywPvt70jN; _ga=GA1.2.1788536487.1437330029; locale=en_GB; sb=_U0HV7uSQVX_Z8Oov3bZav9c; pl=n; lu=giTXKkQ81PDlziOlnp5_5J7A; c_user=100000601825742; xs=204%3As6GCwRc3trP-_w%3A2%3A1479817217%3A5827; fr=0J8CbTl5k918hSbLX.AWWGwk7QSJhzwUuSO-iL8J2fpEo.BVkPqC.Nv.Fg0.0.0.BYPH2T.AWXxfm--; csm=2; s=Aa7PrE1w24FGNzCh.BYNDgB; p=-2; presence=EDvF3EtimeF1480361527EuserFA21B00601825742A2EstateFDt2F_5b_5dElm2FnullEuct2F1480325937BEtrFA2loadA2EtwF2218223787EatF1480361522186G480361527040CEchFDp_5f1B00601825742F15CC; act=1480361603300%2F10; wd=1466x536"
fb_dtsg = "AQGQIXXXTjK_:AQH9HojIEPNb"


def listFD(url, ext=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

url = 'http://10.5.5.9:8080/videos/DCIM/100GOPRO/'
ext = 'MP4'
password = 'srishtigopro'

print "Clicking photos; connecting to gopro..."

os.system('wpa_cli select_network 1')

time.sleep(13)

camera = GoProHero(password=password)

for x in xrange(10):
	camera.command('record', 'on')
	time.sleep(1) # delays for 1 second
	camera.command('record', 'off')

	time.sleep(1) # delays for 1 second

	file_list = listFD(url, ext)
	video_url = file_list[-1]

	cap = cv2.VideoCapture(video_url)

	t =  datetime.datetime.now().strftime("%d_%B_%Y_%I:%M:%S%p")

	while cap.isOpened():
	    ret,frame = cap.read()
	    frame_name = "frame_%s.jpg" % t
	    cv2.imwrite(frame_name, frame)
	    break

	cap.release()
	time.sleep(1)

print "conecting to SENSOR"
os.system('wpa_cli select_network 2')
time.sleep(10)

print "sending images to S3, messages to MQTT clients"
from mqtt_publish import publish_message

for f in os.listdir("."):
    if f.endswith(".jpg"):
        fyl = open(f, "rb")
        upload_to_s3(fyl, "imagestoressiot", f)
	publish_message("Image",f)
	print "sent " + f

lol = []
for f in os.listdir("."):
    if f.endswith(".jpg"):
        output = subprocess.check_output("recog" + " " + f, shell=True)
	lol.append(output)

print "Recognition results"
print lol

fb = {}
for f in os.listdir("."):
	if f.endswith(".jpg"):
		for item in recognize(f,access_token,cookie,fb_dtsg):
			if(item['certainity']>0.8):
				if f in fb:
					fb[f].append(item['name'])
				else:
					fb[f] = [item['name']]

print("Facebook Recognition")
print(fb)

print("Check timeseries plot on any client.")
