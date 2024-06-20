import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()}")
    print(f"QoS: {message.qos}")
    

# Define the MQTT broker details
broker_address = "mqtt.eclipseprojects.io"
broker_port = 1883

# Initialize the MQTT client and callbck function
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Subscribe to the topic
client.subscribe("paho/test/topic")

# Loop forever to receive messages from publisher
client.loop_forever()