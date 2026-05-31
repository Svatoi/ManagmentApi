from fastapi import FastAPI

app = FastAPI()

@app.get('/healthcheck', tags=['health'])
def healtcheck():
    return {"status":"all good"}