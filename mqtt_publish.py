import paho.mqtt.client as paho
import os
import socket
import ssl
from time import sleep
from random import uniform

connflag = False

def on_connect(client, userdata, flags, rc):
    global connflag
    connflag = True
    print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

#def on_log(client, userdata, level, buf):
#    print(msg.topic+" "+str(msg.payload))

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
#mqttc.on_log = on_log

awshost = "a1n1j1jd1jtkgg.iot.us-west-2.amazonaws.com"
awsport = 8883
clientId = "RasPi3"
thingName = "RasPi3"
caPath = "./creds/root-CA.crt"
certPath = "./creds/d69802753f-certificate.pem.crt"
keyPath = "./creds/d69802753f-private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_start()

def publish_message(topic, message, mqtt_client=mqttc):
    while True:
        sleep(0.5)
        if connflag:
            mqttc.publish(topic, message, qos=1)
            break
        else:
            print("waiting for connection...")
