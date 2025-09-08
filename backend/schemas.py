from pydantic import BaseModel


# class User:
#     id: int
#     username: str (unique)
#     email: str (unique)
#     user_type: Enum["VENDOR", "BUYER"]
#     company_name: str
#     created_at: datetime

# class Product:
#     id: int
#     vendor_id: int (FK)
#     name: str
#     category: str
#     price: float  # Base price per unit
#     min_quantity: int  # Minimum order quantity
#     stock: int
#     created_at: datetime



# class Order:
#     id: int
#     buyer_id: int (FK)
#     total_amount: float
#     discount_percent: float
#     final_amount: float
#     created_at: datetime



# class OrderItem:
#     id: int
#     order_id: int (FK)
#     product_id: int (FK)
#     quantity: int
#     unit_price: float
#     subtotal: float

