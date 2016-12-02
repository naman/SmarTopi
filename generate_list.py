import os
import json
import subprocess

from fbrecog import recognize

d = []

recog = 'python /usr/local/lib/python2.7/dist-packages/tensorflow/models/image/imagenet/classify_image.py --image_file'


access_token = "EAACEdEose0cBAIgT23CMg6fm7ccibTb3X6dZB4ZBUZBHoKEJsndKNWsQO5r9H6aQ6clO3ZBmHyLvbYlmt1LTfsLHr682nZAVi8mE11ZBRitBOpNi3zeJZBpyiHgd8QGHm8KshmFdyjgiL1PrXcQVmrdHfFNb2ZCQ5ya881XQRLGzAAZDZD"
cookie = "datr=fPqQVfDF5cEMKwcywPvt70jN; _ga=GA1.2.1788536487.1437330029; locale=en_GB; sb=_U0HV7uSQVX_Z8Oov3bZav9c; pl=n; lu=giTXKkQ81PDlziOlnp5_5J7A; act=1480403909806%2F37; c_user=100000601825742; xs=204%3As6GCwRc3trP-_w%3A2%3A1479817217%3A5827; fr=0J8CbTl5k918hSbLX.AWWVWUk_stCb76nL3z39SA5UOXs.BVkPqC.Nv.Fg0.0.0.BYPSvF.AWUNU7kF; csm=2; s=Aa7PrE1w24FGNzCh.BYNDgB; p=-2; presence=EDvF3EtimeF1480404349EuserFA21B00601825742A2EstateFDutF1480404349142Et2F_5b_5dElm2FnullEuct2F1480362430828EtrFA2loadA2EtwF974806435EatF1480404348875CEchFDp_5f1B00601825742F2CC; wd=1466x536"
fb_dtsg = "AQHarJKhSvmq:AQH1lfFvPRVN"

for f in os.listdir("./ImageData/"):
	if f.endswith(".jpg"):
		output = subprocess.check_output(recog  + " ImageData/" +f, shell=True)
		dicti = {}
		dicti["name"] = f
		dicti["recognition"] = output

		dicti["fb"] = []
		for item in recognize("ImageData/" + f,access_token,cookie,fb_dtsg):
			# print item
			if "fb" in dicti:
				dicti["fb"].append(item['name'])
		
		dicti["fb"] = str(dicti["fb"])
		d.append(dicti)
		say_string = "The scene in front of you contains"  + output + "objects and it may contain your facebook friends " + ','.join(dicti["fb"]) 
        # output = subprocess.check_output("espeak " + say_string, shell=True)
        print 
print json.dumps(d)
