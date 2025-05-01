from fastapi import FastAPI

from app.database.db import init_db
from app.api import user
app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(user.router)

@app.get('/')
async def root():   
    return {'Welcome to my FastAPI app!'}





