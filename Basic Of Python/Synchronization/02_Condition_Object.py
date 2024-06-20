# with condition object help -> threads to wait until a certain condition is met
# A condition object has acquire() and release() methods that call the corresponding methods of the associated lock.
# aquire() -> method is used to acquire the underlying lock of the Condition object. This must be done before calling other methods like wait(), notify(), or notify_all().
# release() -> release the underlying lock of the Condition object. This must be done after the condition has been modified and the thread no longer needs exclusive access to the shared resource.


from threading import *
import time
import random

numbers=[]
def taskA(c):
   while True:
      c.acquire()
      num=random.randint(1,10)
      print("Generated random number:", num)
      numbers.append(num)
      print("Notification issued")
      c.notify()
      c.release()
      time.sleep(5)

def taskB(c):
   while True:
      c.acquire()
      print("waiting for update")
      c.wait()
      print("Obtained random number", numbers.pop())
      c.release()
      time.sleep(5)

c=Condition()
t1=Thread(target=taskB, args=(c,))
t2=Thread(target=taskA, args=(c,))
t1.start()
t2.start()


