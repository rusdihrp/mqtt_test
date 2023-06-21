import paho.mqtt.client as paho
from paho import mqtt
import json

# define static variable
broker = "mqtt-dashboard.com"
port = 1883
timeout = 60

username = ''
password = ''
topic = "test_topic/1"

value_sensor = 15

json_all_sensor = {
    "sensor1": "jarak",
    "sensor2": "camera"
}

json_data = {
    "sensor": value_sensor,
    "jenis_sensor": json_all_sensor
}

json_sum = json.dumps(json_data)

print("data json"+ str(json_sum) +" \n")


def on_connect(client, userdata, flag, rc):
    print("Connected with result code "+str(rc))
    client.publish(topic, json_sum) 

def on_publish(client, userdata, result):
    print("data published \n")

client = paho.Client("d01", userdata=None) #client ID name
client.username_pw_set(username=username, password=password)
client.on_connect = on_connect
client.on_publish = on_publish
client.connect(broker, port, timeout)
client.loop_forever()