from cgitb import handler
from fastapi import FastAPI

from app.api.api_v1.api import router as api_router
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Serverless FastAPI"}

app.include_router(api_router, prefix="/api/v1")
handler = Mangum(app)
