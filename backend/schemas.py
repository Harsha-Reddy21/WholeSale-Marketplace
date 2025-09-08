from pydantic import BaseModel
from datetime import datetime




class UserLogin(BaseModel):
    email: str
    password: str

class UserCreate(BaseModel):
    username: str
    email: str
    user_type: str
    company_name: str
    password: str


class UserResponse(BaseModel):
    id: int
    created_at: datetime



class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    created_at: datetime

class ProductCreate(ProductBase):
    pass 

class ProductResponse(ProductBase):
    id: int
    created_at: datetime


class OrderBase(BaseModel):
    id: int 
    user_id: int
    total_amount: float
    created_at: datetime

class OrderCreate(OrderBase):
    pass 

class OrderResponse(OrderBase):
    id: int
    created_at: datetime

class OrderItemBase(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int
    unit_price: float
    subtotal: float

class OrderItemCreate(OrderItemBase):
    pass 

class OrderItemResponse(OrderItemBase):
    id: int
    created_at: datetime
    subtotal: float


class DiscountResponse(BaseModel):
    total_quantity: int
    total_value: float
    discount_percent: float
    discount_amount: float
    final_amount: float
    breakdown: dict

