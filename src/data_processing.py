import csv
import pandas as pd

filepath = r'C:\Users\LENOVO\Downloads\python-coding-test\data\sales_data.csv'

def process_sales_df(file_path):
    """
    Reads sales CSV and computes:
      - Total revenue per region
      - Top-selling product by quantity
      - Average order value
    Returns formatted string output.
    """

    df = pd.read_csv(filepath) # Load csv
    df['revenue'] = df['quantity'] * df['price'] # Compute reveneue
    region_revenue = df.groupby('region')['revenue'].sum().to_dict() # Total revenue per region
    product_sales = df.groupby('product')['quantity'].sum()
    product_sales   
    top_product = product_sales.idxmax()
    top_quantity = product_sales.max()
    avg_order_value = df['revenue'].mean()
    output_lines = ['Revenue by region: ']

    for region, revenue in region_revenue.items():
        output_lines.append(f'{region}: {int(revenue):,}')

    output_lines.append(f'Top-selling product: {top_product} ({top_quantity} units)')
    output_lines.append(f'Average order value: {int(avg_order_value)}')

    return '\n'.join(output_lines)



































# import csv

# def process_sales_df(file_path):
#     """
#     TODO:
#     1. Read the CSV file
#     2. Compute:
#         - Total revenue per region
#         - Top-selling product (by quantity)
#         - Average order value
#     3. Return a formatted string of results
#     """
#     # Example structure for aggregation
#     region_revenue = {}
#     product_sales = {}
#     total_value = 0
#     total_orders = 0

#     # TODO: Implement logic

#     # Example formatted output
#     output = """
# Revenue by region:
# South: ₹XXXXX
# North: ₹XXXXX
# ...

# Top-selling product: <product> (<units> units)
# Average order value: ₹XXXXX
# """
#     return output
