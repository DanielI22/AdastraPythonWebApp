from fastapi import APIRouter
from ..service import product_service

router = APIRouter()

@router.get("/products/")
def read_products():
    return product_service.get_products()

@router.get("/products/popular")
def read_products_popular(limit: int = 10):
    return product_service.get_products_popular(limit)
