#Queue object method:
# get() − The get() removes and returns an item from the queue.
# put() − The put adds item to a queue.
# qsize() − The qsize() returns the number of items that are currently in the queue.
# empty() − The empty( ) returns True if queue is empty; otherwise, False.
# full() − the full() returns True if queue is full; otherwise, False.

import queue
#Constructor for priority queue:
queue.PriorityQueue(maxsize=0)
# maxsize is an integer that sets the upper limit on the number of items that can be placed in the queue. 
# If maxsize is less than or equal to zero, the queue size is infinite.

from time import sleep
from random import random, randint
from threading import Thread
from queue import PriorityQueue

queue = PriorityQueue()

def producer(queue):
   print('Producer: Running')
   for i in range(5):

      # create item with priority
      value = random()
      priority = randint(0, 5)
      item = (priority, value)
      queue.put(item)
   # wait for all items to be processed
   queue.join()

   queue.put(None)
   print('Producer: Done')

def consumer(queue):
   print('Consumer: Running')

   while True:

      # get a unit of work
      item = queue.get()
      if item is None:
         break

      sleep(item[1])
      print(item)
      queue.task_done()
   print('Consumer: Done')

producer = Thread(target=producer, args=(queue,))
producer.start()

consumer = Thread(target=consumer, args=(queue,))
consumer.start()

producer.join()
consumer.join()
