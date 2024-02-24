from ..data import queries
import pandas as pd

def get_users_data():
    return queries.fetch_users().to_dict(orient='records')

def get_user_activity(user_id: int):
    orders_df = queries.fetch_orders()
    user_orders = orders_df[orders_df['user_id'] == user_id].copy()
    
    # Convert 'order_date' to datetime and extract year-month
    user_orders['order_month'] = pd.to_datetime(user_orders['order_date']).dt.strftime('%B')

    monthly_activity = user_orders.groupby('order_month').size().reset_index(name='orders_count')
    
    return {"user_id": user_id, "monthly_activity": monthly_activity.to_dict(orient='records')}