import csv

def process_sales_data(file_path):
    """
    Reads sales CSV and computes:
      - Total revenue per region
      - Top-selling product by quantity
      - Average order value
    Returns formatted string output.
    """

    region_revenue = {}
    product_sales = {}
    total_value = 0
    total_orders = 0

    # Read CSV and aggregate
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            order_id = row['order_id']
            product = row['product']
            quantity = int(row['quantity'])
            price = float(row['price'])
            region = row['region']

            # Revenue for region
            region_revenue[region] = region_revenue.get(region, 0) + (quantity * price)

            # Product sales count
            product_sales[product] = product_sales.get(product, 0) + quantity

            # Totals for avg order value
            total_value += (quantity * price)
            total_orders += 1

    # Compute metrics
    top_product = max(product_sales.items(), key=lambda x: x[1])
    avg_order_value = total_value / total_orders if total_orders > 0 else 0

    # Build output
    output_lines = ["Revenue by region:"]
    for region, revenue in region_revenue.items():
        output_lines.append(f"{region}: ₹{int(revenue):,}")

    output_lines.append("")
    output_lines.append(f"Top-selling product: {top_product[0]} ({top_product[1]} units)")
    output_lines.append(f"Average order value: ₹{int(avg_order_value):,}")

    return "\n".join(output_lines)































# import csv

# def process_sales_data(file_path):
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
