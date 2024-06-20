# Semaphore class in threading module defines acquire() and release() methods.

# Semaphore class in threading module defines acquire() and release() methods.

# The basic concept of semaphore is to use an internal counter 
# which is decremented by each acquire() call 
# and incremented by each release() call

from threading import *
import time

# creating thread instance where count = 3
lock = Semaphore(4)   #counter start with 4

# creating instance
def synchronized(name):
   
   # calling acquire method
   lock.acquire()

   for n in range(3):
      print('Hello! ', end = '')
      time.sleep(1)
      print( name)

      # calling release method
      lock.release()

# creating multiple thread
thread_1 = Thread(target = synchronized , args = ('Thread 1',))
thread_2 = Thread(target = synchronized , args = ('Thread 2',))
thread_3 = Thread(target = synchronized , args = ('Thread 3',))

# calling the threads
thread_1.start()
thread_2.start()
thread_3.start()