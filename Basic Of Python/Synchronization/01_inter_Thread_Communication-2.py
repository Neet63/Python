from threading import *
import time

def producer(event, data, done_event):
    for i in range(5):
        time.sleep(1)  # Simulate a time-consuming task
        item = f'item_{i}'
        data.append(item)
        print(f'Produced: {item}')

        event.set()  # Signal that a new item has been produced
        time.sleep(1)  # Simulate some delay before clearing the event
        event.clear()  # Reset the event
    done_event.set()  # Signal that production is done

def consumer(event, data, done_event):
    while not done_event.is_set() or data:
        print("Consumer waiting for event...")
        event.wait()  # Wait until the event is set
        while event.is_set() and data:
            item = data.pop(0)
            print(f'Consumed: {item}')
            time.sleep(2)  # Simulate a time-consuming task
        event.clear()  # Ensure event is cleared after consuming


event = Event()
done_event = Event()
data = []

producer_thread = Thread(target=producer, args=(event, data, done_event))
consumer_thread = Thread(target=consumer, args=(event, data, done_event))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("Producer and Consumer have completed execution.")
