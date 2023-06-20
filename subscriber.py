import paho.mqtt.client as mqtt
import json
import time

# define static variable
# broker = "localhost" # for local connection
broker = "mqtt-dashboard.com"  # for online version
port = 1883
timeout = 60

username = ''
password = ''

topic = "test_topic/1"

read_payload = ''
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic, qos=0)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode('utf-8')))
    global read_payload
    try:
        read_payload = json.loads(msg.payload.decode('utf-8'))
    except json.decoder.JSONDecodeError:
        # includes simplejson.decoder.JSONDecodeError
        print('Decoding JSON has failed')
        
# Create an MQTT client and attach our routines to it.
client = mqtt.Client("d02")
client.username_pw_set(username=username, password=password)
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(broker, port, timeout)
client.loop_start()

while True:
    print("value " + str(read_payload))
    time.sleep(1)   