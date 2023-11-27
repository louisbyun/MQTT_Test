import paho.mqtt.client as mqtt

# Connect to the second MQTT broker
client = mqtt.Client("Subscriber")
client.connect("localhost", 1884, 60)

# Define a callback function for when a message is received
def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

client.on_message = on_message

# Subscribe to a topic on the second broker for receiving messages
client.subscribe("test/topic")

# Start the loop to wait for messages
client.loop_forever()
