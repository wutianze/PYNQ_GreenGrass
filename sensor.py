from pynq.overlays.base import BaseOverlay
from pynq.lib.pmod import *
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from time import sleep
from datetime import date, datetime
import math
import socket

base = BaseOverlay("base.bit")

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

    #button message:1/2/3/4
    global btn
    try:
        btn = int(message.payload)
    except Exception as e:
    	print(e)
    #btn1 increase, btn2 decrease
    if (btn == 1):
        #sleep(0.2)
        print("btn == 1\n")
    elif (btn == 2):
        #sleep(0.2)
        print("btn == 2\n")
    elif (btn == 3):
        print("btn == 3\n")
    base.leds[btn-1].on()
    sleep(0.2)
    base.leds[btn-1].off()

# Loading Base Overlay

pynq_self = "pynq_sensor"
local_ip = get_host_ip()
# AWS IoT certificate based connection
myMQTTClient = AWSIoTMQTTClient("pynq_greengrass_sensor")

#Here to put your own endpoint
myMQTTClient.configureEndpoint("xxxx.amazonaws.com", 443)

#Here to put your own files
myMQTTClient.configureCredentials("root-ca-cert.pem", "xxxx.private.key", "xxxx.cert.pem")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
 
#connect and publish
myMQTTClient.connect()
 
#loop and publish sensor reading
while 1:
        #get button instruction
    try:
        myMQTTClient.subscribe("xxxx", 1,customCallback) # here xxxx maybe hello/world/pubsub
    except Exception as e:
        print(e)
            #pass
    print("loop\n")
    sleep(0.2)


