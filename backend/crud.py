from schemas import UserCreate, ProductCreate, OrderCreate, OrderItemCreate, DiscountResponse
from database import get_db
from fastapi import Depends
from models import User, Product, Order, OrderItem
from sqlalchemy import select
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends


async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db.add(User(**user.model_dump()))
    await db.commit()
    return user


async def get_user(email: str, db: AsyncSession = Depends(get_db)):
    user = db.execute(select(User).where(User.email == email)) 
    print('user',user)
    result=user.scalar_one_or_none()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result


async def create_product(product: ProductCreate,db:AsyncSession=Depends(get_db)):
    db.add(Product(**product.model_dump()))
    await db.commit()
    return product



async def get_products(db:AsyncSession=Depends(get_db)):
    products = await db.execute(select(Product))
    result = products.scalars().all()
    print('result',result)
    if not result:
        raise HTTPException(status_code=404, detail="Products not found")
    return result

async def get_product(product_id: int, db:AsyncSession=Depends(get_db)):
    
    product = db.execute(select(Product).where(Product.id == product_id))
    print('product',product)
    result = product.scalar_one_or_none()
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return result



async def create_order(order: OrderCreate,db:AsyncSession=Depends(get_db)):


    db.add(Order(**order.model_dump()))
    await db.commit()
    return order

async def get_orders(user_id: int, db:AsyncSession=Depends(get_db)):

    orders = db.execute(select(Order).where(Order.user_id == user_id))
    result = orders.scalars().all()
    print('orders',orders)
    return orders

async def get_order(order_id: int, db:AsyncSession=Depends(get_db)):

    order = db.execute(select(Order).where(Order.id == order_id)).scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

async def create_order_item(order_item: OrderItemCreate,db:AsyncSession=Depends(get_db)):

    db.add(OrderItem(**order_item.model_dump()))
    await db.commit()
    return order_item

async def get_order_items(order_id: int, db:AsyncSession=Depends(get_db)):

    order_items = db.execute(select(OrderItem).where(OrderItem.order_id == order_id)).scalars().all()
    return order_items

async def get_order_item(order_item_id: int, db:AsyncSession=Depends(get_db)):

    order_item = db.execute(select(OrderItem).where(OrderItem.id == order_item_id)).scalar_one_or_none()
    if not order_item:
        raise HTTPException(status_code=404, detail="Order item not found")
    return order_item


async def calculate_discount(user_id: int, items: list[OrderItemCreate],db:AsyncSession=Depends(get_db)):
    discount_response = DiscountResponse()
    total_items = len(items)
    total_quantity = sum(item.quantity for item in items)
    total_value = sum(item.quantity * item.price for item in items)
    quantity_bonus = 0
    value_bonus = 0
    loyalty_bonus = 0
 
    if total_quantity >= 100:
        quantity_bonus += 5
    elif total_quantity >= 500:
        quantity_bonus += 10
    elif total_quantity >= 1000:
        quantity_bonus += 15
    
    if total_value  >= 1000:
        value_bonus += 3
    elif total_value >= 5000:
        value_bonus += 7
    elif total_value >= 10000:
        value_bonus += 12
        
    if user_id:
        buyer = await get_user(user_id, db=db)
        if buyer.previous_orders >= 1:
            loyalty_bonus += 2
        elif buyer.previous_orders >= 4:
            loyalty_bonus += 5
    
    discount_percent = max(quantity_bonus+ value_bonus+ loyalty_bonus, 25)
    discount_amount = total_value * discount_percent / 100
    final_amount = total_value - discount_amount
    return DiscountResponse(total_quantity=total_quantity, total_value=total_value, discount_percent=discount_percent, discount_amount=discount_amount, final_amount=final_amount, breakdown=breakdown)
   
    breakdown = {
        "quantity_bonus": quantity_bonus,
        "value_bonus": value_bonus,
        "loyalty_bonus": loyalty_bonus
    }

