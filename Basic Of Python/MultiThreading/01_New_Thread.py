# _thread.start_new_thread ( function, args[, kwargs] )

import _thread
import time

import thread

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print (count, ". %s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-A", 1, ) )
   _thread.start_new_thread( print_time, ("Thread-B", 4, ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass


def greet():
   print("Hello")

#start a thread
thread1 = _thread("Thread-1")
#to start thread ->  threadname.start()
# this automatically call run()
thread1.start()