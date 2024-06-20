# Event object manages the state of an internal flag
# set() ->  flag is initially false and becomes true
# clear() -> reset to false
# wait() -> blocks until the flag is true.

from threading import *
import time

def signal_state():
   while True:
      time.sleep(5)
      print("Traffic Police Giving GREEN Signal")
      event.set()    #signal that traffic can move
      time.sleep(10)
      print("Traffic Police Giving RED Signal")
      event.clear()  #signal that traffic must stop
 
def traffic_flow():
   num=0
   while num<10:   #max no. of vehicle
      print("Waiting for GREEN Signal")
      event.wait()    #wait until event flag is set( indicating green signal)
      print("GREEN Signal ... Traffic can move")

      while event.is_set():  #loop that allow vehicle to move in traffic
         num=num+1         #num of vehicle
         print("Vehicle No:", num," Crossing the Signal")
         time.sleep(2)     # every 2 second one vehicle will be moved from traffic
      print("RED Signal ... Traffic has to wait")

event=Event()
t1=Thread(target=signal_state)
t2=Thread(target=traffic_flow)
t1.start()
t2.start()