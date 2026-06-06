from fastapi import FastAPI
from app.core.config import settings
from app.api.item import router as item_router

app = FastAPI(title=settings.app_name)

app.include_router(item_router)

@app.get('/healthcheck', tags=['health'])
def healtcheck():
    return {"status":"all good"}