# POST /products - Add product (vendors only)
# GET /products - List all products
# GET /products/{id} - Get product details


from fastapi import APIRouter
from crud import create_product, get_products, get_product
from schemas import ProductCreate

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/")
async def create_product(product: ProductCreate):
    return await create_product(product)

@router.get("/")
async def get_products():
    return await get_products()