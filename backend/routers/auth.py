

# POST /auth/register - Register user
# POST /auth/login - Login with JWT

from fastapi import APIRouter
from schemas import User


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
async def register(user: User):
    pass 


@router.post("/login")
async def login(user: User):
    pass 