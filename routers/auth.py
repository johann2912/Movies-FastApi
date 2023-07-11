from fastapi import APIRouter
from utils.jwt_manager import encoded_token
from schemas.auth import User

auth_router = APIRouter()

@auth_router.post("/login", tags=["auth"])
def login(user: User):
    token: str = encoded_token(user.dict())
    return token