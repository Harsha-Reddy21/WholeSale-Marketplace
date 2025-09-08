# POST /orders/calculate - Calculate discount for cart items
# POST /orders - Place order with discount
# GET /orders/my - Get user's orders


from fastapi import APIRouter
from crud import calculate_discount_for_cart, create_order, get_orders
from schemas import CartCreate, OrderCreate

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/calculate")
async def calculate_discount_for_cart(cart: CartCreate):
    return await calculate_discount_for_cart(cart)

@router.post("/")
async def create_order(order: OrderCreate):
    return await create_order(order)

@router.get("/my")
async def get_orders(user_id: int):
    return await get_orders(user_id)    