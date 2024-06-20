import time
import paho.mqtt.client as mqtt

def on_publish(client, userdata, mid, reason_code, properties):
    # reason_code and properties will only be present in MQTTv5. It's always unset in MQTTv3
    try:
        userdata.remove(mid)
    except KeyError:
        print("on_publish() is called with a mid not present in unacked_publish")
        print("This is due to an unavoidable race-condition:")
        print("* publish() return the mid of the message sent.")
        print("* mid from publish() is added to unacked_publish by the main thread")
        print("* on_publish() is called by the loop_start thread")
        print("While unlikely (because on_publish() will be called after a network round-trip),")
        print(" this is a race-condition that COULD happen")
        print("")
        print("The best solution to avoid race-condition is using the msg_info from publish()")
        print("We could also try using a list of acknowledged mid rather than removing from pending list,")
        print("but remember that mid could be re-used !")


unacked_publish = set()    # set to track unacknowledged message IDs
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)  # Create mqtt.client object
mqttc.on_publish = on_publish  #Setting up the callback function


mqttc.user_data_set(unacked_publish)  # Associate the unacked_publish set with the MQTT client's user data
mqttc.connect("mqtt.eclipseprojects.io")  #  Connect to MQTT Broker
mqttc.loop_start()   #  Start MQTT client's network loop in seperate thread


# to publish meassage give follow arguments:  
# topic, message u want to give  and QOS

msg_info = mqttc.publish("paho/test/topic", "my message3", qos=0)
unacked_publish.add(msg_info.mid)  # adding mid to unacked_publish set

msg_info2 = mqttc.publish("paho/test/topic", "my message4", qos=0)
unacked_publish.add(msg_info2.mid)

# Wait for all message to be published successfully
while len(unacked_publish):
    time.sleep(0.1)

# Due to race-condition described above, the following way to wait for all publish is safer
# Use wait_for_publish() to ensure all messages have been successfully published
msg_info.wait_for_publish()
msg_info2.wait_for_publish()

mqttc.disconnect()   # Disconnect from MQTT Broker
mqttc.loop_stop()    # Stop the network loop 

print(unacked_publish)
