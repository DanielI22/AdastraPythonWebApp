from ..data import queries
import pandas as pd

def get_reviews_data():
    return queries.fetch_reviews().to_dict(orient='records')


def get_products_reviews():
     products_df = queries.fetch_products()
     reviews_df = queries.fetch_reviews()
     aggregated_reviews = reviews_df.groupby('product_id').agg({'review_text': list, 'rating': 'mean'})
     merged_df = pd.merge(products_df, aggregated_reviews, left_on='id', right_on='product_id', how='left')
     merged_df['rating'] = merged_df['rating'].fillna(0)
     merged_df['review_text'] = merged_df['review_text'].fillna('No reviews')
     selected_columns = merged_df[['name', 'category', 'rating', 'review_text']]
     return selected_columns.to_dict(orient='records')