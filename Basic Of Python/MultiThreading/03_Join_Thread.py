# The join() method in thread class blocks the calling thread until the thread whose join() method is called terminates

# thread.join(timeout)
# timeout − it should be a floating point number specifying a timeout for which the thread is to be blocked.


#Name the thread
import threading
import time
class myThread (threading.Thread):
   def __init__(self, name):
      threading.Thread.__init__(self)
      self.name = name

   def run(self):
      print ("Starting " + self.name)
      for count in range(1,6):
         time.sleep(1)
         print ("Thread name: {} Count: {}".format ( self.name, count ))
      print ("Exiting " + self.name)

# Create new threads
thread1 = myThread("Thread-1")
thread2 = myThread("Thread-2")

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")


