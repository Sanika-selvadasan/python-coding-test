
import pandas as pd
import threading
import time
import random



# Define what each worker does
def process_order(order):

    time.sleep(random.uniform(0.1, 0.5)) #Simulated work time
    order_id = order['order_id']
    product = order['product']
    quantity = order['quantity']

    print(f"Worker - {threading.current_thread().name} processed \n"
      f"Order {order_id}: {product} x{quantity}")

def load_orders(file_path):
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')

def process_order_mutithreaded(file_path):
    orders = load_orders(file_path)
    threads = []

    for i, order in enumerate(orders, start=1):
        thread = threading.Thread(target=process_order, args=(order,), name=str(i))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

print('All orders processed')



















# import csv
# import threading
# import time
# import random

# def worker(order):
#     time.sleep(random.uniform(0.1, 0.5))
#     print(f"Worker-{threading.current_thread().name} processed Order {order['order_id']}: {order['product']} x{order['quantity']}")

# def process_orders_multithreaded(file_path):
#     """
#     TODO:
#     1. Read orders from CSV
#     2. Create and start threads for each order
#     3. Wait for all threads to complete
#     """
#     threads = []
#     orders = []

#     # TODO: Read CSV and populate 'orders'

#     # Example threading logic
#     for order in orders:
#         t = threading.Thread(target=worker, args=(order,))
#         threads.append(t)
#         t.start()

#     for t in threads:
#         t.join()

#     print("All orders processed.")
