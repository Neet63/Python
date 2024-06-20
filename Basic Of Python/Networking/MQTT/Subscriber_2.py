import paho.mqtt.client as mqtt

# Callback function when a message is received
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")
    print(f"QoS: {msg.qos}")

# Callback function when the client connects to the broker
def on_connect(client, userdata, flags, rc):   # rc = race-condition
    if rc == 0:
        print("Connected successfully")
        # Subscribe to the topic
        client.subscribe("paho/test/topic")
    else:
        print(f"Connect failed with code {rc}")

# Create an MQTT client instance
client = mqtt.Client()

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect("mqtt.eclipseprojects.io")

# Start the loop to process network traffic and dispatch callbacks
client.loop_forever()
