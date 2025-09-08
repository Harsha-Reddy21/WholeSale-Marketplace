


from fastapi import APIRouter
from crud import create_product, get_products, get_product
from schemas import ProductCreate
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/")
async def create_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    return await create_product(product, db=db)

@router.get("/")   
async def get_products(db: AsyncSession = Depends(get_db)):
    return await get_products(db=db)
    

@router.get("/{product_id}")
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    return get_product(product_id, db=db)
    
    
    