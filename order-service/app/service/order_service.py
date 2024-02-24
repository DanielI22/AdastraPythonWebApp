from ..data import queries
from fastapi import HTTPException
import pandas as pd

def get_orders_data():
    return queries.fetch_orders().to_dict(orient='records')

def get_orders_count():
    users_df = queries.fetch_users()
    orders_df = queries.fetch_orders()
    orders_count = orders_df.groupby('user_id').size().reset_index(name='orders_count')
    merged_df = pd.merge(users_df, orders_count, left_on='id', right_on='user_id', how='left')
    merged_df['orders_count'] = merged_df['orders_count'].fillna(0)
    selected_columns = merged_df[['name', 'email', 'orders_count']]
    return selected_columns.to_dict(orient='records')

def get_user_orders(user_id):
    users_df = queries.fetch_users()
    orders_df = queries.fetch_orders()
    order_items_df = queries.fetch_order_items()

    if user_id not in users_df['id'].values:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_orders_df = orders_df[orders_df['user_id'] == user_id]

    # If no orders found for the user
    if user_orders_df.empty:
        return {"user_id": user_id, "orders": []}
    
    orders_with_items_df = pd.merge(user_orders_df, order_items_df, left_on='id', right_on='order_id', how='left')
    
    grouped_orders = orders_with_items_df.groupby('order_id').apply(
    lambda x: {
        'status': x['status'].iloc[0],
        'order_date': x['order_date'].iloc[0],
        'items': x[['product_name', 'quantity', 'price_at_purchase']].to_dict('records')
    }
    ).reset_index(name='order_details')

    response = grouped_orders.to_dict(orient='records')
    return {"user_id": user_id, "orders": response}

def get_order_status(status: str):
    
    orders_df = queries.fetch_orders()
    filtered_orders = orders_df[orders_df['status'].str.lower() == status.lower()]
    
    if filtered_orders.empty:
        return {"status": status, "message": "No orders found with this status", "orders": []}
    
    return {"status": status, "orders": filtered_orders.to_dict(orient='records')}