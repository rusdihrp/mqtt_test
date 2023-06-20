import paho.mqtt.client as paho
from paho import mqtt

# define static variable
broker = "mqtt-dashboard.com"
port = 1883
timeout = 60

username = ''
password = ''
topic = "test_topic"

def on_connect(client, userdata, flag, rc):
    print("Connected with result code "+str(rc))
    client.publish(topic, "1") 

def on_publish(client, userdata, result):
    print("data published \n")

client = paho.Client("d01", userdata=None) #client ID name
client.username_pw_set(username=username, password=password)
client.on_connect = on_connect
client.on_publish = on_publish
client.connect(broker, port, timeout)
client.loop_forever()