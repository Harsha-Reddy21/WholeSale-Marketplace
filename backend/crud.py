from schemas import UserCreate, ProductCreate, OrderCreate, OrderItemCreate
from models import User, Product, Order, OrderItem
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from auth import hash_password
from discount import calculate_discount
from fastapi import HTTPException
from auth import verify_password
from schemas import UserLogin
from schemas import CartCreate, OrderItemCreate, UserCreate
from models import Cart, OrderItem

async def create_user(user: UserCreate):
    db = next(get_db())
    db.add(User(**user.model_dump()))
    await db.commit()
    return user 

async def get_user(user_id: int):
    db = next(get_db())
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user



async def create_product(product: ProductCreate):
    db = next(get_db())
    db.add(Product(**product.model_dump()))
    await db.commit()
    return product

async def get_products():
    db = next(get_db())
    products = db.execute(select(Product)).scalars().all()
    return products

async def get_product(product_id: int):
    db = next(get_db())
    product = db.execute(select(Product).where(Product.id == product_id)).scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

async def calculate_discount_for_cart(cart: CartCreate):
    discount = calculate_discount(cart.buyer_id, cart.total_quantity, cart.total_value)
    return discount

async def create_order(order: OrderCreate):
    db = next(get_db())
    db.add(Order(**order.model_dump()))
    await db.commit()
    return order

async def get_orders(user_id: int):
    db = next(get_db())
    orders = db.execute(select(Order).where(Order.user_id == user_id)).scalars().all()
    return orders

async def get_order(order_id: int):
    db = next(get_db())
    order = db.execute(select(Order).where(Order.id == order_id)).scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

async def create_order_item(order_item: OrderItemCreate):
    db = next(get_db())
    db.add(OrderItem(**order_item.model_dump()))
    await db.commit()
    return order_item

async def get_order_items(order_id: int):
    db = next(get_db())
    order_items = db.execute(select(OrderItem).where(OrderItem.order_id == order_id)).scalars().all()
    return order_items

async def get_order_item(order_item_id: int):
    db = next(get_db())
    order_item = db.execute(select(OrderItem).where(OrderItem.id == order_item_id)).scalar_one_or_none()
    if not order_item:
        raise HTTPException(status_code=404, detail="Order item not found")
    return order_item

async def get_user(user_id: int):
    db = next(get_db())
    user = db.execute(select(User).where(User.email == user.email)).scalar_one_or_none()
    if not user or not verify_password(user.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user