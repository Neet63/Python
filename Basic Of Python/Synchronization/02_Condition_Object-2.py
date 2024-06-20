import threading
import time

# Create a Condition object
cond = threading.Condition()

# Shared resource
data = []

def producer():
    while True:
        cond.acquire()
        try:
            if len(data) < 5:
                item = len(data) + 1
                data.append(item)
                print(f"Produced {item}")
                cond.notify()  # Notify any waiting consumer
            else:
                print("Queue full, producer is waiting")
                cond.wait()  # Wait for a signal that the condition has changed
        finally:
            cond.release()
        time.sleep(1)

def consumer():
    while True:
        cond.acquire()
        try:
            if data:
                item = data.pop(0)
                print(f"Consumed {item}")
                cond.notify()  # Notify any waiting producer
            else:
                print("Queue empty, consumer is waiting")
                cond.wait()  # Wait for a signal that the condition has changed
        finally:
            cond.release()
        time.sleep(1.5)

# Create and start producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
