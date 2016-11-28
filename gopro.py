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

access_token = "EAACEdEose0cBAF2LiQE6mNG8ixIvblmwHwlhAwjo7tOas1ahfXlGUpLsJkQWq5iq3ENkEojFtKC5xEUSQs$
cookie = "datr=fPqQVfDF5cEMKwcywPvt70jN; _ga=GA1.2.1788536487.1437330029; locale=en_GB; sb=_U0HV7uS$
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

fb = []
for f in os.listdir("."):
    if f.endswith(".jpg"):
	fb.append(recognize(f,access_token,cookie,fb_dtsg))

print "Facebook Recognition"
print fb

print "Check timeseries plot on any client."
