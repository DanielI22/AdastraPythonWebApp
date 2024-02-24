from fastapi import APIRouter
from ..service import user_service

router = APIRouter()

@router.get("/users/")
def read_users():
    return user_service.get_users_data()

@router.get("/users/{user_id}/activity")
def read_user_activitiy(user_id: int):
    return user_service.get_user_activity(user_id)