from data_processing import process_sales_data
from threading_simulation import process_orders_multithreaded

def main():
    file_path = "../data/sales_data.csv"

    # Part 1 - Data Processing
    print("\n=== Part 1: Data Processing ===")
    results = process_sales_data(file_path)
    print(results)

    # Part 2 - Threading Simulation
    print("\n=== Part 2: Threading Simulation ===")
    process_orders_multithreaded(file_path)

if __name__ == "__main__":
    main()
