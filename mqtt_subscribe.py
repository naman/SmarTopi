import paho.mqtt.client as paho
import os
import socket
import ssl
from s3_get_file import s3_get_file

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc) )
    client.subscribe("#" , 1 )

def on_message(client, userdata, msg):
    print("topic: "+msg.topic)
    print("payload: "+str(msg.payload, 'utf-8'))
    s3_get_file(str(msg.payload, 'utf-8'), "imagestoressiot")

#def on_log(client, userdata, level, msg):
#    print(msg.topic+" "+str(msg.payload))

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
#mqttc.on_log = on_log

awshost = "a1n1j1jd1jtkgg.iot.us-west-2.amazonaws.com"
awsport = 8883
clientId = "Subscriber1"
thingName = "Subscriber1"
caPath = "./SubscriberCreds/root-CA.crt"
certPath = "./SubscriberCreds/46e50a4a8e-certificate.pem.crt"
keyPath = "./SubscriberCreds/46e50a4a8e-private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_forever()