import paho.mqtt.client as mqtt
import time

# Connect to the first MQTT broker
client = mqtt.Client("Publisher")
client.connect("localhost", 1883, 60)

# Publish a message to the first broker
client.publish("test/topic", "Hello from Publisher")

# Disconnect the client
client.disconnect()
