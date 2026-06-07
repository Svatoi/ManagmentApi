from fastapi import FastAPI

from app.core.config import settings
from app.api import item_router, order_router, auth_router

app = FastAPI(title=settings.app_name)

app.include_router(item_router)
app.include_router(order_router)
app.include_router(auth_router)

@app.get('/healthcheck', tags=['health'])
def healtcheck():
    return {"status":"all good"}