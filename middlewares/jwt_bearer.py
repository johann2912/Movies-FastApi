from fastapi.security import HTTPBearer
from fastapi import Request
from utils.jwt_manager import decoded_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = decoded_token(auth.credentials)
        return data