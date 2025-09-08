from fastapi import APIRouter, HTTPException
from schemas import UserCreate, UserLogin
from auth import hash_password, verify_password, create_access_token
from crud import create_user, get_user
from database import get_db
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession





router = APIRouter(prefix="/auth", tags=["auth"])
@router.post("/register")
async def register(user: UserCreate, db:AsyncSession = Depends(get_db)):
    user.password = hash_password(user.password)
    return await create_user(user, db)

@router.post("/login")
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await get_user(user.email, db)

    if not result or not verify_password(user.password, result.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return result
    access_token = create_access_token(result.model_dump())
    return {"access_token": access_token, "token_type": "bearer"}

