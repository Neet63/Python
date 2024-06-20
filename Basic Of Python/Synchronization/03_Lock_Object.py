# Lock class defines acquire() and release() methods.
# Lock.acquire(blocking, timeout) -> syntex for aquring lock
# Lock.release() -> release the lock and call only in locked state if called in unblocked state than it will give runtime error

from threading import *
import time

lock=Lock()
threads=[]

class myThread(Thread):
   def __init__(self,name):
      Thread.__init__(self)
      self.name=name

   def run(self):
      lock.acquire()
      synchronized(self.name)
      lock.release()

def synchronized(threadName):
   print ("{} has acquired lock and is running synchronized method".format(threadName))
   counter=5
   while counter:
      print (counter, ',', end='')
      time.sleep(2)
      counter=counter-1
   print('\nlock released for', threadName)

t1=myThread('Thread1')
t2=myThread('Thread2')

t1.start()
threads.append(t1)

t2.start()
threads.append(t2)

for t in threads:
   t.join()
print ("end of main thread")




