
from fastapi import APIRouter
from crud import calculate_discount, create_order, get_orders
from schemas import OrderCreate
from schemas import OrderItemCreate
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/calculate")
async def calculate_discount(items: list[OrderItemCreate], user_id: int, db: AsyncSession = Depends(get_db)):
    return await calculate_discount(user_id, items, db=db)

@router.post("/")
async def create_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    return await create_order(order, db=db)

@router.get("/my")
async def get_orders(user_id: int, db: AsyncSession = Depends(get_db)):
    return await get_orders(user_id, db=db)    