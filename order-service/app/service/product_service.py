from ..data import queries
import pandas as pd

def get_products():
    return queries.fetch_products().to_dict(orient='records')

def get_products_popular(limit):
    order_items_df = queries.fetch_order_items()
    products_df = queries.fetch_products()
    
    # Aggregate total quantities sold by product_id
    total_sold = order_items_df.groupby('product_id')['quantity'].sum().reset_index(name='total_quantity')
    total_sold_with_names = pd.merge(total_sold, products_df, left_on='product_id', right_on='id')
    most_sold_products = total_sold_with_names.sort_values(by='total_quantity', ascending=False)
    most_sold_products = most_sold_products.head(limit)
    final_result = most_sold_products[['name', 'total_quantity']]
    
    return final_result.to_dict(orient='records')
