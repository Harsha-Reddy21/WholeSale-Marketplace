from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class UserType(Enum):
    VENDOR = "VENDOR"
    BUYER = "BUYER"

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    user_type: UserType
    company_name: str


class UserLogin(BaseModel):
    email: str
    password: str


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
    user_id: int
    total_amount: float

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    created_at: datetime

class OrderItemBase(BaseModel):
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