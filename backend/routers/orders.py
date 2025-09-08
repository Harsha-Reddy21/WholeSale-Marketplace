# POST /orders/calculate - Calculate discount for cart items
# POST /orders - Place order with discount
# GET /orders/my - Get user's orders
# POST /orders/calculate
# {
#   "items": [
#     {"product_id": 1, "quantity": 150},
#     {"product_id": 2, "quantity": 75}
#   ]
# }

# Response:
# {
#   "total_quantity": 225,
#   "total_value": 2500.00,
#   "discount_percent": 12,
#   "discount_amount": 300.00,
#   "final_amount": 2200.00,
#   "breakdown": {
#     "quantity_bonus": 5,
#     "value_bonus": 3,
#     "loyalty_bonus": 4
#   }
# }

from fastapi import APIRouter
from crud import calculate_discount, create_order, get_orders
from schemas import OrderCreate
from schemas import OrderItemCreate

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/calculate")
async def calculate_discount(items: list[OrderItemCreate], user_id: int):
    return await calculate_discount(user_id, items)

@router.post("/")
async def create_order(order: OrderCreate):
    return await create_order(order)

@router.get("/my")
async def get_orders(user_id: int):
    return await get_orders(user_id)    