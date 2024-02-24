from fastapi import APIRouter
from ..service import review_service

router = APIRouter()

@router.get("/reviews/")
def read_reviews():
    return review_service.get_reviews_data()


@router.get("/products/reviews/")
def read_products_with_reviews():
    return review_service.get_products_reviews()