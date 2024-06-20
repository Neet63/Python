# scheduler(timefunc=time.monotonic, delayfunc=time.sleep)
# scheduler.enter() − Events can be scheduled to run after a delay, or at a specific time. To schedule them with a delay, enter() method is used.
# scheduler.cancel() − Remove the event from the queue. If the event is not an event currently in the queue, this method will raise a ValueError.
# scheduler.run(blocking=True) − Run all scheduled events.

# To schedule them with a delay, use the enter() method, which takes four arguments.
# A number representing the delay
# A priority value
# The function to call
# A tuple of arguments for the function


import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def schedule_event(name, start):
   now = time.time()
   elapsed = int(now - start)
   print('elapsed=',elapsed, 'name=', name)

start = time.time()
print('START:', time.ctime(start))
scheduler.enter(2, 1, schedule_event, ('EVENT_1', start))
scheduler.enter(5, 1, schedule_event, ('EVENT_2', start))

scheduler.run()