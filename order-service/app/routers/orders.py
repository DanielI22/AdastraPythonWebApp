from fastapi import APIRouter
from ..service import order_service

router = APIRouter()

@router.get("/orders/")
def read_orders():
    return order_service.get_orders_data()

@router.get("/users/orders/count")
def read_orders_count():
    return order_service.get_orders_count()

@router.get("/users/{user_id}/orders")
def read_user_orders(user_id: int):
    return order_service.get_user_orders(user_id)

@router.get("/orders/status/{status}")
def read_orders_status(status: str):
    return order_service.get_order_status(status)