from fastapi import FastAPI
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

from routes import participation, rollcall, api

app = FastAPI()

app.include_router(participation.router)
app.include_router(rollcall.router)
app.include_router(api.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
