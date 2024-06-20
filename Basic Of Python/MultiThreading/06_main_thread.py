from time import sleep
from threading import current_thread
from threading import Thread

def run():
   # get the current thread
   thread = current_thread()
   # is it a daemon thread?
   print(f'Daemon thread: {thread.daemon}')

# create a new thread
thread = Thread(target=run)

# start the new thread
thread.start()

# block for a 0.5 sec
sleep(0.5)