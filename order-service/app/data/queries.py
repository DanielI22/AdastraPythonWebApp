from .database import get_db_engine
import pandas as pd

engine = get_db_engine()

def fetch_users():
    query = "SELECT * FROM users;"
    df = pd.read_sql_query(query, engine)
    return df

def fetch_products():
    engine = get_db_engine()
    query = "SELECT * FROM products;"
    df = pd.read_sql_query(query, engine)
    return df

def fetch_orders():
    engine = get_db_engine()
    query = "SELECT * FROM orders;"
    df = pd.read_sql_query(query, engine)
    return df

def fetch_reviews():
    engine = get_db_engine()
    query = "SELECT * FROM reviews;"
    df = pd.read_sql_query(query, engine)
    return df

def fetch_order_items():
    query = "SELECT orderitems.order_id, orderitems.quantity, orderitems.price_at_purchase, products.id AS product_id, products.name AS product_name FROM orderitems JOIN products ON orderitems.product_id = products.id"
    df = pd.read_sql(query, engine)
    return df