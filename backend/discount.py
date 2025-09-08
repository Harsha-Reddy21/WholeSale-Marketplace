from pydantic import BaseModel
from crud import get_user
from schemas import OrderItemCreate



def calculate_discount(buyer_id: int, items: list[OrderItemCreate]) -> DiscountResponse:
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
        
    if buyer_id:
        buyer = get_user(buyer_id)
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
            
   

    
class DiscountResponse(BaseModel):
    total_quantity: int
    total_value: float
    discount_percent: float
    discount_amount: float
    final_amount: float
    breakdown: dict
