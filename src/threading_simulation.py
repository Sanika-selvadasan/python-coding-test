import csv
import threading
import time
import random

def worker(order):
    time.sleep(random.uniform(0.1, 0.5))
    print(f"Worker-{threading.current_thread().name} processed Order {order['order_id']}: {order['product']} x{order['quantity']}")

def process_orders_multithreaded(file_path):
    """
    TODO:
    1. Read orders from CSV
    2. Create and start threads for each order
    3. Wait for all threads to complete
    """
    threads = []
    orders = []

    # TODO: Read CSV and populate 'orders'

    # Example threading logic
    for order in orders:
        t = threading.Thread(target=worker, args=(order,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All orders processed.")
