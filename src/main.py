from data_processing import process_sales_df
from threading_simulation import process_order_mutithreaded

def main():
    file_path = "../data/sales_data.csv"

    # Part 1 - Data Processing
    print("\n=== Part 1: Data Processing ===")
    results = process_sales_df(file_path)
    print(results)

    # Part 2 - Threading Simulation
    print("\n=== Part 2: Threading Simulation ===")
    process_order_mutithreaded(file_path)

if __name__ == "__main__":
    main()
