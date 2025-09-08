from auth import create_access_token
from auth import hash_password, verify_password
from fastapi import APIRouter, HTTPException
from auth import verify_password

from schemas import UserCreate
from schemas import UserLogin



router = APIRouter(prefix="/auth", tags=["auth"])
@router.post("/register")
async def register(user: UserCreate):
    user.password = hash_password(user.password)
    return await create_user(user)

@router.post("/login")
async def login(user: UserLogin):
    user.password = hash_password(user.password)
    user = await create_user(user.model_dump())
    if not user or not verify_password(user.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user
    access_token = create_access_token(user.model_dump())
    return {"access_token": access_token, "token_type": "bearer"}