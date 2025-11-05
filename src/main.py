import argparse
from data_processing import process_sales_df
from threading_simulation import process_order_mutithreaded

def main():
    # ----------------------------------------
    # 1. Setup argument parser
    # ----------------------------------------
    parser = argparse.ArgumentParser(
        description="Process sales data and simulate order processing."
    )

    # Add command-line options
    parser.add_argument(
        "--file",
        required=True,
        help="Path to the sales data CSV file (e.g. ../data/sales_data.csv)"
    )

    parser.add_argument(
        "--threads",
        action="store_true",
        help="Enable multithreaded order processing"
    )

    # Parse arguments
    args = parser.parse_args()

    file_path = args.file
    use_threads = args.threads

    # ----------------------------------------
    # 2. Part 1 - Data Processing
    # ----------------------------------------
    print("\n=== Part 1: Data Processing ===")
    results = process_sales_df(file_path)
    print(results)

    # ----------------------------------------
    # 3. Part 2 - Threading Simulation
    # ----------------------------------------
    print("\n=== Part 2: Threading Simulation ===")
    if use_threads:
        print("Running with multithreading enabled...")
        process_order_mutithreaded(file_path)
    else:
        print("Running sequentially (no threads)...")
        # Simple sequential version
        from threading_simulation import load_orders, process_order
        orders = load_orders(file_path)
        for order in orders:
            process_order(order)

if __name__ == "__main__":
    main()
