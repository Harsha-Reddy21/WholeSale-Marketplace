from fastapi import FastAPI
from database import create_tables
import uvicorn
from routers import auth, products, orders


app = FastAPI(title='WholeSale-Marketplace', description='A whole sale marketplace for vendors and buyers')

@app.on_event("startup")
async def startup():
    await create_tables()


@app.get("/health")
async def health():
    return {"status": "Server is running at port 8000"}


app.include_router(auth.router)
app.include_router(products.router)
app.include_router(orders.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)