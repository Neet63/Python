import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()}")
    print(f"QoS: {message.qos}")
    
    # Send an acknowledgment for QoS 1
    if message.qos == 1:
        client.publish("paho/test/topic", "Acknowledgment", qos=1)

# Define the MQTT broker details
broker_address = "mqtt.eclipseprojects.io"
broker_port = 1883

# Define the MQTT client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Subscribe to the topic with QoS 1
client.subscribe("paho/test/topic", qos=1)

# Loop forever to receive messages
client.loop_forever()